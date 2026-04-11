import subprocess

# Get original from git
result = subprocess.run(["git", "show", "066ff5e:compress.html"], capture_output=True, text=True, encoding="utf-8")
original = result.stdout

# The original structure is:
# <head>...</head><body><nav>...</nav><div id="mobile-menu">...</div><style>...<script>toggleMenu
# <nav>...</nav><div id="mobile-menu">...</div><style>...<script>toggleMenu  <- DUPLICATE
# REAL CONTENT STARTS HERE

# Find the second toggleMenu script - that marks end of duplicate
toggle1 = original.find("function toggleMenu")
toggle2 = original.find("function toggleMenu", toggle1 + 1)
script_end = original.find("</script>", toggle2) + len("</script>")

real_content_start = script_end
real_content = original[real_content_start:]
print(f"Real content first 200: {repr(real_content[:200])}")

# Get our clean nav (lines 1-36)
with open("compress.html", "r", encoding="utf-8") as f:
    nav = f.read()

combined = nav.rstrip().replace("</body>\n</html>", "").strip() + "\n" + real_content.lstrip()
with open("compress.html", "w", encoding="utf-8") as f:
    f.write(combined)
print(f"Done - {len(combined.splitlines())} lines")
