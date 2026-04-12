files = ["merge.html","compress.html","split.html","convert.html","pdf-to-word.html","word-to-pdf.html","pdf-to-excel.html","jpg-to-pdf.html"]

for f in files:
    with open(f, "r", encoding="utf-8") as fh:
        content = fh.read()
    
    # Find the donate wrapper div (it has min-width:120px and paypal link inside)
    import re
    old = re.search(r'<div style="min-width:120px;display:flex;justify-content:flex-end;"><a href="https://paypal\.me', content)
    if old:
        content = content.replace(
            '<div style="min-width:120px;display:flex;justify-content:flex-end;"><a href="https://paypal.me',
            '<div id="donate-nav"><a href="https://paypal.me'
        )
        print(f"Fixed {f}")
    else:
        print(f"Pattern not found: {f}")
    
    with open(f, "w", encoding="utf-8") as fh:
        fh.write(content)
