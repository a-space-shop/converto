with open("compress.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Find first occurrence of duplicate <style> after line 35
cut_at = None
for i in range(36, len(lines)):
    if '<style>' in lines[i] and 'nav-links' in lines[i]:
        cut_at = i
        break

if cut_at:
    lines = lines[:cut_at]
    print(f"Cut at line {cut_at+1}, now {len(lines)} lines")
else:
    print("Cut point not found")

with open("compress.html", "w", encoding="utf-8") as f:
    f.writelines(lines)
