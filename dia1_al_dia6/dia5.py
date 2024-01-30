#Funciones
"""
- Crear una función que reciba un número y muestre el anterior y el siguiente.
- Crear una función que una un string y un entero.
- Crear una función que reciba un entero y que retorne el resto y el cociente.
- Pedirle nombre y apellido por separado e imprimir “Apellido, Nombre”. 
- se pude crear todo lo que se pide en el ejercicio anterior con solo una función? 
respuesta: si, se puede crear todo lo que se pide en el ejercicio anterior con solo una función
"""
#Metodos, son las funciones que se ejecutan dentro de una clase y una clase es una plantilla para crear objetos, por lo cual, un objeto es una instancia de una clase.

#Ejercicio 1
dic = {'clave 1': 100, 'clave 2': 200, 'clave 3': 300}

#Aplicar un metodo a un diccionario
a = dic.popitem()  #elimina el ultimo elemento del diccionario
print(a)
print(dic)
print("\n")
#_________________________________________________________________________________________________________________________________________________
"""
Práctica Métodos y Ayuda 1
Remueve los caracteres a la izquierda de nuestro texto principal:

,

:

%

_

#

Utiliza el método lstrip(). Imprime el resultado en pantalla:

",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"

Busca en la documentación acerca del funcionamiento del método solicitado para saber cómo actúa. Puedes utilizar variables intermedias si las necesitas.

- El método lstrip(). significa que elimina los caracteres de la izquierda de la cadena.
"""
print("\n")
#Solución

texto = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
resultado = texto.lstrip(
    '",:_#%_'
)  # Utilizando el método lstrip() para eliminar los caracteres especificados, elimina los caracteres de la izquierda de la cadena.
print(
    resultado
)  # Imprime el resultado final después de eliminar los caracteres especificados. estos serian: ",:_#%_". y quedaria: Pyt%on_ _Total,,,,,,::#

#_________________________________________________________________________________________________________________________________________________
"""Práctica Métodos y Ayuda 2
Añade el elemento "naranja" como el cuarto elemento de la siguiente lista "frutas", utilizando

el método insert():

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]

Busca en la documentación acerca del funcionamiento del método solicitado para saber cómo actúa y cómo es su funcionamiento.

"""
print("\n")
frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3, "naranja")
print(frutas)

#_________________________________________________________________________________________________________________________________________________
print("\n")
"""
Práctica Métodos y Ayuda 3
Verifica si los sets a continuación forman conjuntos aislados (es decir, que no tienen elementos en común), utilizando el método isdisjoint(). Almacena dicho resultado en la variable conjuntos_aislados:

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
Busca en la documentación acerca del funcionamiento del método solicitado para saber cómo actúa y cómo es su funcionamiento."""

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_smartphones)
print(conjuntos_aislados)

#_________________________________________________________________________________________________________________________________________________
print("\n")
#Crear funciones - Métodos = funciones en Python

#Descripciones
"""
palabra   DEF -> nombre de la función -> ( )parentesis para pasar parametros

def nombre_funcion(parametro1, parametro2, parametro3):
    codigo = parametro1 + parametro2 + parametro3
    return codigo
    imprimir("codigo" + parametro1 + parametro2 + parametro3))
"""
print("\n")
print("Ejemplo\n")
#Ejercicio 1


def saludar_persona(nombre):
    #Esta funcion sirve para saludar a una persona
    print('Hola ' + nombre)


saludar_persona('Javier')

#_________________________________________________________________________________________________________________________________________________

print("\n")
print("Práctica 1:")
#Práctica 1
"""
Práctica Crear Funciones 1
Declara una función llamada saludar, que cada vez que sea llamada imprima en pantalla "¡Hola mundo!"

Solo debes definir la función, no debes invocarla luego.
"""

print("Solución:\n")


def saludar():
    print("¡Hola mundo!")


saludar()

print("\n")
print("Solución completa: \n")


def saludar(llamada):
    print(llamada)


saludar("¡Hola mundo!")

