#polnomio legendre

import numpy as np
import sympy as sym
import math
import matplotlib.pyplot as plt

_x = sym.symbols('x', real=True)

def legendre(x, n):
    return sym.simplify((1/((2**n)*(math.factorial(n))))*sym.diff((((x**2)-1)**n),x,n))

def legendre1(l):
    return sym.lambdify([_x],l, "numpy")

def derivada_legendre(f):
    return sym.lambdify([_x],sym.diff(f,_x), "numpy")

#ingrese n

n = 2
print(legendre(_x,n))

def Derivative(f,x,n,h=1e-2):
    return (f(x+h,n)-f(x-h,n))/(2*h)

def GetNewtonMethod(f,xn,n,itmax=100,precision=1e-8):
    
    error = 1.
    it = 0
    
    f1 = legendre1(f(_x,n))
    df = derivada_legendre(f(_x,n))
    
    while error > precision and it < itmax:
        
        try:
            
            xn1 = xn - f1(xn)/df(xn)
            # Criterio de parada
            error = np.abs(f1(xn)/df(xn))
            
        except ZeroDivisionError:
            print('Division por cero')
            
        xn = xn1
        it += 1
        
   # print('Raiz',xn,it)
    
    if it == itmax:
        return False
    else:
        return xn

def GetAllRoots(n, tolerancia=5):
    
    Roots = np.array([])
    
    for k in range(n):
        
        i = np.cos(((4*k+3)*np.pi)/(4*n+2))
        
        root = GetNewtonMethod(legendre,i,n)
        
        if root != False:
            
            croot = np.round(root, tolerancia)
            
            if croot not in Roots:
                Roots = np.append(Roots,croot)
                
    Roots.sort()
    
    return Roots

print(GetAllRoots(2))