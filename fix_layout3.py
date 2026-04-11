with open("compress.html", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace(
    "body{background:var(--bg);color:var(--text);font-family:var(--font-mono);min-height:100vh;overflow-x:hidden;display:block}section{display:block;width:100%;float:none;clear:both}",
    "body{background:var(--bg);color:var(--text);font-family:var(--font-mono);min-height:100vh;overflow-x:hidden}"
)

content = content.replace(
    '<section class="hero" style="position:relative;overflow:hidden">',
    '<section class="hero">'
)

with open("compress.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Done")
