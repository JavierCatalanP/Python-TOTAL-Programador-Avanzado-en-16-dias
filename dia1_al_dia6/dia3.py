print("Practica día 3 \n\n")
"""
index( )
Utilizamos el método index( ) para explorar strings, ya quepermite hallar el índice de aparición de un caracter o cadena decaracteres dentro de un texto dado.

* string.index(value, start, end) *

String.index = variable quealmacena un string
value = valor a buscar - caracter(es)buscado(s)
Start =las apariciones antes delíndice start se ignoran

*string.rindex(value, start, end)*
string[i] = devuelve el caracter en el índice i*

*: En Python, el índice en primera posición es el 0
"""
#Metodo Index
print("Metodo Index")
mi_texto = "Esta es una prueba"
resultado = mi_texto.index("a")#Contabiliza las apariciones de la letra a
print(resultado)
resultado = mi_texto[9] #busca de derecha a izquierda
print(resultado)
resultado = mi_texto[-3] #busca de izquierda a derecha
print(resultado)

#Metodo Index con valor de start
print("Metodo Index con valor de start")
mi_texto = "Esta es una prueba"
resultado = mi_texto.index("prueba")#Contabiliza las apariciones de la palabra y contabiliza desde donde comienza
print(resultado)

resultado = mi_texto.index("a")# busca desde izquierda a derecha
print(resultado)

resultado = mi_texto.index("a", 5, 11)# busca desde izquierda a derecha
print(resultado)
print("\n\n")

#Metodo riindex 
print("Metodo riindex")
mi_texto = "Esta es una prueba"
resultado = mi_texto.rindex("a")#Contabiliza las apariciones de derecha a izquierda
print(resultado)
print("\n\n")

#Practica Método Index() 1
print("Practica Método Index() 1")
"""
Práctica Método Index() 1
Encuentra y muestra en pantalla qué caracter ocupa la quinta posición dentro de la siguiente palabra: "ordenador"
"""
palabra = "ordenador"
resultado =palabra[4]
print(resultado)
print("\n\n")

print("Practica Método Index() 2")
"""
Práctica Método Index() 2
Encuentra y muestra en pantalla el índice de la primera aparición de la palabra "práctica" en la siguiente frase:

"En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
"""

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
resultado= frase.index("práctica")
print(resultado)
print("\n\n")

print("Practica Método Index() 2")
"""

Práctica Método Index() 3
Encuentra y muestra en pantalla el índice de la última aparición de la palabra "práctica" en la siguiente frase:

"En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."""
frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
resultado = frase.rindex("práctica")
print(resultado)
print("n")

#Extraer Sub string
"""substrings
Podemos extraer porciones de texto utilizando lasherramientas de manipulación de strings conocidas comoslicing (rebanar).

string[start:stop:step]

Start = índice de inicio del sub-string(incluido)
stop = índice de finalización del sub-string(excluido)
step = salto de caracteres "paso"

"""
saludo = "Hola_Mundo"
print(saludo[2:6])#extrae la palabra la_m
print(saludo[2:6:2])#extrae la palabra l_
print(saludo[2:6:3])#extrae la palabra lm    
print(saludo[::-1])#extrae la palabra odnum_aH
print("\n")
"""
Práctica Métodos de String 1
Imprime el siguiente texto en mayúsculas, empleando el método específico de strings:"""
#Solución Práctica Métodos 
print("Práctica Métodos de String 1")
frase = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."
mayuscula = frase.upper()
print(mayuscula)
print("\n")

print("Práctica Métodos de String 1")
"""
Práctica Métodos de String 2
Une la siguiente lista en un string, separando cada elemento con un espacio. Utiliza el método apropiado de listas/strings, y muestra en pantalla el resultado."""
lista_palabras = ["La","legibilidad","cuenta."]

print(" ".join(lista_palabras))
print("\n")

print("Práctica Métodos de String 3")
"""
Práctica Métodos de String 3
Reemplaza en la siguiente frase:

"Si la implementación es difícil de explicar, puede que sea una mala idea."

los siguientes pares de palabras:

"difícil" --> "fácil"

"mala" --> "buena"

y muestra en pantalla la frase con ambas palabras modificadas."""

