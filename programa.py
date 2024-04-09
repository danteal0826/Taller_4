#Con esto ya se importa la biblioteca
import numpy as np

#Una forma de crear arreglos ndarray es usando una lista

miLista=[3,5,7,9]
#Arreglo unidimensional
miArreglo=np.array(miLista)
#Dimensiones, atributos de ndarray
print(miArreglo.ndim)
print(miArreglo.shape)
print(miArreglo.size)
print(miArreglo.dtype)
print(miArreglo.itemsize)

miArreglo2=np.array([3,6,7,90])