#_________________________________________________________________________________________________________________________________________________
print("\n")
print("\n Práctica 2: ")
"""
Práctica Crear Funciones 2
Declara una función llamada bienvenida, que tome como argumento el nombre de una persona, y que cada vez que sea llamada imprima en pantalla "¡Bienvenido {nombre_persona}!"

Crea la variable nombre_persona, y almacena dentro de la misma el nombre que prefieras.

Solo debes definir la función y crear la variable, no debes invocar la función luego.
"""

print("Solución:\n")


def bienvenida(nombre_persona):
    print(f"¡Bienvenido {nombre_persona}!")


bienvenida("Juan Pérez")

#_________________________________________________________________________________________________________________________________________________
print("\n")
print("\n Práctica 3: ")
"""
Práctica Crear Funciones 3
Declara una función llamada cuadrado, que tome como argumento un número cualquiera, y que cada vez que sea llamada, imprima en pantalla el cuadrado de dicho número (es decir, la potencia 2 del valor).

El nombre del argumento que debe tomar dicha función es un_numero. Crea dicha variable y asígnale un número cualquiera.

Solo debes definir la función y crear la variable, no debes invocar la función luego.
"""
print("Solución:\n")


def cuadrado(un_numero):
    print(un_numero**2)


cuadrado(3)

print("Con impresión\n")


def cuadrado(un_numero):
    print(un_numero**2)


cuadrado(3)

print("\n")

print("Solución Completa:\n")


def cuadrado_c(un_numero):
    print(f"El cuadrado de {un_numero} es {un_numero**2}")


cuadrado_c(3)

#_________________________________________________________________________________________________________________________________________________
#Return
print("\n")
print("Opción 1 de Return\n")


def multiplicar(numero1, numero2):
    return numero1 * numero2


resultado = multiplicar(5, 10)
print(resultado)

print("Opción 2 de Return\n")


def multiplicar(numero1, numero2):
    total = numero1 * numero2  #variable local
    return total


resultado = multiplicar(5, 10)
print(resultado)

print("Opción 3 de Return\n")


def multiplicar(numero1, numero2):
    total = numero1 * numero2  #variable local
    print(total)  #Imprime el valor de la variable local
    return total  #Guaradar el valor de la variable local


resultado = multiplicar(5, 10)

#_________________________________________________________________________________________________________________________________________________
print("\nPráctica 1")
"""
Práctica Return 1
Crea una función llamada potencia que tome dos valores numéricos como argumentos. Deberá devolver el número que resulte de resolver una potencia, utilizando el primer número como base, y el segundo como exponente:
3 elevado a 4 = 3 * 3 * 3 * 3 = 81
"""


def potencia(base, exponente):
    return base**exponente


resultado = potencia(3, 4)
print(resultado)
print("\n")
#_________________________________________________________________________________________________________________________________________________
print("\nPráctica 2")
"""
Práctica Return 2
Crea una función llamada usd_a_eur que tome como único parámetro un valor numérico (un monto en dólares estadounidenses), y devuelva como resultado el monto equivalente en euros. A fines de este ejemplo, tomaremos la conversión 1 USD = 0.90 EUR.

Crea una variable llamada dolares y almacena en ella un monto cualquiera para entregárselo a tu función y evaluar su resultado.

Pista: para realizar la conversión, la función internamente debe multiplicar este valor en dólares por 0.90 para obtener el monto equivalente en euros.
"""


def usd_a_eur(dolares):
    return dolares * 0.90


dolares = 100
print(usd_a_eur(dolares))

print("\n")
#_________________________________________________________________________________________________________________________________________________
print("\n Práctica 3")
"""Práctica Return 3
Crea una función llamada invertir_palabra que tome los caracteres de una palabra dada como argumento, invierta el orden de sus caracteres y los devuelva de ese modo y en mayúsculas.

Por ejemplo, si le proporcionamos la palabra "Python", deberá devolver: "NOHTYP"

También, deberás crear una variable llamada palabra, que contenga el string que tú prefieras, para sumisitrarle como argumento a la función creada.

Pista: dentro de la función creada, deberás utilizar métodos de strings ya vistos."""