var = "Si la implementación es difícil de explicar, puede que sea una mala idea."
print("Práctica Métodos de String 3")
var2 = var.replace("difícil", "fácil")
var = var2
var = var.replace("mala", "buena")
print(var)
print("\n")

#Propiedades de los strings
"""
-son inmutables, es decir, no se pueden modificar una vez creados.
- pueden concatenarse con el operador +
- pueden ser comparados con el operador ==
- pueden ser comparados con el operador <
- pueden ser comparados con el operador >
- pueden ser comparados con el operador <=
- pueden ser comparados con el operador >=
- pueden ser comparados con el operador !=
- pueden ser comparados con el operador in
- pueden ser comparados con el operador not in
- pueden ser comparados con el operador is
- pueden ser comparados con el operador is not
- pueden ser comparados con el operador not is
- pueden ser comparados con el operador not is not
- pueden ser comparados con el operador is is
- pueden ser comparados con el operador is is not
- pueden ser comparados con el operador not is is
- pueden ser comparados con el operador not is is not
- pueden ser multilineas
- pueden ser de longitud variable
- pueden ser de tipo variable"""

n1 = "Javi"
n2 = "er"
print(n1 + n2)#concatena
print(n1 * 3)#multiplica
print(n1 == n2)#compara
print(n1 < n2)#compara
print(n1 > n2)#compara

poema = """Mil pequeños peces blancos
      comosi hirviera
      de color del agua"""

print("agua" in poema) #busca la palabra agua en el poema
print("agua" == poema) #compara si la palabra agua esta en el poema
print("agua" not in poema) #busca la palabra agua en el poema

print(len(poema)) #cuenta los caracteres

print("\n")
print("Práctica Propiedades de String 1")
"""
Práctica Propiedades de Strings 1
Concatena 15 veces el texto "Repetición" y muestra el resultado en pantalla. Por suerte, conoces que los strings son multiplicables y puedes realizar esta actividad de forma simple y elegante."""
var = "Repetición"
print(var *15)

print("\n")
print("Práctica Propiedades de String 2")

"""Práctica Propiedades de Strings 2
Verifica si la palabra "agua" no se encuentra en el siguiente haiku. Debes imprimir el booleano.

Tierra mojada,

mis recuerdos de viaje

entre las lluvias"""

var = """Tierra mojada
mis recuerdos de viaje,
entre las lluvias"""
var2 = "agua"

print(var2 not in var )

print("\n")
print("Práctica Propiedades de String 2")
"""
Práctica Propiedades de Strings 3
Muestra en pantalla el largo (en números de caracteres) de la palabra electroencefalografista."""
var= "electroencefalografista"
print(len(var))
print("\n")

#Listas, []
mi_lista1 = ["Juan", "Pedro", "Laura", "Carmen", "Susana"]

mi_lista2 = [12, 34, True, 78.9]

mi_lista3 = mi_lista1+mi_lista2

resultado = len(mi_lista1)#cuenta los elementos de la lista

print(type(mi_lista1))
print(type(mi_lista2)) 
print(type(mi_lista3))
print(len(mi_lista1))
print(len(mi_lista2))
print(len(mi_lista3))
print(mi_lista1[0])
print(mi_lista2[2])
print(mi_lista3[3])

print(mi_lista3)
mi_lista3[0] = 'J,C' # sobre escribe el elemento 0
print(mi_lista3)
print("\n")

#Metodos en las listas
mi_lista1.append("Lorenzo")#agrega un elemento al final de la lista
print(mi_lista1)
mi_lista1.insert(6,"HI")#agrega
print(mi_lista1)

eliminado = mi_lista1.pop(0)#elimina el elemento en el indice 0
print("\n")
mi_lista1.remove("HI")#elimina    
print(mi_lista1)
print("\n")
mi_lista1.sort()#ordena la lista
print(mi_lista1)
print("\n")

print(type(mi_lista1))
mi_lista1.reverse()#invierte la lista

print("\n")

#Práctica Listas 1
"""Práctica Listas 1
Crea una lista con 5 elementos, dentro de la variable mi_lista. Puedes incluir strings, booleanos, números, etc."""
mi_lista = ['string', 1, 30.2, "cuatro", 123]
print(mi_lista)

