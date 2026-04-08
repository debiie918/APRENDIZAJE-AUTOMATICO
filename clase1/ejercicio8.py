#Crea un array de 15 valores aleatorios entre 1 y 100 e imprime su máximo, mínimo y promedio.
import numpy as np
array_aleatorios = np.array([2, 4, 99, 12, 45, 67, 23, 89, 34, 56, 78, 90, 10, 22, 31])
maximo = np.max(array_aleatorios)
minimo = np.min(array_aleatorios)
promedio = np.average(array_aleatorios)
print("El valor máximo :", maximo)
print("El valor mínimo es:", minimo)
print("Y el promedio de ambos es:", promedio)

