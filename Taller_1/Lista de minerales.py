import minerales as m
import pandas as pd
import numpy as np

#archivo= "minerales.txt"
separador= "/t"

datos=pd.read_csv("minerales.txt", sep='\t')
datosArray=np.array(datos)

for i in range(len(datos)):
    for j in range len(8):
        mineral=m.Mineral(datosArray[i][j])
        print(mineral)





"""archivo=open("minerales.txt","r")
print(archivo.read())
archivo.close()"""