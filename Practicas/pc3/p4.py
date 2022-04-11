import json

def cargar_datos():
    file = open('elecciones2021.json', 'r')
    data = json.load(file)
    file.close()
    return data

def calcularvotos(dic):
    ganador = ''
    votos = 0
    for i in range(len(dic['candidato'])):
        if sum(dic['candidato'][i]['votos']) > votos:
            votos = sum(dic['candidato'][i]['votos'])
            ganador = dic['candidato'][i]['nombre']
    return ganador, votos

ganador, n_votos = calcularvotos(cargar_datos())
print(f"{ganador} {n_votos}")
