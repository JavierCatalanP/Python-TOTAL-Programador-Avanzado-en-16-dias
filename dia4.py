#Meta día 4
"""
• operadores de comparación
• operadores lógicos
• control de flujo
• loops
• rango
• enumerador
• zip
• random
y más...
"""
#Operadores de comparación
"""
Operadores de Comparación = se obtiene un valor booleano
10 >= 8 // False

(=) asignando algo  

(==) Comparación

"""
mi_bool = 5 + 5 == 10 - 2 + 10  #True
print(mi_bool)
mb2 = 'blanco' == 'blanco'  #True
print(mb2)
mb3 = 'blanco' == 'negro'  #False
print(mb3)
mb4 = 'blanco' == 'Blanco'  #True
print(mb4)
mb5 = 'blanco' == 'Blanco'.lower()  #True
print(mi_bool)
print(mb5)
mb6 = 'blanco'.upper() == 'blanCO'  #
print(mb6)
mb7 = 'blanco'.upper() == 'blanco'.upper()  #True
print(mb7)
mb8 = '100' == 100  #False
print(mb8)
print9 = 100.0 == 100  #True
print(print9)

#Práctica Operadores de Comparación 1
print('Práctica Operadores de Comparación 1')
print("\n")
"""
Práctica Operadores de Comparación 1
Crea dos variables (num1 y  num2) con los valores 36 y 17 respectivamente. Verifica si num1 es mayor o igual que num2 y almacena el resultado de dicha comparación en una variable llamada mi_bool
"""
#Solución
num1 = 36
num2 = 17

mi_bool = num1 >= num2
print(mi_bool)

#Práctica Operadores de Comparación 2
print('Práctica Operadores de Comparación 2')
print("\n")
"""

Práctica Operadores de Comparación 2
Crea dos variables (num1 y  num2):

Dentro de num1, almacena el resultado de la operación raíz cuadrada de 25

Dentro de num2, almacena el número 5.

Verifica si num1 es igual a num2 y almacena el resultado de dicha comparación en una variable llamada mi_bool."""

#Solución
num1 = 25**0.5
num2 = 5

mi_bool = num1 == num2

print(mi_bool)

#Práctica Operadores de Comparación 3
print('Práctica Operadores de Comparación 3')
print("\n")
"""

Práctica Operadores de Comparación 3
Crea dos variables (num1 y  num2):

Dentro de num1, almacena el resultado de la operación 64 x 3

Dentro de num2, almacena el resultado de la operación 24 x 8

Verifica si num1 es diferente a num2 y almacena el resultado de dicha comparación en una variable llamada mi_bool."""
#Solución
num1 = 24 * 8
num2 = 64 * 3

mi_bool = num1 != num2

print(mi_bool)

print("\n")
#Operadores Logicos
"""
Y = and
o = or
no = not
"""
a = 10
b = 5
c = 2
print(a > b and b < c)
print("\n")

mi_bool = 4 > 5 < 6
print(mi_bool)
print("\n")

mi_bool = 4 > 5 and 5 < 6  #True
print(mi_bool)
print("\n")

mi_bool = (55 == 55) and ('perro' == 'perro')  #True
print(mi_bool)
print("\n")

mi_bool = 1 == 10 or 3 == 30  #False
print(mi_bool)
print("\n")

texto = " esta frase es breve"
mi_bool = 'esta' in texto  #True
print(mi_bool)
print("\n")

mi_bool = ('esta' in texto) and ('breve' in texto)  #True
print(mi_bool)
print("\n")

mi_bool = ('esta' in texto) or ('python' in texto)  #True
print(mi_bool)
print("\n")

mi_bool = 'a' == 'a' and 'b' == 'b'  #True
print(mi_bool)
print("\n")

mi_bool = not ('a' == 'a' and 'b' == 'b')  #False
print(mi_bool)
print("\n")

mi_bool = not ('a' != 'a' and 'b' == 'b')  #True
print(mi_bool)
print("\n")

#Práctica Operadores Lógicos 1
"""
Crea tres variables (num1 ,  num2 y num3):

Dentro de num1, almacena el valor 36

Dentro de num2, almacena el resultado de la operación 72/2

Dentro de num3, almacena el valor 48

Verifica si num1 es mayor que num2, y menor que num3. Almacena el resultado de dicha comparación en una variable llamada mi_bool.

"""
num1 = 36
num2 = 72 / 2
num3 = 48
mi_bool = ((num1 > num2) and num3)
print(mi_bool)
print("\n")
#Práctica Operadores Lógicos 2
"""

Práctica Operadores Lógicos 2
Crea tres variables (num1 ,  num2 y num3):

Dentro de num1, almacena el valor 36

Dentro de num2, almacena el resultado de la operación 72/2

Dentro de num3, almacena el valor 48

Verifica si num1 es mayor que num2, o menor que num3. Almacena el resultado de dicha comparación en una variable llamada mi_bool.
"""
num1 = 36
num2 = 72 / 2
num3 = 48
mi_bool = (num1 > num2 or num2 < num3)
print(mi_bool)
print("\n")