def invertir_palabra(palabra):
    resultado = palabra[::-1].upper()
    print(resultado)
    return resultado


invertir_palabra('Ptyhon')


#Mejorada
def invertir_palabra2(palabra):
    return palabra[::-1].upper()


palabra = "Python"
print(invertir_palabra2(palabra))

print("\n")
#_________________________________________________________________________________________________________________________________________________
print("\n")
print("\nFunciones dinámicas")


def chequear_3A_cifras(numero):
    return numero in range(100,
                           1000)  #Estamos haciendo una comparación booleeana


resultado = chequear_3A_cifras(658)
print(resultado)

print("\nEjemplo:")


def chequear_3_cifras(lista):  #chequear una lista

    lista_3_cifras = []

    for n in lista:
        if n in range(100, 1000):
            lista_3_cifras.append(n)  #Agrega a la lista
        else:
            pass  #Si no se cumple la condición, no hacemos nada
    return lista_3_cifras


resultado = chequear_3_cifras([65, 159, 600])
print(resultado)

print("\nPráctica 1")
"""
Práctica Funciones Dinámicas 1
Crea una función (todos_positivos) que reciba una lista de números como parámetro, y devuelva True si todos los valores de una lista son positivos, y False si al menos uno de los valores es negativo. Crea una lista llamada lista_numeros con valores positivos y negativos.

No invoques la función, solo es necesario definirla."""


def todos_positivos(lista_numeros):
    for numero in lista_numeros:
        if numero <= 0:
            return False
    return True


def imprimir_numeros(lista_numeros):
    numeros_positivos = []
    numeros_negativos = []
    for n in lista_numeros:
        if n > 0:
            numeros_positivos.append(n)
        elif n < 0:
            numeros_negativos.append(n)

    print(f"Números positivos: {numeros_positivos}")
    print(f"Números negativos: {numeros_negativos}")


lista_numeros = [1, -2, 3, 4, 5]
imprimir_numeros(lista_numeros)
print(todos_positivos(lista_numeros))  # Prints: False

print("\n")
#_________________________________________________________________________________________________________________________________________________
print("\nPráctica 2")
"""
Práctica Funciones Dinámicas 2
Crea una función (suma_menores) que sume los números de una lista (almacenada en la variable lista_numeros) siempre y cuando sean mayores a 0 y menores a 1000, y devuelva el resultado de dicha suma."""


def suma_menores(lista_numeros):
    suma = 0
    for n in lista_numeros:
        if n > 0 and n < 1000:
            suma += n
    return suma


lista_numeros = [3000, 4000, 5000]
print(suma_menores(lista_numeros))
print("\n")
#_________________________________________________________________________________________________________________________________________________
print("\nPráctica 3")
"""
Práctica Funciones Dinámicas 3
Crea una función (cantidad_pares) que cuente la cantidad de números pares que existen en una lista (lista_numeros), y devuelva el resultado de dicha cuenta."""
print("\n")


def cantidad_pares(
        lista_numeros):  #Función que cuenta la cantidad de números pares
    pares = 0  #Variable local
    for n in lista_numeros:  #ciclo for: recorre la lista: n toma los valores de la lista
        if n % 2 == 0:  #Si el número es par, entonces:
            pares += 1  #sume 1 a la variable pares
    return pares  #devuelve el valor de la variable pares


lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  #Lista de números
print(cantidad_pares(lista_numeros))  #Imprime la cantidad de números pares
#_________________________________________________________________________________________________________________________________________________
print("\n Reforzamiento Funciones, desempacar taples y listas")

#Datos sin funciones
precios_de_cafe = [('capuchino', 1.5), ('e)xpresso', 2.0), ('mocaccino', 2.5)]


