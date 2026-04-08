
#Dada una matriz 5x5 de enteros aleatorios entre 1 y 20, calcula la suma de cada fila y columna
import numpy as np

matriz = np.array([
    [1.2, 1.5, 1.3, 1.7, 1.9],
    [2.0, 2.3, 2.1, 2.5, 2.7], 
    [3.1, 3.4, 3.2, 3.6, 3.8],
    [4.1, 4.4, 4.2, 4.6, 4.8],
    [5.1, 5.4, 5.2, 5.6, 5.8]
])
for i in range(5):
    sum_fila = sum(matriz[i])
    print("La suma de la fila", i, "es:", sum_fila)
    