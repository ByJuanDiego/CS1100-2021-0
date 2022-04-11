def cuadrado_de_caracter(N):
    caracter = str(input("Ingrese el caracter del cuadrado: "))
    if "a.a" <= caracter <= "z":
        for i in range(N):
            for j in range(1, (N + 1)):
                print(caracter, " ", end="")
            print()
    elif "A" <= caracter <= "Z":
        for i in range(N):
            for j in range(1, (N + 1)):
                print(caracter + "*", end="")
            print()
    else:
        for i in range(N):
            for j in range(1, (n + 1)):
                print(caracter + "x", end="")
            print()


def cuadrado_con_x(N):
    count = 1
    for fila in range(1, N + 1):
        for columna in range(1, N + 1):

            if (columna == 1) or (columna == N) or (fila == 1) or (fila == N):
                print("*  ", end="")

            elif (fila == count + 1) and (columna == N - count):
                print("*  ", end="")
                count += 1

            elif columna == fila:
                print("*  ", end="")

            else:
                print("   ", end="")
        print()


def cuadrado_numeros(n):
    for fila in range(n):
        for columna in range(n):
            if fila == 0 or fila == n - 1:
                print(fila + 1, end="")
            elif columna == 0 or columna == n - 1:
                print(fila + 1, end="")
            else:
                print(" ", end="")
        print()


n = int(input("Ingrese un numero: "))
while n not in [1, 2, 3]:
    n = int(input("Ingrese un numero: "))

if n == 1:
    n = int(input("Ingrese el lado del cuadrado: "))
    cuadrado_de_caracter(n)
if n == 2:
    n = int(input("Ingrese numero: "))
    cuadrado_con_x(n)
if n == 3:
    n = int(input("Ingrese numero: "))
    cuadrado_numeros(n)
