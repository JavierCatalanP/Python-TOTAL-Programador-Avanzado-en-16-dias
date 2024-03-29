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

print("Rangos")
"""
- range(inicio, fin, paso)
"""
for numero in range(1, 10):
    print(numero) #imrpime del 1 al 9
    print(numero * 2) #multiplica por 2

print("\n")

for numero in range(5):
    print(numero) #imrprime del 0 al 4

for numero in range(1,5):
    print(numero) #imrprime del 1 al 4

for numero in range(10,100,2): #
    print(numero) #imrprime del 10 al 100 de 2 en 2
#---
lista = list(range(1, 11))   # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista) #imrprime del 1 al 10

#Práctica Rango 1
"""Práctica Rango 1
Crea una lista formada por todos los números desde el 2500 al 2585 (inclusive). Almacena dicha lista en la variable mi_lista."""

mi_lista = list(range(2500, 2586))


print("\n")
#Práctica Rango 2
"""Práctica Rango 2
Utilizando la función range(), crea en una única linea de código una lista formada por todos los números múltiplos de 3 desde el 3 al 300 (inclusive). Almacena dicha lista en la variable mi_lista."""
mi_lista = list(range(3, 301, 3))

print("\n")
#Práctica Rango 3
"""Práctica Rango 3
Utiliza la función range() y un loop para sumar los cuadrados de todos los números del 1 al 15 (inclusive). Almacena el resultado en una variable llamada suma_cuadrados.

Para ello:

Crea un rango de valores que puedas recorrer en un loop

Para cada uno de estos valores, calcula su valor al cuadrado (potencia de 2). Puede que necesites crear variables intermedias (de manera opcional).

Suma todos los valores al cuadrado obtenidos. Acumula la suma en la variable suma_cuadrados.""""
suma_cuadrados = 0 #inicializo la variable

for i in range(1, 16):#range(1,16)
    suma_cuadrados += i**2#suma_cuadrados = suma_cuadrados + i**2


print("\n")
#Práctica Enumerador 1
"""
- enumerate() = devuelve un objeto enumerador que contiene los índices y valores de una secuencia.
"""
lista = ["a", "b", "c", "d", "e"]

indice = 0

for item in lista:
    print(indice, item)
    indice += 1 #indice = indice + 1 = 0 + 1 = 1
#ahora con enumerate
for item in enumerate(lista):
    print(item) #imprime tuplas = (indice, valor)= (0, "a")

#ejmplo 2
for indice, item in enumerate(lista):
    print(indice, item) #imprime tuplas = (indice, valor)= (0, a)

#ejemplo 3
mi_tuples = list(enumerate(lista))
print(mi_tuples) #imprime lista de tuplas = [(0, a), (1, b), (2, c), (3, d), (4, e)]
print(mi_tuples[1][0])#imprime el indice del valor 1 = 1 

print("\n")
#Práctica Enumerador 1
"""Práctica Enumerador 1
Imprime en pantalla frases como la siguiente:

'{nombre} se encuentra en el índice {indice}'

Donde nombre debe ser cada uno de los nombres de la lista a continuación, y el índice, obtenido mediante enumerate().

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

Puedes modificar la línea print() otorgada como ejemplo, pero las frases entregadas deberán ser iguales.

Tip: utiliza loops!"""

lista_nombres = [
    "Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío",
    "Emiliano", "Melisa"
]

for indice, nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')#i=0, nombre=Marcos


print("\n")
#Práctica Enumerador 2
"""

Práctica Enumerador 2
Crea una lista formada por las tuplas (indice, elemento), formadas a partir de obtener mediante enumerate() los índices de cada caracter del string "Python".

Llama a la lista obtenida con el nombre de variable lista_indices .
"""
lista_indices=list(enumerate("Python"))
print(lista_indice) #imprime [(0, 'P'), (1, 'y'), (2, 't'), (3, '


print("\n")
#Práctica Enumerador 3
"""
Práctica Enumerador 3
Imprime en pantalla únicamente los índices de aquellos nombres de la lista a continuación, que empiecen con M:

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

Puedes resolverlo de diferentes maneras, pero servirá que tengas presente todos o algunos de los siguientes elementos:

Loops

Condicionales if

El método enumerate()

Métodos de strings o indexado
"""
lista_nombres = [
    "Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío",
    "Emiliano", "Melisa"
]

