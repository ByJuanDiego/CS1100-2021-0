def promedioEdad(alumnos):
    suma = 0
    for i in range(len(alumnos)):
        suma += alumnos[i][2]
    prom = suma / len(alumnos)
    return round(prom, 2)

def alumnoJove(alumnos):
    posicion = 0
    for i in range(len(alumnos)):
        if i == 0:
            posicion = i
        elif (i != 0) and (alumnos[i][2] < alumnos[posicion][2]):
            posicion = i
    return alumnos[posicion][0]

def alumnoPeso(alumno):
    posicion = 0
    for i in range(len(alumno)):
        if i == 0:
            posicion = i
        elif (i != 0) and (alumnos[i][4] < alumnos[posicion][4]):
            posicion = i

    return alumnos[posicion][0]

def dividirlista(alumno):
    F = []
    M = []
    for i in range(len(alumno)):
        if alumno[i][5] == "M":
            M.append(alumno[i][0])
        elif alumno[i][5] == "F":
            F.append(alumno[i][0])
    return M, F

# [Nombre, Apellido, Edad, Talla, Peso, Genero]
alumnos = [["Luis",     "Yi",       19, 1.82, 80, "M"],
           ["Paul",     "Tipula",   19, 1.90, 72, "M"],
           ["Joaquin",  "Cayo",     22, 1.80, 90, "M"],
           ["Martin",   "Robles",   17, 1.60, 62, "M"],
           ["Luis",     "Piñas",    21, 1.80, 70, "M"],
           ["Diana",    "Garcia",   16, 1.60, 60, "F"],
           ["Paul",     "Tipula",   19, 1.70, 72, "M"],
           ["Manuel",   "Gonzalez", 16, 1.70, 73, "M"],
           ["Carlos",   "Segura",   19, 1.73, 68, "M"],
           ["Giordano", "Alvites",  23, 1.83, 82, "M"],
           ["Alfieri",  "Podesta",  17, 1.77, 60, "M"],
           ["Ana",      "Adriano",  18, 1.63, 57, "F"]]

print(promedioEdad(alumnos))
print(alumnoJove(alumnos))
print(alumnoPeso(alumnos))
hombres, mujeres = dividirlista(alumnos)
print("Los hombres son: {}\nLas mujeres son: {}".format(hombres, mujeres))
