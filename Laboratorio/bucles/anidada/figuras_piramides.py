def piramide(N):
    for fila in range(1, N+1):
        print("* "*fila)
    print()
def piramide_invertida(N):
    count = 0
    for fila in range(1, N+1):
        print("* "*(N-count))
        count += 1
def piramide_invertida_1(N):
    count = 0
    for fila in range(1, N+1):
        print("  "*count + "* "*(N-count))
        count += 1
def piramide_1(N):
    count = 1
    for fila in range(1, N+1):
        print("  "*(N-count) + "* "*count)
        count += 1
def piramide_numeros(N):
    for fila in range(N):
        for columna in range(N):
            if columna <= fila:
                print("{}  ".format(columna+1), end="")
            else:
                print("   ", end="")
        print()
def triangulo_rectangulo(n):
    for fila in range(n):
        for columna in range(n):
            if columna == 0:
                print("{} ".format(fila + 1) + "* ", end="")
            elif (fila == n - 1) or (fila == columna):
                print("* ", end="")
            else:
                print("  ", end="")
        print()
def piramide_binaria(n):
    for fila in range(n):
        for columna in range(n):
            if columna <= fila:
                if (fila % 2 == 0) and (columna % 2 > 0):
                    print("0", end="")
                if (fila % 2 == 0) and (columna % 2 == 0):
                    print("1", end="")
                if (fila % 2 > 0) and (columna % 2 > 0):
                    print("1", end="")
                if (fila % 2 > 0) and (columna % 2 == 0):
                    print("0", end="")

        print()

n = int(input("Ingrese un numero: "))
while n not in [1, 2, 3, 4, 5, 6, 7]:
    n = int(input("Ingrese un numero: "))

if n == 1:
    n = int(input("Ingrese numero: "))
    piramide(n)
if n == 2:
    n = int(input("Ingrese numero: "))
    piramide_invertida(n)
if n == 3:
    n = int(input("Ingrese numero: "))
    piramide_invertida_1(n)
if n == 4:
    n = int(input("Ingrese numero: "))
    piramide_1(n)
if n == 5:
    n = int(input("Ingrese numero: "))
    piramide_numeros(n)
if n == 6:
    n = int(input("Ingrese numero: "))
    triangulo_rectangulo(n)
if n == 7:
    n = int(input("Ingrese numero: "))
    piramide_binaria(n)
