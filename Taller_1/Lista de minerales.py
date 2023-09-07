import minerales as m
import pandas as pd
import numpy as np

#archivo= "minerales.txt"
separador= "/t"

datos=pd.read_csv("minerales.txt", sep='\t')
datosArray=np.array(datos)
mineralesArray=np.array([])

print(datosArray)
for i in range(len(datos)):
    mineral=m.Mineral(datosArray[i][0],datosArray[i][1],datosArray[i][2],datosArray[i][3],datosArray[i][4],datosArray[i][5],datosArray[i][6],datosArray[i][7])
    mineralesArray = np.append(mineralesArray,mineral)

print(mineralesArray)
