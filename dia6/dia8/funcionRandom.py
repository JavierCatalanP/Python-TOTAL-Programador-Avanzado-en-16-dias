import random

def imprimir_numeros_aleatorios():
    num1 = int(input("Por favor, introduce el primer número: "))
    num2 = int(input("Por favor, introduce el segundo número: "))

    if num1 > num2:
        num1, num2 = num2, num1

    cantidad = int(input("Por favor, introduce la cantidad de números aleatorios a imprimir: "))
    for _ in range(cantidad):
        print(random.randint(num1, num2))

imprimir_numeros_aleatorios()
