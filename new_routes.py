# Add these routes to your existing main.py
# Paste them BEFORE the last line: app.mount("/", ...)

# ─── Merge PDF ────────────────────────────────────────────────────────────────

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

        return FileResponse(
            path=str(output_path),
            media_type="application/pdf",
            filename="merged.pdf"
        )

    except Exception as e:
        raise HTTPException(500, detail=f"Merge failed: {str(e)}")


# ─── Compress PDF ─────────────────────────────────────────────────────────────

@app.post("/api/compress-pdf")
async def compress_pdf(
    file: UploadFile = File(...),
    level: str = Form("ebook")
):
    # Valid Ghostscript PDFSETTINGS levels
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
        # Try Ghostscript first (best compression)
        result = subprocess.run([
            "gs",
            "-sDEVICE=pdfwrite",
            "-dCompatibilityLevel=1.4",
            f"-dPDFSETTINGS=/{level}",
            "-dNOPAUSE", "-dQUIET", "-dBATCH",
            f"-sOutputFile={dst_path}",
            str(src_path)
        ], capture_output=True, text=True, timeout=120)

        if result.returncode != 0 or not dst_path.exists():
            raise RuntimeError("Ghostscript failed")

    except Exception:
        # Fallback: use PyPDF2 to re-write (basic compression)
        try:
            import PyPDF2
            reader = PyPDF2.PdfReader(str(src_path))
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

    return FileResponse(
        path=str(dst_path),
        media_type="application/pdf",
        filename="compressed.pdf"
    )
