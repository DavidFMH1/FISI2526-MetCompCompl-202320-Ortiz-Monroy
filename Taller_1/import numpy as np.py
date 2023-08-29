import numpy as np
import matplotlib.pyplot as plt

def tuplas(archivo):
    arch=open(archivo)
    lista=[]
    prim_T = arch.readline()
    lam = ""
    n = ""
    while prim_T != "":
        if prim_T == "    data: |\n":
            for i in prim_T:
                if i != " ":
                    if len(lam) <= 4:
                        lam += str(i)
                    elif len(n) <= 8:
                        n += str(i)
            print ((float(lam),float(n)))
        lam=""
        n=""
    else:
        prim_T=arch.readline()

    return

ruta="c:\\Users\\ekkol\\OneDrive\\Documentos\\David Monroy\\FISI2526-MetCompCompl-202320-Ortiz-Monroy\\Taller_1\\Adhesivos Ópticos\\Iezzi.yml"
tuplas(ruta)