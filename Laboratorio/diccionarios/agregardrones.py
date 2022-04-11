def addDrone(codigo, nombre, color, tipo):
    # drone ={"codigo": codigo, "nombre":nombre,"color":color, "tipo":tipo }
    drone = {"codigo": codigo, "nombre": nombre, "color": color, "tipo": tipo}
    drones.append(drone)


def getDrone(codigo):  # Obtener información del drone desde código
    buscado = None
    for drone in drones:
        if drone["codigo"] == codigo:
            buscado = drone
            break
    return buscado


def imprimirDrones():
    for i in drones:
        print(i)


drones = []
addDrone("D1", "DJI MINI 2", "GRIS", "AUTONOMO")
addDrone("D2", "DJI Mavic Air 2", "BLANCO", "MULTIRROTOR")
addDrone("D3", "DJI Mavic Mini", "AZUL", "AUTONOMO")
addDrone("D4", "Parrot Anafi", "BLANCO", "AUTONOMO")
addDrone("D5", "DJI PHANTOM 4 ", "BLANCO", "AUTONOMO")
mapa = []


def generarMapa(numfilas, numcols):  # Generando el mapa (el plano) para los drones
    for fila in range(numfilas):
        unafila = ["."] * numcols
        mapa.append(unafila)


def insertDroneMapa(codigo, nfila, ncol):  # Insertando Drone en el mapa
    if getDrone(codigo) is not None:
        mapa[nfila][ncol] = getDrone(codigo)
    else:
        print("No se ha encontrado información dedl código.")


def imprimirMapa(numfilas, numcols):
    for fila in range(numfilas):
        for col in range(numcols):
            if mapa[fila][col] == ".":
                print(mapa[fila][col], end="\t")
            else:
                print(mapa[fila][col]["codigo"], end="\t")
        print()


fils = 10
cols = 10
generarMapa(fils, cols)
imprimirMapa(fils, cols)
insertDroneMapa("D1", 5, 5)
insertDroneMapa("D2", 1, 3)
insertDroneMapa("D3", 3, 7)
insertDroneMapa("D4", 7, 7)
imprimirMapa(fils, cols)
imprimirDrones()
