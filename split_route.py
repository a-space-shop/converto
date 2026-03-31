# Add this route to main.py BEFORE the app.mount line

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
        reader = PyPDF2.PdfReader(str(src_path))
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
