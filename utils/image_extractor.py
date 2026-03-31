import fitz
import os


OUTPUT_DIR = "static/extracted_images"


def extract_images(pdf_path):

    doc = fitz.open(pdf_path)

    extracted = []

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for page_index in range(len(doc)):

        images = doc[page_index].get_images(full=True)

        for img_index, img in enumerate(images):

            xref = img[0]

            base_img = doc.extract_image(xref)   # correct function

            image_bytes = base_img["image"]

            ext = base_img["ext"]

            filename = f"page{page_index+1}_img{img_index}.{ext}"

            filepath = os.path.join(OUTPUT_DIR, filename)

            with open(filepath, "wb") as f:
                f.write(image_bytes)

            extracted.append(filepath)

    return extracted