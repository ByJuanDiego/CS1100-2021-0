"""La empresa “Factorías del Perú”, recientemente adquirió un nuevo sensor de temperatura para
medir la temperatura del centro de incubadora y se requiere obtener las dos(2) temperaturas
más altas con la indicación de la hora, min, seg en el que ocurrió dicho evento. Se debe
almacenar el resultado del sensor en un archivo y luego ordenarla y obtener cual
fue el mayor en que hora, min, segundo. (si hay empates mostrarlos)"""
import time
import random

def sensorTemp():
    seg = 0
    min = 0
    hora = 0
    print("El valor ingresado de horas puede ser 0")
    hora1 = int(input("Ingrese las horas que el sensor contará   [0-24]: "))
    print("\nEl valor ingresado de minutos puede ser 0")
    min1 = int(input("Ingrese los minutos que el sensor contará  [0-59]: "))
    print("\nEl valor ingresado de segundos debe ser: 0 < S, y S <= 59")
    seg1 = int(input("Ingrese los segundos que el sensor contará [1-59]: "))
    print()

    f = open("texto.txt", "a")  # abrimos el archivo en modo append para introducir los datos

    while True:

        valor = "Tiempo: {} : {} : {} => °C: {}".format(str(hora), str(min), str(seg), str(random.randrange(0, 101, 2)))
        f.write("{}\n".format(valor))
        print(valor)

        if hora == hora1 and min1 == min and seg == seg1:   # se rompe el bucle cuando alcanza la hora ingresada
            break

        seg += 1
        if seg == 60:
            seg = 0
            min += 1
        if min == 60:
            min = 0
            hora += 1
        time.sleep(1)

    f.close()
    lista_temps = []
    matriz_datos = []
    f = open("texto.txt", "r")  # abrimos el archivo en modo lectura para extraer los datos

    for linea in f:
        datos = ''
        for char in linea:
            if char in '1234567890:':
                datos += char
        datos = datos.split(":")
        del datos[0]
        for i in range(len(datos)):
            datos[i] = int(datos[i])
        matriz_datos.append(datos)
        lista_temps.append(datos[3])

    maxima1 = max(lista_temps)
    i = lista_temps.index(maxima1)
    print()
    print("La mayor temperatura N˚1 fue {} y se consiguió a la hora {}:{}:{}"
          .format(matriz_datos[i][3], matriz_datos[i][0], matriz_datos[i][1], matriz_datos[i][2]))
    del lista_temps[i], matriz_datos[i]

    maxima2 = max(lista_temps)
    i = lista_temps.index(maxima2)
    print("La mayor temperatura N˚2 fue {} y se consiguió a la hora {}:{}:{}"
          .format(matriz_datos[i][3], matriz_datos[i][0], matriz_datos[i][1], matriz_datos[i][2]))

    if maxima1 == maxima2: print("Es un empate!!!")

    f.close()

sensorTemp()
