import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math 
import sympy as sym

_x = sym.symbols('x', real=True)
x = np.linspace(-1,3,100)
h = 1.3e-4

def function(x,a,b):
    return np.sqrt((a**2+((b**2/a**2)-1)*x**2)/((a**2+h)-x**2))

def Derivative(f,x,n,h=1e-2):
    return (f(x+h,n)-f(x-h,n))/(2*h)

def integra_rectang(f, x_0, x_1, pres):
    
    x = np.linspace(x_0,x_1,pres)
    
    h = x[1]-x[0]
    
    res = 0
    
    for i in range(len(x)-1):
        res += (((h)*f(x[i]))+((h)*f(x[i+1])))/2
        
    return res

def integral_trapecio(f, x_0, x_1, pres):
    
    x = np.linspace(x_0,x_1,pres)
    
    h = x[1]-x[0]
    
    res = (h/2)*(f(x_0,x_0,3)+f(x_1,x_0,3))
    
    for i in range(len(x)-1):
        res += h*(f(x[i],x_0,3))
    
    return res

def integral_simpson1_3(f, a, b):
    
    x_m = (a+b)*0.5
    
    h = x_m-a
    
    res = (h/3)*(f(a,a,b)+4*f(x_m,a,b)+f(b,a,b))
    
    return res

def simpson_compuesto(f,x_0,x_1,pres):
    
    x = np.linspace(x_0,x_1,pres)
    
    h = x[1]-x[0]
    
    res = f(x_0)+f(x_1)
    
    for i in range(len(x[1:-1])):
        if i%2 == 0:
            res += 4*f(x[i])
        else:
            res += 2*f(x[i])
    return res*(h/3)

#print(integra_rectang(function,0,1,100))
print(integral_trapecio(function,-1+h,1-h,100))
#print(integral_simpson1_3(function,1,1))
#print(simpson_compuesto(function,0,1,100))