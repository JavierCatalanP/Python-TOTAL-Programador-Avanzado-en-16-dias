class Vaca:
    
    def __init__(self, nombre):
        self.nombre = nombre
        
    def hablar(self):
        print(self.nombre + "dice Muuu")
        
class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def hablar(self):
        print(self.nombre + "dice Beee")
        
vaca1 = Vaca('Aurora')
oveja1 = Oveja('Nube')

vaca1.hablar()
oveja1.hablar()


"""
Vamos a llamar dentro de la función a animal a hablar

y dejamos ahí la función.

Vamos a crear ahora una llamada a la función, vamos a llamarlo pero con distintos objetos.

Primero vamos a llamar a Animal, hablar y le vamos a pasar al objeto vaca.

Uno.

Lo ejecutamos y vemos que ahora dice que porque pudo entrar este objeto se encontró con su método hablar

y lo pudo ejecutar y ahora lo vamos a volver a ejecutar, pero esta vez con oveja uno, que es un objeto

de forma distinta, insisto y ahora dice Nube, dice ve.

Y aquí volvemos a comprender la importancia que tiene el polimorfismo en los lenguajes de programación

que lo permiten.

Como Python tiene la importancia de que más allá del animal que tú pases aquí y no importa su forma,

puede ejecutar métodos que tengan el mismo nombre.

Recuerda, son clases distintas.

Vaca y oveja podrían tener miles de diferencias, pero comparten el mismo nombre de método.

Entonces, como programadores podemos aprovechar las ventajas del polimorfismo para iterar a través

de objetos de diferentes formas, para llamar a métodos que tengan el mismo nombre, aunque hagan cosas

diferentes.

O también podemos crear funciones que ejecuten esos métodos diferentes sin importar que tipo de objeto

le vamos a pasar.

Polimorfismo una virtud o un pilar de la programación.

Orientada a objetos.

Este fue el segundo pilar.

Ya vimos la herencia, ahora el polimorfismo.

Vamos a aprender algunas cositas más antes de terminar el día y de hacer nuestro proyecto del día de

hoy y el día de mañana vamos a seguir viendo los demás pilares de la programación orientada a objetos.

Nos vemos en la próxima lección.
"""
def animal_habla(animal):
    animal.hablar()
    
animal_habla(vaca1)
animal_habla(oveja1)


print("\n----------------------------------------------------------------")
print('Práctica Polimorfismo 1')
print("\n----------------------------------------------------------------")
"""La función incorporada en Python len() tiene un comportamiento polimórfico, ya que calcula el largo de un objeto en función de su tipo (strings, listas, tuples, entre otros), devolviendo la cantidad de items o caracteres que lo componen.

Crea un iterador que recorra los siguientes objetos: palabra, lista, tupla y muestre en pantalla (print()) para cada uno de ellos su longitud con la función len().

Puedes recordar cómo implementar la función len() siguiente enlace: https://docs.aws.amazon.com/es_es/redshift/latest/dg/r_LEN.html"""

palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)

for dato in [palabra, lista, tupla]:
    print(len(dato))
    
    