import os

PAYPAL = "https://paypal.me/editpdffyi"

pages = {
    "convert.html":    ("#7c6af7","#f76a8c","#1e1a2e","rgba(124,106,247,.4)","rgba(124,106,247,.15)","rgba(124,106,247,.4)","#7c6af7","#fff","rgba(124,106,247,.4)"),
    "merge.html":      ("#6af7c8","#7c6af7","#162420","rgba(106,247,200,.4)","rgba(106,247,200,.15)","rgba(106,247,200,.4)","#6af7c8","#0a0a0f","rgba(106,247,200,.3)"),
    "compress.html":   ("#f76a8c","#f7a06a","#241820","rgba(247,106,140,.4)","rgba(247,106,140,.15)","rgba(247,106,140,.4)","#f76a8c","#fff","rgba(247,106,140,.4)"),
    "split.html":      ("#6af77c","#6af7c8","#162416","rgba(106,247,124,.4)","rgba(106,247,124,.15)","rgba(106,247,124,.4)","#6af77c","#0a0a0f","rgba(106,247,124,.3)"),
    "pdf-to-word.html":("#7c6af7","#f76a8c","#1e1a2e","rgba(124,106,247,.4)","rgba(124,106,247,.15)","rgba(124,106,247,.4)","#7c6af7","#fff","rgba(124,106,247,.4)"),
    "word-to-pdf.html":("#f76a8c","#7c6af7","#241820","rgba(247,106,140,.4)","rgba(247,106,140,.15)","rgba(247,106,140,.4)","#f76a8c","#fff","rgba(247,106,140,.4)"),
    "pdf-to-excel.html":("#f76a8c","#7c6af7","#241820","rgba(247,106,140,.4)","rgba(247,106,140,.15)","rgba(247,106,140,.4)","#f76a8c","#fff","rgba(247,106,140,.4)"),
    "jpg-to-pdf.html": ("#6af7c8","#7c6af7","#162420","rgba(106,247,200,.4)","rgba(106,247,200,.15)","rgba(106,247,200,.4)","#6af7c8","#0a0a0f","rgba(106,247,200,.3)"),
}

def make_banner(c1,c2,bg,border,chk_bg,chk_bd,chk_col,btn_col,shadow):
    return f'''<div id="donate-banner" style="display:none;position:fixed;inset:0;z-index:9999;background:rgba(0,0,0,0.75);backdrop-filter:blur(6px);align-items:center;justify-content:center;"><div style="position:relative;max-width:480px;width:90%;border-radius:20px;padding:40px 32px 32px;text-align:center;background:linear-gradient(160deg,{bg},#1a1a26);border:1px solid {border};box-shadow:0 24px 60px rgba(0,0,0,.6)"><div style="position:absolute;width:300px;height:300px;border-radius:50%;filter:blur(80px);opacity:0.12;top:-100px;left:50%;transform:translateX(-50%);background:{c1};pointer-events:none"></div><button onclick="document.getElementById('donate-banner').style.display='none'" style="position:absolute;top:14px;right:14px;background:rgba(255,255,255,.06);border:none;color:#9090aa;font-size:16px;cursor:pointer;width:30px;height:30px;border-radius:50%;display:flex;align-items:center;justify-content:center;">&#10005;</button><div style="width:52px;height:52px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:22px;background:{chk_bg};border:2px solid {chk_bd};color:{chk_col};margin:0 auto 18px">&#10003;</div><div style="font-family:Syne,sans-serif;font-size:22px;font-weight:800;letter-spacing:-0.5px;margin-bottom:12px;background:linear-gradient(135deg,{c1},{c2});-webkit-background-clip:text;-webkit-text-fill-color:transparent">Download Complete</div><div style="font-size:13px;line-height:1.8;color:#9090aa;margin-bottom:24px">EditPDF is free because of generous people like you.<br>If it helped, please feel free to support us by making a donation.</div><a href="{PAYPAL}" target="_blank" style="display:inline-block;background:linear-gradient(135deg,{c1},{c2});color:{btn_col};border-radius:12px;padding:13px 32px;font-family:Syne,sans-serif;font-size:14px;font-weight:800;text-decoration:none;box-shadow:0 4px 24px {shadow}">&#9829;&nbsp; Donate</a></div></div>'''

show_js = "document.getElementById('donate-banner').style.display='flex';"

triggers = {
    "convert.html": "a.href = downloadUrl; a.download = outName; a.click();",
    "merge.html": "downloadArea.classList.add('visible')",
    "compress.html": "downloadArea.classList.add('visible')",
    "split.html": "downloadArea.classList.add('visible')",
    "pdf-to-word.html": "downloadArea.classList.add('visible')",
    "word-to-pdf.html": "downloadArea.classList.add('visible')",
    "pdf-to-excel.html": "downloadArea.classList.add('visible')",
    "jpg-to-pdf.html": "downloadArea.classList.add('visible')",
}

for filename, colors in pages.items():
    if not os.path.exists(filename):
        print(f"SKIP {filename} - not found")
        continue
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    # Remove old inline banner if exists
    if 'id="donate-banner"' in content:
        start = content.find('<div id="donate-banner"')
        depth = 0
        i = start
        while i < len(content):
            if content[i:i+4] == "<div":
                depth += 1
            elif content[i:i+6] == "</div>":
                depth -= 1
                if depth == 0:
                    end = i + 6
                    break
            i += 1
        content = content[:start] + content[end:]
        print(f"Removed old banner from {filename}")
    banner = make_banner(*colors)
    # Insert before </body>
    content = content.replace("</body>", banner + "\n</body>")
    # Fix JS trigger
    trigger = triggers[filename]
    if trigger in content and show_js not in content:
        content = content.replace(trigger, trigger + "\n    " + show_js)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"DONE {filename}")

print("All done!")
