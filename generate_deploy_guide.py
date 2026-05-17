"""Run this once to generate the deployment guide Word document."""
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

doc = Document()

# ── Page margins ──────────────────────────────────────────────────────────────
section = doc.sections[0]
section.top_margin    = Inches(1)
section.bottom_margin = Inches(1)
section.left_margin   = Inches(1.2)
section.right_margin  = Inches(1.2)

# ── Helpers ───────────────────────────────────────────────────────────────────
def heading1(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(18)
    p.paragraph_format.space_after  = Pt(4)
    run = p.add_run(text)
    run.bold = True
    run.font.size = Pt(16)
    run.font.color.rgb = RGBColor(0x1A, 0x1A, 0x80)
    return p

def heading2(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after  = Pt(2)
    run = p.add_run(text)
    run.bold = True
    run.font.size = Pt(12)
    run.font.color.rgb = RGBColor(0x44, 0x44, 0xAA)
    return p

def body(text):
    p = doc.add_paragraph(text)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.left_indent = Inches(0)
    for run in p.runs:
        run.font.size = Pt(11)
    return p

def bullet(text, indent=0):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.left_indent = Inches(0.3 + indent * 0.25)
    run = p.add_run(text)
    run.font.size = Pt(11)
    return p

def code_block(text):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent  = Inches(0.3)
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after  = Pt(4)
    # light grey shading
    pPr = p._p.get_or_add_pPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), 'F0F0F0')
    pPr.append(shd)
    run = p.add_run(text)
    run.font.name = 'Courier New'
    run.font.size = Pt(10)
    return p

def note(text):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent  = Inches(0.3)
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after  = Pt(6)
    run = p.add_run("⚠  " + text)
    run.font.size = Pt(10)
    run.font.italic = True
    run.font.color.rgb = RGBColor(0xAA, 0x66, 0x00)
    return p

def divider():
    doc.add_paragraph("─" * 72)

def checkbox(text):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.3)
    p.paragraph_format.space_after = Pt(4)
    run = p.add_run("☐  " + text)
    run.font.size = Pt(11)
    return p

# ══════════════════════════════════════════════════════════════════════════════
# TITLE PAGE
# ══════════════════════════════════════════════════════════════════════════════
title = doc.add_paragraph()
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
title.paragraph_format.space_before = Pt(40)
title.paragraph_format.space_after  = Pt(8)
tr = title.add_run("editpdf.fyi — Server Deployment Guide")
tr.bold = True
tr.font.size = Pt(22)
tr.font.color.rgb = RGBColor(0x1A, 0x1A, 0x80)

sub = doc.add_paragraph()
sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
sub.paragraph_format.space_after = Pt(4)
sr = sub.add_run("Step-by-step instructions for uploading updated files to your VPS")
sr.font.size = Pt(12)
sr.font.color.rgb = RGBColor(0x66, 0x66, 0x66)

date_p = doc.add_paragraph()
date_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
date_p.paragraph_format.space_after = Pt(32)
dr = date_p.add_run("Updated: April 2026")
dr.font.size = Pt(10)
dr.font.color.rgb = RGBColor(0x99, 0x99, 0x99)

divider()

# ══════════════════════════════════════════════════════════════════════════════
# BEFORE YOU START
# ══════════════════════════════════════════════════════════════════════════════
heading1("Before You Start — One-Time Setup")

body("You only need to do this section once. If you have already done it, skip to Step 1.")

heading2("Generate Your FERNET_KEY")

body("The server will not start without this. Run the command below on your local machine or directly on the VPS:")

code_block("python -c \"from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())\"")

body("Copy the output. It will look like this (yours will be different):")

code_block("fGpZ2kL9mXqR7vNwYhJcUeAsDfTbOiPl3uCnKjHyWx8=")

note("Save this key somewhere safe — a password manager, a notes app, anywhere secure. If you lose it you will need to generate a new one and restart the server.")

heading2("Set the FERNET_KEY on Your VPS")

body("How you set it depends on how you run the server. Choose the method that matches your setup:")

heading2("Option A — If you start the server manually (SSH session)")
code_block("export FERNET_KEY=\"paste-your-key-here\"\nuvicorn main:app --host 0.0.0.0 --port 8000")

note("This only lasts until you close the SSH session. Use Option B or C for a permanent setup.")

heading2("Option B — If you use a .env file")
body("Open or create a file called .env in your backend folder on the server and add:")
code_block("FERNET_KEY=paste-your-key-here")
body("Then start the server with:")
code_block("uvicorn main:app --host 0.0.0.0 --port 8000 --env-file .env")

