import numpy as np
import pandas as pd


print("\n\nPUNTO 1: Crear una matriz de Numpy aleatoria de 4 dimensiones y un size de 1200000 ")
m1 = np.random.random([100, 100, 10, 12]).round(2)
print(f"La matriz tiene {m1.size} elementos")
print(f"La matriz tiene {m1.ndim} dimensiones")
print(f"La matriz tiene la forma: {m1.shape}")

print("\n\nPUNTO 2: Crea una copia de la matriz creada en el ítem anterior (usar método copy) de solo 3 dimensiones (Cortando una de las dimensiones); \nPUNTO 3 De la matriz 3D, muestra todos los atributos propios de dicha matriz , dimensión, tamaño,etc")
print("***Copia 3D de la matriz del punto 1, fijando la dimensión 0 en cero:")
m2 = m1[0,:,:,:].copy()
print(f"El tamaño resultante es: {m2.size} elementos")
print(f"La dimensión resultante es: {m2.ndim}D")
print(f"La forma resultante es: {m2.shape}")

print("\n\nPUNTO 4 Modificar su forma y pasarla a 2D")
m4 = m2.copy().reshape([12, 1000])
print(m4)
