tools = {
    "split.html": "tool:'split'",
    "pdf-to-word.html": "tool:'pdf-to-word'",
    "word-to-pdf.html": "tool:'word-to-pdf'",
    "pdf-to-excel.html": "tool:'pdf-to-excel'",
    "jpg-to-pdf.html": "tool:'jpg-to-pdf'",
}
for filename, tool_tag in tools.items():
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
    cleaned = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if ("donate-banner" in line and "style.display='flex'" in line
                and "downloadBtn" not in line and "<div" not in line and "onclick=" not in line):
            i += 1
            while i < len(lines) and ("donate-banner" in lines[i] or (tool_tag in lines[i] and "gtag" in lines[i])):
                i += 1
            continue
        cleaned.append(line)
        i += 1
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(cleaned)
    print(f"Fixed {filename}")

with open("convert.html", "r", encoding="utf-8") as f:
    c = f.read()
c = c.replace(
    "document.getElementById('donate-banner').style.display='flex'; document.getElementById('donate-banner').style.display='flex';",
    "document.getElementById('donate-banner').style.display='flex';"
)
with open("convert.html", "w", encoding="utf-8") as f:
    f.write(c)
print("Fixed convert.html")
