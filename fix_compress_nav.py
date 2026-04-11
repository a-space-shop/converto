with open("compress.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Find the duplicate nav content starting at line 37 (index 36)
# It starts after the </script> on line 36 and goes until </nav> or <body content
# Find the second hamburger button
cleaned = []
skip = False
for i, line in enumerate(lines):
    if i >= 36 and '<button id="hamburger"' in line and not skip:
        skip = True
    if skip and "</nav>" in line:
        skip = False
        continue
    if not skip:
        cleaned.append(line)

with open("compress.html", "w", encoding="utf-8") as f:
    f.writelines(cleaned)
print(f"Done - removed {len(lines)-len(cleaned)} lines")
