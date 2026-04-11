with open("compress.html", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace(
    '.hero{position:relative;z-index:1;padding:100px 24px 60px;text-align:center}',
    '.hero{position:relative;z-index:1;padding:100px 24px 60px;text-align:center;width:100%;box-sizing:border-box}'
)
content = content.replace(
    '.features{position:relative;z-index:1;max-width:700px;margin:80px auto;padding:0 24px;clear:both}',
    '.features{position:relative;z-index:1;max-width:700px;margin:80px auto;padding:0 24px}'
)

with open("compress.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Done")
