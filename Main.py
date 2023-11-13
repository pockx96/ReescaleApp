import os
from file_Os import *

if __name__ == "__main__":
    # Solicitar la ruta del archivo PDF desde el usuario
    pdf_path = r"{}".format(input("Ingrese la ruta del archivo PDF: "))
    pdf_path = pdf_path.strip('"')
    # Verificar si la ruta es válida
    if not os.path.exists(pdf_path):
        print("La ruta del archivo PDF no es válida.")
    else:
        pdf_to_folder(pdf_path)
