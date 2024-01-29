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

















