print("Practica día 2 \n\n")
"""
- Tipos de datos
- Conversiones
- Variables
- Formatear strings
- Operaciones matemáticas
- redondear"""

# Tipos de datos
print("Tipos de datos \n\n")
"""
String (str) "hola", "45#$%$#", " ", "123"
Integer (int) 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
Floaring (float) 1.2, 2.3, 3.4, 4.5, 5.6, 6.7
Listas (list) [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Boolean (bool) True, False
Diccionario (dict) {"nombre": "Juan", "edad": 25} Clave = Valor    
Tuples (tuple) (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) #Orden que no se puede modificar nunca
Sets(set) {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} #No se repiten valores
"""
#Variales
print("Variables \n\n")
nombre1 = "J.C" #Dinamicamente pueden variar su contenido
edad = 37
print(nombre1, edad)
#Ejemplo 2
print("Ejemplo 2 \n")
#nombre2 = input("Dime tu nombre: ")
#print("Tu nombre es: " + nombre2)
#Ejemplo 3 concatenar variales
#frase = "Mi nombre es " + nombre2 + " y mi edad es " + str(edad)
#print((frase)+"\n")
#Ejemplo 4
#num1 = int(input("Dime un número: "))
#num2 = int(input("Dime otro número: "))
#print("La suma de los números es: " + #str(num1 + num2))
"""
Práctica con Variables 1
Declara dos variables, llamadas nombre y edad.

Asigna a la variable nombre el valor "Tony Soprano", y a la edad, el valor 51.
"""
print("Práctica con Variables 1 \n\n")
nombre = "Tony Soprano"
edad = 51
#Solución Practica 1
print("Solución Practica 1 \n")
print(nombre, edad)
print("Mi nombre es " + nombre + " y mi edad es " + str(edad))
print("\n\n")

"""
      Práctica con Variables 2
      Crea tres variables:

      nombre

      apellido

      nombrecompleto

      A nombre, asígnale el valor "Julia", y en apellido, asigna el valor "Roberts". Finalmente, construye la variable nombrecompleto concatenando las variables (recuerda sumar un espacio intermedio).
"""
#Solución Practica 2
print("Solución Practica 2 \n")
nombre = "Julia"
apellido = "Roberts"
nombrecompleto = nombre + " "+ apellido

print(nombrecompleto)

"""
Práctica con Variables 3
Declara la variable curso, asígnale el valor "Python", y muestra en pantalla la frase:

Estás tomando un curso de curso

Para ello deberás concatenar la primera parte de la frase con el valor que asumirá la variable. Recuerda agregar un espacio antes de concatenar la variable al resto del texto.
"""
#Solución Practica 3
print("Solución Practica 3 \n")
curso = "Python"
print("Estás tomando un curso de", curso)

#Buena practica es escribir variables con guión bajo en minuscula y no camercase
#Ejemplo
curso_python = "Python"
#Omitir espacios, acentos y la letra ñ, no usar numeros al comienzo de la variable
#Ejemplo
mes_8c = "Agosto"
#No usar palabras reservadas (input, print, if, else, string, int, etc))
#Ejemplo
#class = "Clase"
# No usar signos (como $, %, &, : "',<>/?\()!@#$%&, etc)

#Intergers y Floats
print("Intergers y Floats \n\n")

mi_numero_1 = 1
mi_numero_2 = 2.6
mi_numero_3 = True
mi_numero_4 = 2,6
mi_numero_5 = "'2,6'"
print(mi_numero_1, (type(mi_numero_1)))
print(mi_numero_2, (type(mi_numero_2)))
print(mi_numero_3, (type(mi_numero_3)))
print(mi_numero_4, (type(mi_numero_4)))
print(mi_numero_5, (type(mi_numero_5)))

#edad = input("Dime tu edad: ")
#print("Tu edad es " + edad)
#nueva_edad = int(edad) + 1
#print("pronto vas a tener ",  nueva_edad)

#Practica con intergers
"""
Práctica con Integers
Declara una variable numérica llamada num_entero que contenga un valor de tipo integer de tu elección.

Imprime el tipo de dato de dicha variable.
"""
print("Practica con Integers \n\n")
#Solución Practica Integers
print("Solución Practica Integers\n")
num_entero = 33
print((str(num_entero) + "\n"))

"""Práctica con Floats
Declara una variable numérica llamada num_decimal que contenga un valor de tipo float de tu elección.

Imprime el tipo de dato de dicha variable.
"""
print("Practica con Floats \n\n")
#Solución Practica Floats
num_decimal = 33.3
print(type(num_decimal))

