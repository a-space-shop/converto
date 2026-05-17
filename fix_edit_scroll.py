with open("edit.html", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace(
    "body{margin:0;padding:0;overflow:hidden",
    "body{margin:0;padding:0;overflow-x:hidden"
)
content = content.replace(
    "html,body{overflow:hidden",
    "html,body{overflow-x:hidden"
)

with open("edit.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Done")
