with open("compress.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Everything from line 37 onwards (index 36) is corruption
# Cut there and add proper closing tags
result = lines[:36]
result.append('</body>\n')
result.append('</html>\n')

with open("compress.html", "w", encoding="utf-8") as f:
    f.writelines(result)
print(f"Done - {len(result)} lines")
for i, line in enumerate(result[33:], start=34):
    print(f"{i}: {line.rstrip()[:120]}")
