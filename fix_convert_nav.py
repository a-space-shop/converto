with open("convert.html", "r", encoding="utf-8") as f:
    content = f.read()

donate_btn = '<a href="https://paypal.me/editpdffyi" target="_blank" style="background:linear-gradient(135deg,#7c6af7,#f76a8c);color:#fff;border:none;border-radius:8px;padding:8px 18px;font-family:Syne,sans-serif;font-size:13px;font-weight:700;cursor:pointer;text-decoration:none;white-space:nowrap;">&#9829;&nbsp;Donate</a>'

old = '<div id="nav-links" style="display:flex;gap:32px;align-items:center">'
new = f'<div style="min-width:120px;display:flex;justify-content:flex-end;">{donate_btn}</div>\n  <div id="nav-links" style="display:flex;gap:32px;align-items:center;position:absolute;left:50%;transform:translateX(-50%);">'

if old in content:
    content = content.replace(old, new)
    content = content.replace(
        'justify-content:space-between;padding:20px 24px;',
        'justify-content:space-between;padding:20px 24px;position:relative;'
    )
    print("Fixed!")
else:
    print("Pattern not found")

with open("convert.html", "w", encoding="utf-8") as f:
    f.write(content)
