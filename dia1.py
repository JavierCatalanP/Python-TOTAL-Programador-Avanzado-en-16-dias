""" Día 1: Día de Programación (Día 1)
PRINT singnifica = Mostrar 
"""
print("Practica 1\n")
print("Python TOTAL - Programador Avanzado en 16 días\n")


"""
Práctica Print 1
Crea un código que imprima en pantalla la expresión Me encanta estudiar Python.

Aclaración: presta mucha atención al texto que debes reproducir, ya que errores ortográficos y de puntuación, espacios en blanco adicionales y saltos de línea innecesarios pueden ocasionar errores inesperados que no son detectados por el módulo de evaluación, devolviendo un error en tu ejercicio.
"""

#Solución Practica 1
var = "Me encanta estudiar Python "
print(var)

"""Práctica Print 2
Crea un código que imprima en pantalla la expresión Estudiar con "Python Total" es super divertido

Aclaración: presta mucha atención al texto que debes reproducir, ya que errores ortográficos y de puntuación, espacios en blanco adicionales y saltos de línea innecesarios pueden ocasionar errores inesperados que no son detectados por el módulo de evaluación, devolviendo un error en tu ejercicio.
"""
#Solución Practica 2
print("\n\n")
print("Practica 2\n")
print('Estudiar con "Python Total" es super divertido\n')

"""Práctica Print 3
Crea un código que imprima en pantalla el número 555, pero no debes imprimirlo directamente, sino como resultado de una operación matemática

Aclaración: presta mucha atención al texto que debes reproducir, ya que errores ortográficos y de puntuación, espacios en blanco adicionales y saltos de línea innecesarios pueden ocasionar errores inesperados que no son detectados por el módulo de evaluación, devolviendo un error en tu ejercicio.
"""
#Solución Practica 3
print("\n\n")
var1= 500
var2= 55
total= var1 + var2
print("Practica 3\n")
print(total)

#String
print('Comillas simples\n') #Lineal
print("Comillas dobles\n") #Lineal
print("""Comillas triples
Para parrafos
con salto del lineas\n""") #Parrafos
print("hola" + " " + 'J.C\n') #concatenando 3 cadenas
print("me llamo  \"J.C\\n")#Comillas en cadena
print("Esta es una linea\nY esta es otra\n") #Salto de linea
print("\tEsta es una linea con tabulación\n")#Esta linea equivale a tab
print('This isn\'t a number\n')#Esta linea equivale a \ apostrofe
print("This is a number: " + str(3))#Esta linea equivale a \ a
print("\n")
print('Este signo \\ es con barra invertida\n\n\n' )#Esta linea equivale a \ barra invertida

"""Práctica String 1
Crea un código que imprima en pantalla la siguiente expresión (pero usando print una sola vez):

Línea 1
Línea 2
Línea 3
Aclaración: presta mucha atención al texto que debes reproducir, ya que errores ortográficos y de puntuación, espacios en blanco adicionales y saltos de línea innecesarios pueden ocasionar errores inesperados que no son detectados por el módulo de evaluación, devolviendo un error en tu ejercicio.
"""

#Solución Practica  String 1
print("Solución Practica  String 1\n")
print("Línea 1\nLínea 2\nLínea 3\n")

"""Práctica String 2
Crea un código que imprima en pantalla la siguiente expresión.

A	B	C
D	E	F
G	H	I
Notas:

- Observa que la distancia horizontal entre los números ha sido creada con UNA tabulación.

- Puedes usar una o más declaraciones print

Aclaración: presta mucha atención al texto que debes reproducir, ya que errores ortográficos y de puntuación, espacios en blanco adicionales y saltos de línea innecesarios pueden ocasionar errores inesperados que no son detectados por el módulo de evaluación, devolviendo un error en tu ejercicio.
"""
#Solución Practica  String 2
print("Solución Practica  String 2\n")
print("A\tB\tC\nD\tE\tF\nG\tH\tI\n")

"""
Práctica String 3
Crea un código que imprima en pantalla la siguiente expresión:

Barra Normal: /
Barra Invertida: \
Aclaración: presta mucha atención al texto que debes reproducir, ya que errores ortográficos y de puntuación, espacios en blanco adicionales y saltos de línea innecesarios pueden ocasionar errores inesperados que no son detectados por el módulo de evaluación, devolviendo un error en tu ejercicio.
"""
#Solución Practica  String 3
print("Solución Practica  String 3\n")
print("Barra" " ""Normal: /\nBarra" " ""Invertida: \\\n\n\n")

#Input = petición o pedido
#input( "¿Cual es tu nombre? ") #Petición
#print("Hola " + input("¿Cual es tu nombre? ")) #Respuesta
nombre = print("Hola tú eres " + (input("¿Cual es tu nombre? ")) + " " + (input("¿Cúal es tu apellido? ")))  #Respuesta

"""Práctica Input 1
Crea un código que le permita ingresar una respuesta al usuario, haciéndole la siguiente pregunta:

¿Qué estás estudiando?

El código debe poder imprimir en pantalla lo ingresado por el usuario (utilizando print).

Aclaración: no deben imprimirse strings adicionales a la respuesta del usuario.
"""
#Solución Practica  Input 1
print("Solución Practica  Input 1\n")
print(input("¿Qué estás estudiando?"))
print("\n\n")

"""Práctica Input 2
Crea un código que le permita ingresar una respuesta al usuario, haciéndole la siguiente pregunta:

¿En qué país vives?

El código debe poder imprimir en pantalla lo ingresado por el usuario (utilizando print).

Aclaración: no deben imprimirse strings adicionales a la respuesta del usuario."""

#Solución Practica  Input 2
print("Solución Practica  Input 2\n")
print(input("¿En qué país vives?"))
print("\n\n")

"""
Práctica Input 3
Crea un código que muestre en pantalla el nombre completo del usuario, permitiéndole ingresar su nombre y apellido con las siguientes instrucciones:

Escribe tu nombre:
Escribe tu apellido:
El código debe poder imprimir en pantalla el nombre y apellido del usuario, separados por un espacio."""

#Solución Practica  Input 3
print("Solución Practica  Input 3\n")
print("" + (input("Escribe tu nombre: ")) + " " + (input("Escribe tu apellido: ")))
print("\n\n")

"""Practica Final,
crear un programa que solicite 2 nombre y cree el nombre de tu marca entre comillas.

"""
print("Solución Practica Final\n")
print("El nombre de tu cerveza\nes '" + input("Que ciudad te gustaria visitar?: ") + " " + input("Cual es tu color favorito?: ") + "'\nFelicitaciones!")
