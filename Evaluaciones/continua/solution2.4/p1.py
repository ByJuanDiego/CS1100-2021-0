# Tres opciones
opcion = str(input("Ingrese la opcion (i, j, k): "))

numero_1 = int(input("Ingrese el numero 1: "))
numero_2 = int(input("Ingrese el numero 2: "))
numero_3 = int(input("Ingrese el numero 3: "))
numero_4 = int(input("Ingrese el numero 4: "))
numero_5 = int(input("Ingrese el numero 5: "))

negativos = 0
multiplos_de_5 = 0

if opcion == "i":
    promedio = (numero_5 + numero_4 + numero_3 + numero_2 + numero_1)/5
    print("Respuesta: El promedio es {}".format(promedio))
elif opcion == "j":
    if numero_5 < 0:
        negativos += 1
    if numero_4 < 0:
        negativos += 1
    if numero_3 < 0:
        negativos += 1
    if numero_2 < 0:
        negativos += 1
    if numero_2 < 0:
        negativos += 1
    print("Respuesta: La cantidad de numeros negativos es {}".format(negativos))
elif opcion == "k":
    if numero_1 % 5 == 0:
        multiplos_de_5 += 1
    if numero_2 % 5 == 0:
        multiplos_de_5 += 1
    if numero_3 % 5 == 0:
        multiplos_de_5 += 1
    if numero_4 % 5 == 0:
        multiplos_de_5 += 1
    if numero_5 % 5 == 0:
        multiplos_de_5 += 1
    print("Respuesta: La cantidad de multiplos de 5 es {}".format(multiplos_de_5))
