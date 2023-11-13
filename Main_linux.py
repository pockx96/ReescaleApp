# -*- coding: utf-8 -*-

import os
from file_Os import *

if __name__ == "__main__":
    # Solicitar la ruta del archivo PDF desde el usuario
    pdf_path = input("Ingrese la ruta del archivo PDF: ").strip('"')

    # Utilizar os.path.join para construir la ruta correctamente
    pdf_path = os.path.join(pdf_path)

    if not os.path.exists(pdf_path):
        print("La ruta del archivo PDF no es válida.")
    else:
        pdf_to_folder(pdf_path)