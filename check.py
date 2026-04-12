with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()
idx = content.find("max-width:768px")
print(repr(content[idx:idx+200]))