#practica Operadores Lógicos 3
"""
Práctica Operadores Lógicos 3
Verifica si las palabras almacenadas en las siguientes variables:

palabra1 = "éxito", y

palabra2 = "tecnología"

no se encuentran en la frase a continuación, y almacena el resultado de esta comprobación (un booleano) en una variable llamada mi_bool:

"Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"

Elon Musk"""

frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"

mi_bool = not (palabra1 == frase) and not (palabra2 == frase)
print(mi_bool)
print("\n")

#Control de Fujos
"""
Controlar el flujo con 3 palabras claves, estas son:
- if (si se cumple una condición).
if una_condicion:
    print(“se cumple la condición”) #Ejecuta el código si se cumple la condición. Si no cuenta con la condición, no se ejecuta el código.

- elif (si no se cumple la condición anterior, pero se cumple otra).
elif otra_condicion:
    print(“se cumple la condición”) #Ejecuta el código si se cumple. Si no se cumple la condición, no se ejecuta el código.

- else (si no se cumple ninguna de las condiciones anteriores).
else:
    print(“no se cumple ninguna condición”) #Ejecuta el código si no se cumple ninguna de las condiciones anteriores.

Ejemplo general:

if una_condicion:
    print(codigo_a)
elif otra_condicion:
    print(codigo_c)
elif otra_condicion:
print(codigo_d)
else:
    print(codigo_b)    
#python lee desde arriba hacia abajo, por lo que si no se cumple la condición anterior
"""
#Práctica Control de Fujo 1

if 5 == 9:
    print("Es correcto, 10 es mayor que 9")
else:
    print("No es correcto, 10 no es mayor que 9")

mascota = "Gato"
if mascota == 'Gato':
    print('Tienes un Gato')
elif mascota == 'Perro':
    print('Tienes un Perro')
elif mascota == 'pez':
    print('Tienes un pez')
else:
    print('No tienes mascota')

edad = 16
calificacion = 9

if edad < 18:
    print('Eres menor de edad')
    if calificacion >= 7:
        print('Aprobaste')
    else:
        print('Reprobaste')
else:
    print('Eres mayor de edad')
    if calificacion >= 7:
        print('Aprobaste')
    else:
        print('Reprobaste')

#Práctica Control de Fujo 1
"""
Práctica Control de Flujo 1
Utilizando las variables num1 y num2, que se alimentan con el input del usuario (tal como en el código ya proporcionado):

Crea una estructura de control de flujo que compare los valores de las variables, y arroje un resultado de acuerdo al caso:

"num1 es mayor que num2"

"num2 es mayor que num1"

"num1 y num2 son iguales"

Debes mostrar en pantalla el valor de las variables ingresadas en lugar de num1 y num2.
"""

#num1 = int(input("Ingresa un número:"))
#num2 = int(input("Ingresa otro número:"))

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"{num1} y {num2} son iguales")
"""""
# Pedir input al usuario para num1 y num2
num1 = int(input("Ingresa el valor para num1: "))
num2 = int(input("Ingresa el valor para num2: "))

# Comparar los valores de las variables
if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"{num1} y {num2} son iguales")
"""
#Práctica Control de Fujo 2
print("\n")
""" 
Práctica Control de Flujo 2
Las leyes de un país establecen que un adulto puede conducir si tiene licencia para hacerlo, y para optar por una licencia para conducir, debe de tener 18 años o más.

Crea una estructura condicional para verificar si una persona de 16 años sin licencia puede conducir, y muestra el resultado que corresponda en pantalla:

"Puedes conducir"

"No puedes conducir aún. Debes tener 18 años y contar con una licencia"

"No puedes conducir. Necesitas contar con una licencia"

Utiliza la base de código ya proporcionada para plantear la estructura de control de flujo apropiada y verificar dichas condiciones.

"""
# Práctica Control de Flujo 2

edad = 16
tiene_licencia = False

if edad >= 18 and tiene_licencia:
    print("Puedes conducir")
