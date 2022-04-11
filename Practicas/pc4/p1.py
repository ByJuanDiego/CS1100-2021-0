from json import dump, load

def agregarVoto(dic, i):
    voto = int(input(f"Votante ({i+1}):\n- Partido politico Peru 2021 (1)\n- Partido politico Mejor Amigo (2)\n"))
    if voto == 1: dic['Partido politico Peru 2021'] += 1
    else: dic['Partido politico Mejor Amigo'] += 1

diccionario = {"Partido politico Peru 2021": 0, "Partido politico Mejor Amigo": 0}
num = int(input("Ingresar la cantidad de votantes: "))

for i in range(num): agregarVoto(diccionario, i)

with open('votos.json', 'w') as file:
    dump(diccionario, file, indent=4)

print('Conteo final .')
with open('votos.json', 'r') as file:
    diccionario = load(file)
    for key in diccionario: print(f"{key}: {diccionario[key]}")
