def EsTriangular(n):
    r = (8 * n + 1) ** (1 / 2)
    if r - int(r) > 0:  # Si es triangular esta resta deberia dar 0
        return False
    else:
        return True


def ObtenerAnhioAsiento(n):
    global asientos
    global anhio

    n = str(n)
    ultimoDigito, penultimoDigito, antepenultimoDigito = int(n[-1]), int(n[-2]), int(n[-3])
    asientos = ultimoDigito + penultimoDigito + antepenultimoDigito
    anhio = 9 * 224 + (ultimoDigito - 1)


def ValidaSoat(placa, asiento):
    placa = str(placa)
    sumatoria = 0
    count = 0

    while count < len(placa):
        sumatoria += int(placa[count])
        count += 1

    if EsTriangular(sumatoria) and (5 <= asiento <= 24):
        return True
    else:
        return False


def ValidaCitv(placa, anhio):
    if EsTriangular(placa) and EsTriangular(anhio):
        return True
    else:
        return False


placa = int(input("input: "))
while not (len(str(placa)) == 4):  # Bucle de restriccion
    placa = int(input("input: "))

asientos = 0
anhio = 0

ObtenerAnhioAsiento(placa)  # Esta funcion cambia los valores de asiento y año globalmente

if ValidaSoat(placa, asientos) and ValidaCitv(placa, anhio):
    print("output: cumple")
else:
    print("output: no cumple")
