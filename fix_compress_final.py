with open("compress.html", "r", encoding="utf-8") as f:
    content = f.read()

# Find the script tag on line 36 and remove everything after it up to the next </nav>
# The script tag contains the toggleMenu function but then has a rogue nav injected after
import re

# Remove the duplicate nav that got injected after the toggleMenu script
# Pattern: </script> then nav content then </nav>
content = re.sub(
    r'(function toggleMenu\(\)\{[^}]+\})\s*<button id="hamburger".*?</nav>',
    r'\1',
    content,
    flags=re.DOTALL
)

with open("compress.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Done")
