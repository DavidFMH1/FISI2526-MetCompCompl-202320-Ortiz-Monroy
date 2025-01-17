import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

archivo_g = pd.read_csv('C:\\Users\\david\\OneDrive\\Documentos\\programas\\Metodos\\FISI2526-MetCompCompl-202320-Ortiz-Monroy\\Taller_1\\graphite_mceligot_2016.csv', sep='\t')
archivo_o = pd.read_csv('C:\\Users\\david\\OneDrive\\Documentos\\programas\\Metodos\\FISI2526-MetCompCompl-202320-Ortiz-Monroy\\Taller_1\\olivine_angel_2017.csv', sep='\t')

d_a = np.array(archivo_g)
d_b = np.array(archivo_o)

def leer_array(a):
    m = []
    for i in a:
        for j in i:
            l = j.split(sep=',')
            m.append((float(l[0]),float(l[1])))
    return m

def grafica(l):
    
    x = []
    y = []

    for i in l:
        x.append(i[0])
        y.append(i[1])
    
    for i in range(len(x)-1):
        dx = x[i+1]-x[i]
        dy = y[i+1]-y[i]
        
        alpha = (dy/dx)*(1/y[i])
        
        plt.scatter(y[i],alpha)
    plt.ylabel("Alpha")
    plt.xlabel("Temperatura")
    plt.savefig('C:\\Users\\david\\OneDrive\\Documentos\\programas\\Metodos\\FISI2526-MetCompCompl-202320-Ortiz-Monroy\\Taller_1\\olivine_angel_2017')
    plt.scatter(x,y)
    plt.ylabel("Volumen")
    plt.xlabel("Temperatura")
    plt.savefig('C:\\Users\\david\\OneDrive\\Documentos\\programas\\Metodos\\FISI2526-MetCompCompl-202320-Ortiz-Monroy\\Taller_1\\olivine_angel_2017')
    
l = leer_array(d_a)
k = leer_array(d_b)

grafica(l)
#grafica(k)