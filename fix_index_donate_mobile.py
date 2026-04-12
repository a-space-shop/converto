with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Add donate-nav id
content = content.replace(
    '<div style="min-width:120px;display:flex;justify-content:flex-end;">',
    '<div id="donate-nav" style="min-width:120px;display:flex;justify-content:flex-end;">'
)

# Add mobile hide rule
content = content.replace(
    '#logo{position:absolute;left:50%;transform:translateX(-50%);}',
    '#logo{position:absolute;left:50%;transform:translateX(-50%);}#donate-nav{display:none!important}'
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Done")

# Verify
with open("index.html", "r", encoding="utf-8") as f:
    c = f.read()
print("donate-nav id:", "donate-nav" in c)
print("hide rule:", "donate-nav{display:none" in c)
