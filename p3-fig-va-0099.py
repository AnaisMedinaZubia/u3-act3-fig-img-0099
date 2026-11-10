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