elif edad < 18:
    print(
        "No puedes conducir aún. Debes tener 18 años y contar con una licencia"
    )
else:
    print("No puedes conducir. Necesitas contar con una licencia")

print("\n")
#Práctica Control de Fujo 3
"""
Práctica Control de Flujo 3
Para acceder a un determinado puesto de trabajo, el candidato debe ser capaz de programar en Python y tener conocimientos de inglés.

Crea una estructura condicional para evaluar a un candidato dadas estas condiciones, y muestra el mensaje correspondiente en pantalla:

"Cumples con los requisitos para postularte"

"Para postularte, necesitas saber programar en Python y tener conocimientos de inglés"

"Para postularte, necesitas tener conocimientos de inglés"

"Para postularte, necesitas saber programar en Python"

Utiliza la base de código ya proporcionada para plantear la estructura de control de flujo apropiada y verificar dichas condiciones. Evalúa a un candidato que sabe inglés, pero no programa en Python.
"""

# Práctica Control de Flujo 3

habla_ingles = True
sabe_python = False

if habla_ingles and sabe_python:
    print("Cumples con los requisitos para postularte")
elif (not habla_ingles) and (not sabe_python):
    print(
        "Para postularte, necesitas saber programar en Python y tener conocimientos de inglés"
    )
elif not habla_ingles:
    print("Para postularte, necesitas tener conocimientos de inglés")
else:
    print("Para postularte, necesitas saber programar en Python")

#Introccuón a los Loops
"""
- Bucles for = se utiliza para repetir un bloque de código un número determinado de veces. = 
for i in range(5):

- Bucles while = mientras = se utiliza para repetir un bloque de código mientras se cumpla una condición. = 
wile condicion:

- Bucles anidados = Bucles dentro de otro bucle = se utiliza para repetir un bloque de código un número determinado de veces. = 
for i in range(5):
    for j in range(3):
    
- Bucles infinitos = Bucles sin fin = se utiliza para repetir un bloque de código indefinidamente. = 
while True:
    
- Bucles break = romper = se utiliza para romper un bucle en su ciclo actual. = 
for i in range(5):
    if i == 3:
        break
    
- Bucles continue = saltar a la siguiente iteración = se utiliza para saltar a la siguiente iteración de un bucle. = 
for i in range(5):
    if i == 3:
        continue
            
- Bucles else = else en un bucle for = se utiliza para ejecutar un bloque de código cuando el bucle ha terminado de iterar.  = 
for i in range(5):
    print(i)
else:
    prin("Bucle terminado")
    
- Bucles pass = no hace nada = se utiliza para saltar a la siguiente iteración de un bucle sin ejecutar ningún código. = 
for i in range(5):
    pass

- Bucles range = range(inicio, fin, paso) = se utiliza para crear un objeto de tipo range que representa una secuencia de números. = 
for i in range(5):
    print(i)

- Bucles enumerate = bucles con índices = se utiliza para iterar sobre una secuencia y obtener el índice y el valor de cada elemento. = 
for i, elemento in enumerate(secuencia):
    print(i, elemento)

- Bucles zip = combinar dos listas = se utiliza para combinar dos listas en una sola secuencia de tuplas. = 
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
for elemento1, elemento2 in zip(lista1, lista2):
    print(elemento1, elemento2)
    
- Bucles all = todos = se utiliza para verificar si todos los elementos de una secuencia son verdaderos.  = 
if all(elemento in secuencia):
    print("Todos los elementos son verdaderos")

- Bucles any = alguno = se utiliza para verificar si algún elemento de una secuencia es verdadero. = 
if any(elemento in secuencia):
    print("Al menos un elemento es verdadero")

- Bucles filter = filtrar = se utiliza para crear una nueva secuencia que contiene solo los elementos que cumplen una condición. = 
nueva_secuencia = filter(lambda elemento: elemento > 5, secuencia)

- Bucles map = mapear = se utiliza para aplicar una función a cada elemento de una secuencia. = 
nueva_secuencia = map(lambda elemento: elemento * 2, secuencia)

- Bucles sorted = ordenar = se utiliza para ordenar una secuencia de elementos. = 
nueva_secuencia = sorted(secuencia)


"""
#Loop = Rpiten  un blo que de coincide con una condicion (For y While)

#For = se utiliza para repetir un bloque de código un número determinado de veces.
#Wile = mientras = se utiliza para repetir un bloque de código mientras se cumpla
print("\n")

print("Ejemplo 1")
nombres = ["Juan", "María", "Pedro", "Ana"]
#por cada elemento en nombres, imprime "Hola"