#opción 1
def cafe_mas_caro(lista_precios):  #Función que devuelve el cafe más caro
    precio_mayor = 0  #Variable local
    cafe_mas_caro = ''  #Variable local

    for cafe, precio in lista_precios:  #ciclo for: recorre la lista: cafe toma los valores de la lista: precio toma los
        if precio > precio_mayor:  #Si el precio es mayor al precio mayor:
            precio_mayor = precio  #El precio mayor toma el valor del precio
            cafe_mas_caro = cafe  #El cafe más caro toma el valor del cafe
        else:  #Si no se cumple la condición anterior, entonces:
            pass  #No hace nada

    return (cafe_mas_caro, precio_mayor
            )  #Devuelve el cafe más caro y el precio mayor


print(cafe_mas_caro(
    precios_de_cafe))  #Imprime el cafe más caro y el precio mayor


#Opción 2
def cafe_mas_caro(lista_precios):  #Función que devuelve el cafe más caro
    precio_mayor = 0  #Variable local
    cafe_mas_caro = ''  #Variable local

    for cafe, precio in lista_precios:  #ciclo for: recorre la lista: cafe toma los valores de la lista: precio toma los
        if precio > precio_mayor:  #Si el precio es mayor al precio mayor:
            precio_mayor = precio  #El precio mayor toma el valor del precio
            cafe_mas_caro = cafe  #El cafe más caro toma el valor del cafe
        else:  #Si no se cumple la condición anterior, entonces:
            pass  #No hace nada

    return (cafe_mas_caro, precio_mayor
            )  #Devuelve el cafe más caro y el precio mayor


cafe, precio = cafe_mas_caro(precios_de_cafe)  #Desempaquetado de tuplas
print(f'El cafe mas caro es {cafe}, cuyo precio es {precio}'
      )  #Imprime el cafe más caro y el precio mayor
print("\n")
#_________________________________________________________________________________________________________________________________________________
print("\nIteraciones entre funciones")
"""Las salidas de una determinada función pueden convertirse enentradas de otras funciones. De esa manera, cada funciónrealiza una tarea definida, y el programa se construye a partirde la interacción entre funciones.
interacción
Python
TOTAL
entre funciones

def funcion_1():
...
return


Ejemplo: Juego elige el palito:
eliges entre 4 palitos, si te toca el más corto piertes.
"""
#Guión:

#Importar Librerias
from random import shuffle

#Lista Incial que contenga los Palitos
palitos = ['-', '---', '----', '-----']


# Mezclar Palitos
def mezclar(lista):  #Función que mezcla los palitos
    shuffle(lista)  #Función que mezcla los palitos
    return lista  #Devuelve la lista


print(mezclar(palitos))  #Imprime la lista mezclada


# Pedirle Intento
def probar_suerte():
    intento = ''

    while intento not in ['1', '2', '3',
                          '4']:  #Mientras el intento no esté en las opciónes:
        intento = input('Elige un palito (1, 2, 3, 4): '
                        )  #Pide el intento va a ser un número
    return int(intento)  #Devuelve el intento


intento1 = probar_suerte()  #Desempaquetado de tuplas
print(intento1)  #Imprime el intento


#Comprobar Intento
def chequear_intento(
        lista,
        intento):  #Función que comprueba el intento, y devuelve el palito
    if lista[intento - 1] == '-':  #Si el intento es igual a la lista:
        print('¡A lavar los platos!')  #Imprime que perdió
    else:
        print("Esta vez te has salvado")  #Imprime que ganó

    print(f"Te ha tocado {lista[intento-1]}")  #Imprime el palito que tocó"


palitos_mezclados = mezclar(palitos)  #Desempaquetado de tuplas
selección = probar_suerte()  #Desempaquetado de tuplas
chequear_intento(palitos_mezclados, selección)  #Imprime el palito que tocó

print("\n")
#_________________________________________________________________________________________________________________________________________________
print("\nPráctica 1")
"""
Práctica sobre Interacción entre Funciones 1
Crea una función (lanzar_dados) que arroje dos dados al azar y devuelva sus resultados:

La función debe retornar dos valores resultado, que se encuentren entre 1 y 6).

Dicha función no debe requerir argumentos para funcionar, sino que debe generar internamente los valores aleatorios.

Proporciona el resultado de estos dos dados a una función que se llame evaluar_jugada (es decir, esta segunda función debe recibir dos argumentos) y que retorne -sin imprimirlo- un mensaje según la suma de estos valores:

Si la suma es menor o igual a 6:

"La suma de tus dados es {suma_dados}. Lamentable"

Si la suma es mayor a 6 y menor a 10:

"La suma de tus dados es {suma_dados}. Tienes buenas chances"

Si la suma es mayor o igual a 10:

"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

Pistas: utiliza el método choice o randint de la biblioteca random para elegir un valor al azar entre 1 y 6.
"""

