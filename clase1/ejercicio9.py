#Genera una matriz 5x5 con valores del 1 al 25 y extrae su diagonal.
import numpy as np
matriz = np.array([
    [0.05, 0.25, 0.50, 0.75, 1.00],
    [1.25, 1.50, 1.75, 2.00, 2.25],
    [2.50, 2.75, 3.00, 3.25, 3.50],
    [3.75, 4.00, 4.25, 4.50, 4.75],
    [5.00, 5.25, 5.50, 5.75, 6.00]
])
print ("la diagonal de esta matriz es:", matriz[0, 0], matriz[1, 1], matriz[2, 2], matriz[3, 3], matriz[4, 4])

