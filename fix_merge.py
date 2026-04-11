with open("merge.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

cleaned = []
skip_next = False
for i, line in enumerate(lines):
    if "donate-banner" in line and "downloadBtn" not in line and "<div id=" not in line and "onclick=" not in line:
        skip_next = True
        continue
    if skip_next and ("donate-banner" in line or "gtag" in line and "merge" in line):
        continue
    skip_next = False
    cleaned.append(line)

with open("merge.html", "w", encoding="utf-8") as f:
    f.writelines(cleaned)

print("Done")