print("\n")
"""
Práctica Listas 2
Agrega el elemento "motocicleta" a la siguiente lista de medios de transporte:

medios_transporte = ["avión", "auto", "barco", "bicicleta"]

No debes modificar la línea de código ya suministrada, sino que debes emplear el método apropiado de listas para añadir un nuevo elemento."""

medios_transporte = ["avión", "auto", "barco", "bicicleta"]
medios_transporte.append('motocicleta')
print(medios_transporte)

print("\n")

"""
Práctica Listas 3
Utiliza el método pop() para quitar el tercer elemento de la siguiente lista llamada frutas, y almacénalo en una variable llamada eliminado. Utiliza métodos de listas sin alterar la línea de código ya suministrada.

manzana

banana

mango

cereza

sandía"""

frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
eliminado = frutas.pop(2)
print(frutas)


#Diccionarios
"""
-son inmutables, es decir, no se pueden modificar una vez creados.
- pueden contener cualquier tipo de datos, incluso otros diccionarios.
- pueden ser de longitud variable
- pueden ser de tipo variable
- pueden contener cualquier tipo de datos, incluso otros diccionarios.
- no tienne un orden específico    
"""
mi_diccionario = {'c1':'valor 1', 'c2':'valor 2', 'c3':'valor 3'}#crea un diccionario
print(type(mi_diccionario))
print(mi_diccionario)

resultado = mi_diccionario['c2']#busca el valor de la clave c2
print(resultado)

cliente = {'nombre':'Juan', 'edad':34, 'saldo':2500.0, 'talla':'M'}
consulta = (cliente['nombre'])#
print("\n")
print(consulta  +" Tiene "  + str(cliente['edad'])+ " y su saldo es:  " + str(cliente['saldo']) + " Solo le alcanza para una polera talla: " + cliente['talla'])
print("\n")

dic = {'clave1':123, 'clave2':[1,2,3], 'clave3':{'clave31':100, 'clave32':200, 'clave33':cliente}}
print(dic['clave3']['clave31'])#busca el valor de la clave3 y luego la clave31

dic = {'c1':['a', 'b','c'], 'c2':['d', 'e', 'f'], 'c3':['g', 'h', 'i']}
       
print(dic['c2'][1].upper())#busca el valor de la clave2 y luego el elemento 1 y lo pone en mayuscula

print("\n")

#Agregar elementos a un diccionario
dic = {'c1':['a', 'b','c'], 'c2':['d', 'e']}
print(dic)
dic['c3'] = ['g', 'h', 'i']#agrega un elemento al diccion
print(dic)
dic[2] = 'hola'#agrega un elemento al diccion
print(dic)
dic[2]= '8' #Reemplaza el valor de la clave 2
print(dic)

print("\n")

#Eliminar elementos de un diccionario
dic = {'c1':['a', 'b','c'], 'c2':['d', 'e']}
print(dic)
del dic['c2']#elimina el elemento c2
print(dic)

print("\n")

print(dic.keys())#muestra las claves
print(dic.values())#muestra los valores
print(dic.items)#muestra los elementos

#Práctica Diccionarios 1
print("PRACTICA DICCIONARIOS 1")
print("\n")
"""
Práctica Diccionarios 1

Práctica Diccionarios 1
Crea un diccionario llamado mi_dic que almacene la siguiente información de una persona:

nombre: Karen

apellido: Jurgens

edad: 35

ocupacion: Periodista

Los nombres de las claves y valores deben ser iguales a la consigna."""

#solución practica 1 diccionario
mi_dic = {
 "nombre": "Karen",
 "apellido": "Jurgens",
 "edad": 35,
 "ocupacion": "Periodista"   
}
print("\n")
#Práctica Diccionarios 2
print("PRACTICA DICCIONARIOS 2")
print("\n")
"""
Práctica Diccionarios 2
Crea una función print que devuelva del segundo item de la lista llamada points2, dentro del siguiente diccionario.

Si el valor 300 cambiara en el futuro, el código debería funcionar igual para devolver el valor que se encuentre en esa misma posición. Para ello, deberás hacer referencia a los nombres de las claves y/o índices según corresponda."""

def print_second_point(d):
    return d["puntos"]["points2"][1]

mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}

print(print_second_point(mi_dict))
print("\n")

