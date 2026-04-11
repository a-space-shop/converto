with open("compress.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

result = []
skip = False
for i, line in enumerate(lines):
    if i == 36 and '<div id="mobile-menu"' in line:
        skip = True
    if skip and line.strip() == '</div>':
        skip = False
        continue
    if not skip:
        result.append(line)

with open("compress.html", "w", encoding="utf-8") as f:
    f.writelines(result)
print(f"Done - {len(lines)} -> {len(result)} lines")
for i, line in enumerate(result[33:42], start=34):
    print(f"{i}: {line.rstrip()[:120]}")