"""
Práctica con Tipos de Datos Numéricos
¿De qué tipo es el resultado de la suma de 7.5 + 2.5? Genera el código para verificarlo.

Para ello, crea dos variables:

num1 = 7.5

num2 = 2.5

A continuación, muestra en pantalla el tipo de dato que resulta de la suma de ambos números.

Realiza el mismo ejercicio en PyCharm para ver el resultado. ¿Coindice con lo que esperabas?
"""
print("Practica con Tipos de Datos Numéricos \n\n")
#Solución Practica Tipos de Datos Numéricos (Python automaticamente realiza la conversión de tipos de datos)
num1 = 7
num2 = 2.5
total = num1 + num2
print(type(total))

#Conversiones implicitas

num1 = num1 + num2
total1 = int(num2)#Conveirte a entero
print("Conversiones implicitas \n\n")
print(type(num1))
print(type(num2))
print(type(total1))
print(total1)

#edad=input("Dime tu edad: ")
print(type(edad))
edad = int(edad) #conversión de string a entero
print(type(edad))
nueva_edad = 1 + edad
print ("Tu nueva edad es :", str(nueva_edad))
print(type(nueva_edad))

#Práctica con conversiones 1
"""
Práctica con Conversiones 1
Convierte el valor de num1 en un int e imprime el tipo de dato que resulta:"""
print("Práctica con Conversiones 1 \n\n")
#Solucion Practica Conversiones 1
num1 = 7.5
num1 = int(num1)
print(type(num1))
print("\n\n")

"""
Práctica con Conversiones 2
Convierte el valor de num2 en un float e imprime el tipo de dato que resulta:
"""

print("Práctica con Conversiones 2 \n\n")
#Solucion Practica Conversiones 2
num2 = 10
num2 = float(num2)
print(type(num2))
print("\n\n")
"""
Práctica con Conversiones 3
Suma los valores de num1 y num2.

No modifiques el valor de las variables ya declaradas, sino aplica las conversiones necesarias dentro de la función print().
"""
print("Práctica con Conversiones 3 \n\n")
#Solucion Practica Conversiones 3
num1 = "7.5"
num2 = "10"

print(float(num1) + int(num2))
print("\n\n")

#Formatear Cadenaa
"""
1- Función format
print("Mi auto es {} y de matrícula {} ".format(color_auto,matricula))
2- cadenas literales
print(f "Mi auto es (color_autol y de matrícula (matricula"),
"""

x = 10
y = 5
print("Mis numeros son " + str(x) + str(y)) #I[mpresiones con conversiones
print("Mis numeros son {} y {}".format(x,y)) #Impresiones con format
print("La suma de {} y {} es {}".format(x,y,x+y)) #Impresiones con format
color="rojo"
matricula = 541926
print (f"El auto es {color} y su matricula es {matricula}") #Impresiones con format

"""
Práctica Formatear Cadenas 1
Necesitamos imprimir el nombre y número de asociado dentro de la siguiente frase:

Estimado/a (nombre_asociado), su número de asociado es: (numero_asociado)

Recuerda que la precisión de tu respuesta (espacios, ortografía y puntuación), es muy importante para llegar al resultado correcto.
"""
#Solucion Practica Formatear Cadenas 1
print("Práctica Formatear Cadenas 1 \n\n")
nombre_asociado = "Jesse Pinkman"
numero_asociado1 = 399058

print(f"Estimado/a {nombre_asociado}, su número de asociado es: {numero_asociado1}\n\n")

"""

Práctica Formatear Cadenas 2
Muestra al usuario la cantidad de puntos acumulados dentro de la siguiente frase:

Has ganado (puntos_nuevos) puntos! En total, acumulas (puntos_totales) puntos

Recuerda que la precisión de tu respuesta (espacios, ortografía y puntuación), es muy importante para llegar al resultado correcto.
"""
#Solucion Practica Formatear Cadenas 2
print("Práctica Formatear Cadenas 2 \n")
puntos_nuevos = 350
puntos_totales = 1225
print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos\n\n")

"""

Práctica Formatear Cadenas 3
Muestra al usuario la cantidad de puntos acumulados dentro de la siguiente frase:

Has ganado (puntos_nuevos) puntos! En total, acumulas (puntos_totales) puntos

En esta ocasión, la cantidad de puntos acumulados (totales) será igual a los puntos_anteriores más los puntos_nuevos.

Recuerda que la precisión de tu respuesta (espacios, ortografía y puntuación), es muy importante para llegar al resultado correcto.
"""
#Solucion Practica Formatear Cadenas 3
print("Práctica Formatear Cadenas 3 \n")
puntos_anteriores = 875
puntos_nuevos = 350
puntos_totales = puntos_anteriores + puntos_nuevos
print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos\n\n")

#Operadores matemáticos






















