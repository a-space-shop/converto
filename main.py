# backend/main.py
# Document Converter API — FastAPI + Python
# Install deps: pip install fastapi uvicorn python-multipart pdf2docx pdf2image pillow python-docx weasyprint

import os, uuid, shutil, subprocess
from pathlib import Path
from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import threading, time

app = FastAPI(title="Converto API")

# Allow frontend to call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # Restrict in production
    allow_methods=["*"],
    allow_headers=["*"],
)

# Temp directory for uploads/outputs
UPLOAD_DIR = Path("/tmp/converto")
UPLOAD_DIR.mkdir(exist_ok=True)

# ─── Auto-delete files older than 1 hour ─────────────────────────────────────
def cleanup_old_files():
    while True:
        now = time.time()
        for f in UPLOAD_DIR.glob("*"):
            if now - f.stat().st_mtime > 3600:
                f.unlink(missing_ok=True)
        time.sleep(300)  # check every 5 min

threading.Thread(target=cleanup_old_files, daemon=True).start()

# ─── Supported conversion matrix ─────────────────────────────────────────────
CONVERSIONS = {
    ("pdf",  "docx"),
    ("pdf",  "png"),
    ("pdf",  "jpg"),
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

# ─── Converter functions ──────────────────────────────────────────────────────

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
        # Multi-page: save as zip of images
        import zipfile, io
        zip_path = dst.with_suffix('.zip')
        with zipfile.ZipFile(zip_path, 'w') as zf:
            for i, page in enumerate(pages):
                buf = io.BytesIO()
                page.save(buf, fmt.upper())
                zf.writestr(f"page_{i+1}.{fmt}", buf.getvalue())
        dst.rename(zip_path) if dst != zip_path else None
        return zip_path
    return dst

def convert_to_pdf_via_libreoffice(src: Path, dst_dir: Path) -> Path:
    """Use LibreOffice headless for docx/xlsx/pptx/html → pdf"""
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

# ─── Main endpoint ────────────────────────────────────────────────────────────

@app.post("/api/convert")
async def convert_file(
    file: UploadFile = File(...),
    from_format: str = Form(...),
    to_format: str   = Form(...),
):
    # Validate conversion pair
    pair = (from_format.lower(), to_format.lower())
    if pair not in CONVERSIONS:
        raise HTTPException(400, detail=f"Conversion {from_format} → {to_format} is not supported.")

    # Save uploaded file
    job_id  = uuid.uuid4().hex
    job_dir = UPLOAD_DIR / job_id
    job_dir.mkdir()

    src_path = job_dir / f"input.{from_format}"
    with open(src_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    dst_path = job_dir / f"output.{to_format}"

    try:
        if pair == ("pdf", "docx"):
            convert_pdf_to_docx(src_path, dst_path)

        elif pair in {("pdf", "png"), ("pdf", "jpg")}:
            dst_path = convert_pdf_to_image(src_path, dst_path, to_format)

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

@app.get("/health")
def health(): return {"status": "ok"}

# Serve frontend (place index.html in ../frontend/)
if Path("index.html").exists():
    app.mount("/", StaticFiles(directory="../frontend", html=True), name="static")
