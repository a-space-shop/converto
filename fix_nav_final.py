with open("compress.html", "r", encoding="utf-8") as f:
    content = f.read()

# Remove the unclosed second nav tag and its duplicates
# The second nav starts with: <nav style="position:fixed...position:relative...
content = content.replace(
    '</script><nav style="position:fixed;top:0;left:0;right:0;z-index:100;display:flex;align-items:center;justify-content:space-between;padding:20px 24px;position:relative;background:rgba(10,10,15,0.7);backdrop-filter:blur(16px);border-bottom:1px solid #2a2a3d">\n',
    '</script>\n'
)

with open("compress.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Done")
