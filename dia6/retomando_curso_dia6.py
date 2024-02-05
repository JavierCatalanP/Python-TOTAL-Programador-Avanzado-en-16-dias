#_________________________________________________________
    #Metodo
#_________________________________________________________

# Solicitar Nombre y Edad al Usuario
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")

# Limpiar Pantalla (Este método puede variar según el entorno de ejecución)
# En este ejemplo, se utiliza el atajo Ctrl + L en la consola de Python.
# Ten en cuenta que en otros entornos la forma de limpiar pantalla puede ser diferente.
print("\033c")

# Mostrar el Resultado
print(f"¡Hola, {nombre}, Tienes {edad} años.")

#_________________________________________________________
    #System
#_________________________________________________________
from os import system
nombre=input("Dime tu nombre: ")
edad=input("Dime tu edad: ")
system ('cls')
print (f"Tu nombre es {nombre} y tienes {edad} años")

#_________________________________________________________
    #Práctica Archivos y Funciones 1
#_________________________________________________________

"""Crea una función llamada abrir_leer() que abra (open) un archivo indicado como parámetro, y devuelva su contenido (read)."""

def abrir_leer(ruta_archivo):
    try:
        with open(ruta_archivo, 'r') as archivo:
            contenido = archivo.read()
            return contenido
    except FileNotFoundError:
        return f"El archivo {ruta_archivo} no fue encontrado."
    except Exception as e:
        return f"Ocurrió un error al abrir y leer el archivo: {e}"

# Ejemplo de uso
ruta_del_archivo = "ruta/del/archivo.txt"  # Reemplaza con la ruta y nombre de tu archivo
resultado = abrir_leer(ruta_del_archivo)

print(resultado)

"""Explicación del código:

Explicación detallada:

1.- def abrir_leer(ruta_archivo):' : Define la función abrir_leer que toma la ruta del archivo como parámetro.

2.- try:' : Inicia un bloque try que contiene el código propenso a errores.

3.- with open(ruta_archivo, 'r') as archivo: ': Utiliza la declaración with para abrir el archivo en modo lectura ('r'). Esto garantiza que el archivo se cierre correctamente después de su uso.

4.- contenido = archivo.read(): Lee el contenido del archivo y lo almacena en la variable contenido.

5.- return contenido: Retorna el contenido del archivo.

6.- except FileNotFoundError:' : Captura la excepción específica FileNotFoundError que ocurre cuando el archivo no se encuentra. Retorna un mensaje indicando que el archivo no fue encontrado.

7.- except Exception as e:' : Captura cualquier otra excepción no anticipada. Retorna un mensaje indicando que ocurrió un error al abrir y leer el archivo, mostrando detalles específicos del error.

8.- Ejemplo de uso: Se proporciona una ruta de archivo de ejemplo ruta_del_archivo y se llama a la función abrir_leer con esa ruta. El resultado se almacena en la variable resultado.

9.- print(resultado): Imprime el resultado, que es el contenido del archivo o un mensaje de error en caso de problemas.
"""

#Modo simple
def abrir_leer(archivo):
    archivo = open(archivo)
    return archivo.read()
#_________________________________________________________
    #Práctica Archivos y Funciones 2
#_________________________________________________________
"""
Crea una función llamada sobrescribir() que abra (open) un archivo indicado como parámetro, y sobrescriba cualquier contenido anterior por el texto "contenido eliminado"""
def sobrescribir(ruta_archivo):
    try:
        # Abre el archivo en modo escritura ('w') para sobrescribir el contenido
        with open(ruta_archivo, 'w') as archivo:
            # Sobrescribe el contenido del archivo con el texto "contenido eliminado"
            archivo.write("contenido eliminado")
        return f"El archivo {ruta_archivo} ha sido sobrescrito con éxito."
    except FileNotFoundError:
        # Captura la excepción si el archivo no se encuentra
        return f"El archivo {ruta_archivo} no fue encontrado."
    except Exception as e:
        # Captura cualquier otra excepción no anticipada
        return f"Ocurrió un error al sobrescribir el archivo: {e}"

# Ejemplo de uso
ruta_del_archivo = "ruta/del/archivo.txt"  # Reemplaza con la ruta y nombre de tu archivo
resultado = sobrescribir(ruta_del_archivo)

print(resultado)

