with open("compress.html", "r", encoding="utf-8-sig") as f:
    lines = f.readlines()

result = []
skip = False
for i, line in enumerate(lines):
    if i >= 35 and '<button id="hamburger"' in line and not skip:
        skip = True
    if skip and '</nav>' in line:
        skip = False
        continue
    if not skip:
        result.append(line)

with open("compress.html", "w", encoding="utf-8") as f:
    f.writelines(result)
print(f"Done - {len(lines)} -> {len(result)} lines")
