n = int(input("Ingresa la cantidad de numeros a ingresar: "))
m = 1
mayor = 0
while n != 0:
    num = int(input("Ingresa el numero nro {}: ".format(m)))
    if m == 1:
        mayor = num
    elif num > mayor:
        mayor = num
    n -= 1
    m += 1
print("El mayor numero es: {}".format(mayor))

""" n = (1, 5, 6, 7, 8, 9, 10)
count = 0
mayor = 0
while count != len(n):

    if n[count] > mayor:
        mayor = n[count]
    count += 1
print("El mayor numero es: {}".format(mayor)) """
