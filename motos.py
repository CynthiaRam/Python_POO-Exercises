class Motocicleta:
    
    estado = "Nuevo"
    
    def __init__(self,color,matricula,combustible_litros,numero_ruedas,marca,modelo,
                 fecha_fabricacion,velocidad_punta,peso, motor):
        self.color = color
        self.matricula = matricula
        self.combustible_litros = combustible_litros
        self.numero_ruedas = numero_ruedas
        self.marca = marca
        self.modelo = modelo
        self.fecha_fabricacion = fecha_fabricacion
        self.velocidad_punta = velocidad_punta
        self.peso = peso
        self.motor = motor
    
    def arrancar(self):
        if self.motor == False:
            print("El motor ha arrancado")
            self.motor = True
            print(self.motor)
            
        else:
            print("Motor ya estaba en marcha")
            
    
    def detener(self):
        if self.motor == True:
            print("Motor se ha detenido")
            self.motor = False
            print(self.motor)
            
        else:
            print("Motor ya estaba detenido")
            
moto1 = Motocicleta("Azul","RAM123",10,2,"Suzuki","Prime","1-02-2023", 30,12,False)
moto2 = Motocicleta("Rojo","KBA456",10,2,"Yamaha","Premium","30-06-2022", 45,35,True)
