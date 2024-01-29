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