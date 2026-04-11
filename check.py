with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if "nav-links" in line and "<div" in line:
        print(f"{i+1}: {line.rstrip()[:150]}")
