#!pip install opencv-python
#!pip install matplotlib
#terminal

import cv2
import matplotlib.pyplot as plt

def show_image(image, title="Image"):
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()

image1_path = '/content/drive/MyDrive/ex2_241/loro.png'  # Reemplaza con la ruta de tu imagen
image2_path = '/content/drive/MyDrive/ex2_241/oso.png'  # Reemplaza con la ruta de tu imagen

image1 = cv2.imread(image1_path)
image2 = cv2.imread(image2_path)

show_image(image1, "Image 1")
show_image(image2, "Image 2")


# Sumar las imágenes
sum_image = cv2.addWeighted(image1,0.5, image2,0.5,0)
show_image(sum_image, "Suma Imagen")

# Restar las imágenes
subtract_image = cv2.subtract(image1, image2)
show_image(subtract_image, "Resta Imagen")
