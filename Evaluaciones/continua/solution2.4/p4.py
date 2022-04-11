# Rombo
from math import ceil

# Variables

n = int(input("Ingresa un numero: "))
while n < 7:
    n = int(input("Ingresa un numero: "))
if n % 2 == 0:
    n -= 1

centro = ceil(n / 2)
count1 = 2
count2 = centro
count1_2 = 3
count2_2 = centro + 1
count1_3 = centro + 1
count2_3 = 3
count1_4 = centro + 1
count2_4 = n - 2

for fila in range(1, n + 1):
    for columna in range(1, n + 1):
        # Para imprimir los numeros:
        if columna == 1:
            if fila < 10:
                print("{}   ".format(fila), end="")
            elif fila >= 10:
                print("{}  ".format(fila), end="")
        # Para imprimir el borde:
        if (fila == 1) or (fila == n) or (columna == 1) or (columna == n):
            print("*", end="")
        # Para imprimir el lado superior izquierdo del rombo:
        elif (fila == count1) and (columna == count2):
            count1 += 1
            count2 -= 1
            print("*", end="")
        # Para imprimir el lado superior derecho del rombo:
        elif (fila == count1_2) and (columna == count2_2):
            count1_2 += 1
            count2_2 += 1
            print("*", end="")
        # Para imprimir el lado inferior izquierdo del rombo:
        elif (fila == count1_3) and (columna == count2_3):
            count1_3 += 1
            count2_3 += 1
            print("*", end="")
        # Para imprimir el lado superior derecho del rombo:
        elif (fila == count1_4) and (columna == count2_4):
            count1_4 += 1
            count2_4 -= 1
            print("*", end="")
        # Para imprimir los espacios en blanco
        else:
            print(" ", end="")
    # Para saltar a la siguiente fila
    print()
