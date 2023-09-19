import numpy as np 
import minerales as m
import pandas as pd

class ExpansionTermicaMineral(m.Mineral):
    def __init__(self, nombre, dureza, lustre, rompimiento_por_fractura, color, composicion, sistema_cristalino, specific_gravitiy, archivo):
        self.archivo=archivo
        m.Mineral.__init__(self, nombre, dureza, lustre, rompimiento_por_fractura, color, composicion, sistema_cristalino, specific_gravitiy)

    def csv(archivo):
        datos=pd.read_csv(archivo,sep=",")
        datosArray=np.array(datos)
        temperatura=np.array([])
        volumen=np.array([])
        array=np.array()
        for i in range(len(datosArray)):
            temperatura=np.append(temperatura,datosArray[i][0])
        for i in range(len(datosArray)):
            volumen=np.append(volumen,datosArray[i][1])

        return np.append(array,temperatura,volumen)
        
           

 

    
