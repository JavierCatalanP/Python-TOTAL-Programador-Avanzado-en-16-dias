class  Pajaro: #Clase basica
    pass       #Sin contenidos

mi_pajaro = Pajaro()  #Objeto 1
otro_pajaro= Pajaro()  #Objeto 2


print(mi_pajaro)
print(otro_pajaro)
print(type(mi_pajaro))

print(f"¿Es el mismo objeto? {mi_pajaro is otro_pajaro}:")   #False, son dos instancias diferentes. 
print(f"\n¿Están relacionados? {mi_pajaro == otro_pajaro}:")#True, comparten la misma clase y atributos.
