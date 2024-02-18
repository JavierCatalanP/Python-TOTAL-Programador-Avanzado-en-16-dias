#Métodos

class Pajaro:
    
    alas = True
    
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie
        
    def piar(self):
        print('pio, mi color es {}'.format(self.color))
        
    def volar(self, metros):
        print(f"El pajaro ha volado {metros} metros")
        
piolin = Pajaro('amarillo', 'canario')


piolin.piar()
piolin.volar(50)


print("\n----------------------------------------------------------------")
print('Práctica 1 - Métodos ')
print("----------------------------------------------------------------\n")
"""Crea una clase Perro. Dicho perro debe poder ladrar.
Crea el método ladrar() y ejecútalo en una instancia de Perro. Cada vez que ladre, debe mostrarse en pantalla "Guau!"."""

#Crear una clase Perro con un método ladrar()
class Perro:
    def ladrar(self):
        print("Guau!")

#Ejecutar el método ladrar() en una instancia de Perro
perro1 = Perro()  # Crear una instancia de Perro
perro1.ladrar()   # Llamar al método ladrar()
    

print("\n----------------------------------------------------------------")
print('Práctica 2 - Métodos ')
print("----------------------------------------------------------------\n")

"""Crea una clase llamada Mago, y crea un método llamado lanzar_hechizo() (deberá imprimir "¡Abracadabra!").

Crea una instancia de Mago en el objeto merlin, y haz que lance un hechizo."""

class Mago:
    def lanzar_hechizo(self):
        print("¡Abracadabra!")
merlin = Mago() # Crear una instancia de Mago

merlin.lanzar_hechizo()  # Llamar al método lanzar_hechizo()

print("\n----------------------------------------------------------------")
print('Práctica 3 - Métodos ')
print("----------------------------------------------------------------\n")

"""Crea una instancia de la clase Alarma, que tenga un método llamado postergar(cantidad_minutos). El método debe imprimir en pantalla el mensaje

"La alarma ha sido pospuesta {cantidad_minutos} minutos"
"""
class Alarma: #Crea una instancia de la clase Alarma
    def postergar(self, cantidad_minutos): #Metódo Constructor
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos") #Print en pantalla la alarma ha sido pospuesta 10 minutos
        
        
        
