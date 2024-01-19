# En Python a partir de la versión 3.10 se puede hacer un "match" = coincidencia de patrones. esto es muy útil para hacer menos ifs y más legible el código. 
# mach elige una opción entre varias opciones y ejecuta la primera que coincida.
# Ejemplo:
x = int(input("Ingrese un número: "))
match x:
    case 0:
        print("x es 0")
    case 1:
        print("x es 1")
    case 2:
        print("x es 2")
    case 3:
        print("x es 3")
    case 4:
        print("x es 4")
    case 5:
        print("x es 5")
    case 6:
        print("x es 6")
    case 7:
        print("x es 7")
    case 8:
        print("x es 8")
    case 9:
        print("x es 9")
    case 10:
        print("x es 10")
    case _:
        print("x es mayor que 10")

# Ejemplo 2:
#Sin embargo, en Python no hay un switch, sino que hay que usar match.
# match es una forma de hacer un switch en Python.

print("\n")
#Sin Match:
serie = "N-02"

if serie == "N-01":
    print("Samsung")
elif serie == "N-02":
    print("Nokia")
elif serie == "N-03":
    print("LG")
elif serie == "N-04":
    print("Motorola")
else:
    print("No existe ese producto")

print("\n")
#Con Match:
serie = "N-02"

match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("LG")
    case "N-04":
        print("Motorola")
    case _:    
        print("No existe ese producto")

print("\n")
# Ejemplo 3:
cliente = {'nombre': 'Federico',
           'edad': 45,
           'ocupacion': 'instructor'}

pelicula = {'titulo': 'Matrix', 
            'ficha_tecnica': {'protagonista': 'Keanu reeves',
                              'director': 'Lana y Lilly Wachowski'}}

elementos = [cliente, pelicula, 'libro']

for e in elementos:
    match e:
        case {'nombre': nombre,
              'edad': edad,
              'ocupacion': ocupacion}:
            print("Es un cliente")
            print (nombre, edad, ocupacion)
        case {'titulo': titulo,
              'ficha_tecnica': {'protagonista': protagonista,
                                'director': director}}:
            print("Es una pelicula")
            print(titulo, protagonista, director)
        case _:# Dejar por defeco el caso por si no se encuentra nada
             print("No se que es esto") #si no es ninguna de las anteriores, se ejecuta el default.

