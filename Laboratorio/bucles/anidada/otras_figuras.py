def reloj_arena(n):
    count = 1
    for fila in range(1, n + 1):
        for columna in range(1, n + 1):
            if fila == 1:
                print("* ", end="")
            elif fila == n:
                print("* ", end="")
            elif (fila == count + 1) and (columna == n - count):
                print("* ", end="")
                count += 1
            elif fila == columna:
                print("* ", end="")
            else:
                print("  ", end="")

        print()


def zeta(n):
    count = 1
    for fila in range(1, n + 1):
        for columna in range(1, n + 1):
            if (fila == 1) or (fila == n):
                print("* ", end="")
            elif (fila == count + 1) and (columna == n - count):
                print("* ", end="")
                count += 1
            else:
                print("  ", end="")
        print()


def zeta_invertida(n):
    for fila in range(1, n + 1):
        for columna in range(1, n + 1):
            if (fila == 1) or (fila == n):
                print("* ", end="")
            elif fila == columna:
                print("* ", end="")
            else:
                print("  ", end="")
        print()


def tres_lineas(n):
    for fila in range(1, n + 1):
        for columna in range(1, n + 1):
            if (fila == 1) or (columna == 1) or (fila == columna):
                print("*  ", end="")
            else:
                print("   ", end="")
        print()


n = int(input("Ingresa un numero: "))
while n not in [1, 2, 3, 4]:
    n = int(input("Ingresa un numero: "))
if n == 1:
    n = int(input("Ingrese numero: "))
    reloj_arena(n)
if n == 2:
    n = int(input("Ingrese numero: "))
    zeta(n)
if n == 3:
    n = int(input("Ingrese numero: "))
    zeta_invertida(n)
if n == 4:
    n = int(input("Ingrese numero: "))
    tres_lineas(n)
