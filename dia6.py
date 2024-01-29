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