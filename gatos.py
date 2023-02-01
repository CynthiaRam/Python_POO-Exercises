# crear una clase llamada gato 
# 3 atributos nombre edad y alimentos favoritos (string , entero , lista)
# metodo si es adulto , si un alimento es el favorito del gato 

class Gato:
    
    especie = "mamifero"
    
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        self.alimentos=[]
        
    def esAdulto(self):
        if self.edad > 1:
            print(self.nombre, "Es adulto")
        else:
            print(self.nombre, "Es cachorro")
            
    def alimentoFavorito(self, alimento):
        return alimento in self.alimentos
    
p=Gato('Peluchin',2)
p.nombre