with open("compress.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Line 36 (index 35) has </script> followed by a full duplicate <nav>...</nav>
# We need to strip everything after </script> on that line
cleaned = []
for i, line in enumerate(lines):
    if i == 35 and '</script>' in line and '<nav' in line:
        # Keep only up to and including </script>
        line = line[:line.index('</script>') + len('</script>')] + '\n'
    cleaned.append(line)

# Also need to remove the nav lines that follow (lines 37 onwards until </nav>)
result = []
skip = False
for i, line in enumerate(cleaned):
    if i >= 36 and '<button id="hamburger"' in line and not skip:
        skip = True
    if skip and '</nav>' in line:
        skip = False
        continue
    if not skip:
        result.append(line)

with open("compress.html", "w", encoding="utf-8") as f:
    f.writelines(result)
print(f"Done - {len(lines)} -> {len(result)} lines")
