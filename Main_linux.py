# -*- coding: utf-8 -*-
import os
from file_Os import *

def print_ascii_art():
    os.system('clear')


    ascii_art = """
         _ _
    .-. | | |
    |M|_|A|N|                           "REESCALE APP"
    |A|a|.|.|< 
    |T|r| | | \\
    |H|t|M|Z|  \\      "CONVIERTE PDF EN IMÁGENES ¡FÁCIL Y GRATIS!"
    | |!| | |   \>     
    """"""""""""""""""

  """
    print(ascii_art)

def main():
    print_ascii_art()
    print("### Bienvenido a tu aplicación de extracción de imágenes de PDF ###\n")

    while True:
        # Solicitar la ruta del archivo PDF desde el usuario
        pdf_path = input("> Ingrese la ruta del archivo PDF ('exit' para salir):").strip('"')

        if pdf_path.lower() == 'exit':
            print("Saliendo de la aplicación. ¡Hasta luego!")
            break

        # Utilizar os.path.join para construir la ruta correctamente
        pdf_path = os.path.join(pdf_path)

        if not os.path.exists(pdf_path):
            print("La ruta del archivo PDF no es válida.")
        else:
            pdf_to_folder(pdf_path)


if __name__ == "__main__":
    main()
