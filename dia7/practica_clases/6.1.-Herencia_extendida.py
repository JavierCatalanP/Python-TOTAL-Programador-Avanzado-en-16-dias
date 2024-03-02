
#Herencia extendida
class Animal:
    
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color
    
    def nacer(self):
        print("Este animal ha nacido")
        
    def hablar(self):
        print("Este animal emite un sonido")


class Pajaro(Animal):
    
    #crear el propio metodo
    def __init_subclass__(self, edad, color, altura_vuelo):
        self.edad = edad
        self.color = color
        self.altura_vuelo = altura_vuelo
    
    def hablar(self):#Este método existe y sustituye
        print("Pio")  
        
    def volar(self, metros):
        print(f"El pajaro volvo {metros} metros")
    
piolin = Pajaro(3, 'amarillo')

piolin.nacer() #1.- Acceder y modifican atributos del objeto

piolin.hablar() #Otro tipo de método donde hereda y modifica el estado de la clase.

piolin.volar(50)

mi_animal = Animal(5, 'negro')