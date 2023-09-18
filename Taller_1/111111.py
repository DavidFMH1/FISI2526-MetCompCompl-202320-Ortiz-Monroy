import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

N = 12
x = np.linspace(0,np.pi/2,N+1)

def function(x):
    return np.cos(x)

def cuarta_derivada(f,x):
    h = x[1]-x[0]
    return (f(x+2*h)-4*f(x+h)+6*f(x)-4*f(x-h)+f(x-2*h))/h**4

def error(f,x):
    
    h = x[1]-x[0]
    
    f4 = cuarta_derivada(function,x)
    
    maxf = np.max(np.abs(f4))
    
    err = ((x[-1]-x[0])*(h**4)*(maxf))/180
    
    return err

print(error(function,x))
