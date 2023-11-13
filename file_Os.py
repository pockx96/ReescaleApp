# -*- coding: utf-8 -*-


import os
import re
import shutil
from extract import *
from scale import *
# import PyPDF2

# def abrir_archivo_pdf(ruta_pdf):
#     try:
#         archivo_pdf = open(ruta_pdf, 'rb')
#         return archivo_pdf
#     except FileNotFoundError:
#         print("No se pudo encontrar el archivo PDF en la ruta especificada.")
#         return None

# def copiar_texto_pdf(ruta_pdf):
#     archivo_pdf = abrir_archivo_pdf(ruta_pdf)
#     if archivo_pdf:
#         lector_pdf = PyPDF2.PdfFileReader(archivo_pdf)
#         texto = ""
#         for pagina_num in range(lector_pdf.numPages):
#             pagina = lector_pdf.getPage(pagina_num)
#             texto += pagina.extractText()
#         archivo_pdf.close()
#         return texto
#     else:
#         return None



def clean_filename(filename):
    # Eliminar caracteres no permitidos en nombres de archivo y directorios
    cleaned_filename = re.sub(r'[\\/:*?"<>|]', '', filename)
    return cleaned_filename

def delete_images_in_folder(folder_path):
    # Obtener una lista de archivos en el directorio
    files = os.listdir(folder_path)
    # Recorrer todos los archivos en el directorio
    for file in files:
        # Comprobar si el archivo es una imagen (puedes agregar más extensiones si es necesario)
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')):
            # Crear la ruta completa del archivo
            file_path = os.path.join(folder_path, file)

            # Eliminar el archivo de imagen
            os.remove(file_path)

def pdf_to_folder(pdf_path):
    # Obtener el nombre del archivo sin la extensión ".pdf"
    pdf_filename = os.path.basename(pdf_path)
    folder_name = os.path.splitext(pdf_filename)[0]

    # Limpiar el nombre de la carpeta para eliminar caracteres no permitidos
    cleaned_folder_name = clean_filename(folder_name)

    # Crear una carpeta con el nombre limpio en la ubicación del archivo PDF
    folder_path = os.path.join(os.path.dirname(pdf_path), cleaned_folder_name)
    os.makedirs(folder_path, exist_ok=True)

    # Mover el archivo PDF a la carpeta
    new_pdf_path = os.path.join(folder_path, pdf_filename)
    shutil.move(pdf_path, new_pdf_path)

    extract_images_from_pdf(new_pdf_path,folder_path)
    screenshots_folder = os.path.join(folder_path, "screenshots")
    os.makedirs(screenshots_folder, exist_ok=True)
    # copiar_texto_pdf(new_pdf_path)
    # abrir_archivo_pdf(new_pdf_path)

    scale_all_images(folder_path,screenshots_folder,folder_name)
    delete_images_in_folder(folder_path)


