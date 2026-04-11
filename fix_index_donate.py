with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace(
    "background:linear-gradient(135deg,#7c6af7,#f76a8c);color:#fff;border:none;border-radius:8px;padding:8px 18px;font-family:Syne,sans-serif;font-size:13px;font-weight:700;cursor:pointer;text-decoration:none;white-space:nowrap;\">&#9829;&nbsp;Donate</a></div>",
    "background:linear-gradient(135deg,#00ff87,#60efff);color:#0a0a0f;border:none;border-radius:8px;padding:8px 18px;font-family:Syne,sans-serif;font-size:13px;font-weight:700;cursor:pointer;text-decoration:none;white-space:nowrap;\">&#9829;&nbsp;Donate</a></div>"
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Done")
