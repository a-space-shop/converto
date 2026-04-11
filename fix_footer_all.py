files = ["merge.html", "split.html", "pdf-to-excel.html", "word-to-pdf.html", "index.html"]

for f in files:
    with open(f, "r", encoding="utf-8") as fh:
        content = fh.read()
    if 'href="/about.html">About' not in content:
        content = content.replace(
            '<a href="/privacy.html">Privacy Policy</a></div></footer>',
            '<a href="/privacy.html">Privacy Policy</a><a href="/about.html">About</a></div></footer>'
        )
        with open(f, "w", encoding="utf-8") as fh:
            fh.write(content)
        print(f"Fixed {f}")
    else:
        print(f"Already has About: {f}")
