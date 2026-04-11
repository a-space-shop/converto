with open("word-to-pdf.html", "r", encoding="utf-8") as f:
    lines = f.readlines()
for i, line in enumerate(lines[144:158], start=145):
    print(f"{i}: {line.rstrip()[:120]}")