for i, nombre in enumerate(lista_nombres):
    if nombre[0] == "M":
        print(i)#imprime los indices de los nombres que empiezan con M

print("\n")
#Práctica Zip 1
"""
- zip() = combina dos o más secuencias (puede ser cualquier objeto iterable) y las combina en una sola secuencia de tuplas.
- zip(secuencia1, secuencia2, ...) = combina las secuencias en una sola secuencia de tuplas.
- zip(secuencia1, secuencia2, ...) = solo almacena los valores de la secuencia1 en la primera tupla, los valores de la secuencia o la lista mas pequeña en la segunda tupla, etc."""
#ejemplo 1
nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta"]
edades = [22, 21, 20, 19, 18, 17]

combinados= zip(nombres, edades)
print(combinados) #imprime objeto zip = <zip object at 0x7f9f5d3b0d10> = [(Marcos, 22), (Laura, 21), (Mónica, 20), (Javier, 19), (Celina, 18), (Marta, 17)] 

#ejemplo 2
nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta"]
edades = [22, 21, 20, 19, 18, 17]

combinados= list(zip(nombres, edades)) #convierte a lista Castearlo
print(combinados) #imprime lista de tuplas = [(Marcos, 22), (Laura, 21), (Mónica, 20), (Javier, 19), (Celina, 18), (Marta, 17)]

#ejemplo 3
nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta"]
edades = [22, 21, 20, 19, 18, 17]
ciudades = ["Linares", "Buenos Aires", "La Plata", "Córdoba", "Santa Fe", "Rosario"]
combinados = list(zip(nombres, edades, ciudades))#convierte a lista Castearlo.
print(combinados) #imprime lista de tuplas = [(Marcos, 22, Linares), (Laura, 21, Buenos Aires), (Mónica, 20, La Plata), (Javier, 19, Córdoba), (Celina, 18, Santa Fe), (Marta, 17, Rosario)] = deja fuerza a la lista mas pequeña. en esta caso dejó fuerza a la ciudad de Rosario. eso por no tener la misma cantidad de elementos.

for nombre, edad, ciudad in combinados:
    print(f"Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}") #esto imprime: Nombre: Marcos, Edad: 22, Ciudad: Linares, Nombre: Laura, Edad: 21, Ciudad: Buenos Aires, Nombre: Mónica, Edad: 20, Ciudad: La Plata, Nombre: Javier, Edad: 19, Ciudad: Córdoba, Nombre: Celina, Edad, 18, Ciudad: Santa Fe, Nombre: Marta, Edad: 17, Ciudad: Rosario

print("\n")
#Práctica Zip 1
"""

Práctica Zip 1
Muestra en pantalla frases como la del siguiente ejemplo:

La capital de Alemania es Berlín

Utiliza la función zip, loops, y las siguientes listas de países y capitales para resolverlo rápida y eficientemente.

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
"""

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

for pais, capital in zip(paises, capitales):
    print(f"La capital de {pais} es {capital}")


print("\n")
#Práctica Zip 2
"""
Práctica Zip 2
Crea un objeto zip formado a partir de listas, de un conjunto de marcas y productos que tú prefieras, dentro de la variable mi_zip.
"""
marcas = ["Nike", "Lenovo", "Nissan"]
productos = ["zapatillas", "notebook", "automóviles"]

mi_zip = zip(marcas, productos)


print("\n")
#Práctica Zip 3
"""Práctica Zip 3
Crea el zip con las traducciones los números del 1 al 5 en español, portugués e inglés (en el mismo orden), y convierte el objeto generado en una lista almacenada en la variable numeros:

uno / um / one

dos / dois / two

tres / três / three

cuatro / quatro / four

cinco / cinco / five

El resultado deberá seguir la estructura:

[('uno', 'um', 'one'), ('dos', 'dois', 'two'), ... ]"""

espaniol = ["uno", "dos", "tres", "cuatro", "cinco"]
portugues = ["um", "dois", "três", "quatro", "cinco"]
ingles = ["one", "two", "three", "four", "five"]

numeros = list(zip(espaniol, portugues, ingles))

#min y max
#min() = devuelve el valor más pequeño de un iterable o el valor más pequeño

print("\n")
#Forma 1
menor = min(2,32,4,5,6,7,8,9,10)
mayor = max(2,32,4,5,6,7,8,9,10)
print(menor)
print(mayor)

