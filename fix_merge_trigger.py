with open("merge.html", "r", encoding="utf-8") as f:
    content = f.read()

# Remove donate trigger from downloadArea line
content = content.replace(
    "downloadArea.classList.add('visible')\n    document.getElementById('donate-banner').style.display='flex';",
    "downloadArea.classList.add('visible')"
)

# Make sure downloadBtn.onclick has the trigger
content = content.replace(
    "downloadBtn.onclick=()=>{const a=document.createElement('a');a.href=url;a.download='merged.pdf';a.click();}",
    "downloadBtn.onclick=()=>{const a=document.createElement('a');a.href=url;a.download='merged.pdf';a.click();document.getElementById('donate-banner').style.display='flex';}"
)

with open("merge.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Done")
