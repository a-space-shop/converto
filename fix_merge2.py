with open("merge.html", "r", encoding="utf-8") as f:
    content = f.read()

# Remove the injected "<!DOCTYPE html>\n<body>" that appears mid-document
content = content.replace('</script><!DOCTYPE html>\n<body>', '</script>')

with open("merge.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Done")
