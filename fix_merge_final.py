with open("merge.html", "r", encoding="utf-8") as f:
    content = f.read()

# Fix 1: add donate trigger inside downloadBtn.onclick
content = content.replace(
    "downloadBtn.onclick=()=>{const a=document.createElement('a');a.href=url;a.download='merged.pdf';a.click()}",
    "downloadBtn.onclick=()=>{const a=document.createElement('a');a.href=url;a.download='merged.pdf';a.click();document.getElementById('donate-banner').style.display='flex';}"
)

# Fix 2: remove the stale loose trigger on line 308
content = content.replace(
    "\n    document.getElementById('donate-banner').style.display='flex';;if(typeof\ngtag!=='undefined')gtag('event','conversion_success',{tool:'merge'});;\n",
    "\n    if(typeof gtag!=='undefined')gtag('event','conversion_success',{tool:'merge'});\n"
)

with open("merge.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Done")
