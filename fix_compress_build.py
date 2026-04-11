import subprocess
result = subprocess.run(["git", "show", "066ff5e:compress.html"], capture_output=True, text=True, encoding="utf-8")
original = result.stdout

# Get CSS/head from second document
script_end = 7874 + len("</script>")
second_doc = original[script_end:]
head_start = second_doc.find("<head>")
head_end = second_doc.find("</head>") + len("</head>")
head = second_doc[head_start:head_end]

body_start = second_doc.find("<body>") + len("<body>")
body_end = second_doc.find("</body>")
body_content = second_doc[body_start:body_end]

# Get our clean nav from current compress.html (lines 16-36)
with open("compress.html", "r", encoding="utf-8") as f:
    lines = f.readlines()
nav_lines = lines[15:36]  # <body> to </script>toggleMenu
nav = "".join(nav_lines)

# Build final file
final = f"""<!DOCTYPE html>
<html lang="en">
{head}
<body>
{nav}
{body_content.strip()}
</body>
</html>
"""

with open("compress.html", "w", encoding="utf-8") as f:
    f.write(final)

with open("compress.html", "r", encoding="utf-8") as f:
    lines = f.readlines()
print(f"Done - {len(lines)} lines")
for i, line in enumerate(lines[14:40], start=15):
    print(f"{i}: {line.rstrip()[:120]}")
