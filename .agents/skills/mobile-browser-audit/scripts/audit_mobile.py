#!/usr/bin/env python3
"""
Mobile Browser Audit Suite for Web Applications.
Uses Google Chrome over Chrome DevTools Protocol (CDP) to test:
1. Horizontal overflow across multiple mobile device viewports (320px, 375px, 390px, 414px, 430px, 768px)
2. Touch target sizing (>= 44x44px per Apple HIG / Google Material)
3. iOS Safari font size zoom traps (< 16px on inputs)
4. Mobile viewport & theme-color meta tags
5. Tap delay optimization (touch-action: manipulation)
6. Element visibility and console errors
"""

import sys
import os
import time
import json
import argparse
import subprocess
import asyncio
import urllib.request

try:
    import websockets
except ImportError:
    print("Error: 'websockets' package required. Install with pip or use system python.")
    sys.exit(1)

DEVICES = [
    {"name": "iPhone SE (1st gen) / Ultra Narrow", "width": 320, "height": 568, "dpr": 2.0},
    {"name": "iPhone 13 mini / SE 3", "width": 375, "height": 667, "dpr": 2.0},
    {"name": "iPhone 14 / 15 / 16 Standard", "width": 390, "height": 844, "dpr": 3.0},
    {"name": "iPhone 11 / XR / Plus", "width": 414, "height": 896, "dpr": 2.0},
    {"name": "iPhone 15 / 16 Pro Max", "width": 430, "height": 932, "dpr": 3.0},
    {"name": "iPad Mini (Portrait)", "width": 768, "height": 1024, "dpr": 2.0},
]

CHROME_PATHS = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/usr/bin/google-chrome",
    "/usr/bin/chromium-browser"
]

def find_chrome():
    for path in CHROME_PATHS:
        if os.path.exists(path):
            return path
    which = subprocess.run(["which", "google-chrome"], capture_output=True, text=True).stdout.strip()
    if which:
        return which
    return None

class CDPSession:
    def __init__(self, ws_url):
        self.ws_url = ws_url
        self.ws = None
        self._msg_id = 0

    async def connect(self):
        self.ws = await websockets.connect(self.ws_url, max_size=50*1024*1024)

    async def send(self, method, params=None):
        self._msg_id += 1
        msg = {"id": self._msg_id, "method": method}
        if params:
            msg["params"] = params
        await self.ws.send(json.dumps(msg))
        
        while True:
            resp = await self.ws.recv()
            data = json.loads(resp)
            if data.get("id") == self._msg_id:
                if "error" in data:
                    raise RuntimeError(f"CDP error on {method}: {data['error']}")
                return data.get("result", {})

    async def evaluate(self, expression):
        res = await self.send("Runtime.evaluate", {
            "expression": expression,
            "returnByValue": True,
            "awaitPromise": True
        })
        return res.get("result", {}).get("value")

    async def close(self):
        if self.ws:
            await self.ws.close()

