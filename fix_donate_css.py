files = ["index.html","merge.html","compress.html","split.html","convert.html","pdf-to-word.html","word-to-pdf.html","pdf-to-excel.html","jpg-to-pdf.html"]

for f in files:
    with open(f, "r", encoding="utf-8") as fh:
        content = fh.read()
    # Remove inline style from donate-nav so CSS can control it
    content = content.replace(
        '<div id="donate-nav" style="min-width:120px;display:flex;justify-content:flex-end;">',
        '<div id="donate-nav">'
    )
    # Add CSS rule for donate-nav
    content = content.replace(
        '#donate-nav{display:none!important}',
        ''
    )
    # Add proper CSS block
    content = content.replace(
        '</style>',
        '#donate-nav{min-width:120px;display:flex;justify-content:flex-end;}@media(max-width:768px){#donate-nav{display:none!important}}</style>',
        1  # Only replace first occurrence
    )
    with open(f, "w", encoding="utf-8") as fh:
        fh.write(content)
    print(f"Fixed {f}")
