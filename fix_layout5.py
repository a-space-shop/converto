with open("compress.html", "r", encoding="utf-8") as f:
    content = f.read()

# Force hero to be full viewport width
content = content.replace(
    '.hero{position:relative;z-index:1;padding:100px 24px 60px;text-align:center;width:100%;box-sizing:border-box}',
    '.hero{position:relative;z-index:1;padding:100px 24px 60px;text-align:center;display:block;width:100vw;margin-left:calc(-50vw + 50%);box-sizing:border-box}'
)

with open("compress.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Done")
