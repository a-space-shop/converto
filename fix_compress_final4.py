with open("compress.html", "r", encoding="utf-8") as f:
    content = f.read()

# Remove the second mobile-menu that appears after the script tag
# It appears right after </script> on line 36
import re
content = re.sub(
    r'(<script>function toggleMenu[^<]*</script>\n)<div id="mobile-menu"[^>]*>.*?</div>\n',
    r'\1',
    content,
    flags=re.DOTALL,
    count=1
)

with open("compress.html", "w", encoding="utf-8") as f:
    f.write(content)

with open("compress.html", "r", encoding="utf-8") as f:
    lines = f.readlines()
print(f"Total lines: {len(lines)}")
for i, line in enumerate(lines[33:42], start=34):
    print(f"{i}: {line.rstrip()[:120]}")
