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
dic = {'clave 1':100, 'clave 2':200, 'clave 3':300}

#Aplicar un metodo a un diccionario
a = dic.popitem()#elimina el ultimo elemento del diccionario
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
resultado = texto.lstrip('",:_#%_')  # Utilizando el método lstrip() para eliminar los caracteres especificados, elimina los caracteres de la izquierda de la cadena.
print(resultado)# Imprime el resultado final después de eliminar los caracteres especificados. estos serian: ",:_#%_". y quedaria: Pyt%on_ _Total,,,,,,::#

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
    print(un_numero ** 2)
cuadrado(3)

print("Con impresión\n")
def cuadrado(un_numero):
    print(un_numero ** 2)
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
    total = numero1 * numero2 #variable local
    return total
resultado = multiplicar(5, 10)
print(resultado)

print("Opción 3 de Return\n")
def multiplicar(numero1, numero2):
    total = numero1 * numero2 #variable local
    print(total) #Imprime el valor de la variable local
    return total #Guaradar el valor de la variable local
resultado = multiplicar(5, 10)

#_________________________________________________________________________________________________________________________________________________
print("\nPráctica 1")
"""
Práctica Return 1
Crea una función llamada potencia que tome dos valores numéricos como argumentos. Deberá devolver el número que resulte de resolver una potencia, utilizando el primer número como base, y el segundo como exponente:
3 elevado a 4 = 3 * 3 * 3 * 3 = 81
"""
def potencia(base, exponente):
    return base ** exponente
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
    return numero in range(100,1000)  #Estamos haciendo una comparación booleeana
resultado = chequear_3A_cifras(658)
print(resultado)

print("\nEjemplo:")

def chequear_3_cifras(lista): #chequear una lista

    lista_3_cifras = []
    
    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)#Agrega a la lista
        else:
            pass #Si no se cumple la condición, no hacemos nada
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
print(todos_positivos(lista_numeros)) # Prints: False

print("\n")

#_________________________________________________________________________________________________________________________________________________
print("\n")

print("\n")
#_________________________________________________________________________________________________________________________________________________
print("\n")

print("\n")
#_________________________________________________________________________________________________________________________________________________
print("\n")

print("\n")
#_________________________________________________________________________________________________________________________________________________
print("\n")

print("\n")
#_________________________________________________________________________________________________________________________________________________
print("\n")

print("\n")
#_________________________________________________________________________________________________________________________________________________
print("\n")

print("\n")
#_________________________________________________________________________________________________________________________________________________
print("\n")

print("\n")
#_________________________________________________________________________________________________________________________________________________