#Multiplica dos matrices 3x3 de enteros aleatorios entre 1 y 10
import numpy as np
array_1 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
array_2 = np.array([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])
resultado = np.dot(array_1, array_2)
print("El resultado de la multiplicación de las dos matrices es:")
print(resultado)

    