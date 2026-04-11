with open("split.html", "r", encoding="utf-8") as f:
    content = f.read()

old = "downloadArea.classList.add('visible')\nfinally{splitBtn.classList.remove('loading');splitBtn.disabled=false}"
new = "downloadArea.classList.add('visible')\n}catch(err){errorMsg.textContent='Failed: '+err.message;errorMsg.classList.add('visible');if(typeof gtag!=='undefined')gtag('event','conversion_failed',{tool:'split'});progressW.classList.remove('visible')}\nfinally{splitBtn.classList.remove('loading');splitBtn.disabled=false}"

if old in content:
    content = content.replace(old, new)
    print("Fixed!")
else:
    print("Pattern not found")

with open("split.html", "w", encoding="utf-8") as f:
    f.write(content)
