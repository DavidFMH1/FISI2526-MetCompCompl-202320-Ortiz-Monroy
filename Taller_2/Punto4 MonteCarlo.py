import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

N=1000000
x_1=np.random.uniform(0,np.pi,N)

def funcion(x):
    return np.e**(-x)

# Punto 4.1

f=funcion(x_1)
b=np.pi
a=0
I=(b-a)/N*sum(f)
valr=-np.exp(-np.pi)+1
error=abs((valr-I)/valr)*100
print("El resultado de tu integral es {0}, con un error porcentual de {1}%".format(I,error))

#Punto 4.3

R=1
x = np.random.uniform(-R,R,N)
y = np.random.uniform(-R,R,N)
z = np.random.uniform(-R,R,N)

suma=0

for i in range (N):
    if x[i]**2+y[i]**2+z[i]**2<=R**2:
        suma+= np.sin(x[i]**2+y[i]**2+z[i]**2)*np.exp(x[i]**2+y[i]**2+z[i]**2)

I= ((2*R)**3)*suma/N
print(I)