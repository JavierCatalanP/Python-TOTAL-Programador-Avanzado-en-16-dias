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
