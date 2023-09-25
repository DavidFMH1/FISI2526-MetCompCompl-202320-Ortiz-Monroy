import numpy as np
import matplotlib.pyplot as plt
import math
import sympy as sym

_t = sym.symbols('t')

def flujo2(t,r=0.025/2,w=3.5,B=0.05,f=1000):
    return np.pi*(r**2)*B*sym.cos(w*t)*sym.cos(2*np.pi*f*t)

def derSympy(f):
    return sym.diff(f,_t)

def corriente2(t,R=1750):
    return(-1/R)*derSympy(flujo2(t))

def GetNewton(f,df,xn,itmax=10000,precision=1e-14):
    
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
    
def GetRoots(f,df,x,tolerancia = 10):
    
    Roots = np.array([])
    
    for i in x:
        
        root = GetNewton(f,df,i)

        if  type(root)!=bool:
            croot = np.round( root, tolerancia )
            
            if croot not in Roots:
                Roots = np.append(Roots, croot)
                
    Roots.sort()
    
    return Roots

def Getinstants(f,df,x):
    roots = GetRoots(f,df,x)
    r = np.array([])
    for i in roots:
        if i >= 0:
            if len(r) < 3:
                r = np.append(r,i) 
    return r

t = np.linspace(0,0.001,100)

ro = Getinstants(sym.lambdify([_t],corriente2(_t),'numpy'),sym.lambdify([_t],derSympy(corriente2(_t)),'numpy'),t)

c = sym.lambdify([_t],corriente2(_t),'numpy')

plt.scatter(t,c(t))
plt.show()
print(ro)