import matplotlib as mpl

class Mineral:
    
    def __init__(self, nombre, dureza, lustre, rompimiento_por_fractura, color, composicion, sistema_cristalino, specific_gravitiy):
        
        self.nombre=nombre
        self.dureza=dureza
        self.lustre=lustre
        self.rompimiento_por_fractura=rompimiento_por_fractura
        self.color=color
        self.composicion=composicion
        self.sistema_cristalino=sistema_cristalino
        self.specific_gravity=specific_gravitiy
        
    def silicato (self):
        a=True
        if "Si" and "O" in self.composicion:
            return a
        else:
            a=False
            return a
        
    def densidad (self):
        densidad= 997*self.specific_gravity
        return densidad
            
    def color_comun(self):
        return( mpl.colors(self.color))    
        
    def dureza_rompimiento_organizacion (self):
        tipo_de_rompimiento=""
        if self.rompimiento_por_fractura == False:
            tipo_de_rompimiento= "No se rompe por fractura"
        else:
            tipo_de_rompimiento="Se rompe por fractura"

        return(str(self.dureza)+", "+tipo_de_rompimiento+", "+(self.sistema_cristalino))
        

mineral1= Mineral(nombre="grafito", dureza=1.5, lustre="METÁLICO", rompimiento_por_fractura=False, color="#5f6168", composicion="SiO", sistema_cristalino="HEXAGONAL", specific_gravitiy=2.2)

print(mineral1.dureza_rompimiento_organizacion())