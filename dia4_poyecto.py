"""yecto del Día 4
A medida que aprendemos a programar, también se incrementa la cantidad de problemas a
los que somos capaces de encontrarle solución gracias al código. Y esto implica que entonces
nuestros desafíos van a ser cada vez más elevados.
Ya sabes usar operadores de comparación, operadores lógicos, hacer control de flujo, hacer
loops, conoces declaraciones muy útiles como random, zip, rango y muchas más. Entonces, ya
estás en condiciones de subir de nivel y que te pida que programes algo un poco más
complicado de lo que hemos hecho hasta ahora. Y hoy vas a crear por primera vez un juego
completamente funcional, con el que podrás divertirte tú mismo un rato.
La consigna es esta: el programa le va a preguntar al usuario su nombre, y luego le va a decir
algo así como “Bueno, Juan, he pensado un número entre 1 y 100, y tienes solo ocho intentos
para adivinar cuál crees que es el número”. Entonces, en cada intento el jugador dirá un
número y el programa puede responder cuatro cosas distintas:
 Si el número que dijo el usuario es menor a 1 o superior a 100, le va a decir que ha elegido
un número que no está permitido.
 Si el número que ha elegido el usuario es menor al que ha pensado el programa, le va a
decir que su respuesta es incorrecta y que ha elegido un número menor al número secreto.
 Si el usuario eligió un número mayor al número secreto, también se lo hará saber de la
misma manera.
 Y si el usuario acertó el número secreto, se le va a informar que ha ganado y cuántos
intentos le ha tomado.
Si el usuario no ha acertado en este primer intento, se le va a volver a pedir que elija otro
número. Y así hasta que gane o hasta que se agoten los ocho intentos.
¿Te animas? Claro que sí.
Y te recuerdo lo mismo que siempre. Lo importante es que aceptes el desafío. Que te pases un
buen rato intentándolo y puedes lograrlo o no, pero no dejes de darle vueltas al problema.
Cuando quieras, puedes pasar a la lección siguiente con la solución. Yo voy a estar ahí
intentando resolverlo a mi manera, para mostrarte cómo lo haría yo.
Pon buena música, una bebida caliente o fresca, un rincón tranquilo y a programar. 
"""
#Solución

import random
print("Bienvenido al juego de adivinar el número")
print("Estoy pensando en un número entre 1 y 100")
numero_secreto = random.randint(1,100) #genera un número aleatorio entre 1 y 100
#print(numero_secreto)
intentos = 0
while intentos < 8:#mientras queden intentos
    print("¿Cuál es el número?")
    numero_usuario = int(input())#le pedimos al usuario que adivine el número
    if numero_usuario < 1 or numero_usuario > 100:#si el número es menor a 1 o mayor a 100     
        print("El número que has elegido no está permitido")
    elif numero_usuario < numero_secreto:#si el número es menor al número secreto 
        print("El número que has elegido es menor al número secreto")
    elif numero_usuario > numero_secreto:#si el número es mayor al número secreto
        print(f"El número que has elegido es mayor al número secreto")
    else:#si el número es igual al número secreto
        print(f"¡Felicidades! Has acertado el número secreto que eran {numero_secreto}")
        print(f"Has necesitado {intentos} intentos")
        break#salimos del bucle
    intentos += 1#aumentamos el número de intentos
if intentos == 8:#si no hemos acertado en 8 intentos
    print(f"Lo siento, no has acertado el número secreto que era {numero_secreto}")#le decimos que no ha acertado



print("\n")
# Solución del profe

from random import randint

intentos = 0
numero_secreto = randint(1,100)
nombre = input("¿Dime tu nombre: ? ")

print(f"Bueno {nombre}, he pensado un número entre 1 y 100\nTienes solo 8 intentos para adivinar")

while intentos < 8:#loop while se repite tantas veces como se necesite.  ejecuta mientras queden intentos
    estimado = int(input("¿Cuál es el número?: "))
    intentos += 1

    if estimado < numero_secreto:
        print("Mi numero es mas alto")
    if estimado > numero_secreto:
        print("Mi numero es mas bajo")
    if estimado == numero_secreto:
        print(f"Felicitaciones {nombre} has adivinado el número secreto en {intentos} intentos")
        break
if estimado != numero_secreto:
    print(f"Lo siento {nombre} no has adivinado el número secreto, era {numero_secreto}")




