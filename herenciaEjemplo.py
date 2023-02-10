class Empleado:
    def __init__(self, nombre, edad , sueldo):
        self.nombre = nombre
        self.edad = edad
        self.sueldoBase = sueldo
    
    def calcularSueldo(self, descuentos, bonos):
        return self.sueldoBase - descuentos + bonos

class AgenteVentas(Empleado):
    def __init__(self, nombre, edad, sueldo,mostrador):
        self.numeroMostrador = mostrador
        super().__init__(nombre, edad, sueldo) # Referencia a Herencia de Empleado

class Tripulante(Empleado):
    def mostrarRenovacion(self):
        if self.edad <= 50:
            print("Renovar cada año") 
        else:
            print("Renovar cada 6 meses")
            
empleado1 = Empleado("Empleado Uno",25,55000)
empleado1.nombre
empleado2 = AgenteVentas("Cynthia Ramirez",31,55000,7)
empleado2.nombre
empleado2.calcularSueldo(0,3000)
empleado3 = Tripulante("Empleado Tres",35,30000)
empleado3.mostrarRenovacion()