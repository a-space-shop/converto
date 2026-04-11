with open("compress.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

cleaned = []
skip = False
for i, line in enumerate(lines):
    if i >= 36 and '<div id="mobile-menu"' in line and not skip:
        skip = True
    if skip and line.strip() == '</div>':
        skip = False
        continue
    if not skip:
        cleaned.append(line)

with open("compress.html", "w", encoding="utf-8") as f:
    f.writelines(cleaned)
print(f"Done - removed {len(lines)-len(cleaned)} lines")
