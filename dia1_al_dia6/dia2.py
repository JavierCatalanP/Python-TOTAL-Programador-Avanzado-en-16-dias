
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
nombre1 = "J.C"  #Dinamicamente pueden variar su contenido
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
nombrecompleto = nombre + " " + apellido

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
mi_numero_4 = 2, 6
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
total1 = int(num2)  #Conveirte a entero
print("Conversiones implicitas \n\n")
print(type(num1))
print(type(num2))
print(type(total1))
print(total1)

#edad=input("Dime tu edad: ")
print(type(edad))
edad = int(edad)  #conversión de string a entero
print(type(edad))
nueva_edad = 1 + edad
print("Tu nueva edad es :", str(nueva_edad))
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
print("Mis numeros son " + str(x) + str(y))  #I[mpresiones con conversiones
print("Mis numeros son {} y {}".format(x, y))  #Impresiones con format
print("La suma de {} y {} es {}".format(x, y, x + y))  #Impresiones con format
color = "rojo"
matricula = 541926
print(f"El auto es {color} y su matricula es {matricula}"
      )  #Impresiones con format
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

print(
    f"Estimado/a {nombre_asociado}, su número de asociado es: {numero_asociado1}\n\n"
)
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
print(
    f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos\n\n"
)
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
print(
    f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos\n\n"
)

#Operadores matemáticos
x = 16
y = 2
z = 2

print(f"{x} mas {y} es igual a {x+y}")  #Suma
print(f"{x} menos {y} es igual a {x-y}")  #Resta
print(f"{x} por {y} es igual a {x*y}")  # multiplicación
print(f"{x} dividido {y} es igual a {x/y}")  #División
print(f"{x} elevado a {y} es igual a {x**y}")  #Potencia
print(f"{x} elevado a {3} es igual a {x**3}")  #Potencia x 3
print(f"{x} modulo {y} es igual a {x%y}"
      )  #Modulo significa el residuo de una división
print(
    f"{z} dividido al piso de {y} es igual a {z//y}"
)  #División al piso significa que solo se muestra el entero de la división
print(f"La raíz cuadrada de {x} es igual a {x**0.5}")  #Raíz cuadrada
print(f"El 20% de {x} es igual a {x*0.2}%")  #20% de x

print("\n\n")
"""
Práctica Operadores Matemáticos 1
Muestra en pantalla el cociente (división al piso) de los siguientes dos números: 874 dividido entre 27.

Debes mostrar solo el valor numérico que resulta de esta operación.
"""
#Solucion Practica Operadores Matemáticos 1
print("Práctica Operadores Matemáticos 1 \n")
x = 874
y = 27
print(f"{x//y}")
"""
Práctica Operadores Matemáticos 2
Muestra en pantalla el módulo (es decir, el resto) de la división entre 456 y 33.

Debes mostrar solo el valor numérico que resulta de esta operación.
"""
print("\n\n")
#Solucion Practica Operadores Matemáticos 2
print("Práctica Operadores Matemáticos 2 \n")
x = 456
y = 33
print(f"{x%y}")
print("\n\n")
"""
Práctica Operadores Matemáticos 3
Calcula y muestra en pantalla la raíz cuadrada de 783.

Debes mostrar solo el valor numérico que resulta de esta operación.
"""
#Solucion Practica Operadores Matemáticos 3
print("Solucion Practica Operadores Matemáticos 3 \n")
x = 783
print(f"{x**0.5}")
print("\n\n")

#Redondeo
print(f"El número {x} redondeado a 2 decimales es {round(x,2)}"
      )  #Redondeo a 2 decimales
print(f"El número {x} trunca a 2 decimales es {round(x,2)}"
      )  #Trunca a 2 decimales
resultado = (round(90 / 7))
print(resultado)
print("\n")

valor = round(95.555555555555555555555, 2)  #Se configura la variable
print(valor)
print(type(valor))  #Tipo de dato float

print("\n")
valor = round(
    95.555555555555555555555)  #Se modifica la variable y el tipo de dato
print(valor)
print(type(valor))  #Tipo de dato int

print("\n")
valor = 95.555555555555555555555
print(round(valor))
print(type(valor))  #Tipo de dato float
print("\n\n")
"""
Práctica Redondeo 1
Redondea el resultado de la división 10/3 a un número con 2 decimales, y muestra en pantalla el valor redondeado.
"""
#Solución Practica Redondeo 1
print("Solución Practica Redondeo 1\n")
x = round((10 / 3), 2)
print(x)
print("\n")
"""
Práctica Redondeo 2
Redondea el número 10.676767 al entero más próximo, y muestra en pantalla el resultado.
"""
#Solución Practica Redondeo 2
print("Solución Practica Redondeo 2\n")
valor = 10.676767
print(round(valor))
print("El valor redondeado es: ", round(valor))
print("\n")
"""
Práctica Redondeo 3
Calcula la raíz cuadrada de 5, y muestra en pantalla el resultado redondeado con 4 posiciones decimales.
"""
#Solución Practica Redondeo 3
print("Solución Practica Redondeo 3\n")
x = 5
print(float(round((5**0.5), 4)))
print("\n")
"""
La situación es esta: tú trabajas en una empresa donde los vendedores reciben comisiones
del 13% por sus ventas totales, y tu jefe quiere que ayudes a los vendedores a calcular sus
comisiones creando un programa que les pregunte su nombre y cuánto han vendido en este
mes. Tu programa le va a responder con una frase que incluya su nombre y el monto que le
corresponde por las comisiones.
Esto no es un programa complejo, pero es entendible que pueda complicarse cuando estás
aprendiendo. Por más que lo que has aprendido hasta ahora es muy simple, ponerlo todo junto
en un solo programa puede ser complejo, por lo que te doy un par de ayudas:
 Este programa debería comenzar preguntando cosas al usuario, por lo tanto, vas a
necesitar input para poder recibir los ingresos del usuario y deberías usar variables para
almacenar esos ingresos. Recuerda que los ingresos de usuarios se almacenan como
strings. Por lo tanto, deberías convertir uno de esos ingresos en un float para poder hacer
operaciones con él.
 ¿Y qué operaciones necesitas hacer? Bueno, calcular el 13% del número que haya
ingresado el usuario. Es decir, que debes multiplicar ese número por 13 y luego dividirlo
por 100. Recuerda almacenar ese resultado en una variable.
 Sería bueno que para imprimir en pantalla el resultado te asegures de que esa
información no tenga más de dos decimales, para que sea fácil de leer, y luego organiza
todo eso en un string al que debes dar formato. Recuerda que conocimos dos maneras
de hacerlo y cualquiera de ellas es válida.
No dejes de intentar resolverlo, y si se te complica, en la próxima lección lo hacemos juntos.
"""

#Solución Practica Redondeo 3
#Forma 1
comision = 0.13
nombre = input("Ingrese su nombre: ")
ventas = int(input("Ingrese el total de ventas: "))
comision_total = round(ventas * comision, 2)
print(f"Hola {nombre}, tu comisión es de ${(comision_total)}")

print("\n")
#forma 2
nombre = input("Por favor, dume tu nombre: ")
ventas = int(input("diga sus ventas totales del mes: "))
comision = round(ventas * 13 / 100, 2)
print(f"Hola {nombre}, tus comisiones de este mes son de ${comision}")
