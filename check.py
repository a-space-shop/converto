with open("split.html", "r", encoding="utf-8") as f:
    lines = f.readlines()
for i, line in enumerate(lines[314:325], start=315):
    print(f"{i}: {line.rstrip()[:120]}")
