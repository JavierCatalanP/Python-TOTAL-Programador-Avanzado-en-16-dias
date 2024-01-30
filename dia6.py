print('Día 6')

"""
- Abrir y manipular archivos
- Crear archivos nuevos
- Escribir y sobreescribir archivos
- Navega entre directorios
- Crear y eliminar carpetas
"""
print("Abrir y manipular archivos")

""" E (Entrada) /S (Salida) - I (Input) / O (Output) 
- abrir = open()
- leer = read()
- escribir = write()
- cerrar = close()
"""
print("\nAbrir un archivo")
mi_archivo = open('prueba.txt')
print(mi_archivo.read()) #Abre el archivo

print("\nReadline y rstrip\n")

mi_archivo = open('prueba.txt')

for l in mi_archivo:
    print('Aquí dice: '+l)

mi_archivo = open('prueba.txt')
una_linea = mi_archivo.readline()

una_linea = mi_archivo.readline()
print(una_linea.upper())

una_linea = mi_archivo.readline()
print(una_linea.rstrip())

mi_archivo = open('prueba.txt')
todas = mi_archivo.readline()
#todas = todas.pop()
print(todas)

mi_archivo.close()# Cierra el archivo

#__________________________________________________
print("\nEjercicio 1\n")
"""
Práctica Abrir y Manipular Archivos 1
Abre el archivo texto.txt e imprime su contenido.

Nota: el archivo se encuentra guardado en la misma carpeta donde se aloja tu código
"""
print("Solución 1\n")

archivo = open("texto.txt")
print(archivo.read())

#__________________________________________________
print("\nEjercicio 2\n")
"""

Práctica Abrir y Manipular Archivos 2
Imprime la primera línea del archivo texto.txt

No olvides abrir el archivo y cerrarlo luego de ejecutar tu código.

Nota: el archivo se encuentra guardado en la misma carpeta donde se aloja tu código.
"""
print("Solución 2\n")

archivo = open("texto.txt")
una_linea = archivo.readline()
print(una_linea)

#__________________________________________________
print("\nEjercicio 3\n")
"""
Práctica Abrir y Manipular Archivos 3
Abre el archivo texto.txt e imprime únicamente la segunda línea.
"""
print("Solución 3\n")

archivo = open("texto.txt")
lines = archivo.readlines()
if len(lines) > 1:
    print(lines[1].strip())
print(archivo.read())

#__________________________________________________
print("\nCrear y escribir archivos\n")
"""
solo lectura = mi_archivo = open('archivo.txt','r') viene por defecto
Solo escritura = mi_archivo = open('archivo.txt','w')
solo escritura al final del archivo = mi_archivo = open('archivo.txt','q')
se crea el archivo si no existe, de existir solo deja escribir al final del archivo.
"""
#No permite ya que es solo modo lectura
archivo = open('prueba.txt', 'r')
archivo.write('soy el nuevo texto')
archivo.close()
#__________________________________________________
#Permite escribir (como no existe prueba1.txt, lo crea con el contenido dentro)
archivo = open('prueba1.txt', 'w')
archivo.write('Reemplazo el nuevo texto\n')
archivo.write('con Hola Mundo adicional') #Si el archivo existe, reemplaza el contenido
archivo.close()
#__________________________________________________
#Agrega texto en vez de reescribir
archivo = open('prueba1.txt', 'a')
archivo.write("""\n\nAgrego 
más texto
desde una nueva
codificación 
con privilegio
a""")
archivo.close()

#__________________________________________________
#Práctica Crear y Escribir Archivos 1
"""
Práctica Crear y Escribir Archivos 1
Abre el archivo llamado "mi_archivo.txt", y cambia su contenido por el texto "Nuevo texto".

Imprime el contenido completo de "mi_archivo.txt" al finalizar.

Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura.
"""
# Abre el archivo en modo escritura ('w')
with open('mi_archivo.txt', mode='w', encoding='utf-8') as file:
    # Escribe el nuevo contenido en el archivo
    file.write("Nuevo texto")

# Abre el archivo en modo lectura ('r')
with open('mi_archivo.txt', mode='r', encoding='utf-8') as file:
    # Lee el contenido del archivo
    contenido = file.read()

    # Imprime el contenido del archivo
    print(contenido)


#__________________________________________________
#Práctica Crear y Escribir Archivos 2
"""
Práctica Crear y Escribir Archivos 2
Abre el archivo llamado "mi_archivo.txt", y añade una línea al final del mismo que diga: "Nuevo inicio de sesión".

Imprime el contenido completo de "mi_archivo.txt" al finalizar.

Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura."""

with open('mi_archivo.txt', mode='a', encoding='utf-8') as file:
    
    file.write("Nuevo inicio de sesión")

with open('mi_archivo.txt', mode='r', encoding='utf-8') as file:
    # Lee el contenido del archivo
    contenido = file.read()

    # Imprime el contenido del archivo
    print(contenido)

#__________________________________________________
#Práctica Crear y Escribir Archivos 3
"""
Práctica Crear y Escribir Archivos 3
Utiliza el método writelines para escribir los valores de la siguiente lista al final del archivo "registro.txt" . Inserta un tabulador entre cada elemento de la lista para separarlos.

registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

Imprime el contenido completo de "registro.txt" al finalizar.

Pista: recuerda que el símbolo para concatenar un tabulador en un string es \t. También, deberás cerrar el archivo en modo escritura y volverlo a abrir en modo lectura para poder imprimir su contenido.
"""
# Abre el archivo en modo añadir ('a')
with open('registro.txt', mode='a', encoding='utf-8') as file:
    # Concatena cada elemento de la lista con un tabulador y lo escribe al archivo
    file.writelines([f"{valor}\t" for valor in registro_ultima_sesion])

# Abre el archivo en modo lectura ('r')
with open('registro.txt', mode='r', encoding='utf-8') as file:
    # Lee el contenido del archivo
    contenido = file.read()

    # Imprime el contenido del archivo
    print(contenido)

"""En este código, se utiliza el modo apara abrir el archivo en modo agregar y agregar los valores de la lista registro_ultima_sesional final del mismo. Después de escribir en el archivo, se cierra automáticamente al salir del bloque with. Luego, se vuelve a abrir el archivo en modo lectura y se lee su contenido completo utilizando la función read(). Finalmente, se imprime el contenido del archivo utilizando la función print().

Es importante recordar cerrar el archivo después de escribir en él para liberar los recursos del sistema. Si no se cierra el archivo, puede causar problemas de rendimiento o incluso bloquear el archivo. En este caso, el bloque withse encarga de cerrar el archivo automáticamente después de leerlo.

La función writelines()acepta una lista de cadenas y las escribe una después de la otra en el archivo sin agregar ningún carácter especial entre ellas. Por lo tanto, se utiliza una comprensión de lista para concatenar cada valor de la lista registro_ultima_sesioncon un tabulador \tantes de escribirlo al archivo. Esto garantiza que cada valor se separe correctamente con un tabulador en el archivo.

¿Es útil esta conversación hasta ahora?


"""





