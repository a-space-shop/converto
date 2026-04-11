with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Remove About link from nav - find and remove it
import re
content = re.sub(r'\s*<a href="/about\.html"[^>]*>About</a>', '', content)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Done")
