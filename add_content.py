import os

pages = {
    "compress.html": {
        "how_to_title": "How to Compress a PDF",
        "how_to_p1": "Compressing a PDF with EditPDF is simple and completely free. Start by uploading your PDF file — either drag it into the upload box or click to browse your files. Once uploaded, click the Compress PDF button. Our tool will process your file entirely in your browser, reducing the file size while maintaining as much quality as possible. When compression is complete, you can see exactly how much space was saved before downloading your compressed PDF.",
        "how_to_p2": "There is no sign-up required and your files never leave your device. Everything happens locally in your browser, which means your documents stay completely private.",
        "faqs": [
            ("How much can I reduce a PDF file size?", "The amount of compression depends on the content of your PDF. Image-heavy PDFs can often be reduced by 50-90%. PDFs that are mostly text may see smaller reductions of 10-30%."),
            ("Will compressing a PDF reduce its quality?", "Our compression tool focuses on reducing file size with minimal quality loss. For most documents the difference is not noticeable."),
            ("Is there a file size limit?", "You can compress PDF files up to 100MB. If your file is larger, try splitting it first using our Split PDF tool."),
            ("Why do I need to compress a PDF?", "Compressed PDFs are easier to email, upload to websites, and store. Many email providers have attachment limits of 10-25MB."),
            ("Is my PDF safe when I compress it?", "Yes. EditPDF compresses your PDF entirely in your browser. Your file is never uploaded to any server."),
            ("Can I compress a scanned PDF?", "Yes. Scanned PDFs are usually image-based and often respond very well to compression, sometimes achieving reductions of 70% or more."),
        ]
    },
    "merge.html": {
        "how_to_title": "How to Merge PDF Files",
        "how_to_p1": "Merging PDF files with EditPDF takes just a few clicks. Upload the PDF files you want to combine by dragging them into the upload area or clicking to browse. You can upload multiple files at once. Once uploaded, drag and reorder the files into the sequence you want. When happy with the order, click the Merge PDFs button.",
        "how_to_p2": "The entire process runs in your browser — no files are uploaded to any server. You can merge as many PDFs as you need, completely free and without signing up.",
        "faqs": [
            ("How many PDF files can I merge at once?", "You can merge as many PDF files as you need. There is no hard limit on the number of files."),
            ("Can I reorder pages before merging?", "Yes. After uploading your files you can drag and drop them into any order before merging."),
            ("Is there a file size limit for merging?", "Individual files can be up to 100MB each."),
            ("Will merging PDFs reduce their quality?", "No. Merging PDFs does not affect the quality of the content. Text, images, and formatting are preserved exactly."),
            ("Do I need to create an account?", "No. EditPDF is completely free and requires no sign-up or account creation."),
            ("Are my files kept private?", "Yes. Merging happens entirely in your browser. Your files are never sent to any server."),
        ]
    },
    "split.html": {
        "how_to_title": "How to Split a PDF",
        "how_to_p1": "Splitting a PDF with EditPDF is quick and easy. Upload your PDF file by dragging it into the upload box or clicking to browse. Once uploaded, choose how you want to split it — extract specific pages, split by page range, or separate every page into its own file. Then click the Split PDF button.",
        "how_to_p2": "Everything runs directly in your browser with no file uploads to any server. Your documents stay completely private, and the tool is free with no account required.",
        "faqs": [
            ("Can I extract specific pages from a PDF?", "Yes. You can choose exactly which pages to extract by entering page numbers or ranges."),
            ("Can I split a PDF into individual pages?", "Yes. You can separate every page of a PDF into its own individual file."),
            ("Is there a page limit for splitting?", "There is no strict page limit. You can split PDFs of any length."),
            ("Will splitting affect the quality of my PDF?", "No. Splitting a PDF does not affect its quality. The extracted pages will be identical to the original."),
            ("Can I split a password-protected PDF?", "Password-protected PDFs cannot be split without first removing the password protection."),
            ("Are my files private when I split them?", "Yes. All processing happens in your browser. Your files are never sent to a server."),
        ]
    },
    "pdf-to-word.html": {
        "how_to_title": "How to Convert PDF to Word",
        "how_to_p1": "Converting a PDF to Word with EditPDF takes just a few seconds. Upload your PDF file by dragging it into the upload box or clicking to browse. Once uploaded, click the Convert to Word button. Our servers will process your PDF and produce a fully editable Word document (DOCX) ready to download.",
        "how_to_p2": "EditPDF uses LibreOffice and advanced Python libraries to preserve fonts, layout, tables, and images. Files are permanently deleted within 60 minutes. No sign-up required.",
        "faqs": [
            ("Is the PDF to Word conversion accurate?", "We use LibreOffice and advanced Python libraries to preserve text, fonts, tables, images, and layout as closely as possible."),
            ("Can I edit the Word document after conversion?", "Yes. The resulting DOCX file is fully editable in Microsoft Word, Google Docs, and LibreOffice Writer."),
            ("What is the maximum file size?", "The maximum file size is 25MB. If larger, try compressing it first."),
            ("Can I convert a scanned PDF to Word?", "Scanned PDFs are images rather than text. For best results use a digitally created PDF."),
            ("How long are my files kept on your servers?", "Your files are permanently deleted within 60 minutes of conversion."),
            ("Do I need Microsoft Word?", "No. Microsoft Word, Google Docs, and LibreOffice Writer all support the DOCX format."),
        ]
    },
    "word-to-pdf.html": {
        "how_to_title": "How to Convert Word to PDF",
        "how_to_p1": "Converting a Word document to PDF with EditPDF is simple. Upload your DOCX or DOC file by dragging it into the upload box or clicking to browse. Click Convert to PDF and our servers will produce a professional PDF preserving your fonts, images, tables, and layout.",
        "how_to_p2": "PDF files are universally readable, cannot be accidentally edited, and look the same on every device. No sign-up required and files are permanently deleted within 60 minutes.",
        "faqs": [
            ("Will my formatting be preserved?", "Yes. We use LibreOffice which preserves fonts, images, tables, headers, footers and page layout with high accuracy."),
            ("Do you support .doc as well as .docx?", "Yes. We support both .docx and .doc formats."),
            ("Is there a file size limit?", "The maximum file size is 25MB."),
            ("Why convert Word to PDF?", "PDF files are universally readable, preserve formatting exactly, and are the standard for professional documents."),
            ("How long are my files kept on your servers?", "Your files are permanently deleted within 60 minutes."),
            ("Is this tool free?", "Yes. Word to PDF conversion is completely free with no limits and no sign-up required."),
        ]
    },
    "pdf-to-excel.html": {
        "how_to_title": "How to Convert PDF to Excel",
        "how_to_p1": "Converting a PDF to Excel with EditPDF is quick and easy. Upload your PDF, click Convert to Excel, and our servers will extract tables and data into an editable XLSX spreadsheet ready to download.",
        "how_to_p2": "Works best with digitally created PDFs containing clear table structures. Files are permanently deleted within 60 minutes. No sign-up required.",
        "faqs": [
            ("How accurate is PDF to Excel conversion?", "PDFs with clearly formatted tables convert with high accuracy. Scanned PDFs may require some manual cleanup."),
            ("What types of PDFs work best?", "Digitally created PDFs with clear table structures. Bank statements and financial reports typically convert well."),
            ("Is there a file size limit?", "The maximum file size is 25MB."),
            ("Can I edit the spreadsheet after conversion?", "Yes. The XLSX file is fully editable in Microsoft Excel, Google Sheets, and LibreOffice Calc."),
            ("How long are my files kept on your servers?", "Permanently deleted within 60 minutes."),
            ("Do I need Microsoft Excel?", "No. Google Sheets and LibreOffice Calc also support XLSX."),
        ]
    },
    "jpg-to-pdf.html": {
        "how_to_title": "How to Convert JPG to PDF",
        "how_to_p1": "Upload your JPG, PNG, or other image files by dragging them into the upload box. You can upload multiple images at once and reorder them to set the page order. Click Convert to PDF and your document is ready instantly.",
        "how_to_p2": "Runs entirely in your browser — no files uploaded to any server. Supports JPG, PNG, WEBP and other formats. Completely free with no sign-up required.",
        "faqs": [
            ("What image formats are supported?", "EditPDF supports JPG, JPEG, PNG, and WEBP. You can mix formats in the same PDF."),
            ("Can I combine multiple images into one PDF?", "Yes. Each image becomes a separate page. You can drag to reorder before converting."),
            ("Will the image quality be preserved?", "Yes. Images are embedded at their original resolution."),
            ("Is there a limit on how many images I can convert?", "No strict limit. The practical limit is your browser memory."),
            ("Are my images private?", "Yes. Everything happens in your browser. Images are never sent to any server."),
            ("Why convert images to PDF?", "PDF is the universal format for sharing and printing. It lets you combine multiple images into one organised document."),
        ]
    },
    "convert.html": {
        "how_to_title": "How to Convert Files Online",
        "how_to_p1": "Select the format you want to convert from and to using the dropdowns. Upload your file and click Convert. Our servers produce a high-quality converted document ready to download in seconds.",
        "how_to_p2": "Supports PDF, Word, Excel, PowerPoint, JPG, PNG and more. Files are permanently deleted within 60 minutes. No sign-up required.",
        "faqs": [
            ("What file formats can I convert?", "PDF, Word (DOCX), Excel (XLSX), PowerPoint (PPTX), JPG, PNG, HTML and more."),
            ("How accurate is the conversion?", "We use LibreOffice and best-in-class Python libraries to preserve text, fonts, tables, images, and layout."),
            ("Is there a file size limit?", "The maximum file size is 25MB."),
            ("How long does conversion take?", "Most conversions complete in under 10 seconds."),
            ("Are my files kept private?", "Files are processed on secure servers and permanently deleted within 60 minutes."),
            ("Do I need to sign up?", "No. All conversions are completely free with no account required."),
        ]
    },
    "edit.html": {
        "how_to_title": "How to Edit a PDF Online",
        "how_to_p1": "Upload your PDF by dragging it into the editor or clicking to browse. Once loaded, use the toolbar to add text, highlight sections, draw freehand, and annotate your document. All tools are available instantly in your browser.",
        "how_to_p2": "Everything runs locally in your browser — your file is never uploaded to any server. Completely private and free with no sign-up required.",
        "faqs": [
            ("What can I do with the PDF editor?", "Add text, highlight content, draw freehand, add shapes, and annotate your PDF without needing Adobe Acrobat."),
            ("Do I need to install any software?", "No. The editor runs entirely in your browser on any modern device."),
            ("Are my files kept private?", "Yes. All editing happens locally. Your PDF is never uploaded to any server."),
            ("Can I save my edited PDF?", "Yes. Click Download to save your edited PDF with all annotations applied."),
            ("What browsers are supported?", "Chrome, Firefox, Safari, and Edge. We recommend the latest version of Chrome."),
            ("Is there a file size limit?", "No strict limit since processing happens in your browser."),
            ("Can I edit text in a PDF?", "You can add text annotations on top. To edit original text, use our PDF to Word tool first."),
            ("Is the PDF editor free?", "Yes. Completely free with no limits and no sign-up required."),
        ]
    },
}

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

for filename, data in pages.items():
    if not os.path.exists(filename):
        print(f"SKIP: {filename}")
        continue
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    if 'class="content-section"' in content:
        print(f"ALREADY HAS content: {filename}")
        continue
    faq_html = ""
    for q, a in data["faqs"]:
        faq_html += f'    <div class="faq-item"><div class="faq-q">{q}</div><div class="faq-a">{a}</div></div>\n'
    new_section = f'\n<section class="content-section">\n  <h2>{data["how_to_title"]}</h2>\n  <p>{data["how_to_p1"]}</p>\n  <p>{data["how_to_p2"]}</p>\n  <div class="faq">\n    <h2>Frequently Asked Questions</h2>\n{faq_html}  </div>\n</section>'
    if ".content-section{" not in content:
        content = content.replace("</style>", faq_css + "\n  </style>", 1)
    if "<footer" in content:
        content = content.replace("<footer", new_section + "\n<footer", 1)
        print(f"DONE: {filename}")
    else:
        content += new_section
        print(f"DONE (appended): {filename}")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

print("All done!")
