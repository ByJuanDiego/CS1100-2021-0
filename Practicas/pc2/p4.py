
from random import randint

def generarMatriz(dimensiones):
    return [[randint(3, 9) for _ in range(dimensiones)] for _ in range(dimensiones)]

def agregarObjeto(matriz, dimensiones):
    x = randint(0, dimensiones - 2)
    y = randint(0, dimensiones - 2)
    matriz[y][x], matriz[y+1][x+1], matriz[y][x+1], matriz[y+1][x] = 1, 1, 1, 1
    return matriz

def imprimirMatriz(matriz, dimensiones):
    for f in range(dimensiones):
        for c in range(dimensiones):
            print(matriz[f][c], end="\t")
        print()

def quitarBloque(matriz, dimensiones, coordenadas):
    if matriz[coordenadas[0]][coordenadas[1]] == 1:
        matriz = [[0 for _ in range(dimensiones)] for _ in range(dimensiones)]
    else:
        matriz[coordenadas[0]][coordenadas[1]] = 0
    return matriz

tamanho = 6
matrix = generarMatriz(tamanho)
matrix = agregarObjeto(matrix, tamanho)

imprimirMatriz(matrix, tamanho)
input = [int(n) for n in input("Ingrese ubicacion del bloque : ").split()] # Almacena las coordenadas en una lista

matrix = quitarBloque(matrix, tamanho, input)
print('\nOutput: ')
imprimirMatriz(matrix, tamanho)
