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
        
        
        

#Tipos de Métodos

"""
Decoradores:
- Métodos de instancia = Son métodos visto anteriormente. Tienen las siguientes características:
        * Acceden y modifican atributos del objeto.
        * acceder a otros métodos.
        * Modificar el estado de la clase.
    Ejemplo:
    
    def mi_metodo(self):
        print('algo')
    mi_metodo()    
    
- Métodos de clase @classmethod = En segundo lugar, tenemos los métodos de clase.
Estos se definen colocando antes, como dijimos arriba, class methods y en sus parámetros, en vez de poner self, ponemos CLS por clase.

Estos métodos no están asociados a las instancias de nuestra clase, sino a la clase en sí misma.

Por lo tanto, pueden ser llamados no solamente desde una instancia de nuestra clase, sino también directamente desde la clase.

Estos métodos, a diferencia de los métodos de instancia, no pueden acceder a los atributos de instancia,pero sí pueden modificar, por supuesto, los atributos de la clase. Ejemplo:

    @classmethod
    def mi_metodo(cls): #"cls" por clase
        print('algo')


- Métodos estáticos @staticmethod = Se pueden definir con el decorador static method y no aceptan como parámetro ni self ni cls.

Es por eso que no pueden modificar el estado ni de la clase ni de la instancia, pero por supuesto, pueden aceptar parámetros de entrada.

Por lo tanto, el uso de los métodos estáticos puede resultar útil para indicar que un método no podrá modificar el estado de la instancia ni de la clase.

En otras palabras, los métodos estáticos se podrían ver como funciones normales, de esas que usamos fuera de una clase, con la salvedad de que estos sí van ligados a una clase concreta.
    Ejemplo:
    
    @staticmethod
    def mi_metodo():
        print('algo')

"""