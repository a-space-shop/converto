with open("compress.html", "r", encoding="utf-8") as f:
    nav_top = f.read()

import subprocess
result = subprocess.run(["git", "show", "066ff5e:compress.html"], capture_output=True, text=True, encoding="utf-8")
original = result.stdout

# The original has TWO complete navs followed by mobile-menu then real content
# We want everything after the second mobile-menu closing </div>
# Find third </div> after second nav end
first_nav_end = original.find("</nav>")
second_nav_end = original.find("</nav>", first_nav_end + 1)

# After second nav, skip the mobile-menu div
after_second_nav = original[second_nav_end + len("</nav>"):]
mobile_menu_end = after_second_nav.find("</div>")
real_content = after_second_nav[mobile_menu_end + len("</div>"):]

print(f"First 150 chars of real content: {repr(real_content[:150])}")

combined = nav_top.rstrip() + "\n" + real_content.lstrip()
with open("compress.html", "w", encoding="utf-8") as f:
    f.write(combined)
print(f"Done - total lines: {len(combined.splitlines())}")
