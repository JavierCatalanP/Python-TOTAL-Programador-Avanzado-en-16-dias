#Clases atributos 
"""Primero que nada, es importante distinguir que existen dos [2] tipos de atributos.

Por un lado están los atributos [1] de clase.

Se trata de atributos que pertenecen a la clase y por lo tanto serán los mismos para todos los objetos

que vayan a ser creados desde esta clase.

Por ejemplo, si nuestra clase tiene el atributo alas igual a true, eso significa que luego todos los

objetos pájaros que creemos van a tener ese mismo atributo.

Es decir, que todos los objetos pájaros van a decir que es verdad que tienen alas.

Pero por otro lado, también están los atributos de instancia que pertenecen a la instancia de la clase

o al objeto.

Son atributos particulares que pueden ser distintos en cada instancia.

En nuestro caso, de cada pájaro, por ejemplo, el atributo color va a tener un valor distinto para

cada pájaro que vayamos a crear.

Uno puede ser negro, otro marrón.

Y así ahora mismo en pizza vamos a aprender primero a crear atributos de instancia y luego los atributos

de clase."""


#Creando atributos de instancia

class Pajaro:
    #Atributos de clase
    alas = True 
    
    def __init__(self, color, especie): #Metódo Constructor
        self.color = color #Atributo de instancia
        self.especie = especie #Atributo de instancia
        
mi_pajaro = Pajaro('negro', 'tucán') #Atributos de instancia

print(f" Mi pajaro es un {mi_pajaro.especie}, y es de color {mi_pajaro.color}") #Mi pajaro es un tucán, y es de color negro

print(mi_pajaro.alas) #True 
print(Pajaro.alas) #True   / Todos los objetos comparten los mismos atributos de la clase. 

#self representa a la instancia del objeto de ser creado
#color se escribe 3 veces , 


print("\n----------------------------------------------------------------")
print('Práctica 1 - Atributos ')
print("----------------------------------------------------------------\n")
"""Práctica Atributos 1
Crea una clase llamada Casa, y asígnale atributos: color, cantidad_pisos.
Crea una instancia de Casa, llamada casa_blanca, de color "blanco" y cantidad de pisos igual a 4.
"""
class Casa:

    def __init__ (self, color, cantidad_pisos): #Metódo Constructor
        self.color = color #Atributo de instancia
        self.cantidad_pisos = cantidad_pisos #Atributo de instancia
        
casa_blanca = Casa('blanco', 4) #Atributos de instancia

print(f"Tu casa es de color {casa_blanca.color}, y tiene {casa_blanca.cantidad_pisos} pisos")


print("\n----------------------------------------------------------------")
print('Práctica 2 - Atributos ')
print("----------------------------------------------------------------\n")
"""Práctica Atributos 2
Crea una clase llamada Cubo, y asígnale el atributo de clase:
caras = 6
y el atributo de instancia:
color
Crea una instancia cubo_rojo, de dicho color.
"""

class Cubo :
    caras = 6
    
    def __init__ (self, color): #Metódo Constructor
        self.color = color #Atributo de instancia
cubo_rojo = Cubo('rojo') #Atributos de instancia

print(f"Tu cubo es de color {cubo_rojo.color}, y tiene {cubo_rojo.caras} caras")

print("\n----------------------------------------------------------------")
print('Práctica 3 - Atributos ')
print("----------------------------------------------------------------\n")
"""Práctica Atributos 3
Crea una clase llamada Personaje, y asígnale el siguiente atributo de clase:

real = False

Crea una instancia llamada harry_potter con los siguientes atributos de instancia:

especie = "Humano"

magico = True

edad = 17
"""

class Personaje:
    real = False
    
    def __init__ (self, especie, magico, edad): #Metódo Constructor
        self.especie = especie #Atributo de instancia
        self.magico = magico #Atributo de instancia
        self.edad = edad #Atributo de instancia
        
harry_potter = Personaje('Humano', True, 17) #Atributos de instancia

print(f"Tu personaje es de la especie {harry_potter.especie}, y es magico? {harry_potter.magico}")