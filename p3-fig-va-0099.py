import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import cv2 

# Anais Medina  NC 0099
print("Anais Medina NC 0099")
print("UIII Act3 colocar puntos a una imagen  en blanco y negro")
mi_iagen = cv2.imread("Mary.jpg")
plt.imshow(mi_iagen)
plt.title("Mary y Anais Medina NC 0099")
plt.show()
print("----- Puntos en la imagen-------")
plt.imshow(mi_iagen)
x = [100,100,300,350]
y = [100,400,500,200]
plt.scatter(x, y, s=20, c="red")
plt.show()
print("----- cuadro en la imagen-------")
img_Mary = cv2.imread("Mary.jpg")
plt.imshow(img_Mary)
x = [100, 100, 500, 500, 100]
y = [500, 100, 100, 500, 500]
plt.plot(x, y, c="blue")
plt.show()
 

print("----- Cuadro en la imagen -----")
img_Mary = cv2.imread("Mary.jpg")
img_Mary = cv2.cvtColor(img_Mary, cv2.COLOR_BGR2RGB)

plt.imshow(img_Mary)

x = [100, 100, 500, 500, 100]
y = [500, 100, 100, 500, 500]

plt.plot(x, y, c="blue")
plt.title("Cuadro en la imagen de Mary")
plt.show()

print("----- Circulo en la imagen -----")
img_Mary = cv2.imread("Mary.jpg")
img_Mary = cv2.cvtColor(img_Mary, cv2.COLOR_BGR2RGB)

plt.imshow(img_Mary)

circulo = plt.Circle((300, 300), 100, color="red", fill=False)

plt.gca().add_patch(circulo)
plt.title("Circulo en la imagen de Mary")
plt.show() 