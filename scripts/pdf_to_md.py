#!/usr/bin/env python3
"""
Simple PDF -> Markdown converter using PyMuPDF (fitz).

Usage:
  python3 scripts/pdf_to_md.py input.pdf output.md --img-dir assets/imagenes/sonido_images

This will extract images to the img-dir and embed them with relative paths in the Markdown.
"""
import sys
import os
from pathlib import Path

try:
    import fitz
except Exception as e:
    print("PyMuPDF (fitz) is required. Install with: pip install pymupdf", file=sys.stderr)
    raise

def ensure_dir(p: Path):
    p.mkdir(parents=True, exist_ok=True)

def extract_pdf_to_md(pdf_path: Path, out_md: Path, img_dir: Path, author: str = "Nombre A."):
    ensure_dir(out_md.parent)
    ensure_dir(img_dir)

    doc = fitz.open(str(pdf_path))

    images_written = []
    md_lines = []

    # Front matter
    md_lines.append('---')
    md_lines.append(f'title: "Sonido"')
    md_lines.append(f'date: {__import__("datetime").date.today().isoformat()}')
    md_lines.append('layout: critica')
    md_lines.append('excerpt: "Importado desde PDF"')
    md_lines.append(f'author: "{author}"')
    md_lines.append('---\n')

    for page_num in range(len(doc)):
        page = doc[page_num]
        # Extract text
        text = page.get_text("text")
        if text and text.strip():
            md_lines.append(text.strip())
            md_lines.append('\n')

        # Extract images from page
        image_list = page.get_images(full=True)
        for img_index, img in enumerate(image_list, start=1):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image.get("image")
            image_ext = base_image.get("ext", "png")
            img_name = f"sonido_page{page_num+1}_img{img_index}.{image_ext}"
            img_path = img_dir / img_name
            with open(img_path, "wb") as f:
                f.write(image_bytes)
            rel = os.path.relpath(img_path, out_md.parent).replace(os.sep, "/")
            md_lines.append(f"![{img_name}]({rel})\n")
            images_written.append(img_path)

    # Write markdown file
    out_md.write_text("\n".join(md_lines), encoding="utf-8")
    return images_written

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input PDF file")
    parser.add_argument("output", help="output markdown file")
    parser.add_argument("--img-dir", help="images directory", default=None)
    parser.add_argument("--author", help="author credit", default="Nombre A.")
    args = parser.parse_args()

    pdf_path = Path(args.input)
    out_md = Path(args.output)
    img_dir = Path(args.img_dir) if args.img_dir else Path(out_md.parent) / (out_md.stem + "_images")

    if not pdf_path.exists():
        print("Input PDF not found:", pdf_path, file=sys.stderr)
        sys.exit(2)

    images = extract_pdf_to_md(pdf_path, out_md, img_dir, author=args.author)
    print("Wrote:", out_md)
    print("Images:", len(images), "->", img_dir)

if __name__ == '__main__':
    main()
