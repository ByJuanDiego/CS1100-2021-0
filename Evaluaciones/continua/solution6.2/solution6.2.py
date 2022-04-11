import time
import random
import json

def cargar():
    with open("minidic.json", "r") as file:
        dict = json.load(file)
        return dict

def limpiarContenido(dic):
    dic.clear()
    return dic

def agrerarDatos(tiempo, temperatura, dic):
    dic[tiempo] = temperatura

def guardar(dict):
    with open("minidic.json", "w") as file:
        json.dump(dict, file, indent=4, sort_keys=True)

def encontrarMayor(dict):
    maxTemp, hora = 0, ''

    for temperatura in dict.values():
        if temperatura > maxTemp:
            maxTemp = temperatura
    for tiempo in dict.keys():
        if dict[tiempo] == maxTemp:
            hora = tiempo
    return maxTemp, hora

def sensorTemp():

    seg = 0
    min = 0
    hora = 0
    print("El valor ingresado de horas puede ser 0")
    horaFinal = int(input("Ingrese las horas que el sensor contará   [0-24]: "))
    print("\nEl valor ingresado de minutos puede ser 0")
    minFinal = int(input("Ingrese los minutos que el sensor contará  [0-59]: "))
    print("\nEl valor ingresado de segundos debe ser: 0 < S, y S <= 59")
    segFinal = int(input("Ingrese los segundos que el sensor contará [1-59]: "))
    print()

    data = cargar()
    data = limpiarContenido(data)

    while True:
        temp = random.randrange(0, 101, 2)
        valor = "Tiempo: {}:{}:{} => °C: {}".format(str(hora), str(min), str(seg), str(temp))
        print(valor)
        agrerarDatos('{}:{}:{}'.format(str(hora), str(min), str(seg)), temp, data)

        if hora == horaFinal and min == minFinal and seg == segFinal:  # se rompe el bucle cuando alcanza la hora ingresada
            break

        else:
            seg += 1
            if seg == 60:
                seg = 0
                min += 1
            if min == 60:
                seg = 0
                min = 0
                hora += 1
            time.sleep(1)

    guardar(data)
    with open("minidic.json", "r") as file:
        data = json.load(file)

    maxTemp1, hora1 = encontrarMayor(data)
    print("\nLa mayor temperatura N˚1 fue {} y se consiguió a la hora {}".format(maxTemp1, hora1))
    del data[hora1]         # elimina la mayor temperatura para poder buscar la segunda mayor
    maxTemp2, hora2 = encontrarMayor(data)
    print("La mayor temperatura N˚2 fue {} y se consiguió a la hora {}".format(maxTemp2, hora2))
    data[hora1] = maxTemp1  # devolvemos la mayor temperatura que habia sido eliminada

    if maxTemp1 == maxTemp2: print("\nEs un empate!")
    else: print("\nNo hubo empate!")
    guardar(data)

sensorTemp()
