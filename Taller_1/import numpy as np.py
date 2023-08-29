import numpy as np
import matplotlib.pyplot as plt

def tuplas(archivo):
    arch=open(archivo)
    lista=[]
    prim_T = arch.readline()
    lam = ""
    n = ""
    while prim_T != "    data: |\n":
        prim_T = arch.readline()
    
    if prim_T == "    data: |\n":
        prim_T = arch.readline()
        while prim_T != "" and prim_T != "SPECS:\n":
            for i in prim_T:
                if i != " ":
                    if len(lam) <= 4:
                        lam += str(i)
                    elif len(n) <= 8:
                        n += str(i)
            print ((float(lam),float(n)))
            prim_T = arch.readline( )
            lam=""
            n=""

    return

ruta='c:\\Users\\juanm\\OneDrive\\Documentos\\Felipe universidad\\FISI2526-MetCompCompl-202320-Ortiz-Monroy\\Taller_1\\Adhesivos Ópticos\\Iezzi.yml'
tuplas(ruta)