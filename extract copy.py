# -*- coding: utf-8 -*-

import os
import fitz

def extract_images_from_pdf(pdf_path, output_dir):
    # Crear un directorio de salida si no existe
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Abrir el archivo PDF
    pdf_document = fitz.open(pdf_path)

    # Extraer las imágenes y guardarlas en la ruta de salida
    images = []
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        image_list = page.get_images(full=True)
        for img_idx, img_info in enumerate(image_list):
            image_obj = pdf_document.extract_image(img_info[0])
            image = image_obj["image"]
            image_extension = image_obj["ext"]  # Obtener la extensión de la imagen
            image_path = os.path.join(output_dir, f"image_page{page_num + 1}_img{img_idx + 1}.{image_extension}")
            with open(image_path, "wb") as f:
                f.write(image)
            images.append(image_path)

    # Cerrar el documento PDF
    pdf_document.close()

    return images

# # Uso de la función
# pdf_file = "D:\CasaGO\VRBO\How do I find which\How do I find which.pdf"
# output_directory = "D:\CasaGO\VRBO\How do I find which\screenshots"
# extracted_images = extract_images_from_pdf(pdf_file, output_directory)
# print("Imágenes extraídas:")
# print(extracted_images)


