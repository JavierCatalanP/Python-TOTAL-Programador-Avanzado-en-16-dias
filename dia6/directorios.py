# Importamos la función open()
from os import Path

# Ruta del archivo
ruta = "C:\\Users\\encatalan\\Downloads\\p1.txt"

# Verificamos si el archivo existe
if path.exists(ruta):
    # Abrimos el archivo en modo lectura
    with open(ruta, 'r') as archivo:
        # Leemos el contenido del archivo
        contenido = archivo.read()

    # Imprimimos el contenido del archivo
    print(contenido)

else:
    print("El archivo no existe.")

#_________________________________________________________
#Crear una carpeta
# Importamos la función makedirs()
from os import makedirs, path

# Ruta del archivo
ruta = "C:\\Users\\encatalan\\Downloads\\p1.txt"

# Obtenemos la ruta de la carpeta contenedora del archivo
ruta_carpeta = path.dirname(ruta)

# Ruta de la nueva carpeta
nueva_ruta = path.join(ruta_carpeta, "nueva_carpeta")

# Creamos la nueva carpeta
makedirs(nueva_ruta, exist_ok=True)

# Imprimimos la ruta de la nueva carpeta
print(nueva_ruta)

#_________________________________________________________
# Ruta del archivo
import os
ruta = "C:\\Users\\encatalan\\Downloads\\p1.txt"
elementos = os.path.split(ruta)
print(elementos)

#_________________________________________________________
# Eliminar carpeta
import os
os.rmdir("C:\\Users\\encatalan\\Downloads\\nueva_carpeta")

#_________________________________________________________
# Leer un archivo
import os
leer_archivo = open("C:\\Users\\encatalan\\Downloads\\p1.txt")
print(leer_archivo.read())

#_________________________________________________________
#Con otro metodo para cualquier sistema operativo FORMA 1

from pathlib import Path

carpeta = Path("C:/Users/encatalan/Downloads")
archivo = carpeta / 'p1.txt'

mi_archivo = open(archivo)
print(mi_archivo.read())

#_________________________________________________________
#Con otro metodo para cualquier sistema operativo FORMA 2

from pathlib import Path

carpeta = Path("/Users/encatalan/Downloads") / 'p1.txt' #Ahorro 1 linea de codigo

mi_archivo = open(carpeta)
print(mi_archivo.read())


#_________________________________________________________
# Agilizar la lectura con pathlib
#_________________________________________________________
from pathlib import Path
#No necesitamos abrir y cerrar el archivo (open and close)
carpeta = Path("/Users/encatalan/Downloads/p1.txt")
print(carpeta.read_text())

#_________________________________________________________
#Nombre del archivo
#_________________________________________________________
from pathlib import Path
#No necesitamos abrir y cerrar el archivo (open and close)
carpeta = Path("/Users/encatalan/Downloads/p1.txt")
print(carpeta.name)

#_________________________________________________________
#Función sufijo donde nos enseña la extensión
#_________________________________________________________
from pathlib import Path
#No necesitamos abrir y cerrar el archivo (open and close)
carpeta = Path("/Users/encatalan/Downloads/p1.txt")
print(carpeta.suffix)

#_________________________________________________________
#Nombre sin la terminación o extensión
#_________________________________________________________
from pathlib import Path
#No necesitamos abrir y cerrar el archivo (open and close)
carpeta = Path("/Users/encatalan/Downloads/p1.txt")
print(carpeta.stem)

#_________________________________________________________
#Comprobar si el archivo existe
#_________________________________________________________
from pathlib import Path
#No necesitamos abrir y cerrar el archivo (open and close)
carpeta = Path("/Users/encatalan/Downloads/p2.txt")

if not carpeta.exists():
    print("Este archivo no existe")
else:
    print("Genial, existe")
    

#_________________________________________________________
#Transformar cualquier ruta a una ruta de windows
#_________________________________________________________
from pathlib import Path, PureWindowsPath
#No necesitamos abrir y cerrar el archivo (open and close)
carpeta = Path("/Users/encatalan/Downloads/p1.txt")

ruta_windows = PureWindowsPath(carpeta)
print(ruta_windows)
    

#Cuestionario sobre Pathlib
"""
Pregunta 1:
¿Cuál de las siguientes es una ventaja del módulo Pathlib?

- Acceso a una semántica más sencilla
- Flexibilidad en el manejo de directorios para Windows y Mac
- Acceso a nuevos métodos y propiedades de directorios
- Todas son correctas *

Pregunta 2:
¿Qué contendrá la variable ruta, luego de ejecutarse el código?
ruta = PureWindowsPath("C:/Users/Usuario/Desktop")

- C:/User/Usuario/Desktop
- C:\User\Usuario\Desktop *
- C:\\User\\Usuario\\Desktop

Pregunta 3:
¿Cuál de las siguientes propiedades utilizarías para verificar la extensión de un archivo?
- name
- suffix *
- stem  
- extension
"""
#_________________________________________________________
#Transformar cualquier ruta a una ruta de windows
#_________________________________________________________