with open("merge.html", "r", encoding="utf-8") as f:
    content = f.read()
idx = content.find("paypal.me")
print(repr(content[max(0,idx-100):idx+100]))
