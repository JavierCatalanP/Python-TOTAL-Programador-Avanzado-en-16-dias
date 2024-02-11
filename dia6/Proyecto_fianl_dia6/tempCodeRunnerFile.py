import os
from pathlib import Path #para las rutas
from os import system #limpiar la pantalla

mi_ruta = Path(Path.home(), "Recetas")

def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1
    return contador


def inicio():
    system('cls')
    print('*' * 50)
    print('*' * 5 + ' Bienvenido a su administrador de Recetas. ' +  '*' * 5)
    print('*' * 50)
    print('\n')
    print(f"Las recetas se encuentren en {mi_ruta} ")
    print(F"Total recetas: {contar_recetas(mi_ruta)}")

    eleccion_menu = 'x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1, 7):
        print("Elige una opción: ")
        print("""
[1] - Leer receta
[2] - Crear  nueva receta
[3] - Crear nueva categoria
[4] - Eliminar receta
[5] - Eliminar categoría
[6] - Salir del programa""")
        eleccion_menu = input()
    return (eleccion_menu)


#Primera Función mostrar categorias:
def mostrar_categorias(ruta):
    print("Categorías:")
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1

    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f"[{contador}]-{carpeta_str}")
        lista_categorias.append(carpeta_str) # lista de categorias se va a alimentar de carpeta categoria
        contadot += 1

    return lista_categorias

#Segunda Función elegir categorías:
def elegir_categoria(lista):
    eleccion_correcta = 'x'

    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista) +1):
        eleccion_correcta = input("\nElije una categorías: ")
    return lista[int(eleccion_correcta)-1]

#Tercera Función mostrar recetas:
def mostrar_recetas(ruta):
    print("Recetas:\n")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1

    for receta in ruta_recetas.glob('*.txt'):
        receta_str = str(receta.name)
        print(f"[{contador}]- {receta_str}")
        lista_recetas.append(receta)
        contador += 1
        return lista_recetas

#Cuarta Función elegir recetas
def elegir_recetas(lista):
    eleccion_receta = 'x'

    while not eleccion_receta.isnumeric() or  int(eleccion_receta) not in range(1, len(lista) + 1):
        eleccion_receta = input('\nElige una receta')
    return lista[int(eleccion_receta)-1]

#Quinta Función Leer una receta
def leer_receta(receta):
    print(Path.read_text(receta))

#Septima Función Crear una receta nueva
def crear_receta(ruta):
    existe = False

    while not existe:
        print("Escribe el nombre de tu receta: ")
        nombre_receta = input() +'.txt'
        print("Escribe tu nueva receta: ")
        contenido_receta = input()
        ruta_nueva = Path(ruta, nombre_receta)

        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f"\n¡La receta {nombre_receta} se ha guardado correctamente!")
            existe = True
        else:
            print("Lo siento, esa receta ya existe")

#Sexta Función Crear una receta nueva
def crear_categoria(ruta):
    existe = False

    while not existe:
        print("Escribe el nombre de la nueva categoría: ")
        nombre_categoria = input() 
        ruta_nueva = Path(ruta, nombre_categoria)

        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f"¡Tu nueva Categoría {nombre_categoria}' se ha creado correctamente!")
            existe = True
        else:
            print("Lo siento, esa categoría ya existe")

#Octava Función eliminar receta
def eliminar_receta(receta):
    Path(receta).unlink()
    print(f"\n¡La receta {receta.name} se ha eliminado correctamente!\n")

#Novena Función eliminar categoría
def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print(f"¡La categoría '{categoria.name}' se han eliminado correctamente!\n")

#Decima Función volver al inicio
def volver_inicio():
    eleccion_regresar = 'x'

    while eleccion_regresar.lower() != 'v':
        eleccion_regresar = input("\nPresione V para volver al menú: ")


finalizar_programa = False

while not finalizar_programa:
    #1.- Menú de inicio
    menu = inicio()
    #1 Realizar arbol de decisiones y Esqueleto del Programa

    if menu == 1:
        #1.1.1.- Mostrar categorías
        mis_categorias =  mostrar_categorias(mi_ruta)

        #1.1.2.- Elegir  una categoria
        mi_categoria = elegir_categoria(mis_categorias)

        #1.1.3.- Mostrar recetas de esa categoría
        mis_recetas = mostrar_recetas(mi_categoria)

        #1.1.4.- Elegir recetas
        mi_receta = elegir_recetas(mis_recetas)

        #1.1.5.- Leer receta
        leer_receta(mi_receta)

        #1.1.6.- Volver al inicio
        volver_inicio()
        pass
    elif menu== 2:
        #1.1.1.- Mostrar categorías
        mis_categorias =  mostrar_categorias(mi_ruta)

        #1.1.2.- Elegir  una categoria
        mi_categoria = elegir_categoria(mis_categorias)    

        #1.2.3.- Crear receta nueva
        crear_receta(mi_categoria) 

        #1.2.4.- Volver inicio
        volver_inicio()
        pass
    elif menu == 3:
        #1.3.1.- Crear categoria
        crear_categoria(mi_ruta)
        #1.3.2.- Volver inicio
        volver_inicio()
        pass
    elif menu == 4:
        #1.1.1.- Mostrar categorías
        mis_categorias =  mostrar_categorias(mi_ruta)

        #1.1.2.- Elegir  una categoria
        mi_categoria = elegir_categoria(mis_categorias)

        #1.4.3.- Mostrar recetas de esa categoría
        mis_recetas = mostrar_recetas(mi_categoria)

        #1.4.4.- Elegir recetas
        mi_receta = elegir_recetas(mis_recetas)

        #1.4.5.- eliminar receta
        eliminar_receta(mi_receta)

        #1.4.6.- Volver al inicio
        volver_inicio()
        pass
    elif menu == 5:
        #1.1.1.- Mostrar categorías
        mis_categorias =  mostrar_categorias(mi_ruta)

        #1.1.2.- Elegir  una categoria
        mi_categoria = elegir_categoria(mis_categorias)

        #1.5.3.- eliminar categoria
        eliminar_categoria(mi_categoria)

        #1.5.4.- Volver al inicio
        volver_inicio()
        pass
    elif menu == 6:
    #1.6.1.- Finalizar el Programa
    finalizar_programa = True
