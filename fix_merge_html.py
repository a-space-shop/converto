with open("merge.html", "r", encoding="utf-8") as f:
    content = f.read()

# Find the second <html lang="en"> and everything up to the next <body> and remove the duplicate header
import re

# Remove the duplicate html/head block that starts mid-document
# Pattern: find second occurrence of <!DOCTYPE or <html lang
parts = content.split('<html lang="en">')
print(f"Found {len(parts)-1} <html lang> tags")

if len(parts) == 3:
    # parts[0] = before first html tag
    # parts[1] = between first and second html tag  
    # parts[2] = after second html tag (the real content continues)
    # We need to find where the duplicate head ends (at <body>) and keep from there
    second_part = parts[2]
    body_pos = second_part.find('<body>')
    if body_pos > 0:
        # Remove everything from second <html> up to and including the duplicate <head>...</head>
        fixed = parts[0] + '<html lang="en">' + parts[1] + second_part[body_pos:]
        with open("merge.html", "w", encoding="utf-8") as f:
            f.write(fixed)
        print("Fixed!")
    else:
        print("Could not find body tag in second part")
else:
    print("Unexpected structure - skipping")
