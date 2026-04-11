with open("compress.html", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace(
    '.features-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:16px}',
    '.features-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:20px;max-width:900px;margin:0 auto}'
)
content = content.replace(
    '.feat{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:24px;transition:border-color .2s,transform .2s}',
    '.feat{background:var(--card);border:1px solid var(--border);border-radius:20px;padding:32px;transition:border-color .2s,transform .2s}'
)
content = content.replace(
    '.feat-icon{font-size:24px;margin-bottom:12px}',
    '.feat-icon{font-size:32px;margin-bottom:16px}'
)
content = content.replace(
    '.feat-title{font-family:var(--font-display);font-size:14px;font-weight:700;margin-bottom:6px}',
    '.feat-title{font-family:var(--font-display);font-size:16px;font-weight:700;margin-bottom:8px}'
)
content = content.replace(
    '.feat-desc{font-size:12px;color:var(--muted);line-height:1.6}',
    '.feat-desc{font-size:13px;color:var(--muted);line-height:1.7}'
)

with open("compress.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Done")
