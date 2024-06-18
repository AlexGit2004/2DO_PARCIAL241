#!pip install scipy
#!pip install numpy
#!pip install opencv-python
#en terminal


import cv2
import numpy as np
from scipy.sparse import coo_matrix
import matplotlib.pyplot as plt

# Función para mostrar imágenes
def show_image(image, title="Image"):
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()

image1_path = '/content/drive/MyDrive/ex2_241/1.jpeg'
image2_path = '/content/drive/MyDrive/ex2_241/2.jpeg'

image1 = cv2.imread(image1_path, cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread(image2_path, cv2.IMREAD_GRAYSCALE)

show_image(image1, "Image 1")
show_image(image2, "Image 2")

sparse_matrix_1 = coo_matrix(image1)
sparse_matrix_2 = coo_matrix(image2)

print("Sparse Matrix 1:")
print(sparse_matrix_1)

print("\nSparse Matrix 2:")
print(sparse_matrix_2)

