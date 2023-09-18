#raices de polinomios 5

import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
import math

_x = sym.symbols('x', real=True)
x = np.linspace(0,50,150)

def function(x,n):
    return np.e**(-x)*(x**n)

def derivada_enesima(f,x,n,h=1e-6):
    
    fc = f(x,n)
    
    return sym.lambdify([x],sym.diff(fc,x,n),'numpy')

def Derivative(f,x,n,h=1e-2):
    return (f(x+h,n)-f(x-h,n))/(2*h)

def function_2(x,n):
    der = derivada_enesima(function,_x,n)
    return  ((np.e**x)/math.factorial(n))*der(x)

def GetNewtonMethod(f,df,xn,n,itmax=100,precision=1e-8):
    
    error = 1.
    it = 0
    
    while error > precision and it < itmax:
        
        try:
            
            xn1 = xn - f(xn,n)/df(f,xn,n)
            # Criterio de parada
            error = np.abs(f(xn,n)/df(f,xn,n))
            
        except ZeroDivisionError:
            print('Division por cero')
            
        xn = xn1
        it += 1
        
   # print('Raiz',xn,it)
    
    if it == itmax:
        return False
    else:
        return xn

def GetAllRoots(x,n, tolerancia=5):
    
    Roots = np.array([])
    
    for i in x:
        
        root = GetNewtonMethod(function_2,Derivative,i,n)
        
        if root != False:
            
            croot = np.round(root, tolerancia)
            
            if croot not in Roots:
                Roots = np.append(Roots,croot)
                
    Roots.sort()
    
    return Roots

def polinomio_laguerre(f,x,_x):
    
    n = 0
    
    while n <= 19:
        r = GetAllRoots(x,n)
        print('ploinomio n°'+str(n+1),r)
        n += 1

print(polinomio_laguerre(function_2,x,_x))