print('\n')
#Forma 2
menor = (2,32,4,5,6,7,8,9,10)
mayor = (2,32,4,5,6,7,8,9,10)
print(min(menor))
print(max(mayor))

#forma 3
lista = [2,32,4,5,6,7,8,9,10]
print(f"El menor es {min(lista)} y el mayor es {max(lista)}"))

#forma 4
nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta"]
print(min(nombres)) #devuelve el valor más pequeño de la lista = Marcos
print(max(nombres)) #devuelve el valor más grande de la lista = Marta    

#forma 5
nombres = ["marcos", "laura", "mónica", "javier", "celina", "marta"]
print(min(nombres)) # devulve el valor más pequeño de la lista = celina = ya que la lista está en minúsculas y el valor más pequeño es la a
print(max(nombres)) #devuelve el valor más grande de la lista = marta = ya que la lista está en minúsculas y el valor más grande es la m.

nombre = "Carlos" 
#busca primero em mayusculas y luego en minusculas
print(min(nombre)) #devuelve el valor más pequeño de la cadena = C
print(max(nombre)) #devuelve el valor más grande de la cadena = s
print(min(nombre.loewr())) #devuelve el valor más pequeño de la cadena = a

dic = {'c1:45', 'c2:56', 'c3:78'}
print(min(dic)) #devuelve el valor más pequeño de la lista = c1
print(max(dic)) #devuelve el valor más grande de la lista = c3
print(min(dic.values())) #devuelve el valor más pequeño de la lista = 45

print("\n")
#Práctica Min y Max 1
"""Práctica Min y Max 1
Obtén el valor máximo entre los valores de la siguiente lista, y almacénalo en una variable llamada valor_maximo:

lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5] """
lista_numeros = [
    44542247 / 2, 21310 / 5, 2134747 * 33, 44556475, 121676, 6654067, 353254,
    123134, 55**12, 611**5
]

valor_maximo = max(lista_numeros)


print("\n")
#Práctica Min y Max 2
"""
Práctica Min y Max 2
Calcula la diferencia entre el valor máximo y el mínimo en la siguiente lista de números, y almacénalo en una variable llamada rango:

lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]
"""
lista_numeros = [
    44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134,
    552512, 611665
]

rango = max(lista_numeros) - min(lista_numeros)


print("\n")
#Práctica Min y Max 3
"""Práctica Min y Max 3
Utilizando max(), min() y métodos de diccionarios, obtén el mínimo valor a partir del siguiente diccionario:

diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}

Almacena dicho valor en una variable llamada edad_minima.

También, obtén el nombre que se ubica último en orden alfabético, y almacénalo en una variable llamada ultimo_nombre."""

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
"""
- Es una librería que nos permite generar números aleatorios.
-    se impoorta con la palabra reservada import

"""


from random import *

aleatorio = randint(1, 10)
print(aleatorio)

aleatorio = uniform(1,5)#genera un número decimal entre 1 y 5
print(aleatorio)#genera un número decimal entre 1 y 5

aleatorio = round(uniform(1,5),1)#redondea a 1 decimal
print(aleatorio)#1.2

aleatorio = random()#genera un número aleatorio entre 0 y 1
print(aleatorio)#0.0 y 1.0    

colores = ["rojo", "verde", "azul", "amarillo", "negro", "blancco"]
aleatorio = choice(colores) #elige un elemento de una lista
print(choice(colores))#elige un elemento aleatorio de la lista

numeros = list(range(1,110,2))#crea una lista de números del 1 al 100 de 2 en 2
shuffer = shuffle(numeros)#mezcla la lista
print(numeros)#mezcla la lista


print("\n")

#Practica 1
"""

Práctica Random 1
Implementa la función randint() de la librería random que te permita obtener un número entero del 1 al 10, y almacena dicho valor en una variable llamada aleatorio
"""
from random import *
aleatorio = randint(1, 10)
print(aleatorio)


print("\n")
#Práctica Random 2
"""
Práctica Random 2
Implementa la función random() de la librería random que te permita obtener un número decimal entre 0 y 1, y almacena dicho valor en una variable llamada aleatorio"""

from random import *

aleatorio = random()


print("\n")
#Práctica Random 3
"""
Práctica Random 3
Utiliza el método choice() de la librería random para obtener un elemento al azar de la lista de nombres a continuación, y almacena el nombre escogido en una variable llamada sorteo.

nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]"""
from random import *

nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]

sorteo = choice(nombres)


