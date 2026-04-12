files = ["index.html","merge.html","compress.html","split.html","convert.html","pdf-to-word.html","word-to-pdf.html","pdf-to-excel.html","jpg-to-pdf.html"]

donate_link = '  <a href="https://paypal.me/editpdffyi" target="_blank" style="display:block;padding:14px 0;font-size:15px;font-weight:500;text-decoration:none;color:#fff;border-top:1px solid #2a2a3d;margin-top:8px;text-align:center;">&#9829;&nbsp;Donate</a>\n'

for f in files:
    with open(f, "r", encoding="utf-8") as fh:
        content = fh.read()
    # Add donate link before closing </div> of mobile menu
    if 'paypal.me' not in content.split('id="mobile-menu"')[1].split('</div>')[0]:
        content = content.replace(
            '  <a href="/split.html" style="display:block;padding:14px 0;font-size:15px;font-weight:500;text-decoration:none;background:linear-gradient(135deg,#f76a8c,#f7a06a);-webkit-background-clip:text;-webkit-text-fill-color:transparent;">Split PDF</a>\n</div>',
            '  <a href="/split.html" style="display:block;padding:14px 0;font-size:15px;font-weight:500;text-decoration:none;background:linear-gradient(135deg,#f76a8c,#f7a06a);-webkit-background-clip:text;-webkit-text-fill-color:transparent;">Split PDF</a>\n' + donate_link + '</div>'
        )
        with open(f, "w", encoding="utf-8") as fh:
            fh.write(content)
        print(f"Fixed {f}")
    else:
        print(f"Already has donate: {f}")
