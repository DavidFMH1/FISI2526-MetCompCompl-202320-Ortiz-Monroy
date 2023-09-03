import numpy as np
import matplotlib.pyplot as plt
import glob
import os

def tuplas(archivo):
    arch=open(archivo)
    lista=[]
    prim_T = arch.readline()
    lam = ""
    n = ""
    blank = 0
    while prim_T != "    data: |\n":
        prim_T = arch.readline()
    
    while prim_T != "" and prim_T != "SPECS:\n":
        if prim_T == "    data: |\n" or "  - type: tabulated k\n" == prim_T or prim_T == "\n":
            prim_T = arch.readline()
        else:
            for i in prim_T:
                if i == " ":
                    blank += 1
                elif i != " " and blank == 8:
                    lam += str(i)
                elif blank == 9 and i != "\n":
                    n += str(i)
            lista.append((float(lam),float(n)))
            prim_T = arch.readline()
            lam=""
            n=""
            blank = 0
    arch.close
    return lista

def graphics(nombre_archivo):
    lista = tuplas(nombre_archivo)
    
    x =[]
    y = []
    for i in lista:
        x.append(i[0])
        y.append(i[1])
        n = os.path.split(nombre_archivo)[1]
        n1= n.replace(".yml","")
        r= os.path.split(nombre_archivo)[0]+"\\"+n1
        n_prom = round(np.mean(y),4)
        lam_prom = np.mean(x)
        dev = round(np.std(y),4)
    plt.scatter(x,y)
    plt.ylabel("Índice de refracción")
    plt.xlabel("Lambda")
    plt.title(n1 + '\n' + 'n promedio = '+str(n_prom)+'  Desviación Estándar = '+str(dev))
    plt.savefig(r)

def iterated_graphics():
    l = glob.glob("**/*.yml", recursive=True)
    for i in range(0,len(l)):
        j = "C:\\Users\\david\\OneDrive\\Documentos\\programas\\Metodos\\FISI2526-MetCompCompl-202320-Ortiz-Monroy\\"+l[i]
        l[i]=j
        graphics(l[i])

iterated_graphics()
#para intentar desde diferentes dispositivos agregue la ruta correspondiente a su dispositivo
#ruta= "C:\Users\david\OneDrive\Documentos\programas\Metodos\FISI2526-MetCompCompl-202320-Ortiz-Monroy\Taller_1\Adhesivos Ópticos\Loctite.yml"
#lista= tuplas(ruta)
#graphics(ruta)
