# Get the more tools section from pdf-to-word.html as reference
with open("pdf-to-word.html", "r", encoding="utf-8") as f:
    ref = f.read()

# Find the more tools section
start = ref.find('<section style="position:relative;z-index:1;max-width:700px;margin:40px auto;padding:0 24px;text-align:center">')
end = ref.find('</section>', start) + len('</section>')
more_tools = ref[start:end]
print("Found section:")
print(more_tools[:200])

# Insert it into word-to-pdf.html before <script>
with open("word-to-pdf.html", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace('\n<script>', '\n' + more_tools + '\n<script>', 1)

with open("word-to-pdf.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Done")