#Práctica Diccionarios 3
print("PRACTICA DICCIONARIOS 3")
print("\n")
"""
Práctica Diccionarios 3
Actualiza la información de nuestro diccionario llamado mi_dic  (reasignando nuevos valores a las claves según corresponda), y agrega una nueva clave llamada "pais" (sin tilde). Los nuevos datos son:

nombre: Karen

apellido: Jurgens

edad: 36

ocupacion: Editora

pais: Colombia

para ello, no debes cambiar la línea de código ya escrita, sino actualizar los valores mediante métodos de diccionarios.

"""
mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}

# Actualizando los valores existentes y agregando una nueva clave
mi_dic["edad"] = 36
mi_dic["ocupacion"] = "Editora"
mi_dic["pais"] = "Colombia"

# Imprimiendo el diccionario actualizado
print(mi_dic)
print("\n")

#Tuples
"""
- son inmutables, es decir, no se pueden modificar una vez creados.
- ocupan menos memoria que las listas.
- a prueba de hacer una lista de millones de elementos, una tupla puede ser más rápida
- a pruebas de dañar una tupla, una tupla puede ser más rápida
- son inmutables como los String, no se pueden modificar
"""
mi_tuple = (1,2,3,4,5, (9,2,3,4,5))
print(mi_tuple)
print(type(mi_tuple))

#Tuples pueden tener distintos valores y tipos de datos
mi_tuple = ("hola", 1, True, [1,2,3], (9,2,3,4,5), "jc")
print(mi_tuple[0])#muestra el elemento 0 de la tupla
print(mi_tuple[-2])#muestra el elemento -2 de la tupla
print(mi_tuple[4:0])#muestra el elemento 1 al 4 de la tupla

#casting
mi_tuple = list(mi_tuple)#convierte la tupla en una lista
print(type(mi_tuple))
print("\n")

t = (1, 2, 3)
x, y, z = t#asigna a cada variable el valor de la tupla
print(x, y, z) #imprime 1 2 3 (Debe contener la misma cantidad de variables que elementos en la tupla)
print(len(t))#muestra la cantidad de elementos de la tupla
print(t.count(1))#muestra la cantidad de veces que se repite el valor 1 en la tup 
print(t.index(2))#muestra la posicion del valor 2 en la tupla


print("\n")
#Práctica Tuples 1)
print("PRACTICA TUPLES 1")
"""
Práctica Tuples 1
Utiliza un método de tuplas para contar la cantidad de veces que aparece el valor 2 en la siguiente tupla, y muestra el resultado (integer) en pantalla:

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)"""
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)

cantiadad_de_2 = mi_tupla.count(2)
print(cantiadad_de_2)
print("\n")
print("\n")

#Práctica Tuples 2)
print("PRACTICA TUPLES 2")
"""
Práctica Tuples 2
Convierte a lista la siguiente tupla, y almacénala en una variable llamada mi_lista.

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)"""

print("\n")

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
mi_lista = list(mi_tupla)
print(mi_lista)

print("\n")


#Práctica Tuples 3)
print("PRACTICA TUPLES 3")

"""
Práctica Tuples 3
Extrae los elementos de la siguiente tupla en cuatro variables: a, b, c, d

mi_tupla = (1, 2, 3, 4)"""

mi_tupla = (1, 2, 3, 4)

a, b, c, d = mi_tupla

print(a)
print(b)
print(c)
print(d)

print("\n")

#Sets
"""
Caracteristicas:
- Se pueden modificar
- No tienen un orden
- No permite duplicados
- No permite subindices
- Se pueden crear con {} o con la función set()
- no poner lisas dentro de los sets
- si admiten valores booleanos
- si acetan valores repetidos
- se pueden hacer operaciones entre sets
- no se pueden hacer operaciones entre sets y listas
- los dicc no se pueden hacer sets
- los seets se pueden uniir con el operador |
"""

mi_set1 = set((1,2,3,4,5))#crea un set a partir de una lista
print(type(mi_set1))
print(mi_set1)

mi_set = {1,2,3,4,5,6}#se crea un set con {}
print(type(mi_set))
print(mi_set)

print(len(mi_set))#muestra la cantidad de elementos del set
print(3 in mi_set)#muestra si el valor 3 esta en el set 

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
s3 = s1.union(s2) #une los sets

