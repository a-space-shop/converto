with open("compress.html", "r", encoding="utf-8") as f:
    content = f.read()

# Force single column by wrapping body content in a block container
# The simplest fix - add CSS to force sections to be full width blocks
old = "body{background:var(--bg);color:var(--text);font-family:var(--font-mono);min-height:100vh;overflow-x:hidden}"
new = "body{background:var(--bg);color:var(--text);font-family:var(--font-mono);min-height:100vh;overflow-x:hidden;display:block}section{display:block;width:100%;float:none;clear:both}"

content = content.replace(old, new)

with open("compress.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Done")
