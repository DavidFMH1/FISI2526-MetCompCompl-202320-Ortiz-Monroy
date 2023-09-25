#Punto 3.1 Polinomios de Laguerre

import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
import math

_x = sym.symbols('x')

def GetLaguerre(n,x):
    if n==0:
        poly = sym.Number(1)
    elif n==1:
        poly = - x + 1
    else:
        poly = ((2*(n-1)+1-x)*GetLaguerre(n-1,x)-((n-1)*GetLaguerre(n-2,x)))/(n)
   
    return sym.expand(poly,x)

def DiffLaguerre(n,x):
    pn = GetLaguerre(n,x)
    return sym.diff(pn,x,1)

def GetNewton(f,df,xn,itmax=10000,precision=1e-12):
    
    error = 1.
    it = 0
    
    while error >= precision and it < itmax:
        
        try:
            
            xn1 = xn - f(xn)/df(xn)
            
            error = np.abs(f(xn)/df(xn))
            
        except ZeroDivisionError:
            print('Zero Division')
            
        xn = xn1
        it += 1
        
    if it == itmax:
        return False
    else:
        return xn
    
def GetRoots(f,df,x,tolerancia = 5):
    
    Roots = np.array([])
    
    for i in x:
        
        root = GetNewton(f,df,i)

        if  type(root)!=bool:
            croot = np.round( root, tolerancia )
            
            if croot not in Roots:
                Roots = np.append(Roots, croot)
                
    Roots.sort()
    
    return Roots

def GetAllRootsGLag(n):

    j = n+((n-1)*np.sqrt(n))
    xn = np.linspace(0,j,100)
    
    Legendre = np.array([])
    DLegendre = np.array([])
    
    for i in range(n+1):
        Legendre =  np.append(Legendre,GetLaguerre(i,_x))
        DLegendre = np.append(DLegendre,DiffLaguerre(i,_x))
    
    poly = sym.lambdify([_x],Legendre[n],'numpy')
    Dpoly = sym.lambdify([_x],DLegendre[n],'numpy')
    Roots = GetRoots(poly,Dpoly,xn)

    if len(Roots) != n:
        ValueError('El número de raíces debe ser igual al n del polinomio.')
    
    return Roots

def GetWeigthsLag(n,x):
    
    weigths = np.array([])
    roots = GetAllRootsGLag(n)
    L_n1 = sym.lambdify([x],GetLaguerre(n+1,x),'numpy')
    
    for i in roots:
        
        w = i/(((n+1)**2)*(L_n1(i))**2)
        
        if w not in weigths:
            
            weigths = np.append(weigths,w)
            
    return weigths

nl = 2
    
print('polinomios de Laguerre')
print(GetLaguerre(nl,_x))
print(GetAllRootsGLag(nl))
print(GetWeigthsLag(nl,_x))

#Punto 3.2 Polinomios de Hermite

def GetHermite(n,x):
    if n == 0:
        poly = sym.Number(1)
    elif n == 1:
        poly = 2*x
    else:
        poly = 2*x*GetHermite(n-1,x) - sym.diff(GetHermite(n-1,x),x,1)
    return sym.expand(poly,x)

def DiffHermite(n,x):
    pn = GetHermite(n,x)
    return sym.diff(pn,x,1)

def GetAllRootsGHer(n):
    
    c = np.sqrt(4*n+1)
    xn = np.linspace(-c,c,100)
    
    Hermite = np.array([])
    DHermite = np.array([])
    
    for i in range(n+1):
        Hermite =  np.append(Hermite,GetHermite(i,_x))
        DHermite = np.append(DHermite,DiffHermite(i,_x))
    
    poly = sym.lambdify([_x],Hermite[n],'numpy')
    Dpoly = sym.lambdify([_x],DHermite[n],'numpy')
    Roots = GetRoots(poly,Dpoly,xn)

    if len(Roots) != n:
        ValueError('El número de raíces debe ser igual al n del polinomio.')
    
    return Roots

def GetWeigthsHer(n,x):
    
    roots = GetAllRootsGHer(n)
    l_h1 = sym.lambdify([x],GetHermite(n-1,x),'numpy')
    weigths = np.array([])
    
    for i in roots:
        
        w = (2**(n-1)*math.factorial(n)*np.sqrt(n))/((n**2)*(l_h1(i)**2))
        
        if w not in weigths:
            
            weigths = np.append(weigths,w)
    
    return weigths

print('polinomios de Hermite')
print(GetHermite(2,_x))
print(GetAllRootsGHer(2))
print(GetWeigthsHer(2,_x))

#Punto 3.3 Aplicación

def function(x):
    return np.sqrt(x)

def IntegralLag(f,n):
    
    r = GetAllRootsGLag(n)
    w = GetWeigthsLag(n,_x)
    
    res = 0
    
    for i in range(len(r)):
        res += w[i]*f(r[i])
        
    return res

print('punto 3 aplicación')
#se integra de esta manera por la forma de la integral resultante en la Imagen_1
print((2/np.sqrt(np.pi))*IntegralLag(function,15))
#se observa que el resultado es aproximadamente 1