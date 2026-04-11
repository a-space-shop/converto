import re

pages = {
    "index.html":       ("linear-gradient(135deg,#7c6af7,#f76a8c)", "#fff"),
    "merge.html":       ("linear-gradient(135deg,#6af7c8,#7c6af7)", "#0a0a0f"),
    "compress.html":    ("linear-gradient(135deg,#f76a8c,#f7a06a)", "#fff"),
    "split.html":       ("linear-gradient(135deg,#6af77c,#6af7c8)", "#0a0a0f"),
    "pdf-to-word.html": ("linear-gradient(135deg,#7c6af7,#f76a8c)", "#fff"),
    "word-to-pdf.html": ("linear-gradient(135deg,#7c6af7,#f76a8c)", "#fff"),
    "pdf-to-excel.html":("linear-gradient(135deg,#f76a8c,#7c6af7)", "#fff"),
    "jpg-to-pdf.html":  ("linear-gradient(135deg,#6af7c8,#7c6af7)", "#0a0a0f"),
}

donate_url = "https://paypal.me/editpdffyi"

for filename, (gradient, btn_color) in pages.items():
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    donate_btn = f'<a href="{donate_url}" target="_blank" style="background:{gradient};color:{btn_color};border:none;border-radius:8px;padding:8px 18px;font-family:Syne,sans-serif;font-size:13px;font-weight:700;cursor:pointer;text-decoration:none;white-space:nowrap;">&#9829;&nbsp;Donate</a>'

    # Replace nav inner content - find the nav tag and restructure it
    # Strategy: find existing nav style and inject new structure

    # Find nav links div and replace with centered + donate layout
    # Look for the id="nav-links" div and wrap it properly
    old_nav_links = r'<div id="nav-links" style="display:flex;gap:32px;align-items:center">'
    new_nav_links = f'<div style="min-width:120px;display:flex;justify-content:flex-end;">{donate_btn}</div>\n  <div id="nav-links" style="display:flex;gap:32px;align-items:center;position:absolute;left:50%;transform:translateX(-50%);">'

    if old_nav_links in content:
        content = content.replace(old_nav_links, new_nav_links)
        # Also update nav to use space-between and relative positioning
        content = content.replace(
            'justify-content:space-between;padding:20px 24px;',
            'justify-content:space-between;padding:20px 24px;position:relative;'
        )
        print(f"Fixed {filename}")
    else:
        print(f"Pattern not found in {filename}")

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
