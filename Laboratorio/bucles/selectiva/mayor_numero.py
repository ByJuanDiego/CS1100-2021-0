n1 = int(input("Ingresa el 1er numero: "))
n2 = int(input("Ingresa el 2do numero: "))
n3 = int(input("Ingresa el 3er numero: "))
n4 = int(input("Ingresa el 4to numero: "))

mayor = n1
if n2 > mayor:
    mayor = n2
if n3 > mayor:
    mayor = n3
if n4 > mayor:
    mayor = n4

print("El mayor numero es: {}".format(mayor))
