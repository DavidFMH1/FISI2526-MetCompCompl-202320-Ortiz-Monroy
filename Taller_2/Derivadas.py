import numpy as np
import matplotlib.pyplot as plt
import math


def flujo_magnetico(t,r=0.025/2,w=3.5,B=0.05,f=1000):
    return np.pi*(r**2)*B*np.sin(w*t)*np.cos(2*np.pi*f*t)

def derivada(t,f,b):
    h=t[1]-t[0]
    print(f(b))
    #return (f(t+h)-f(t-h))/(2*h)

def corriente(dB,R=1750):    
    return -1/R*(dB)

def Newton(B,dB,x_n,itmax=100,precision=1e-10):
    error=1.
    it=0
    while error>precision and it<itmax:
        try:
            x_n1=x_n-B(x_n)/dB(x_n,B)
        except ZeroDivisionError:
            print('División por cero')
        x_n=x_n1
        it+=1
    if it==itmax:
        return False
    else:
        return x_n

def raices(t):
    tole=10
    raices=np.array([])
    for i in t:
        raiz=Newton(I,dI,i)
        if raiz != False:
            aprox=np.round(raiz,tole)
            if aprox not in raices:
                raices=np.append(raices,aprox)
    raices.sort()
    return raices

t=np.linspace(0,1,1000)
B=flujo_magnetico(t)
dB=derivada(t,flujo_magnetico)
I=corriente(dB)
dI=derivada(t,corriente(),dB)
 
print(dI)
#plt.plot(t,B,label="Flujo magnético")
#plt.plot(t,dB,label="Derivada Flujo")
#plt.plot(t,I,label="Corriente",color='g')
#plt.axhline(y=0,color='r')
#print(dI)
#plt.legend()
#plt.show()
