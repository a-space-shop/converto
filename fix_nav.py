files = ["pdf-to-word.html", "word-to-pdf.html", "pdf-to-excel.html", "jpg-to-pdf.html"]

for filename in files:
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    content = content.replace('href="/" style="font-size:14px', 'href="/convert" style="font-size:14px')
    content = content.replace('href="/" style="display:block', 'href="/convert" style="display:block')
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Fixed {filename}")
