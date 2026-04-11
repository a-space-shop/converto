files = {
    "pdf-to-word.html": "tool:'pdf-to-word'",
    "word-to-pdf.html": "tool:'word-to-pdf'",
    "pdf-to-excel.html": "tool:'pdf-to-excel'",
    "jpg-to-pdf.html": "tool:'jpg-to-pdf'",
}

for filename, tool in files.items():
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    old = "downloadArea.classList.add('visible')\n    finally{convertBtn.classList.remove('loading');convertBtn.disabled=false}"
    new = f"downloadArea.classList.add('visible')\n    }}catch(err){{errorMsg.textContent='Failed: '+err.message;errorMsg.classList.add('visible');if(typeof gtag!=='undefined')gtag('event','conversion_failed',{{{tool}}});progressW.classList.remove('visible')}}\n    finally{{convertBtn.classList.remove('loading');convertBtn.disabled=false}}"

    if old in content:
        content = content.replace(old, new)
        print(f"Fixed {filename}")
    else:
        print(f"Pattern not found in {filename}")

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
