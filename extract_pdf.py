import fitz
import os
import sys

pdf_path = r"C:\Users\Hp\Downloads\Osama Group Arabic.pdf(1)(15).pdf"
output_dir = r"c:\Users\Hp\Downloads\osama-omran-main\osama-omran-main\pdf_images"

os.makedirs(output_dir, exist_ok=True)

print(f"Opening PDF: {pdf_path}")
doc = fitz.open(pdf_path)
print(f"Total pages: {len(doc)}")

image_paths = []
for i, page in enumerate(doc):
    # Render page to high-res pixmap (dpi=200 for crisp text and graphics)
    pix = page.get_pixmap(dpi=200)
    output_filename = f"page_{i+1}.png"
    output_path = os.path.join(output_dir, output_filename)
    pix.save(output_path)
    print(f"Saved: {output_filename} ({pix.width}x{pix.height}px)")
    image_paths.append(f"pdf_images/{output_filename}")

print("Extraction complete!")
print("Images list:", image_paths)