print("Solución: \n")
import random  # Importamos a random para poder utilizar sus funciones en lanzar los dados


def lanzar_dados():  # Función que lanza los dados
    dado1 = random.randint(1, 6)  #lanzamiento del primer dado
    dado2 = random.randint(1, 6)  #lanzaemiento del segundo dado
    return dado1, dado2  # Resultados


def evaluar_jugada(dado1, dado2):  # Función que evalua la jugada
    suma_dados = dado1 + dado2  # variable que almacena la suma de los dados
    if suma_dados <= 6:  #validación, si la suma de los dados es menor o igual a 6
        return "La suma de tus dados es {}. Lamentable".format(
            suma_dados)  #retorna el mensaje de la suma de los dados
    elif suma_dados > 6 and suma_dados < 10:  # segunda condición, si la suma de los dados es mayor a 6 y menor a 10
        return "La suma de tus dados es {}. Tienes buenas chances".format(
            suma_dados)  # retorna el mensaje de la suma de los dados
    else:  # si no se cumple ninguna de las condiciones anteriores
        return "La suma de tus dados es {}. Parece una jugada ganadora".format(
            suma_dados)  # retorna el mensaje de la suma de los dados


dados = lanzar_dados(
)  # Desempaquetado de tuplas, iniciando la función lanzar_dados
mensaje = evaluar_jugada(dados[0],
                         dados[1])  # iniciando la función evaluar_jugada
print("Dado 1: {}, Dado 2: {}".format(dados[0], dados[1]))  # Imprime los dados
print(mensaje)  # Imprime el mensaje de

#_________________________________________________________________________________________________________________________________________________
print("\nPráctica 2")
"""
Práctica sobre Interacción entre Funciones 2
Crea una función llamada reducir_lista() que tome una lista como argumento (crea también la variable lista_numeros), y devuelva la misma lista, pero eliminando duplicados (dejando uno solo de los números si hay repetidos) y eliminando el valor más alto. El orden de los elementos puede modificarse.

Por ejemplo, si se le proporciona la lista [1,2,15,7,2] debe devolver [1,2,7].

Crea una función llamada promedio() que pueda recibir como argumento la lista devuelta por la anterior función, y que calcule el promedio de los valores de la misma. Debe devolver el resultado, sin imprimirlo.

Pista: puedes utilizar la función max() para encontrar el valor más alto de una lista"""

print("Solución: \n")


def reducir_lista(lista):  # Función que reducir la lista
    lista_sin_duplicados = list(set(lista))  # Crea una lista sin duplicados
    if lista_sin_duplicados:  # Si la lista no está vacía
        lista_sin_duplicados.pop(
            lista_sin_duplicados.index(max(lista_sin_duplicados))
        )  # Elimina el valor más alto de la lista
    return lista_sin_duplicados  # Devuelve la lista sin duplicados


def promedio(lista):  # Función que calcula el promedio de la lista
    if not lista:  # Si la lista está vacía
        return 0  # Devuelve 0
    else:  # Si la lista no está vacía
        return sum(lista) / len(
            lista
        )  # Devuelve la suma de la lista dividida entre la longitud de la lista


# Ejemplo de uso
lista_numeros = [1, 2, 15, 7, 2]  # Lista de números
lista_reducida = reducir_lista(
    lista_numeros)  # Llama a la función reducir_lista con la lista de números
print("Lista reducida:", lista_reducida)  # Imprime la lista reducida
promedio_lista = promedio(
    lista_reducida)  # Llama a la función promedio con la lista reducida
