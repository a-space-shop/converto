with open("word-to-pdf.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Line 148 (index 147) is the duplicate - remove it
del lines[147]

with open("word-to-pdf.html", "w", encoding="utf-8") as f:
    f.writelines(lines)
print("Done")
