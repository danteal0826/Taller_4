#Con esto ya se importa la biblioteca
import numpy as np

#Una forma de crear arreglos ndarray es usando una lista

#Usando arange
miArreglo=np.arange(-10,10)
print(miArreglo)
miArreglo=miArreglo.reshape((2,10))
print(miArreglo)
print(miArreglo.ndim)