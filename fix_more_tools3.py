with open("pdf-to-word.html", "r", encoding="utf-8") as f:
    ref = f.read()

start = ref.find('<section style="position:relative;z-index:1;max-width:700px;margin:40px auto;padding:0 24px;text-align:center">')
end = ref.find('</section>', start) + len('</section>')
more_tools = ref[start:end]

with open("word-to-pdf.html", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace('  </div>\n<script>', '  </div>\n' + more_tools + '\n<script>')

with open("word-to-pdf.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Done")
print("Inserted:", more_tools[:100])