for elemento in nombres:
    print("Hola" + elemento)

print("\n")

print("Ejemplo 2")
lista = [1, 2, 3, 4, 5]

for numero in lista:  #Por -> variable del blueque -> in = lugar -> lista = elemento
    print(numero)
    print("Número: ", numero)  #Imprime el numero de la lista
    print(f"Número: {numero}")  #imprime el numero y la variable

print("\n")

print("Ejemplo 3")

lista = ['a', 'b', 'c', 'd', 'e']

for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f"La letra {numero_letra} es:  {letra}")
print("\n")

print("Ejemplo 4")
lista = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]

for nombre in lista:
    if nombre.startswith('C'):  #debe imprimir nombre que inicie con C
        print(nombre)

print("\n")

print("Ejemplo 5")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero
    print("Voy a imprimir lo que esta dentro del for: ", mi_valor)
print(f"El valor final de mi_valor es: {mi_valor}")

print("\n")

palabra = 'python'

for letra in palabra:
    print(letra)

print("\n")

dic = {'clave1': '1', 'clave2': '2', 'clave3': '3'}

for item in dic.items():
    print(item)
for item in dic.values():
    print(item)

print("\n")

#Práctica Loop For 1
"""Práctica Loop For 1
Utilizando loops For, saluda a todos los miembros de una clase, imprimiendo "Hola" + su nombre.

Por ejemplo: "Hola María"

alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]
"""
print("\n")

alumnos_clase = [
    "María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"
]

print("\n")
for alumno in alumnos_clase:
    print(f"Hola {alumno}")

#Práctica Loop For 2
"""Práctica Loop For 2
Dada la siguiente lista de números, realiza la suma de todos los números utilizando loops For y almacena el resultado de la suma en una variable llamada suma_numeros:
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]"""
print("\n")

lista_numeros = [
    1, 5, 8, 7, 6, 8, 2, 5, 2, 6, 4, 8, 5, 9, 8, 3, 5, 4, 2, 5, 6, 4
]
suma_numeros = 0

for numero in lista_numeros:
    suma_numeros = suma_numeros + numero
print(suma_numeros)

print("\n")
#Práctica Loop For 3
"""Práctica Loop For 3
Dada la siguiente lista de números, realiza la suma de todos los números pares e impares* por separado en las variables suma_pares y suma_impares respectivamente:

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]

*Recordando de los días anteriores: el módulo (o resto) de un número dividido 2 es cero cuando dicho valor es par, y 1 cuando es impar

num % 2 == 0 (valores pares)

num % 2 == 1 (valores impares)"""

lista_numeros = [
    1, 5, 8, 7, 6, 8, 2, 5, 2, 6, 4, 8, 5, 9, 8, 3, 5, 4, 2, 5, 6, 4
]

suma_pares = 0

suma_impares = 0

for numero in lista_numeros:
    if numero % 2 == 0:
        suma_pares = suma_pares + numero
    else:
        suma_impares = suma_impares + numero
print(f"La suma de los pares es: {suma_pares}")
print(f"La suma de los impares es: {suma_impares}")

print("\n\n")

print("Loop While")
""" Se cumple mientras la condicion sea verdadera
while condicion:
    bloque de codigo
Ejemplo:
cuando un jugador muere, se reinicia el jego descontando las vidas, si no hay vidas, el juego termina.

mientras que = while, se cumpla una condición blooleana, se ejecuta el bloque de codigo. 

palabras que pueden ir dentro de estos loops, estas son:
break = romper el loop
continue = continuar con la siguiente iteracion
pass = saltar a la siguiente iteracion
"""

#Ejemolos antes de las practicas:
#Ejemplo 1
monedas = 5

while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas = monedas - 1  # o colocar monedas -=1 // es lo mismo
else:
    print("Ya no tengo monedas")

print("\n")
#Ejemplo 2

respuesta = 's'
while respuesta == 's':
    respuesta = input("¿Quieres continuar? (s/n): ")
else:
    print("Gracias")

#Ejemplo 3 Con Break
print("\n")
nombre = input('inserte su nombre: ')
for letra in nombre:
    if letra == 'r':
        break
    print(letra)

#Ejemplo 4 Con continue
print("\n")
nombre = input('inserte su nombre: ')
for letra in nombre:
    if letra == 'i':
        continue
    print(letra)


print("\n")
#Práctica Loop While 1
"""Práctica Loop While 1
Crea un Loop While que se imprima en pantalla los números del 10 al 0, uno a la vez."""
numero = 10