print("Promedio:", promedio_lista)  #

print("\n")
#_________________________________________________________________________________________________________________________________________________
print("\nPráctica 3")
"""
Práctica sobre Interacción entre Funciones 3
Crea una función (llamada lanzar_moneda) que devuelva el resultado de lanzar una moneda (al azar). Dicha función debe poder devolver los resultados "Cara" o "Cruz", y no debe recibir argumentos para funcionar.

Crea una segunda función (llamada probar_suerte), que tome dos argumentos: el primero, debe ser el resultado del lanzamiento de la moneda. El segundo argumento, será una lista de números cualquiera (debes crear una lista con valores y llamarla lista_numeros).

Si se le proporciona una "Cara", debe mostrar el mensaje al usuario: "La lista se autodestruirá", y eliminarla (devolverla como lista vacía []).

Si se le proporciona una "Cruz", debe imprimir en pantalla: "La lista fue salvada" y devolver la lista intacta.

Pistas: utiliza el método choice de la biblioteca random para elegir un elemento al azar de una secuencia."""

print("Solución: \n")

import random


def lanzar_moneda():
    return random.choice(["Cara", "Cruz"])


def probar_suerte(resultado, lista_numeros):
    if resultado == "Cara":
        print("La lista se autodestruirá")
        return []
    else:
        print("La lista fue salvada")
        return lista_numeros


# Crear una lista de números
lista_numeros = [1, 2, 3, 4, 5]

# Lanzar la moneda
resultado = lanzar_moneda()

# Probar suerte
nueva_lista = probar_suerte(resultado, lista_numeros)

# Imprimir la nueva lista
print(nueva_lista)
#_________________________________________________________________________________________________________________________________________________

print("\n Argumentos indefinidos (*args)")
"""- *args = argumentos indefinidos, es decir, que no sabemos cuántos argumentos se le pasarán a una función.

- Los argumentos indefinidos se colocan como parámetros al final de la definición de la función.

- Los argumentos indefinidos se indican con un asterisco (*) antes del nombre del parámetro.

    - **kwargs = argumentos indefinidos que significa que no sabemos cuantos argumentos se van a pasar a la función.
"""
# *args


def suma_indefinida(*args):  #convención de nombres de argumentos indefinidos
    return sum(args)


print(suma_indefinida(5, 6, 5))


def suma(*codigos):  #convención de nombres de argumentos indefinidos
    return sum(codigos)  #convención de nombres de argumentos indefinidos


print(suma(15, 6, 15))

#__________________________________________________________________________________

print("\nPráctica sobre Argumentos Indefinidos (*args) 1")
"""Práctica sobre Argumentos Indefinidos (*args) 1
Crea una función llamada suma_cuadrados que tome una cantidad indeterminada de argumentos numéricos, y que retorne la suma de sus valores al cuadrado.



Por ejemplo para los argumentos suma_cuadrados(1,2,3) deberá retornar 14 (1+4+9)."""
print("Solución: \n")


def suma_cuadrados(*args):
    suma = 0
    for arg in args:
        suma += arg**2
    return suma


print(suma_cuadrados(1, 2, 3))  # Debería retornar 14

#__________________________________________________________________________________

print("\nPráctica sobre Argumentos Indefinidos (*args) 2")
"""
Práctica sobre Argumentos Indefinidos (*args) 2
Crea una función llamada suma_absolutos, que tome un conjunto de argumentos de cualquier extensión, y retorne la suma de sus valores absolutos (es decir, que tome los valores sin signo y los sume, o lo que es lo mismo, los considere a todos -negativos y positivos- como positivos).
"""

print("Solución: \n")


def suma_absolutos(*args):
    suma = 0
    for arg in args:
        suma += abs(arg)  #abs es valor absoluto
    return suma


print(suma_absolutos(-1, 2, -3))  # Debería retornar 6

#__________________________________________________________________________________

