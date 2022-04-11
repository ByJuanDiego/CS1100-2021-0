from math import ceil, floor


def round_well(n):
    if n - floor(n) < 0.5:
        return floor(n)
    else:
        return ceil(n)


matriz = []
alumnos = int(input("Ingresa el numero de alumnos: "))
notas = int(input("Ingresa el numero de notas por alumno: "))

print()
suma_general = 0
promedio_general = 0
for alumno in range(alumnos):
    matriz.append([])
    suma = 0
    for nota in range(notas):
        nota = int(input("Ingresa la nota {} del alumno {}: ".format(nota + 1, alumno + 1)))
        suma += nota
        matriz[alumno].append(nota)
    promedio = suma / notas

    print("Las notas del alumno {} son: ".format(alumno + 1), end="")
    for nota in range(notas):
        print(matriz[alumno][nota], end=" ")
    print("y su promedio es de {}".format(round_well(promedio)) + "\n")
    suma_general += promedio

promedio_general = suma_general / alumnos
print("El promedio del salon es: {}".format(promedio_general))
