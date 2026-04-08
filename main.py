# backend/main.py
# Document Converter API — FastAPI + Python
# Install deps: pip install fastapi uvicorn python-multipart pdf2docx pdf2image pillow python-docx weasyprint cryptography

import os, uuid, shutil, subprocess
from pathlib import Path
from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import threading, time

# ─── Encryption ──────────────────────────────────────────────────────────────
from cryptography.fernet import Fernet

ENCRYPTION_KEY = Fernet.generate_key()
fernet = Fernet(ENCRYPTION_KEY)

def encrypt_file(src: Path) -> Path:
    data = src.read_bytes()
    encrypted = fernet.encrypt(data)
    enc_path = src.with_suffix(src.suffix + ".enc")
    enc_path.write_bytes(encrypted)
    src.unlink()
    return enc_path

def decrypt_file(enc_path: Path) -> Path:
    encrypted = enc_path.read_bytes()
    data = fernet.decrypt(encrypted)
    dec_path = enc_path.with_suffix("")
    dec_path.write_bytes(data)
    return dec_path

app = FastAPI(title="Converto API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = Path("/tmp/converto")
UPLOAD_DIR.mkdir(exist_ok=True)

def cleanup_old_files():
    while True:
        now = time.time()
        for f in UPLOAD_DIR.glob("**/*"):
            try:
                if f.is_file() and now - f.stat().st_mtime > 3600:
                    f.unlink(missing_ok=True)
            except Exception:
                pass
        time.sleep(300)

threading.Thread(target=cleanup_old_files, daemon=True).start()

CONVERSIONS = {
    ("pdf",  "docx"),
    ("pdf",  "png"),
    ("pdf",  "jpg"),
    ("pdf",  "xlsx"),
    ("docx", "pdf"),
    ("docx", "txt"),
    ("xlsx", "pdf"),
    ("pptx", "pdf"),
    ("html", "pdf"),
    ("png",  "jpg"),
    ("jpg",  "png"),
    ("jpg",  "pdf"),
    ("png",  "pdf"),
}

def convert_pdf_to_docx(src: Path, dst: Path):
    from pdf2docx import Converter
    cv = Converter(str(src))
    cv.convert(str(dst), start=0, end=None)
    cv.close()

def convert_pdf_to_image(src: Path, dst: Path, fmt: str):
    from pdf2image import convert_from_path
    pages = convert_from_path(str(src), dpi=150)
    if len(pages) == 1:
        pages[0].save(str(dst), fmt.upper())
    else:
        import zipfile, io
        zip_path = dst.with_suffix('.zip')
        with zipfile.ZipFile(zip_path, 'w') as zf:
            for i, page in enumerate(pages):
                buf = io.BytesIO()
                page.save(buf, fmt.upper())
                zf.writestr(f"page_{i+1}.{fmt}", buf.getvalue())
        return zip_path
    return dst

def convert_to_pdf_via_libreoffice(src: Path, dst_dir: Path) -> Path:
    result = subprocess.run(
        ["libreoffice", "--headless", "--convert-to", "pdf", "--outdir", str(dst_dir), str(src)],
        capture_output=True, text=True, timeout=60
    )
    if result.returncode != 0:
        raise RuntimeError(f"LibreOffice error: {result.stderr}")
    out = dst_dir / (src.stem + ".pdf")
    return out

def convert_html_to_pdf_weasyprint(src: Path, dst: Path):
    from weasyprint import HTML
    HTML(filename=str(src)).write_pdf(str(dst))

def convert_image(src: Path, dst: Path, to_fmt: str):
    from PIL import Image
    img = Image.open(src).convert("RGB")
    img.save(str(dst), to_fmt.upper())

def image_to_pdf(src: Path, dst: Path):
    from PIL import Image
    img = Image.open(src).convert("RGB")
    img.save(str(dst), "PDF")

@app.post("/api/convert")
async def convert_file(
    file: UploadFile = File(...),
    convert_to: str = Form(None),
    from_format: str = Form(None),
    to_format: str = Form(None),
):
    if convert_to and not to_format:
        to_format = convert_to
    if not from_format and file.filename:
        from_format = file.filename.rsplit(".", 1)[-1].lower()
    if not from_format or not to_format:
        raise HTTPException(400, detail="Missing format parameters.")

    pair = (from_format.lower(), to_format.lower())
    if pair not in CONVERSIONS:
        raise HTTPException(400, detail=f"Conversion {from_format} to {to_format} is not supported.")

    job_id  = uuid.uuid4().hex
    job_dir = UPLOAD_DIR / job_id
    job_dir.mkdir()

    src_path = job_dir / f"input.{from_format}"
    with open(src_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    enc_src_path = encrypt_file(src_path)
    dst_path = job_dir / f"output.{to_format}"

    try:
        src_path = decrypt_file(enc_src_path)

        if pair == ("pdf", "docx"):
            convert_pdf_to_docx(src_path, dst_path)
        elif pair in {("pdf", "png"), ("pdf", "jpg")}:
            dst_path = convert_pdf_to_image(src_path, dst_path, to_format)
        elif pair == ("pdf", "xlsx"):
            import tabula, openpyxl
            tables = tabula.read_pdf(str(src_path), pages="all", multiple_tables=True)
            if not tables:
                from pdfminer.high_level import extract_text
                ws = wb.active
                ws.title = "Content"
                try:
                    text = extract_text(str(src_path))
                    for line in text.splitlines():
                        if line.strip():
                            ws.append([line.strip()])
                except Exception:
                    ws.append(["Could not extract content from this PDF."])
            wb = openpyxl.Workbook()
            wb.remove(wb.active)
            for i, df in enumerate(tables):
                ws = wb.create_sheet(title=f"Table_{i+1}")
                ws.append(list(df.columns))
                for row in df.itertuples(index=False):
                    ws.append(list(row))
            wb.save(str(dst_path))
        elif from_format in {"docx", "xlsx", "pptx"} and to_format == "pdf":
            dst_path = convert_to_pdf_via_libreoffice(src_path, job_dir)
        elif pair == ("html", "pdf"):
            try:
                convert_html_to_pdf_weasyprint(src_path, dst_path)
            except Exception:
                dst_path = convert_to_pdf_via_libreoffice(src_path, job_dir)
        elif pair in {("png", "jpg"), ("jpg", "png")}:
            convert_image(src_path, dst_path, to_format)
        elif pair in {("jpg", "pdf"), ("png", "pdf")}:
            image_to_pdf(src_path, dst_path)
        elif pair == ("docx", "txt"):
            from docx import Document
            doc = Document(str(src_path))
            text = "\n".join([p.text for p in doc.paragraphs])
            dst_path.write_text(text, encoding="utf-8")
        else:
            raise HTTPException(400, detail="Unsupported conversion.")

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, detail=f"Conversion failed: {str(e)}")
    finally:
        if src_path.exists():
            src_path.unlink(missing_ok=True)
        if enc_src_path.exists():
            enc_src_path.unlink(missing_ok=True)

    if not dst_path.exists():
        raise HTTPException(500, detail="Output file was not created.")

    media_types = {
        "pdf": "application/pdf",
        "docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        "pptx": "application/vnd.openxmlformats-officedocument.presentationml.presentation",
        "png": "image/png", "jpg": "image/jpeg",
        "txt": "text/plain", "html": "text/html",
        "zip": "application/zip",
    }
    media_type = media_types.get(dst_path.suffix.lstrip("."), "application/octet-stream")

    return FileResponse(
        path=str(dst_path),
        media_type=media_type,
        filename=f"converted.{dst_path.suffix.lstrip('.')}",
    )

@app.post("/api/merge-pdf")
async def merge_pdf(files: list[UploadFile] = File(...)):
    if len(files) < 2:
        raise HTTPException(400, detail="Please upload at least 2 PDF files.")
    if len(files) > 20:
        raise HTTPException(400, detail="Maximum 20 files allowed.")
    job_id  = uuid.uuid4().hex
    job_dir = UPLOAD_DIR / job_id
    job_dir.mkdir()
    try:
        import PyPDF2
        merger = PyPDF2.PdfMerger()
        for i, file in enumerate(files):
            file_path = job_dir / f"input_{i}.pdf"
            with open(file_path, "wb") as f:
                shutil.copyfileobj(file.file, f)
            merger.append(str(file_path))
        output_path = job_dir / "merged.pdf"
        with open(output_path, "wb") as f:
            merger.write(f)
        merger.close()
        return FileResponse(path=str(output_path), media_type="application/pdf", filename="merged.pdf")
    except Exception as e:
        raise HTTPException(500, detail=f"Merge failed: {str(e)}")

@app.post("/api/compress-pdf")
async def compress_pdf(file: UploadFile = File(...), level: str = Form("ebook")):
    valid_levels = {"screen", "ebook", "printer", "prepress"}
    if level not in valid_levels:
        level = "ebook"
    job_id  = uuid.uuid4().hex
    job_dir = UPLOAD_DIR / job_id
    job_dir.mkdir()
    src_path = job_dir / "input.pdf"
    dst_path = job_dir / "compressed.pdf"
    with open(src_path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    try:
        result = subprocess.run([
            "gs", "-sDEVICE=pdfwrite", "-dCompatibilityLevel=1.4",
            f"-dPDFSETTINGS=/{level}", "-dNOPAUSE", "-dQUIET", "-dBATCH",
            f"-sOutputFile={dst_path}", str(src_path)
        ], capture_output=True, text=True, timeout=120)
        if result.returncode != 0 or not dst_path.exists():
            raise RuntimeError("Ghostscript failed")
    except Exception:
        try:
            import PyPDF2
            reader = PyPDF2.PdfReader(str(src_path), strict=False)
            writer = PyPDF2.PdfWriter()
            for page in reader.pages:
                page.compress_content_streams()
                writer.add_page(page)
            with open(dst_path, "wb") as f:
                writer.write(f)
        except Exception as e2:
            raise HTTPException(500, detail=f"Compression failed: {str(e2)}")
    if not dst_path.exists():
        raise HTTPException(500, detail="Compressed file was not created.")
    return FileResponse(path=str(dst_path), media_type="application/pdf", filename="compressed.pdf")

@app.post("/api/split-pdf")
async def split_pdf(
    file: UploadFile = File(...),
    method: str = Form("range"),
    ranges: str = Form(""),
    page: int = Form(1),
    n: int = Form(2),
):
    import PyPDF2, zipfile, io
    job_id  = uuid.uuid4().hex
    job_dir = UPLOAD_DIR / job_id
    job_dir.mkdir()
    src_path = job_dir / "input.pdf"
    with open(src_path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    try:
        reader = PyPDF2.PdfReader(str(src_path), strict=False)
        total_pages = len(reader.pages)
        def extract_pages(page_indices, out_path):
            writer = PyPDF2.PdfWriter()
            for i in page_indices:
                if 0 <= i < total_pages:
                    writer.add_page(reader.pages[i])
            with open(out_path, "wb") as f:
                writer.write(f)
        def parse_ranges(ranges_str, total):
            indices = []
            for part in ranges_str.split(','):
                part = part.strip()
                if '-' in part:
                    a, b = part.split('-')
                    indices += list(range(int(a)-1, int(b)))
                elif part.isdigit():
                    indices.append(int(part)-1)
            return [i for i in indices if 0 <= i < total]
        if method == "range":
            indices = parse_ranges(ranges, total_pages)
            if not indices:
                raise HTTPException(400, detail="Invalid page range.")
            out_path = job_dir / "split.pdf"
            extract_pages(indices, out_path)
            return FileResponse(str(out_path), media_type="application/pdf", filename="split.pdf")
        elif method == "single":
            idx = page - 1
            if idx < 0 or idx >= total_pages:
                raise HTTPException(400, detail=f"Page {page} does not exist.")
            out_path = job_dir / f"page_{page}.pdf"
            extract_pages([idx], out_path)
            return FileResponse(str(out_path), media_type="application/pdf", filename=f"page_{page}.pdf")
        elif method == "all":
            zip_buffer = io.BytesIO()
            with zipfile.ZipFile(zip_buffer, 'w') as zf:
                for i in range(total_pages):
                    out_path = job_dir / f"page_{i+1}.pdf"
                    extract_pages([i], out_path)
                    zf.write(out_path, f"page_{i+1}.pdf")
            zip_path = job_dir / "all_pages.zip"
            with open(zip_path, "wb") as f:
                f.write(zip_buffer.getvalue())
            return FileResponse(str(zip_path), media_type="application/zip", filename="all_pages.zip")
        elif method == "every":
            if n < 1:
                raise HTTPException(400, detail="N must be at least 1.")
            zip_buffer = io.BytesIO()
            with zipfile.ZipFile(zip_buffer, 'w') as zf:
                chunk = 0
                for start in range(0, total_pages, n):
                    chunk += 1
                    indices = list(range(start, min(start + n, total_pages)))
                    out_path = job_dir / f"chunk_{chunk}.pdf"
                    extract_pages(indices, out_path)
                    zf.write(out_path, f"chunk_{chunk}_pages_{start+1}-{indices[-1]+1}.pdf")
            zip_path = job_dir / "split_chunks.zip"
            with open(zip_path, "wb") as f:
                f.write(zip_buffer.getvalue())
            return FileResponse(str(zip_path), media_type="application/zip", filename="split_chunks.zip")
        else:
            raise HTTPException(400, detail="Invalid split method.")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, detail=f"Split failed: {str(e)}")

@app.get("/favicon.svg", include_in_schema=False)
async def favicon():
    return FileResponse("favicon.svg", media_type="image/svg+xml")

@app.get("/favicon-mint.svg", include_in_schema=False)
async def favicon_mint():
    return FileResponse("favicon-mint.svg", media_type="image/svg+xml")

@app.get("/favicon-purple.svg", include_in_schema=False)
async def favicon_purple():
    return FileResponse("favicon-purple.svg", media_type="image/svg+xml")

@app.get("/favicon-teal.svg", include_in_schema=False)
async def favicon_teal():
    return FileResponse("favicon-teal.svg", media_type="image/svg+xml")

@app.get("/favicon-orange.svg", include_in_schema=False)
async def favicon_orange():
    return FileResponse("favicon-orange.svg", media_type="image/svg+xml")

@app.get("/favicon-green.svg", include_in_schema=False)
async def favicon_green():
    return FileResponse("favicon-green.svg", media_type="image/svg+xml")

@app.get("/favicon.ico", include_in_schema=False)
async def favicon_ico():
    return FileResponse("favicon.ico", media_type="image/x-icon")

@app.get("/convert", include_in_schema=False)
async def convert_page():
    return FileResponse("convert.html")

@app.get("/pdf-to-word", include_in_schema=False)
async def pdf_to_word():
    return FileResponse("pdf-to-word.html")

@app.get("/word-to-pdf", include_in_schema=False)
async def word_to_pdf():
    return FileResponse("word-to-pdf.html")

@app.get("/jpg-to-pdf", include_in_schema=False)
async def jpg_to_pdf():
    return FileResponse("jpg-to-pdf.html")

@app.get("/pdf-to-excel", include_in_schema=False)
async def pdf_to_excel():
    return FileResponse("pdf-to-excel.html")

@app.get("/sitemap.xml", include_in_schema=False)
async def sitemap():
    return FileResponse("sitemap.xml", media_type="application/xml")

@app.get("/ads.txt", include_in_schema=False)
async def ads_txt():
    return FileResponse("ads.txt", media_type="text/plain")

@app.get("/health")
def health():
    return {"status": "ok"}

if Path("index.html").exists():
    app.mount("/", StaticFiles(directory=".", html=True), name="static")




