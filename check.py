with open("compress.html", "r", encoding="utf-8") as f:
    content = f.read()
# Print everything between </nav> and first section
nav_end = content.find("</nav>")
section_start = content.find("<section")
print(repr(content[nav_end:section_start]))
