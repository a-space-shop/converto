import re

files = {
    "merge.html": "document.getElementById('donate-banner').style.display='flex';",
    "compress.html": "document.getElementById('donate-banner').style.display='flex';",
    "split.html": "document.getElementById('donate-banner').style.display='flex';",
    "pdf-to-word.html": "document.getElementById('donate-banner').style.display='flex';",
    "word-to-pdf.html": "document.getElementById('donate-banner').style.display='flex';",
    "pdf-to-excel.html": "document.getElementById('donate-banner').style.display='flex';",
    "jpg-to-pdf.html": "document.getElementById('donate-banner').style.display='flex';",
}

for filename in files:
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Find downloadBtn.onclick and replace with expanded version
    old = "downloadBtn.onclick=()=>{"
    new = "downloadBtn.onclick=()=>{\n    document.getElementById('donate-banner').style.display='flex';\n    "
    
    if old in content and "donate-banner" not in content.split(old)[1].split("}")[0]:
        content = content.replace(old, new, 1)
        print(f"Added trigger to {filename}")
    else:
        print(f"Skipped {filename} - already has trigger or pattern not found")
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

print("All done!")