print(s3)

#metodos
s3.add(1235) #agrega un elemento al set
s3.remove(3) #elimina un elemento del set
s3.discard(2) #elimina un elemento del set
sorteo = s3.pop() #elimina un elemento del set
print(sorteo)#muestra el elemento eliminado
s3.clear() #limpia el set
print(s3)
print("\n")

#Práctica Sets 1)
print("PRACTICA SETS 1")
"""

Práctica Sets 1
Une los siguientes sets en uno solo, llamado mi_set_3:

{1, 2, "tres", "cuatro"}

{"tres", 4, 5}
"""
mi_set_1 = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5} 

mi_set_3 = mi_set_1.union(mi_set_2)
print(mi_set_3)

print("\n")

#Práctica Sets 2)
print("PRACTICA SETS 2")
"""

Práctica Sets 2
Elimina un elemento al azar del siguiente set, utilizando métodos de sets.

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}"""

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
eliminado = sorteo.pop()

print(eliminado)
print(sorteo)

print("\n")

#Práctica Sets 3)
print("PRACTICA SETS 3")
"""

Práctica Sets 3
Agrega el nombre Damián al siguiente set, utilizando métodos de sets:

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
"""

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}

sorteo.add("Damián")

print(sorteo)
print("\n")

#Booleanos
"""
- Solo tienen 2 valores: True y False
- Se pueden crear de manera indirecta con operadores
- Se pueden comparar con operadores
- Se pueden convertir a enteros
- Los operadores son: ==, !=, <, >, <=, >=
- Los operadores lógicos son: and, or, not
- Los operadores de identidad son: is, is not
- Los operadores de pertenencia son: in, not in
- Los operadores de asignación son: =, +=, -=, *=, /=, %=,
- Los operadores de comparación son: ==, !=, <, >, <=, >=
- booleanos son la base de la IA
"""
var1 = True
var2 = False

numero1 = 5 > 2+3 #5 es mayor que 2+3
numero2 = 5 == 2+3 #5 es igual a 2+3
numero3 = 5 != 2+3 #5 es diferente a 2+3
numero = bool(5>6) #bool convierte un valor a booleano

print(var1)

print(numero1)
print(numero2)
print(numero3)
print(numero)


lista = [1,2,3,4,5]
control = 5 in lista #verifica si el valor 5 esta en la lista
print(type(control)) 
print(control)

print("\n")
#Práctica Booleanos 1)
print("PRACTICA BOOLEANOS 1")
"""
Práctica Booleanos 1
Realiza una comparación que arroje como resultado un booleano y almacena el resultado (True/False) en una variable llamada prueba
"""
#solucion
prueba = 5 < 4

print(prueba)
print("\n")

#Práctica Booleanos 2)
print("PRACTICA BOOLEANOS 2")
"""
Práctica Booleanos 2
Verifica si 17834/34 es mayor que 87*56 y muestra el resultado (booleano) en pantalla utilizando print()
"""
#solucion
resultado = 17834/34 > 87*56

print(resultado)

print("\n")
#Práctica Booleanos 3)

print("PRACTICA BOOLEANOS 3")
"""
Práctica Booleanos 3
Verifica si la raíz cuadrada de 25 es igual a 5 y muestra el resultado (booleano) en pantalla utilizando print()
"""
#solucion
resultado = (5**2 == 25)
print(resultado)
print("\n")

