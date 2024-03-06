
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
        super().__init__(edad, color)
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


#Nuevo ejemplo 
class Padre:
    def hablar(self):
        print("Hola")

class Madre:
    def reir(self):
        print('ja ja ja')
class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass

mi_nieto = Nieto()
mi_nieto.reir()
print(Nieto.__mro__)#Imprime el orden de impreesión de herencia 



print("\n----------------------------------------------------------------")
print('Práctica Herencia Extendida 1 ')
print("\n----------------------------------------------------------------")

"""Si la clase Hija ha heredado de su padre la forma de reir, y de su madre la vocación, y hoy tienen el mismo trabajo en la Fiscalía, crea la herencia múltiple que le permita a esta clase heredar correctamente de Padre y Madre.

Completa el código suministrado a continuación para lograrlo."""

class Padre():
    def trabajar(self):
        print("Trabajando en el Hospital")
    
    def reir(self):
        print("ja ja ja")

class Madre():
    def trabajar(self):
        print("Trabajando en fiscalía")
        
class Hija(Madre, Padre):
    pass

print("\n----------------------------------------------------------------")
print('Práctica Herencia Extendida 2 ')
print("\n----------------------------------------------------------------")

"""
Práctica Herencia Extendida 2
"El ornitorrinco es una de las criaturas más raras del mundo: aunque es un mamífero, pone huevos; y amamanta a sus crías pero no tienen mamas." (National Geographic)

Crea una clase Ornitorrinco que herede de otras clases: Vertebrado, Pez, Reptil, Ave y Mamifero, tal que "construyas" un animal que tiene los siguientes métodos y atributos:

- poner_huevos()

- tiene_pico = True

- vertebrado = True

- venenoso = True

- nadar()

- caminar()

- amamantar()"""

class Vertebrado:
    vertebrado = True

class Ave(Vertebrado):
    tiene_pico = True
    def poner_huevos(self):
        print("Poniendo huevos")

class Reptil(Vertebrado):
    venenoso = True

class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")
    def poner_huevos(self):
        print("Poniendo huevos")

class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")
    def amamantar(self):
        print("Amamantando crías")

class Ornitorrinco(Mamifero, Pez, Reptil, Ave):
    pass


print("\n----------------------------------------------------------------")
print('Práctica Herencia Extendida 3 ')
print("\n----------------------------------------------------------------")
"""Práctica Herencia Extendida 3
Un hijo ha heredado de su padre todas sus características, sin embargo, tienen diferentes hobbies. Logra que la clase Hijo herede de Padre todos sus métodos y atributos, sobreescribiendo el método hobby() para que se devuelva[1]: "Juego videojuegos en mi tiempo libre"

[1]: asegúrate de utilizar return seguido de una cadena de texto"""

class Padre():
    color_ojos = "marrón"
    tipo_pelo = "rulos"
    altura = "media"
    voz = "grave"
    deporte_preferido = "tenis"
    def reir(self):
        return "Jajaja"
    def hobby(self):
        return "Pinto madera en mi tiempo libre"
    def caminar(self):
        return "Caminando con pasos largos y rápidos"
        
class Hijo(Padre):
    def hobby(self):
        return "Juego videojuegos en mi tiempo libre"