print("\n")

#Comprensión de listas
"""
- es una forma de crear listas de manera más corta y con menos líneas de código.
- se utiliza para crear listas de un solo tipo de dato.
- se crea una lista con una sintaxis más corta y menos líneas de código.

"""
print("\n")
#Sin comprensión de lista
palabra = 'python'

lista = []

for letra in palabra:
    lista.append(letra)

print(lista)#['p', 'y', 't', 'h', 'o', 'n']
print("\n")

#con comprensión de lista


palabra = 'python'

lista = [letra for letra in palabra]# debe ser la misma cantidad de letras que la palabra y variable interna que se esta creando.

print(lista)#['p', 'y', 't', 'h', 'o', 'n'] nos ahorramos escribir el for y el append
print("\n")

#Otra forma, con comprensión de lista

lista = [letra for letra in 'python']
print(lista)#['p', 'y', 't', 'h', 'o', 'n']

print("\n")
lista = [letra for letra in range(1,11)] #crea una lista de números del 1 al 10
print(lista)#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10
print("\n")

lista = [letra for letra in range(1,11) if n * 2 > 10] #crea una lista de números del 1 al 10, imprime solo los números que son múltiplos de 2 y mayores a 10

print(lista) # [2, 4, 6, 8, 10]

print("\n")
lista = [n if n * 2 > 10 else 'no' for n in range (0,21,2)]
print (lista)# [0, 'no', 4, 'no', 6, 'no', 8, 'no', 10, 'no', 12, 'no', 14, 'no', 16, 'no', 18, 'no', 20, 'no']

print("\n")
pies = [8, 10, 12, 15, 20]
metros= [p * 0.3281 for p in pies]
print(metros)# [2.47, 3.04, 3.47, 4.22, 5.61]




#Práctica Comprensión de Listas 1
"""
Práctica Comprensión de Listas 1
Para realizar el ejercicio a continuación, puedes optar por diferentes caminos. Si bien en programación el camino correcto es el que devuelve el resultado correcto, te animo a que intentes aplicar los conceptos de comprensión de listas para comenzar a afianzarlos para el futuro. ¡Pueden resultarte muy útiles en tu práctica profesional!

Crea una lista valores_cuadrado formada por los números de la lista valores, elevados al cuadrado.

valores = [1, 2, 3, 4, 5, 6, 9.5]"""

valores = [1, 2, 3, 4, 5, 6, 9.5]

valores_cuadrado = [valor**2 for valor in valores]

def 



print("\n")
#Práctica Comprensión de Listas 2
"""Práctica Comprensión de Listas 2
Para realizar el ejercicio a continuación, puedes optar por diferentes caminos. Si bien en programación el camino correcto es el que devuelve el resultado correcto, te animo a que intentes aplicar los conceptos de comprensión de listas para comenzar a afianzarlos para el futuro. ¡Pueden resultarte muy útiles en tu práctica profesional!

Crea una lista valores_pares formada por los números de la lista valores que (¡adivinaste!) sean pares.

valores = [1, 2, 3, 4, 5, 6, 9.5]"""

valores = [1, 2, 3, 4, 5, 6, 9.5]

valores_pares = [valor for valor in valores if valor % 2 == 0]


print("\n")
#Práctica Comprensión de Listas 3
"""Práctica Comprensión de Listas 3
Para realizar el ejercicio a continuación, puedes optar por diferentes caminos. Si bien en programación el camino correcto es el que devuelve el resultado correcto, te animo a que intentes aplicar los conceptos de comprensión de listas para comenzar a afianzarlos para el futuro. ¡Pueden resultarte muy útiles en tu práctica profesional!

Para la siguiente lista de temperaturas en grados Fahrenheit, expresa estos mismos valores en una nueva lista de valores de temperatura en grados Celsius. La conversión entre tipo de unidades es la siguiente:

°C = (°F - 32) * (5/9)

o expresado de otro modo:

(grados_fahrenheit-32)*(5/9)

La lista de temperaturas es la siguiente:

temperatura_fahrenheit = [32, 212, 275] 
Almacena esta nueva lista en una variable llamada grados_celsius"""


temperatura_fahrenheit = [32, 212, 275]

grados_celsius = [(temperatura - 32) * (5 / 9)
                  for temperatura in temperatura_fahrenheit]


#El operador lógico and devuelve True cuando al menos una de las condiciones que vincula es verdadera.
#incorrecto