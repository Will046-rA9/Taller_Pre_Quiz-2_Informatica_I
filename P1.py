import numpy as np
import pandas as pd


print("\n\nPUNTO 1: Crear una matriz de Numpy aleatoria de 4 dimensiones y un size de 1200000 ")
m1 = np.random.randint([100, 100, 10, 12])
print(f"La matriz tiene {m1.size} elementos")
print(f"La matriz tiene {m1.ndim} dimensiones")
print(f"La matriz tiene la forma: {m1.shape}")

print("\n\nPUNTO 2: Crea una copia de la matriz creada en el ítem anterior (usar método copy) de solo 3 dimensiones (“Cortando una de las dimensiones”)")
