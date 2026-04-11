with open("compress.html", "r", encoding="utf-8") as f:
    nav_top = f.read()

# Get original file
import subprocess
result = subprocess.run(["git", "show", "066ff5e:compress.html"], capture_output=True, text=True, encoding="utf-8")
original = result.stdout

# Find where the second nav ends in the original
# The original has: script toggleMenu -> nav -> ... -> </nav> -> real content
# Find the second </nav> occurrence
first_nav_end = original.find("</nav>")
second_nav_end = original.find("</nav>", first_nav_end + 1)
real_content_start = second_nav_end + len("</nav>")

real_content = original[real_content_start:]
print(f"Real content starts at char {real_content_start}")
print(f"First 200 chars of real content: {repr(real_content[:200])}")

combined = nav_top.rstrip() + "\n" + real_content.lstrip()
with open("compress.html", "w", encoding="utf-8") as f:
    f.write(combined)
print(f"Done - total lines: {len(combined.splitlines())}")
