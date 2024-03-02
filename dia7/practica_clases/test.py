import os

# Especifica la ruta del directorio que deseas listar.
ruta = 'F:/SAC/JAVIER CATALAN/02.- Costos/Pagos/Doc_pendientes'

# Lista los contenidos del directorio especificado.
contenido = os.listdir(ruta)

# Imprime los contenidos.
for item in contenido:
    print(item)
    
    
    #----------------------------------------------
#Si deseas filtrar la lista para mostrar solo los directorios, puedes usar la función filter()junto con os.path.isdirpara filtrar los elementos que son directorios. Aquí tienes cómo hacerlo:

import os

# Especifica la ruta del directorio que deseas listar.
ruta = '/ruta/al/directorio'

# Filtra los contenidos para mostrar solo los directorios.
directorios = list(filter(os.path.isdir, os.listdir(ruta)))

# Imprime los directorios.
for directorio in directorios:
    print(directorio)