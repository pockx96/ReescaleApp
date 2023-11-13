import os
from PIL import Image

def waifu2x_2x_scale(input_path, output_path):
    try:
        # Abre la imagen con Pillow
        image = Image.open(input_path)

        # Reescala la imagen a 2x con un método de interpolación específico (por ejemplo, Image.BICUBIC)
        width, height = image.size
        scaled_image = image.resize((width * 2, height * 2), Image.BICUBIC)  # Puedes probar con Image.BOX o Image.LANCZOS también

        # Guarda la imagen reescalada
        scaled_image.save(output_path)
        print("Reescalado exitoso. Imagen guardada en:", output_path)

    except Exception as e:
        print("Error durante el proceso:", str(e))

# if __name__ == "__main__":
#     # Rutas de la carpeta con las imágenes de entrada y salida
#     input_folder = "D:\CasaGO\Seasons\How do I create a new season\How_do_I_create_a_new_sea"
#     output_folder = "D:\CasaGO\Seasons\How do I create a new season\Screenshots"
#     # Obtener la lista de archivos de imagen en la carpeta de entrada
#     image_files = [f for f in os.listdir(input_folder) if f.endswith((".jpg", ".jpeg", ".png"))]

#     # Procesar cada imagen en la carpeta
#     for image_file in image_files:
#         input_path = os.path.join(input_folder, image_file)
#         output_path = os.path.join(output_folder, f"{os.path.splitext(image_file)[0]}_escala_2x.jpg")
#         waifu2x_2x_scale(input_path, output_path)

def scale_all_images(input_folder, output_folder,img_name):
   
    image_files = [f for f in os.listdir(input_folder) if f.endswith((".jpg", ".jpeg", ".png"))]

    # Procesar cada imagen en la carpeta
    for image_file in image_files:
        input_path = os.path.join(input_folder, image_file)
        output_path = os.path.join(output_folder, f"{img_name}{os.path.splitext(image_file)[0]}_escala_2x.jpg")
        waifu2x_2x_scale(input_path, output_path)

