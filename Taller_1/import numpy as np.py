import numpy as np
import matplotlib.pyplot as plt

def tuplas(archivo):
    arch=open(archivo)
    lista=[]
    prim_T = arch.readline()
    lam = ""
    n = ""
    blank = 0
    while prim_T != "    data: |\n":
        prim_T = arch.readline()
    
    if prim_T == "    data: |\n":
        prim_T = arch.readline()
        while prim_T != "" and prim_T != "SPECS:\n":
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

    return print(lista)

ruta="C:\\Users\\juanm\\OneDrive\\Documentos\\Felipe universidad\\FISI2526-MetCompCompl-202320-Ortiz-Monroy\\Taller_1\\Materia inorgánica\\Sinnock-solid-115.95K.yml"
tuplas(ruta)