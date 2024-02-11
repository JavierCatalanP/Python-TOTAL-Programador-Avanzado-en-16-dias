"""Proyecto del Día 6
Llegó el momento de poner todo lo que hemos aprendido en un proyecto del mundo real. Y el
de hoy sí que nos va a tomar tiempo, porque a pesar de ser relativamente simple, implica mucho
código, muchas funciones y es imprescindible llevar una especie de orden mental de lo que
necesitas hacer. Hoy vas a crear un administrador de recetas. Básicamente esto es un programa
a través del cual un usuario puede leer, crear y eliminar recetas que se encuentren en una base
de datos.
Entonces, antes de comenzar, es necesario que crees en tu ordenador un directorio en la carpeta
base de tu ordenador, con una carpeta llamada Recetas, que contiene cuatro carpetas y cada
una de ellas contiene dos archivos de texto. Dentro de los archivos puedes escribir lo que
quieras, puede ser la receta en sí misma o no, pero eso no es importante para este ejercicio. Lo
importante es que escribas algo para poder leerlas cuando haga falta o, si prefieres, también
puedes directamente descargar y descomprimir el archivo adjunto a esta elección y ubicarlo en
tu directorio raíz si no tienes ganas de crearlo tú mismo.
Aquí viene la consigna: tu código le va a dar primero la bienvenida al usuario, le va a informar
la ruta de acceso al directorio donde se encuentra nuestra carpeta de recetas, le va a informar
cuántas recetas hay en total dentro de esa carpeta, y luego le va a pedir que elija una de
estas opciones que tenemos aquí:
1. La opción 1 le va a preguntar qué categoría elige (carnes, ensaladas, etc.), y una vez que
el usuario elija una, le va a preguntar qué receta quiere leer, y mostrar su contenido.
2. En la opción 2 también se le va a hacer elegir una categoría, pero luego le va a pedir que
escriba el nombre y el contenido de la nueva receta que quiere crear, y el programa va
a crear ese archivo en el lugar correcto.
3. La opción 3 le va a preguntar el nombre de la categoría que quiere crear y va a generar
una carpeta nueva con ese nombre.
4. La opción 4, hará todo lo mismo que la opción uno, pero en vez de leer la receta, la va
a eliminar
5. La opción 5, le va a preguntar qué categoría quiere eliminar
6. Finalmente, la opción 6 simplemente va a finalizar la ejecución del código.
Este programa tiene algunas cuestiones importantes a considerar:
 Cada vez que el usuario realice exitosamente cualquiera de sus opciones, el programa le
va a pedir que presione alguna letra para poder volver al inicio, por lo que el código se 
va a repetir una y otra vez, hasta que el usuario elija la opción 6. Esto implica que todo
el menú debe estar dentro de un loop while que se repita una y otra vez hasta que no se
cumpla la condición de que la elección del usuario sea 6
 Sería genial que cada vez que el usuario vuelva al menú inicial, la consola limpie la
pantalla para que no se acumulen las ejecuciones anteriores. Recuerda que cuentas con
system para poder reiniciar la pantalla y comenzar a mostrar todo desde cero.
 Si bien te he enseñado muchos métodos para administrar archivos, para este ejercicio
vas a necesitar algunos que aún no has visto, pero que están incluidos en los objetos con
los que hemos estado trabajando, por lo que en ocasiones deberás buscar entre los
métodos que trae Path, por ejemplo, leer la documentación y aprender a implementarlo.
Yo sé que sería mucho más fácil que yo te enseñe todo acerca de cada uno de los
métodos, pero recuerda que también es importante que a medida que avanzamos vayas
aprendiendo a gestionar tu propio aprendizaje. Es parte de la vida real y cotidiana del
programador en el mundo en que vivimos.
 Utiliza muchas funciones, todas las que creas necesario. Las funciones ayudan a
compartir, mentalizar el código y hacerlo mucho más dinámico, ordenado, repetible y
más fácil de mantener.
 Recuerda comenzar con un diagrama de flujos o un gráfico hecho a mano que te permita
visualizar con más facilidad el árbol de decisiones que necesitas ejecutar en tu código.
Sin eso te vas a enredar más rápido de lo que crees y se te va a complicar bastante.
 Y, por último, no te frustres si no logras hacerlo o completarlo. Si logras hacer una parte,
un par de funciones, algunas cosas sí y otras no, está muy bien. Siempre estamos
aprendiendo y parte de aprender es no saber.
Mis desafíos siempre te van a estar ubicando en el borde de tus capacidades, sacándote del
lugar de confort para que tu cerebro tenga que desconcertarse y descubrir cómo hacer algo
nuevo. Tu avanza hasta donde puedas."""

"""Crear esta estructura de carpeta y archivos en tu ordenador:

Recetas/Carnes/Etrecotal Malbec.txt
Recetas/Carnes/Matambre a la Pizza.

Recetas/Ensaladas/Ensalada Griega.txt
Recetas/Ensaladas/Ensalada Mediterranea.txt

Recetas/Pastas/Canelones de Espinaca.txt
Recetas/Pastas/Rivalores de Ricotta.txt


Recetas/Postres/Compota de Manzana.txt
Recetas/Postres/Tartara de Frambuesa.txt

[1] Leer receta
[2] Crear receta
[3] Crear categoría
[4] Eliminar receta
[5] Eliminar categoría
[6] Finalizar programa

Opción [6] Finalizar código

- Todo el menu debe estar dentro de un loop while ('envolver' el código en un loop while)
- Usar system('cls') o ('clear') para limpiar la consola
- Buscar en la documentación más métodos  y funciones que puedes usar (son muchos).
- Compartimenta el código en muchas funciones
- Realiza un gráfico con el flujo del programa (diagrama de flujo)
- Lograrlo es opcional, ¡Intentarlo no!
""" 

""" 
[1] Leer receta
[2] Crear receta
[3] Crear categoría
[4] Eliminar receta
[5] Eliminar categoría
[6] Finalizar programa

Opción [6] Finalizar código

- Todo el menu debe estar dentro de un loop while ('envolver' el código en un loop while)
- Usar system('cls') o ('clear') para limpiar la consola
- Buscar en la documentación más métodos  y funciones que puedes usar (son muchos).
- Compartimenta el código en muchas funciones
- Realiza un gráfico con el flujo del programa (diagrama de flujo)
- Lograrlo es opcional, ¡Intentarlo no!

"""
#Importar Módulos
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
