import numpy as np

a=np.array([5,10,15,20,25])
print(a)
b=np.array([3,4,7,9,56])
print(b)

c=a-b
print("1)",c)
c=a+b
print("2)",c)
c=a*b
print("3)",c)
c=a/b
print("4)",c)
c=b**2
print("5)",c)
c=np.sin(b)
print("6)",c)
c=(b>6)
print("7)",c)
c=a@b
print("8)",c)
b+=1
print("9)",b)
c=a/b
print("10)",c)

#La clase ndarrary define otros metodos a trabajar
a=np.array([5,10,-1,20,25])
b=np.array([3,4,7,9,56])
c=a.sum()
print("1)",c)
c=a.min()
print("2)",c)
c=a.sort()
print("3)",c)

#Arreglos bidimensional
a=np.array([[5,10,-1,20,25],[3,6,4,8,12]])
print(a)
print(a.sum())
print(a.sum(axis=1))
print(a.sum(axis=0))
print(a.size)
print(a.shape)
print(np.sqrt(a))
print(np.exp(a))

#ejemplo 1
a=np.array([[5,10,-1,20,25],[3,6,4,8,12]])
b=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(a)
print(b)
c=np.add(a,b)
print(c)
c=a+b
print(c)

#Ejemplo 2
a=np.array([7.8,5.6,3.4])
print(a.round())
a=np.array([7.8656,5.6232323,3.43232323])
print(a.round(decimals=2))
print(np.ceil(a))
print(np.floor(a))
print(np.gradient(a))