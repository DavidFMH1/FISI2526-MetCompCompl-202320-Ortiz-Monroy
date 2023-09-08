import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

archivo = pd.read_csv('C:\\Users\\david\\OneDrive\\Documentos\\programas\\Metodos\\FISI2526-MetCompCompl-202320-Ortiz-Monroy\\Taller_1\\graphite_mceligot_2016.csv', sep='\t')

d_a = np.array(archivo)

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
    
    plt.scatter(x,y)
    plt.show()
    
l = leer_array(d_a)

grafica(l)