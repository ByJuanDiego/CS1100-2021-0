def rectangulo(ancho, alto):
    for fila in range(alto):
        for columna in range(ancho):
            if fila == 0 or fila == alto-1 or columna == 0 or columna == ancho-1:
                print(" * ", end="")
            else:
                print(" - ", end="")
        print()

ancho = int(input("Ingrese el ancho de la figura: "))
alto = int(input("Ingrese el alto de la figura: "))

rectangulo(ancho, alto)