#Proyecto día 3
print(f"Proyecto día 3")
"""
Proyecto del Día 3
Bueno, el tercer día no ha dejado nada que desear. Hemos visto muchas cosas y de las buenas,
y ha llegado la hora de juntar todo lo aprendido y ponerlo en práctica, creando un programa
perfectamente funcional desde cero.
Ahora que ya sabes usar los métodos y las propiedades de los strings, que sabes indexar
conjuntos de datos como los strings, las listas y los tuples, y sobre todo ahora que conoces
todos los tipos de datos que necesitas para poder almacenar lo que sea, vas a poder encontrar
una forma de programar un analizador de texto.
La consigna es la siguiente: vas a crear un programa que primero le pida al usuario que
ingrese un texto. Puede ser un texto cualquiera: un artículo entero, un párrafo, una frase, un
poema, lo que quiera. Luego, el programa le va a pedir al usuario que también ingrese tres
letras a su elección y a partir de ese momento nuestro código va a procesar esa información
para hacer cinco tipos de análisis y devolverle al usuario la siguiente información:
1. Primero: ¿cuántas veces aparece cada una de las letras que eligió? Para lograr esto, te
recomiendo almacenar esas letras en una lista y luego usar algún método propio de string
que nos permita contar cuantas veces aparece un sub string dentro del string. Algo que
debes tener en cuenta es que al buscar las letras pueden haber mayúsculas y minúsculas
y esto va a afectar el resultado. Lo que deberías hacer para asegurarte de que se
encuentren absolutamente todas las letras es pasar, tanto el texto original como las
letras a buscar, a minúsculas.
2. Segundo: le vas a decir al usuario cuántas palabras hay a lo largo de todo el texto. Y
para lograr esta parte, recuerda que hay un método de string que permite transformarlo
en una lista y que luego hay una función que permite averiguar el largo de una lista.
3. Tercero: nos va a informar cuál es la primera letra del texto y cuál es la última. Aquí
claramente echaremos mano de la indexación.
4. Cuarto: el sistema nos va a mostrar cómo quedaría el texto si invirtiéramos el orden de
las palabras. ¿Acaso hay algún método que permita invertir el orden de una lista, y otro
que permita unir esos elementos con espacios intermedios? Piénsalo.
5. Y por último: el sistema nos va a decir si la palabra “Python” se encuentra dentro del
texto. Esta parte puede ser algo complicada de imaginársela, pero te voy a dar una pista:
puedes usar booleanos para hacer tu averiguación y un diccionario para encontrar la
manera de expresarle al usuario tu respuesta. 
"""


#Solución
texto = input("Ingresa un texto a elección: ")
letras = [] #lista vacia

texto = texto.lower()#pasa todo a minusculas

letras.append(input("Ingresa la primera letra: ".lower()))#pasa todo a minusculas
letras.append(input("Ingresa la segunda letra: ".lower()))#pasa todo a minusculas
letras.append(input("Ingresa la tercera letra: ".lower()))#pasa todo a minusculas

print("\n")
print("CANTIDAD DE LETRAS")#
cantidad_letras1 = texto.count(letras[0])#cuenta cuantas veces aparece la letra en el texto
cantidad_letras2 = texto.count(letras[1])#cuenta cuantas veces aparece la letra en el texto
cantidad_letras3 = texto.count(letras[2])#cuenta cuantas veces aparece la letra en el texto

print(f"Hemos encontrado la letra '{letras[0]}' repetida {cantidad_letras1} veces")#imprime la letra y la cantidad de veces que se repite
print(f"Hemos encontrado la letra '{letras[1]}' repetida {cantidad_letras2} veces")#imprime la letra y la cantidad de veces que se repite
print(f"Hemos encontrado la letra '{letras[2]}' repetida {cantidad_letras3} veces")#imprime la letra y la cantidad de veces que se repite

print("\n")
print("CANTIDAD DE PALABRAS")
palabras = texto.split()#saca las palabras del texto
print(f"Hemos encontrado {len(palabras)} palabras en tu texto")#imprime la cantidad de palabras

print("\n")
print("LETRAS DE INICIO Y DE FIN")
letra_inicio = texto[0]#saca la primera letra del texto
letra_final = texto[-1]#saca la ultima letra del texto
print(f"La letra inicial es '{letra_inicio}' y la letra final es '{letra_final}'")#imprime la letra inicial y la final

print("\n")
print("TEXTO INVERTIDO")
palabras.reverse()#invierte el orden de las palabras
texto_invertido = ' '.join(palabras)#une las palabras con espacios
print(f"Si ordenamos tu texto al revés va a decir: '{texto_invertido}'")#

print("\n")
print("BUSCANDO LA PALABRA PYTHON")
buscar_python ='python' in texto
dic = {True:"sí", False:"no"}#crea un diccionario
print(f"La palabra 'Python' {dic[buscar_python]} se encuentra en el texto")#imprime si la palabra python se encuentra en el texto
#Dia 3 terminado.

"""Resumen:
En este día hemos aprendido a trabajar con los strings, los booleanos, los list
"""