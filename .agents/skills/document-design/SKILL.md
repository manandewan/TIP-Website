---
name: document-design
description: Design, typeset, and produce clean, professional documents (executive memos, case competition briefs, whitepapers, proposals, Google Doc/Word/PDF style documents). Strictly enforces vertical rhythm, breathable page budgeting (neither cramped nor leaving huge bottom voids), typography scales, table formatting, and executive visual standards.
argument-hint: "[document-type] [page-count]"
metadata:
  author: tip-design-standards
  version: "1.1.0"
---

# Document Design & Typesetting Standards

Guide for producing world-class, clean, executive-ready "normal documents" (PDF briefs, Word `.docx`, Google Docs format, case competition statements, business whitepapers).

---

## 1. Core Principle: Let the Document Breathe (Balanced Page Budgeting)

A great executive document strikes a balance between density and breathing room:
- **Avoid Claustrophobic Cramping**: Never squeeze tiny fonts (7.5pt/8pt) or razor-thin line spacing just to pack extra content into a page. 
- **Avoid Arbitrary Page-Break Voids**: Do not insert artificial `PageBreak()` calls that leave >30% empty space at the bottom of an internal page.
- **Natural Breathing Room**: Target an **80% to 88% vertical fill rate** per page. Allow comfortable whitespace between sections, after tables, and around callouts.
- **Comfortable Margins**: Use standard **0.75 in to 0.85 in** (54pt–61pt) margins for portrait letter/A4 pages. Avoid extreme 0.5-inch edge-to-edge margins unless creating a dense cheat-sheet or flyer.

---

## 2. Typography Hierarchy & Spacing Rhythm

Executive readability depends on generous line height (leading) and clear typographic scale:

| Element | Font Size | Leading (Line Height) | Spacing Before | Spacing After | Notes |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Document Title** | 16–18 pt | 20–22 pt | 0 pt | 2–4 pt | Bold, primary brand navy (`#0F294A`) |
| **Subtitle** | 10–11 pt | 14–15 pt | 0 pt | 8–10 pt | Oblique/italic, secondary sky accent (`#0284C7`) |
| **H1 (Main Section)** | 11.5–12.5 pt | 15–16 pt | 10–12 pt | 3–4 pt | Bold, `keepWithNext = True` |
| **H2 (Exhibit / Subsection)** | 9.5–10.5 pt | 13–14 pt | 8–10 pt | 3–4 pt | Bold, uppercase or small caps |
| **Body Paragraphs** | 9.2–9.8 pt | 13.5–14.5 pt | 0 pt | 5–6 pt | Slate dark gray (`#334155`), 1.4x–1.5x leading |
| **Bullet Items** | 9.0–9.5 pt | 13.0–14.0 pt | 1 pt | 3–5 pt | Left indent 12–16 pt |
| **Table Headers** | 8.2–8.8 pt | 11.0–11.5 pt | — | — | White bold on dark slate (`#1E293B`) |
| **Table Cells** | 8.2–8.8 pt | 11.5–12.5 pt | — | — | Padding: 4.5–6pt top/bottom, 6–8pt left/right |
| **Running Header / Footer** | 7.5–8.0 pt | 10 pt | 0 pt | 0 pt | Muted slate (`#64748B`), centered or edge-aligned |

---

## 3. Table & Callout Card Standards

### Tables
- **Header**: Deep slate background (`#1E293B`) with crisp white bold text.
- **Zebra Striping**: Alternating light rows (`#F8FAFC` and `#FFFFFF`).
- **Borders**: Clean, subtle light grey gridlines (`#E2E8F0` or `#CBD5E1`), 0.5 pt thickness. Avoid harsh black borders.
- **Alignment**:
  - Text columns: Left-aligned.
  - Financial figures, percentages, and metrics: Right-aligned.
  - Status tags / Phase names: Left or center-aligned.
- **Padding**: Never drop below 4pt vertical padding; 5–6pt is ideal for readability.

### Callout Boxes
- Soft pastel background (e.g., `#F0F9FF` for sky blue, `#F8FAFC` for neutral, `#FEFCE8` for warm insight).
- Clean accent border (1.0 pt solid `#38BDF8` or `#CBD5E1`).
- Generous inner padding: **8 pt to 10 pt vertical**, **10 pt to 14 pt horizontal**.

---

## 4. Glyph Safety
- ReportLab built-in Helvetica cannot render non-ASCII characters (e.g., `₹`, `★`, `✓`, `•` in certain encodings).
- Always use ASCII equivalents:
  - Use `Rs.` or `INR` instead of `₹`.
  - Use `Level 1 / 5` instead of `★☆☆☆☆`.
  - Use standard bullet entities or ASCII `-` / `*`.