while numero >= 0:
    print(numero)
    numero -= 1

print("\n")
#Práctica Loop While 2
"""Práctica Loop While 2
Crea un Loop While que reste de uno en uno los números desde el 50 al 0 (ambos números incluídos) con las siguientes condiciones adicionales:

- Si el número es divisible por 5, mostrar dicho número en pantalla (¡recuerda que aquí puedes utilizar la operación módulo dividiendo por 5 y verificando el resto!)

- Si el número no es divisible por 5, continuar ejecutando el loop sin mostrar el valor en pantalla (no te olvides de seguir restando para que el programa no corra infinitamente)."""
numero = 50

while numero >= 0:
    if numero % 5 == 0: #si el numero es divisible por 5
        print(numero)
        numero -= 5 #resta 5 al numero
    else:
        numero -= 1 #resta 1 al numero 

print("\n")


#Práctica Interrupción de Flujo
"""Práctica Interrupción de Flujo
Crea un loop For a lo largo de la siguiente lista de números, imprimiendo en pantalla cada uno de sus elementos, e interrumpe el flujo en el momento que encuentres un valor negativo:

lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

No debes cambiar el orden de la lista."""

lista_numeros = [
    4, 5, 8, 7, 6, 9, 8, 2, 4, 5, 7, 1, 9, 5, 6, -1, -5, 6, -6, -4, -3
]

for numero in lista_numeros:
    if numero >= 0:
        print(numero)
    else:
        break

print("\n")


#Práctica Rango 1

mi_lista = list(range(2500, 2586))


print("\n")
#Práctica Rango 2

mi_lista = list(range(3, 301, 3))

print("\n")
#Práctica Rango 3

suma_cuadrados = 0

for i in range(1, 16):
    suma_cuadrados += i**2


print("\n")
#Práctica Enumerador 1

lista_nombres = [
    "Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío",
    "Emiliano", "Melisa"
]

for indice, nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')


print("\n")
#Práctica Enumerador 2

lista_indices = list(enumerate("Python"))


print("\n")
#Práctica Enumerador 3

lista_nombres = [
    "Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío",
    "Emiliano", "Melisa"
]

for i, nombre in enumerate(lista_nombres):
    if nombre[0] == "M":
        print(i)

print("\n")
#Práctica Zip 1

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

for pais, capital in zip(paises, capitales):
    print(f"La capital de {pais} es {capital}")


print("\n")
#Práctica Zip 2

marcas = ["Nike", "Lenovo", "Nissan"]
productos = ["zapatillas", "notebook", "automóviles"]

mi_zip = zip(marcas, productos)


print("\n")
#Práctica Zip 3

espaniol = ["uno", "dos", "tres", "cuatro", "cinco"]
portugues = ["um", "dois", "três", "quatro", "cinco"]
ingles = ["one", "two", "three", "four", "five"]

numeros = list(zip(espaniol, portugues, ingles))


print("\n")
#Práctica Min y Max 1

lista_numeros = [
    44542247 / 2, 21310 / 5, 2134747 * 33, 44556475, 121676, 6654067, 353254,
    123134, 55**12, 611**5
]

valor_maximo = max(lista_numeros)


print("\n")
#Práctica Min y Max 2

lista_numeros = [
    44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134,
    552512, 611665
]

rango = max(lista_numeros) - min(lista_numeros)


print("\n")
#Práctica Min y Max 3

diccionario_edades = {
    "Carlos": 55,
    "María": 42,
    "Mabel": 78,
    "José": 44,
    "Lucas": 24,
    "Rocío": 35,
    "Sebastián": 19,
    "Catalina": 2,
    "Darío": 49
}

edad_minima = min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades.keys())


print("\n")
#Práctica Random 1

from random import randint

aleatorio = randint(1, 10)

print("\n")
#Práctica Random 2

from random import *

aleatorio = random()


print("\n")
#Práctica Random 3

from random import *

nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]

sorteo = choice(nombres)


print("\n")
#Práctica Comprensión de Listas 1

valores = [1, 2, 3, 4, 5, 6, 9.5]

valores_cuadrado = [valor**2 for valor in valores]


print("\n")
#Práctica Comprensión de Listas 2

valores = [1, 2, 3, 4, 5, 6, 9.5]

valores_pares = [valor for valor in valores if valor % 2 == 0]


print("\n")
#Práctica Comprensión de Listas 3

temperatura_fahrenheit = [32, 212, 275]

grados_celsius = [(temperatura - 32) * (5 / 9)
                  for temperatura in temperatura_fahrenheit]
