lado = int(input("Ingrese un numero: "))

for ancho in range(lado):
    for alto in range(lado):
        if alto != ancho:
            print("*", end="")
        else:
            print("  ", end="")

    print()
