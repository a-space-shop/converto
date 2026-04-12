import re

files = ["index.html","merge.html","compress.html","split.html","convert.html","pdf-to-word.html","word-to-pdf.html","pdf-to-excel.html","jpg-to-pdf.html"]

donate_link = '\n  <a href="https://paypal.me/editpdffyi" target="_blank" style="display:block;padding:14px 0;font-size:15px;font-weight:500;text-decoration:none;color:#fff;border-top:1px solid #2a2a3d;margin-top:8px;text-align:center;">&#9829;&nbsp;Donate</a>'

for f in files:
    with open(f, "r", encoding="utf-8") as fh:
        content = fh.read()

    # Add donate to hamburger if not already there
    menu_start = content.find('id="mobile-menu"')
    menu_end = content.find('</div>', menu_start)
    menu_section = content[menu_start:menu_end]
    
    if 'paypal.me' not in menu_section:
        content = content[:menu_end] + donate_link + '\n' + content[menu_end:]
        print(f"Added donate to hamburger: {f}")
    else:
        print(f"Already has donate in hamburger: {f}")

    # Hide donate nav button on mobile
    content = content.replace(
        '<div id="donate-nav"',
        '<div id="donate-nav" style="min-width:120px;display:flex;justify-content:flex-end;">'
    ).replace(
        '<div id="donate-nav" style="min-width:120px;display:flex;justify-content:flex-end;" style="min-width:120px;display:flex;justify-content:flex-end;">',
        '<div id="donate-nav" style="min-width:120px;display:flex;justify-content:flex-end;">'
    )

    # Add mobile hide rule for donate-nav
    content = content.replace(
        '#logo{position:absolute;left:50%;transform:translateX(-50%);}',
        '#logo{position:absolute;left:50%;transform:translateX(-50%);}#donate-nav{display:none!important}'
    )

    with open(f, "w", encoding="utf-8") as fh:
        fh.write(content)

print("All done")
