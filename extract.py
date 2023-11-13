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
            image_path = os.path.join(output_dir, "image_page{}_img{}.{}".format(page_num + 1, img_idx + 1, image_extension))
            with open(image_path, "wb") as f:
                f.write(image)
            images.append(image_path)

    # Cerrar el documento PDF
    pdf_document.close()

    return images

if __name__ == "__main__":
    # Solicitar la ruta del archivo PDF desde el usuario
    pdf_path = input("Ingrese la ruta del archivo PDF: ").strip('"')
    output_dir = input("Ingrese la ruta del directorio de salida: ").strip('"')

    # Utilizar os.path.join para construir las rutas correctamente
    pdf_path = os.path.join(pdf_path)
    output_dir = os.path.join(output_dir)

    if not os.path.exists(pdf_path):
        print("La ruta del archivo PDF no es válida.")
    else:
        extracted_images = extract_images_from_pdf(pdf_path, output_dir)
        print("Imágenes extraídas:", extracted_images)