heading2("Option C — If you use systemd (recommended for production)")
body("Edit your service file:")
code_block("sudo nano /etc/systemd/system/editpdf.service")
body("Add this line inside the [Service] section:")
code_block("Environment=\"FERNET_KEY=paste-your-key-here\"")
body("Then reload and restart:")
code_block("sudo systemctl daemon-reload\nsudo systemctl restart editpdf")

divider()

# ══════════════════════════════════════════════════════════════════════════════
# STEP 1 — UPLOAD FILES
# ══════════════════════════════════════════════════════════════════════════════
heading1("Step 1 — Upload the Updated Files to Your Server")

body("The updated files are in this folder on your Windows machine:")
code_block("D:\\Test editpdf.fyi\\backend\\")

body("You need to copy them to your VPS. Use whichever method you normally use:")

heading2("Method A — SCP (command line on Windows)")
body("Open PowerShell or Command Prompt and run:")
code_block("scp -r \"D:\\Test editpdf.fyi\\backend\\*.html\" user@your-server-ip:/path/to/editpdf/\nscp \"D:\\Test editpdf.fyi\\backend\\main.py\" user@your-server-ip:/path/to/editpdf/")
body("Replace user, your-server-ip, and /path/to/editpdf/ with your actual values.")

heading2("Method B — FileZilla or WinSCP (graphical SFTP)")
bullet("Open FileZilla or WinSCP")
bullet("Connect to your server using SFTP (not FTP)")
bullet("Navigate to your backend folder on the left (local) panel")
bullet("Navigate to the editpdf folder on the right (server) panel")
bullet("Drag and drop these files from left to right:", indent=0)
bullet("main.py", indent=1)
bullet("index.html", indent=1)
bullet("about.html", indent=1)
bullet("compress.html", indent=1)
bullet("merge.html", indent=1)
bullet("split.html", indent=1)
bullet("edit.html", indent=1)
bullet("convert.html", indent=1)
bullet("pdf-to-word.html", indent=1)
bullet("word-to-pdf.html", indent=1)
bullet("jpg-to-pdf.html", indent=1)
bullet("pdf-to-excel.html", indent=1)
bullet("privacy.html", indent=1)

heading2("Method C — rsync (if you have WSL or Git Bash)")
code_block("rsync -avz --include='*.html' --include='*.py' --exclude='*' \\\n  \"D:/Test editpdf.fyi/backend/\" \\\n  user@your-server-ip:/path/to/editpdf/")

note("Do NOT upload the fix_*.py scripts. They are old throwaway scripts and are not part of the running site.")

divider()

# ══════════════════════════════════════════════════════════════════════════════
# STEP 2 — VERIFY UPLOAD
# ══════════════════════════════════════════════════════════════════════════════
heading1("Step 2 — Verify the Files Uploaded Correctly")

body("SSH into your server and check the files are there:")
code_block("ssh user@your-server-ip\nls -la /path/to/editpdf/")

body("Confirm you can see main.py and all the .html files with today's date on them.")

body("Check that the Converto references are gone:")
code_block("grep -ri 'converto' /path/to/editpdf/*.py /path/to/editpdf/*.html")

body("This should return no results. If it does return something in main.py or an HTML file, the upload did not include the updated version — re-upload that file.")

divider()

# ══════════════════════════════════════════════════════════════════════════════
# STEP 3 — RESTART THE SERVER
# ══════════════════════════════════════════════════════════════════════════════
heading1("Step 3 — Restart the Server")

note("Make sure FERNET_KEY is set (see Before You Start) before restarting. The server will not start without it.")

heading2("If you use systemd:")
code_block("sudo systemctl restart editpdf\nsudo systemctl status editpdf")
body("Look for 'Active: active (running)' in the status output. If you see an error about FERNET_KEY, go back to the Before You Start section.")

heading2("If you run uvicorn manually:")
code_block("# Stop the old process first\npkill -f uvicorn\n\n# Start with the key set\nexport FERNET_KEY=\"your-key-here\"\ncd /path/to/editpdf\nuvicorn main:app --host 0.0.0.0 --port 8000")

heading2("If you use Docker:")
code_block("docker stop editpdf\ndocker run -d --name editpdf \\\n  -e FERNET_KEY=\"your-key-here\" \\\n  -p 8000:8000 \\\n  your-image-name")

divider()

# ══════════════════════════════════════════════════════════════════════════════
# STEP 4 — TEST THE LIVE SITE
# ══════════════════════════════════════════════════════════════════════════════
heading1("Step 4 — Test the Live Site")

body("Open a browser and go to https://editpdf.fyi. Run through this checklist:")

