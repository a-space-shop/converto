more_tools = """\n  <div class="other-tools">\n    <p>More PDF tools</p>\n    <div class="tools-row">\n      <a href="/pdf-to-word.html" class="tool-link">&#128196; PDF to Word</a>\n      <a href="/merge.html" class="tool-link">&#128206; Merge PDF</a>\n      <a href="/compress.html" class="tool-link">&#128220; Compress PDF</a>\n      <a href="/split.html" class="tool-link">&#9986;&#65039; Split PDF</a>\n      <a href="/jpg-to-pdf.html" class="tool-link">&#128444;&#65039; JPG to PDF</a>\n    </div>\n  </div>"""

with open("word-to-pdf.html", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("  </div>\n\n<script>", "  </div>" + more_tools + "\n\n<script>")

with open("word-to-pdf.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Done")
