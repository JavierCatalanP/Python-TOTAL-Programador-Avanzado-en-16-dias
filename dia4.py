#Meta día 4
"""
• operadores de comparación
• operadores lógicos
• control de flujo
• loops
• rango
• enumerador
• zip
• random
y más...
"""
#Operadores de comparación
"""
Operadores de Comparación = se obtiene un valor booleano
10 >= 8 // False

(=) asignando algo  

(==) Comparación

"""
mi_bool = 5 + 5 == 10 - 2 + 10 #True   
print(mi_bool)    
mb2 = 'blanco'== 'blanco' #True
print(mb2)
mb3 = 'blanco'== 'negro' #False
print(mb3)
mb4 = 'blanco'== 'Blanco' #True
print(mb4)
mb5 =  'blanco'== 'Blanco'.lower() #True
print(mi_bool)    
print(mb5)
mb6 = 'blanco'.upper() == 'blanCO' # 
print(mb6)
mb7 = 'blanco'.upper() == 'blanco'.upper() #True
print(mb7)
mb8 = '100' == 100 #False
print(mb8)
print9 = 100.0 == 100 #True
print(print9)

#Práctica Operadores de Comparación 1
print('Práctica Operadores de Comparación 1')
print("\n")
"""
Práctica Operadores de Comparación 1
Crea dos variables (num1 y  num2) con los valores 36 y 17 respectivamente. Verifica si num1 es mayor o igual que num2 y almacena el resultado de dicha comparación en una variable llamada mi_bool
"""
#Solución 
num1 = 36
num2 = 17

mi_bool = num1 >= num2
print (mi_bool)

#Práctica Operadores de Comparación 2
print('Práctica Operadores de Comparación 2')
print("\n")
"""

Práctica Operadores de Comparación 2
Crea dos variables (num1 y  num2):

Dentro de num1, almacena el resultado de la operación raíz cuadrada de 25

Dentro de num2, almacena el número 5.

Verifica si num1 es igual a num2 y almacena el resultado de dicha comparación en una variable llamada mi_bool."""

#Solución 
num1 = 25 ** 0.5
num2 = 5

mi_bool = num1 == num2

print(mi_bool)

#Práctica Operadores de Comparación 3
print('Práctica Operadores de Comparación 3')
print("\n")
"""

Práctica Operadores de Comparación 3
Crea dos variables (num1 y  num2):

Dentro de num1, almacena el resultado de la operación 64 x 3

Dentro de num2, almacena el resultado de la operación 24 x 8

Verifica si num1 es diferente a num2 y almacena el resultado de dicha comparación en una variable llamada mi_bool."""
#Solución
num1 = 24 * 8
num2 = 64 * 3

mi_bool = num1 != num2

print(mi_bool)