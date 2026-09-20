---
name: document-design
description: Design, typeset, and produce clean, professional documents (executive memos, case competition briefs, whitepapers, proposals, Google Doc/Word/PDF style documents). Strictly enforces vertical rhythm, page budgeting (no awkward empty white spaces), typography scales, table formatting, callout cards, and executive visual standards.
argument-hint: "[document-type] [page-count]"
metadata:
  author: tip-design-standards
  version: "1.0.0"
---

# Document Design & Typesetting Standards

Guide for producing world-class, clean, executive-ready "normal documents" (PDF briefs, Word `.docx`, Google Docs format, case competition statements, business whitepapers).

---

## 1. Golden Rule: No Awkward Empty Whitespace (Page Budgeting)

When producing multi-page documents (especially PDFs and print-ready DOCX):
- **Never leave >20% empty vertical white space** at the bottom of an internal page unless it is the intentional final page of the document.
- **Do not insert artificial page breaks (`PageBreak()`)** without calculating or verifying the vertical height of the preceding page.
- **Budget content per page intentionally**:
  - If a page has extra vertical space, enrich it with:
    - **Exhibit / Data Tables** (e.g. hourly footfall, competitor benchmarking, survey results).
    - **Unit Economics / Financial Cards** (e.g. gross margin breakdown, revenue math).
    - **Executive Callout Boxes** (e.g. "Key Strategic Takeaway", "Field Note", "Management Observation").
    - **Structured Metric Grids** (2-column or 3-column stat blocks).
  - If a page is over-flowing, trim secondary prose, tighten table padding (from 8pt to 5pt), or adjust paragraph `spaceAfter`.
- **Target Page Density**: 80% to 95% of printable vertical height utilized on every page.

---

## 2. Document Anatomy & Hierarchy

Every standard business/academic brief must contain these consistent structural layers:

### A. Document Header (Top of Page 1)
- **Brand Identity**: Clean logo placement (top-left or top-right, balanced aspect ratio).
- **Metadata Tag**: Organization name, Track / Category, Target Audience, Date.
- **Document Title**: 20–24pt Bold, crisp line height.
- **Subtitle / Executive Summary**: 10–11pt italic or light secondary text.
- **Divider Rule**: 1–1.5pt subtle brand accent line.

### B. Section Headings (H1 & H2)
- **H1**: 13–15pt Bold with 10–14pt space before, 4–6pt space after. Keep with next (`keepWithNext = True` in ReportLab / `keep_with_next = True` in docx).
- **H2**: 11–12pt Bold, uppercase or title case.
- **Accent**: Optional left-bar accent or badge style (`[ EXHIBIT 1 ]`).

### C. Body Typography
- **Font Stack**: Helvetica / Arial / Calibri / Georgia / Inter.
- **Font Size**: 9.5pt to 10.5pt for body text.
- **Leading / Line Spacing**: 1.35x to 1.4x (e.g., 10pt font with 14pt leading).
- **Paragraph Spacing**: 5pt to 7pt after paragraphs; avoid double carriage returns (`\n\n`).

### D. Data Exhibits & Tables
- **Header Row**: Solid background (brand dark navy `#1E293B` or `#1B365D`) with white bold text.
- **Zebra Striping**: Alternating light row fill (`#F8FAFC` or `#F1F5F9`).
- **Cell Padding**: 5pt–6pt top/bottom, 8pt–10pt left/right.
- **Alignment**: Text left-aligned; numbers and currency right-aligned; statuses/dates centered.
- **Borders**: Crisp 0.5pt subtle borders (`#CBD5E1` or `#E2E8F0`).

### E. Callout & Highlight Boxes
- Light tinted background (e.g., `#F0FDF4` for green, `#EFF6FF` for blue, `#FEF3C7` for amber).
- Thick left accent border (3–4pt solid color).
- Inner padding (8–12pt all around).
- Bold lead-in header (e.g., `💡 Strategic Insight:` or `⚠️ Core Constraint:`).

### F. Running Headers & Footers (Pages 2+)
- **Header**: Document title & category (8–9pt muted) with subtle 0.5pt line.
- **Footer**: Organization name, Confidentiality notice, and dynamic page number: `Page X of Y`.

---

## 3. Implementation Specifics

### ReportLab (Python PDF Generation)
- Always use `KeepTogether` on tables, callout blocks, and section-header-plus-first-paragraph pairs to prevent awkward splits across pages.
- Set `keepWithNext = True` on all heading `ParagraphStyle`s.
- Glyph Safety: Built-in Helvetica lacks unicode glyphs (`₹`, `★`, `✓`, `™`). Always use ASCII-safe equivalents:
  - Use `Rs.` or `INR` instead of `₹`.
  - Use `[Tier 1]` or `* * *` instead of `★ ★ ★`.
  - Use `[x]` or `[OK]` instead of unicode checkmarks.
- Compute column widths explicitly to fill the exact printable width:
  - Printable width = `PAGE_WIDTH - leftMargin - rightMargin` (e.g., `595.27 - 2*36 = 523.27pt` for A4 with 0.5in margins).
  - Sum of table column widths **must equal** printable width.

### Python-docx (Word Document Generation)
- Set paragraph formatting explicitly (`space_before`, `space_after`, `line_spacing`).
- Table cell margins: Set top, bottom, left, right margins via XML `w:tcMar`.
- Prevent row splitting across pages: `trPr = row._tr.get_or_add_trPr(); trPr.append(parse_xml(r'<w:cantSplit xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"/>'))`.
- Repeat header row on every page: `trPr.append(parse_xml(r'<w:tblHeader xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"/>'))`.

---

## 4. Verification Checklist Before Delivering Any Document

1. [ ] **Page Count & Vertical Balance**:
   - Check rendered pages visually (e.g. convert PDF to PNG and view).
   - Is any internal page less than 75% full? If yes, re-budget content or remove premature page breaks.
2. [ ] **No Orphan Headings**: Does any heading sit alone at the bottom of a page without its body text?
3. [ ] **Table Formatting**: Are column widths properly fitted? Are numbers right-aligned? Is header readable?
4. [ ] **Font Glyphs**: Are there any black boxes or missing characters (`■`)?
5. [ ] **Header/Footer Consistency**: Does the logo appear crisp? Are page numbers accurate?
