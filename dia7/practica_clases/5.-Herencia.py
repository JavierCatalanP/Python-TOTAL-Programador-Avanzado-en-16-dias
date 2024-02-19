#Herencia - Principio 1

#Ejemplo 1
class Animal:
    pass 

class Pajaro(Animal): #Herencia hija de la clase Animal
    pass 

print(Pajaro.__bases__)#[<class 'type'>]


#Ejemplo 2
class Animal:
    def nacer(self):
        print("Este animal ha nacido")
    
class Pajaro(Animal): #Herencia hija de la clase Animal
    pass 

piolin = Pajaro()

piolin.nacer() #Imprime: Este animal ha nacido


#Ejercicio 3
class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color
        
    def nacer(self):
        print("Este animal ha nacido")
    
class Pajaro(Animal): #Herencia hija de la clase Animal
    pass 

piolin = Pajaro(2, 'amarillo')

print(piolin.edad) #Imprime: 2
print(piolin.color) #Imprime: amarillo

print("\n----------------------------------------------------------------")
print('Práctica Herencia 1')
print("----------------------------------------------------------------\n")

"""Crea una clase llamada Persona, que tenga los siguientes atributos de instancia: nombre, edad. Crea otra clase, Alumno, que herede de la primera estos atributos."""

class Persona:
    def __init__(self,nombre, edad):
        self.nombre = nombre
        self.edad = edad
class Alumno(Persona):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
        
print("\n----------------------------------------------------------------")
print('Práctica Herencia 2')
print("----------------------------------------------------------------\n")

"""Crea una clase llamada Mascota, que tenga los siguientes atributos de instancia: edad, nombre, cantidad_patas. Crea otra clase, Perro, que herede de la primera sus atributos."""

class Mascota:
    def __init__(self, edad, nombre, cantidad_patas):
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas

class Perro(Mascota):
    def __init__(self, edad, nombre, cantidad_patas):
        super().__init__(edad, nombre, cantidad_patas)

print("\n----------------------------------------------------------------")
print('Práctica Herencia 3')
print("\n----------------------------------------------------------------")
"""Crea una clase llamada Vehiculo, que contenga los métodos acelerar() y frenar() (puedes dejar el código de los métodos en blanco con pass). Crea una clase llamada Automovil que herede estos métodos de Vehiculo."""

class Vehiculo:
    def acelerar(self):
        pass
    def frenar(self):
        pass
class Automovil(Vehiculo):
    def __init__(self):
        super().__init__()