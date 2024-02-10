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


inicio()