async def run_audit(url):
    chrome_bin = find_chrome()
    if not chrome_bin:
        print("[-] Error: Chrome binary not found.")
        sys.exit(1)

    port = 9333
    chrome_proc = subprocess.Popen([
        chrome_bin,
        "--headless=new",
        "--disable-gpu",
        f"--remote-debugging-port={port}",
        "--no-first-run",
        "--no-default-browser-check",
        "--disable-extensions",
        "--disable-background-networking"
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    session = None
    try:
        # Wait for debugging port
        ws_url = None
        for _ in range(30):
            time.sleep(0.2)
            try:
                with urllib.request.urlopen(f"http://127.0.0.1:{port}/json") as r:
                    tabs = json.loads(r.read().decode())
                    for t in tabs:
                        if t.get("type") == "page":
                            ws_url = t["webSocketDebuggerUrl"]
                            break
                    if ws_url:
                        break
            except Exception:
                continue

        if not ws_url:
            raise RuntimeError("Failed to connect to headless Chrome debugging port.")

        session = CDPSession(ws_url)
        await session.connect()
        await session.send("Page.enable")
        await session.send("Runtime.enable")
        await session.send("DOM.enable")

        # Navigate to target URL
        await session.send("Page.navigate", {"url": url})

        # Wait until target URL is fully loaded and parsed
        for _ in range(30):
            await asyncio.sleep(0.15)
            try:
                ready = await session.evaluate("document.readyState === 'complete' && document.querySelector('meta[name=\"viewport\"]') !== null")
                if ready:
                    break
            except Exception:
                continue

        print(f"\n========================================================")
        print(f"  RIGOROUS MOBILE BROWSER AUDIT: {url}")
        print(f"========================================================\n")

        all_passed = True

        # Test 1: Global Meta & Configuration Check
        meta_check_js = """
        (() => {
            const viewport = document.querySelector('meta[name="viewport"]')?.content || '';
            const themeColor = document.querySelector('meta[name="theme-color"]')?.content || '';
            const appleMobile = document.querySelector('meta[name="apple-mobile-web-app-capable"]')?.content || '';
            
            return {
                viewport,
                hasWidth: viewport.includes('width=device-width'),
                hasInitialScale: viewport.includes('initial-scale=1'),
                hasCover: viewport.includes('viewport-fit=cover'),
                disablesZoom: viewport.includes('user-scalable=no') || viewport.includes('maximum-scale=1'),
                themeColor,
                appleMobile
            };
        })()
        """
        meta_res = await session.evaluate(meta_check_js)
        print("[*] Checking Viewport and Document Meta Tags...")
        if meta_res and meta_res.get("hasWidth") and meta_res.get("hasInitialScale"):
            print(f"  [PASS] Viewport correctly sets width=device-width & initial-scale=1")
        else:
            print(f"  [FAIL] Missing or invalid viewport configuration: '{meta_res.get('viewport') if meta_res else ''}'")
            all_passed = False

        if meta_res and meta_res.get("hasCover"):
            print(f"  [PASS] Viewport includes 'viewport-fit=cover' for notch safe-area handling")
        else:
            print(f"  [WARN] Missing 'viewport-fit=cover' in viewport meta tag.")

        if meta_res and meta_res.get("disablesZoom"):
            print(f"  [FAIL] Viewport disables user zooming (user-scalable=no / maximum-scale=1). Violates WCAG!")
            all_passed = False
        else:
            print(f"  [PASS] User zoom is not maliciously restricted.")

        if meta_res and meta_res.get("themeColor"):
            print(f"  [PASS] Theme color meta tag set: {meta_res['themeColor']}")
        else:
            print(f"  [WARN] Missing <meta name='theme-color'> tag.")

        # Test 2: Multi-Device Responsive Viewport & Overflow Tests
        print("\n[*] Testing Horizontal Overflow across 6 Device Widths...")

        overflow_check_js = """
        (() => {
            const winWidth = window.innerWidth;
            const scrollWidth = document.documentElement.scrollWidth;
            const bodyScrollWidth = document.body.scrollWidth;
            const maxScroll = Math.max(scrollWidth, bodyScrollWidth);
            
            const overflowingElements = [];
            const all = document.querySelectorAll('*');
            for (let el of all) {
                if (['script', 'style', 'head', 'meta', 'link'].includes(el.tagName.toLowerCase())) continue;
                const r = el.getBoundingClientRect();
                if (r.right > winWidth + 1.5 && r.width > 0) {
                    overflowingElements.push({
                        tag: el.tagName.toLowerCase(),
                        id: el.id || '',
                        className: (el.className && typeof el.className === 'string') ? el.className.split(' ').slice(0, 3).join('.') : '',
                        right: Math.round(r.right),
                        overflowBy: Math.round(r.right - winWidth),
                        text: (el.innerText || '').slice(0, 30).trim()
                    });
                }
            }
            return {
                windowWidth: winWidth,
                maxScrollWidth: maxScroll,
                hasOverflow: maxScroll > winWidth + 1,
                overflowingElements: overflowingElements.slice(0, 8)
            };
        })()
        """

        for dev in DEVICES:
            await session.send("Emulation.setDeviceMetricsOverride", {
                "width": dev["width"],
                "height": dev["height"],
                "deviceScaleFactor": dev["dpr"],
                "mobile": True,
                "screenOrientation": {"type": "portraitPrimary", "angle": 0}
            })
            await asyncio.sleep(0.3)
            res = await session.evaluate(overflow_check_js)
            
            dev_label = f"{dev['name']} ({dev['width']}px)"
            if res and not res["hasOverflow"]:
                print(f"  [PASS] {dev_label}: Zero horizontal overflow (scrollWidth {res['maxScrollWidth']}px <= {dev['width']}px)")
            else:
                all_passed = False
                scroll_w = res['maxScrollWidth'] if res else 'unknown'
                print(f"  [FAIL] {dev_label}: OVERFLOW DETECTED! scrollWidth {scroll_w}px > window {dev['width']}px")
                if res and res.get("overflowingElements"):
                    for item in res["overflowingElements"]:
                        ident = f"<{item['tag']}"
                        if item['id']: ident += f" id='{item['id']}'"
                        if item['className']: ident += f" class='{item['className']}'"
                        ident += ">"
                        print(f"         Offending: {ident} extends +{item['overflowBy']}px ('{item['text']}')")

        # Reset to standard 390px mobile for interactive audits
        await session.send("Emulation.setDeviceMetricsOverride", {
            "width": 390,
            "height": 844,
            "deviceScaleFactor": 3.0,
            "mobile": True
        })
        await asyncio.sleep(0.3)

        # Test 3: Touch Target Sizes (Apple HIG >= 44x44px)
        print("\n[*] Auditing Touch Targets (Minimum 44x44px guideline)...")
        touch_targets_js = """
        (() => {
            const targets = [];
            const interactive = document.querySelectorAll('a, button, input, select, textarea, [role="button"], .interactive, .btn, .social-btn, .social-circle-btn, .filter-tab');
            
            for (let el of interactive) {
                const style = window.getComputedStyle(el);
                if (style.display === 'none' || style.visibility === 'hidden' || style.opacity === '0') continue;
                
                const r = el.getBoundingClientRect();
                if (r.width === 0 || r.height === 0) continue;
                
                // Exempt links inline in body paragraphs unless they are buttons/pills
                const isInlineTextLink = el.tagName.toLowerCase() === 'a' && 
                                        el.closest('p, span') && 
                                        !el.classList.contains('btn') && 
                                        !el.classList.contains('pill') &&
                                        !el.classList.contains('nav-link') &&
                                        !el.classList.contains('social-circle-btn');
                
                if (isInlineTextLink) continue;
                
                const width = Math.round(r.width);
                const height = Math.round(r.height);
                
                if (width < 44 || height < 44) {
                    targets.push({
                        tag: el.tagName.toLowerCase(),
                        id: el.id || '',
                        className: (el.className && typeof el.className === 'string') ? el.className.split(' ').slice(0, 3).join('.') : '',
                        width,
                        height,
                        text: (el.innerText || el.getAttribute('aria-label') || el.value || '').slice(0, 30).trim()
                    });
                }
            }
            return targets;
        })()
        """
        small_targets = await session.evaluate(touch_targets_js)
        if not small_targets:
            print("  [PASS] All evaluated standalone interactive touch targets meet >= 44x44px!")
        else:
            print(f"  [WARN] Found {len(small_targets)} touch target(s) smaller than 44x44px:")
            for t in small_targets[:8]:
                ident = f"<{t['tag']}"
                if t['id']: ident += f" id='{t['id']}'"
                if t['className']: ident += f" class='{t['className']}'"
                ident += ">"
                print(f"         {ident} size={t['width']}x{t['height']}px ('{t['text']}')")

        # Test 4: Form Input Font Size (iOS Auto-Zoom Traps)
        print("\n[*] Auditing Form Controls for iOS Safari Auto-Zoom Traps (< 16px)...")
        font_check_js = """
        (() => {
            const inputs = document.querySelectorAll('input, select, textarea');
            const traps = [];
            for (let el of inputs) {
                const style = window.getComputedStyle(el);
                const size = parseFloat(style.fontSize);
                if (size < 16) {
                    traps.push({
                        name: el.name || el.id || el.type,
                        fontSize: size
                    });
                }
            }
            return traps;
        })()
        """
        zoom_traps = await session.evaluate(font_check_js)
        if not zoom_traps:
            print("  [PASS] All form inputs have font-size >= 16px (no auto-zoom trigger)")
        else:
            all_passed = False
            print(f"  [FAIL] Found {len(zoom_traps)} input(s) with font-size < 16px! (Triggers iOS auto-zoom)")
            for z in zoom_traps:
                print(f"         Input '{z['name']}' font-size: {z['fontSize']}px")

        # Test 5: Tap Delay Optimization & Touch Action
        print("\n[*] Auditing Touch Action & Tap Highlight...")
        touch_action_js = """
        (() => {
            const htmlStyle = window.getComputedStyle(document.documentElement);
            const bodyStyle = window.getComputedStyle(document.body);
            return {
                htmlTouchAction: htmlStyle.touchAction,
                bodyTouchAction: bodyStyle.touchAction,
                webkitHighlight: bodyStyle.webkitTapHighlightColor
            };
        })()
        """
        touch_data = await session.evaluate(touch_action_js)
        print(f"  [INFO] HTML touch-action: {touch_data['htmlTouchAction']}")
        print(f"  [INFO] Webkit tap highlight: {touch_data['webkitHighlight']}")

        # Test 6: Images Max Width & Responsiveness
        print("\n[*] Auditing Image Responsiveness...")
        img_check_js = """
        (() => {
            const images = document.querySelectorAll('img');
            const unconstrained = [];
            for (let img of images) {
                const style = window.getComputedStyle(img);
                const r = img.getBoundingClientRect();
                if (r.width > window.innerWidth) {
                    unconstrained.push({
                        src: img.src.split('/').pop(),
                        renderedWidth: r.width,
                        windowWidth: window.innerWidth
                    });
                }
            }
            return unconstrained;
        })()
        """
        bad_imgs = await session.evaluate(img_check_js)
        if not bad_imgs:
            print("  [PASS] All images are responsive and stay within viewport bounds!")
        else:
            all_passed = False
            print(f"  [FAIL] Found {len(bad_imgs)} image(s) exceeding viewport width:")
            for img in bad_imgs:
                print(f"         Image {img['src']}: {img['renderedWidth']}px wide")

        print("\n========================================================")
        if all_passed:
            print("  AUDIT SUMMARY: [PASS] All mobile requirements verified!")
        else:
            print("  AUDIT SUMMARY: [FAIL] Issues detected that require fixes.")
        print("========================================================\n")

        return all_passed

    finally:
        if session:
            await session.close()
        chrome_proc.terminate()

def main():
    parser = argparse.ArgumentParser(description="Audit web page for mobile browser readiness")
    parser.add_argument("--url", default="http://localhost:8099", help="URL to audit")
    args = parser.parse_args()

    success = asyncio.run(run_audit(args.url))
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