print("\nPráctica sobre Argumentos Indefinidos (*args) 3")
"""
Práctica sobre Argumentos Indefinidos (*args) 3
Crea una función llamada numeros_persona que reciba, como primer argumento, un nombre, y a continuación, una cantidad indefinida de números.

La función debe devolver el siguiente mensaje:

"{nombre}, la suma de tus números es {suma_numeros}"
"""

print("Solución: \n")


def numeros_persona(nombre, *args):
    suma_numeros = sum(args)
    return f"{nombre}, la suma de tus números es {suma_numeros}"


print(numeros_persona(
    "Ana", 1, 2, 3))  # Debería retornar "Ana, la suma de tus números es 6"

#__________________________________________________________________________________

print("\nArgumentos Indefinidos (**kwargs)")
"""
**kwargs = 'key word args: Palabra clave argumentos indefinido' (diccionario)
- **kwargs = argumentos indefinidos que significa que no sabemos cuantos argumentos se van a pasar a la función.
#algún código.

def suma(**kwargs):
    #algún código

suma(a=1, b=2, c=3))
"""

print("Práctica 1: \n")


def suma(
    **kwargs
):  #kwargs = argumentos indefinidos que significa que no sabemos cuantos argumentos se van a pasar
    print(type(kwargs))  #<class 'dict'>


suma(x=1, y=2, z=3)  # Debería imprimir {'x': 1, 'y': 2, 'z': 3}

print("\nPráctica 2: \n")


def suma(
    **kwargs
):  #kwargs = argumentos indefinidos que significa que no sabemos cuantos argumentos se van a pasar

    total = 0  #variable que almacena la suma de los valores
    for clave, valor in kwargs.items():  #recorre el diccionario kwargs
        print(f"{clave} = {valor}")  #imprime la clave y el valor
        total += valor  #suma el valor a la variable total
    return total  #retorna la suma de los valores


print(suma(x=1, y=2,
           z=3))  # Debería imprimr: x = 1, y = 2, z = 3, y retornar 6

print("\nPráctica 3: \n")


def prueba(num1, num2, *args, **kwargs):  #kwargs = argumentos indefinidos que significa que no sabemos cuantos argumentos se van a pasar

    print(f'el primer valor es {num1}')  #imprime el primer valor
    print(f'el segundo valor es {num2}')  #imprime el segundo valor

    for arg in args:  #recorre los argumentos indefinidos
        print(
            f'el tercer valor args es = {arg}')  #imprime el tercer valor args

    for clave, valor in kwargs.items():  #recorre el diccionario kwargs
        print(f'{clave} = {valor}')  #imprime la clave y el valor


args = (100, 200, 300, 400, 500)  #tupla de argumentos indefinidos
kwargs = {'x': 'uno', 'y': 'dos', 'z': 'tres'}  #diccionario de argumentos

prueba(15, 50, *args, **kwargs) # imprime todos los valores #__________________________________________________________________________________

print("\nPráctica 1:")
"""
Práctica sobre Argumentos Indefinidos (**kwargs) 1
Crea una función llamada cantidad_atributos que cuente la cantidad de parémetros que se entregan, y devuelva esa cantidad como resultado.
"""
print("Solución: \n")

def cantidad_atributos(**kwargs):
    return len(kwargs)
print(cantidad_atributos(x=1, y=2, z=3))  #
    

#__________________________________________________________________________________

print("\nPráctica 2")
"""
Práctica sobre Argumentos Indefinidos (**kwargs) 2
Crea una función llamada lista_atributos que devuelva en forma de lista los valores de los atributos entregados en forma de palabras clave (keywords). La función debe preveer recibir cualquier cantidad de argumentos de este tipo.
"""

print("Solución: \n")

def lista_atributos(**kwargs):
    return list(kwargs.values())
print(lista_atributos(x=1, y=2, z=3))  #


#__________________________________________________________________________________

print("\nPráctica 3")
"""

Práctica sobre Argumentos Indefinidos (**kwargs) 3
Crea una función llamada describir_persona, que tome como parámetros su nombre y luego una cantidad indetermida de argumentos. Esta función deberá mostrar en pantalla:

Características de {nombre}:
{nombre_argumento}: {valor_argumento}
{nombre_argumento}: {valor_argumento}
etc...
Por ejemplo:

describir_persona("María", color_ojos="azules", color_pelo="rubio")

Mostrará en pantalla:

Características de María:
color_ojos: azules
color_pelo: rubio
"""

