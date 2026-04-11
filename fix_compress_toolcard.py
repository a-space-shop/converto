with open("compress.html", "r", encoding="utf-8") as f:
    content = f.read()

# Line 153 has "  </div>\n" which closes result-area
# We need another </div> to close tool-card before </section>
content = content.replace('  </div>\n</section>\n<section class="features">', '  </div>\n  </div>\n</section>\n<section class="features">')

with open("compress.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Done")
