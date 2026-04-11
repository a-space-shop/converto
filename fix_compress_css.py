with open("compress.html", "r", encoding="utf-8") as f:
    content = f.read()

# Remove 2nd and 3rd duplicate mobile style blocks (keep first at 11805)
# They all look the same so just remove duplicates
import re
mobile_style = r'<style>@media\(max-width:768px\)\{#nav-links.*?</style>'
matches = list(re.finditer(mobile_style, content, re.DOTALL))
print(f"Found {len(matches)} mobile style blocks")

# Keep first, remove rest
for m in reversed(matches[1:]):
    content = content[:m.start()] + content[m.end():]

# Also fix the nav CSS in main style block - change grid to flex
content = content.replace(
    "nav{position:fixed;top:0;left:0;right:0;z-index:100;display:grid;grid-template-columns:1fr auto 1fr;align-items:center;padding:20px 48px;",
    "nav{position:fixed;top:0;left:0;right:0;z-index:100;display:flex;align-items:center;justify-content:space-between;padding:20px 24px;"
)

with open("compress.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Done")
