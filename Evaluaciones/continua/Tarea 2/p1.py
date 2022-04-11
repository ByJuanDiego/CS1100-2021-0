# Piramide
def imprimirPiramide():
    global n

    count = 1
    triangular = 1
    count2 = 2

    for ladrillo in range(1, n+1):
        if ladrillo == triangular:
            print("+ "*count)
            triangular += count2 + count
            count += count2
            count2 += 1

def CalcularAltura():
    global n

    count = 1
    triangular = 1
    count2 = 2
    ladrillos_usados = 0
    altura = 0

    for ladrillo in range(1, n+1):
        if ladrillo == triangular:
            ladrillos_usados += count
            altura += 1
            triangular += count2 + count
            count += count2
            count2 += 1

    sobrantes = n - ladrillos_usados
    print("La altura es: {}".format(altura))
    print("Cubos sobrantes: {}".format(sobrantes))

n = int(input("Input: "))
while not (1 <= n <= 500):    # Bucle de restriccion
    n = int(input("Input: "))

imprimirPiramide()
CalcularAltura()