heading2("Visual checks:")
checkbox("Homepage loads and shows the updated 'Private by design' feature card")
checkbox("Each tool page loads without errors")
checkbox("compress.html shows the green 🔒 badge (it should already — verify it's there)")
checkbox("merge.html shows the green 🔒 badge")
checkbox("split.html shows the green 🔒 badge")
checkbox("edit.html shows the green 🔒 badge (this was added in this update)")
checkbox("convert.html shows the 🔒 server processing card in the features section")
checkbox("No page says 'Converto' anywhere")

heading2("Functional checks:")
checkbox("Compress: upload a PDF, compress it, download it. Should work entirely in browser.")
checkbox("Merge: upload two PDFs, merge them, download. Should work in browser.")
checkbox("Convert: upload a Word doc, convert to PDF. Should upload to server and return a PDF.")
checkbox("PDF to Word: upload a PDF, convert to DOCX. Download and open it.")

heading2("Security check (optional):")
body("Open browser DevTools (F12) → Network tab. Upload a file using Compress. Confirm no network request is made to your server. The file should be processed locally.")
body("Then try Convert. Confirm a POST request goes to /api/convert and returns a file.")

divider()

# ══════════════════════════════════════════════════════════════════════════════
# STEP 5 — SUBMIT TO ADSENSE
# ══════════════════════════════════════════════════════════════════════════════
heading1("Step 5 — Submit to Google AdSense for Re-review")

body("Once the live site is confirmed working, go to your AdSense account and request a re-review.")

bullet("Go to: https://adsense.google.com")
bullet("Sign in to your account")
bullet("Find the policy violation or rejection notice")
bullet("Click 'Request review' or 'Resubmit'")
bullet("Google will re-crawl your live site (not your local files)")
bullet("Review takes 3–7 days typically")

note("The content updates (800+ words per tool page, homepage content, about page) are what should clear the 'thin content' rejection. Make sure the live server is serving the updated HTML before submitting.")

divider()

# ══════════════════════════════════════════════════════════════════════════════
# WHAT CHANGED — SUMMARY
# ══════════════════════════════════════════════════════════════════════════════
heading1("What Changed in This Update")

heading2("main.py")
bullet("FERNET_KEY: Now required as environment variable. Server won't start without it. Fixes bug where fresh key on restart made uploaded files unreadable.")
bullet("API title: 'Converto API' renamed to 'EditPDF API'")
bullet("Upload directory: /tmp/converto renamed to /tmp/editpdf")
bullet("CORS: Locked from allow all (*) to only https://editpdf.fyi")
bullet("Security headers: Every response now sends X-Content-Type-Options, X-Frame-Options, Strict-Transport-Security, and Referrer-Policy")
bullet("Immediate deletion: Files are deleted 30 seconds after the user downloads their result (instead of waiting up to 60 minutes)")

heading2("compress.html")
bullet("Fixed meta description: Removed false claim 'files permanently deleted within 60 minutes' (compress runs in browser — no files are ever uploaded)")

heading2("edit.html")
bullet("Added 🔒 privacy badge at the top of the tool (compress, merge, and split already had this — edit was missing it)")

heading2("index.html")
bullet("Updated 'Private' feature card to honestly describe both tiers: browser-side tools (no upload) and server-side tools (encrypted, 60-min deletion)")

divider()

# ══════════════════════════════════════════════════════════════════════════════
# TROUBLESHOOTING
# ══════════════════════════════════════════════════════════════════════════════
heading1("Troubleshooting")

heading2("Server won't start — RuntimeError about FERNET_KEY")
body("The FERNET_KEY environment variable is not set. Follow the 'Before You Start' section to generate a key and set it before starting uvicorn.")

heading2("Server starts but conversions fail")
body("Check the server logs for error details. Common causes:")
bullet("LibreOffice not installed: sudo apt install libreoffice")
bullet("Missing Python packages: pip install -r requirements.txt")
bullet("Wrong file permissions on /tmp/editpdf: sudo chmod 777 /tmp/editpdf")

heading2("Browser-side tools not working (compress, merge, split, edit)")
body("These run entirely in the browser, so server issues won't affect them. If they don't work:")
bullet("Check browser console (F12) for JavaScript errors")
bullet("Make sure the page loaded the pdf-lib.js script (check Network tab)")
bullet("Try a different browser")

heading2("Old Converto files still showing on live site")
body("Your browser may be caching the old files. Hard refresh: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac). Also check that you uploaded the correct updated files.")

heading2("AdSense still rejected after re-review")
body("Possible reasons:")
bullet("The live server was not updated before you submitted — verify the live pages have 800+ words of content")
bullet("Google needs more time — re-reviews can take up to 2 weeks")
bullet("Other policy issues — check the AdSense policy centre for specific feedback")

doc.save("D:/Test editpdf.fyi/backend/EditPDF_Deployment_Guide.docx")
print("Done — saved to D:/Test editpdf.fyi/backend/EditPDF_Deployment_Guide.docx")