print("Solución: \n")

def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")
describir_persona("María", color_ojos="azules", color_pelo="rubio")

def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for clave, valor in kwargs.items():
        print(f'{clave}: {valor}')

#__________________________________________________________________________________

print("\nProblema Práctico1")
"""
Crea una función llamada devolver_distintos()que reciba
3integers como parámetros.

Si la suma de los 3 numeros es mayor a 15, va a devolver elnúmero mayor.

Si la suma de los 3 numeros es menor a 10, va a devolver elnúmero
menor.

Si la suma de los 3 números es un valor entre 10 y 15(incluidos) va a devolver el número de valor intermedio.
"""

print("Solución: \n")

def devolver_distintos(a,b,c):

    suma = a + b + c #suma de los 3 números
    lista = [a,b,c] #lista de los 3 números para comparar

    if suma > 15:
        return max(lista) #devuelve el número mayor
    elif suma < 10:
        return min(lista) #devuelve el número menor        
    else:
        lista.sort() # ordena la lista de menor a mayor
        return lista[1] #devuelve el número de valor intermedio

print(devolver_distintos(3,5,7)) #devuelve 7


#__________________________________________________________________________________

print("\nProblema Práctico2")
"""
Escribe una función (puedes ponerle cualquier nombre quequieras) que reciba cualquier palabra como parámetro, y quedevuelva todas sus letras únicas (sin repetir) pero en ordenalfabético.
Por ejemplo si al invocar esta función pasamos la palabra"entretenido", debería devolver ['d', 'e', 'i', 'n', 'o', 'r', 't']"""

print("Solución: \n")

def devolver_letras_unicas(palabra):
    letras_unicas = set() #crea un conjunto vacío

    for letra in palabra:
        letras_unicas.add(letra) #agrega cada letra a un conjunto

    mi_lista = list(letras_unicas) #convierte el conjunto en una lista
    mi_lista.sort() #ordena la lista

    return mi_lista

print(devolver_letras_unicas("entretenido")) #devuelve ['d', 'e', 'i', 'n', 'o', 'r', 't']
#__________________________________________________________________________________
print("\nProblema Práctico3")
"""
Escribe una función que requiera una cantidad indefinida deargumentos. Lo que hará esta función es devolver True si enalgún momento se ha ingresado al numero cero repetido dosveces consecutivas.
Por ejemplo:
(5,6,1,0,0,9,3,5) >>> True
(6,0,5,1,0,3,0,1) >>> False
"""

print("Solución: \n")

def ceros_vecinos(*args):
    contador = 0

    for num in args:
        if contador + 1 == len(args):
            return False
        elif args[contador] == 0 and args[contador + 1] == 0:
            return True
        else:
            contador += 1
    return False

print(ceros_vecinos(5,6,1,0,0,9,3,5)) #devuélve True



#__________________________________________________________________________________
print("\nProblema Práctico4")
"""
Escribe una función llamada contar_primos() que requiera un solo argumento numérico.Esta función va a mostrar en pantalla todos los números primos existentes en el rango que va desde cero hasta ese número incluido, y va a devolver la cantidad de números primos que encontró.Aclaración, por convención el 0 y el 1 no se consideran primos.
"""

print("Solución: \n")

def contar_primos(numero):
    primos =[2]
    iteracion = 3

    if numero < 2:
        return 0

    while iteracion <= numero:
        for n in range(3, iteracion, 2): #itera desde 3 hasta el número dado
            if iteracion % n == 0:  #si el número es divisible por n
                iteracion += 2 #se suma 2 para saltar al siguiente número impar
                break
        else:
            primos.append(iteracion)
            iteracion += 2
    print(primos)
    return len(primos)

print(contar_primos(100)) #devuelve 25

    


#__________________________________________________________________________________
print("\n")
"""

"""

print("Solución: \n")
