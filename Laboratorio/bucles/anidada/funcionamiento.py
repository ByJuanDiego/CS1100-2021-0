n = int(input("Ingresa la longitud de lado: "))

for fila in range(n):
    for columna in range(n):
        print("({},{})".format(fila, columna), end="")
    print()
