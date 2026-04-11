more_tools = """<div class="other-tools">
    <p>More PDF tools</p>
    <div class="tools-row">
      <a href="/pdf-to-word" class="tool-link">&#128196; PDF to Word</a>
      <a href="/merge.html" class="tool-link">&#128206; Merge PDF</a>
      <a href="/compress.html" class="tool-link">&#128220; Compress PDF</a>
      <a href="/split.html" class="tool-link">&#9986;&#65039; Split PDF</a>
      <a href="/jpg-to-pdf" class="tool-link">&#128444;&#65039; JPG to PDF</a>
    </div>
  </div>"""

with open("word-to-pdf.html", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("  </div>\n<script>", "  " + more_tools + "\n  </div>\n<script>")

with open("word-to-pdf.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Done")
