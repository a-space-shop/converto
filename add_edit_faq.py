with open("edit.html", "r", encoding="utf-8") as f:
    content = f.read()

if 'class="content-section"' in content:
    print("Already has FAQ")
    exit()

faq_css = """
    .content-section{position:relative;z-index:1;max-width:700px;margin:60px auto;padding:0 24px}
    .content-section h2{font-family:var(--font-display);font-size:28px;font-weight:800;margin-bottom:16px;letter-spacing:-1px}
    .content-section p{font-size:14px;color:var(--muted);line-height:1.8;margin-bottom:16px}
    .faq{margin-top:48px}
    .faq h2{font-family:var(--font-display);font-size:28px;font-weight:800;margin-bottom:24px;letter-spacing:-1px}
    .faq-item{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:20px 24px;margin-bottom:12px}
    .faq-q{font-family:var(--font-display);font-size:14px;font-weight:700;margin-bottom:8px}
    .faq-a{font-size:13px;color:var(--muted);line-height:1.7}
"""

new_section = """
<section class="content-section">
  <h2>How to Edit a PDF Online</h2>
  <p>Upload your PDF by dragging it into the editor or clicking to browse. Once loaded, use the toolbar to add text, highlight sections, draw freehand, and annotate your document. All tools are available instantly in your browser.</p>
  <p>Everything runs locally in your browser — your file is never uploaded to any server. Completely private and free with no sign-up required.</p>
  <div class="faq">
    <h2>Frequently Asked Questions</h2>
    <div class="faq-item"><div class="faq-q">What can I do with the PDF editor?</div><div class="faq-a">Add text, highlight content, draw freehand, add shapes, and annotate your PDF without needing Adobe Acrobat or any other software.</div></div>
    <div class="faq-item"><div class="faq-q">Do I need to install any software?</div><div class="faq-a">No. The editor runs entirely in your browser on any modern device.</div></div>
    <div class="faq-item"><div class="faq-q">Are my files kept private?</div><div class="faq-a">Yes. All editing happens locally. Your PDF is never uploaded to any server.</div></div>
    <div class="faq-item"><div class="faq-q">Can I save my edited PDF?</div><div class="faq-a">Yes. Click Download to save your edited PDF with all annotations applied.</div></div>
    <div class="faq-item"><div class="faq-q">What browsers are supported?</div><div class="faq-a">Chrome, Firefox, Safari, and Edge. We recommend the latest version of Chrome.</div></div>
    <div class="faq-item"><div class="faq-q">Is there a file size limit?</div><div class="faq-a">No strict limit since processing happens in your browser.</div></div>
    <div class="faq-item"><div class="faq-q">Can I edit text in a PDF?</div><div class="faq-a">You can add text annotations on top. To edit original text use our PDF to Word tool first.</div></div>
    <div class="faq-item"><div class="faq-q">Is the PDF editor free?</div><div class="faq-a">Yes. Completely free with no limits and no sign-up required.</div></div>
  </div>
</section>"""

if ".content-section{" not in content:
    content = content.replace("</style>", faq_css + "\n  </style>", 1)

if "</body>" in content:
    content = content.replace("</body>", new_section + "\n</body>")
    print("DONE: edit.html")
else:
    content += new_section
    print("DONE (appended): edit.html")

with open("edit.html", "w", encoding="utf-8") as f:
    f.write(content)