"""
Explicación detallada:

1.- def sobrescribir(ruta_archivo):' : Define la función sobrescribir que toma la ruta del archivo como parámetro.

2.- try:' : Inicia un bloque try que contiene el código propenso a errores.

3.- with open(ruta_archivo, 'w') as archivo:' : Utiliza la declaración with para abrir el archivo en modo escritura ('w'). Esto garantiza que el archivo se cierre correctamente después de su uso.

4.- archivo.write("contenido eliminado"): Sobrescribe el contenido del archivo con el texto "contenido eliminado".

5.- return f"El archivo {ruta_archivo} ha sido sobrescrito con éxito.": Retorna un mensaje indicando que la operación de sobrescritura fue exitosa.

6.- except FileNotFoundError:' : Captura la excepción específica FileNotFoundError que ocurre cuando el archivo no se encuentra. Retorna un mensaje indicando que el archivo no fue encontrado.

7.- except Exception as e:' : Captura cualquier otra excepción no anticipada. Retorna un mensaje indicando que ocurrió un error al sobrescribir el archivo, mostrando detalles específicos del error.

8.- Ejemplo de uso: Se proporciona una ruta de archivo de ejemplo ruta_del_archivo y se llama a la función sobrescribir con esa ruta. El resultado se almacena en la variable resultado.

9.-print(resultado): Imprime el resultado, que es un mensaje indicando el éxito o cualquier error durante la operación."""

#Modo simple
def sobrescribir(archivo):
    archivo_sobrescribir = open(archivo, "w")
    archivo_sobrescribir.write("contenido eliminado")
#_________________________________________________________
    #Práctica Archivos y Funciones 3
#_________________________________________________________
"""
Crea una función llamada registro_error() que abra (open) un archivo indicado como parámetro, y lo actualice añadiendo una línea al final que indique "se ha registrado un error de ejecución". Finalmente, debe cerrar el archivo abierto.
"""
def registro_error(ruta_archivo):
    try:
        # Abre el archivo en modo adjunto ('a') para agregar contenido al final
        with open(ruta_archivo, 'a') as archivo:
            # Añade una línea al final indicando que se ha registrado un error de ejecución
            archivo.write("Se ha registrado un error de ejecución\n")
        return f"Registro de error exitoso en el archivo {ruta_archivo}."
    except FileNotFoundError:
        # Captura la excepción si el archivo no se encuentra
        return f"El archivo {ruta_archivo} no fue encontrado."
    except Exception as e:
        # Captura cualquier otra excepción no anticipada
        return f"Ocurrió un error al registrar el error: {e}"

# Ejemplo de uso
ruta_del_archivo = "ruta/del/archivo.txt"  # Reemplaza con la ruta y nombre de tu archivo
resultado = registro_error(ruta_del_archivo)

print(resultado)

"""
Explicación detallada:

1.- def registro_error(ruta_archivo):' : Define la función registro_error que toma la ruta del archivo como parámetro.

2.- try:: Inicia un bloque try que contiene el código propenso a errores.

3.- with open(ruta_archivo, 'a') as archivo:' : Utiliza la declaración with para abrir el archivo en modo adjunto ('a'). Esto garantiza que el archivo se cierre correctamente después de su uso.

4.- archivo.write("Se ha registrado un error de ejecución\n"): Añade una línea al final del archivo indicando que se ha registrado un error de ejecución.

5.- return f"Registro de error exitoso en el archivo {ruta_archivo}.": Retorna un mensaje indicando que el registro de error fue exitoso.

6.- except FileNotFoundError:' : Captura la excepción específica FileNotFoundError que ocurre cuando el archivo no se encuentra. Retorna un mensaje indicando que el archivo no fue encontrado.

7.- except Exception as e:' : Captura cualquier otra excepción no anticipada. Retorna un mensaje indicando que ocurrió un error al registrar el error, mostrando detalles específicos del error.

8.- Ejemplo de uso: Se proporciona una ruta de archivo de ejemplo ruta_del_archivo y se llama a la función registro_error con esa ruta. El resultado se almacena en la variable resultado.

9.- print(resultado): Imprime el resultado, que es un mensaje indicando el éxito o cualquier error durante la operación.
"""

#Modo simple
def registro_error(archivo):
    mi_archivo = open(archivo, "a")
    mi_archivo.write("se ha registrado un error de ejecución")
    mi_archivo.close()


#_________________________________________________________
    #Cuestionario Día 6
#_________________________________________________________
#Pregunta 1: El método write(ruta_archivo, "a") permite escribir nuevas líneas a continuación de la última que se encuentre en el archivo abierto.
#Respuesta: Falso

#Pregunta 2: ¿Qué método de os utilizarías si deseas crear una carpeta o serie de carpetas en una ruta determinada?
#Respuesta: os.makedir(ruta)

# Pregunta 3: Investiga la documentación de pathlib referida a la propiedad parents, y elige entre las siguientes opciones cuál sería la salida correcta del siguiente código, almacenada en la variable carpeta, dado que se ejecuta en Windows:
#ruta = Path('C:/Users/Usuarui/Desktop/Curso Python' / 'Cuestionario Día6' / 'Pregunta 1'
#Respuesta: C:\Users\Usuario
    
#Pregunta 4: ¿Qué es, para la clase Path, la propiedad stem aplicada sobre una ruta?
#Respuesta: El nombre o componente final de la ruta, sin su sufijo (extensión).
    
#Pregunta 5: ¿Cuál parámetro de os.system debemos utilizar para limpiar la consola en Windows?
    #Respuesta: "cls"