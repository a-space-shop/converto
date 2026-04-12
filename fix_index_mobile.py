with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace(
    '#logo-wrap{position:absolute;left:50%;transform:translateX(-50%);}',
    '#logo-wrap{position:absolute;left:50%;transform:translateX(-50%);}#donate-nav{display:none!important}'
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
print("hide rule added:", "donate-nav{display:none" in content)
