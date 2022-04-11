from random import randint

def crearmatriz(n) :
    return [['*' if f==0 or f==n-1 or c==0 or c==n-1 else randint(1, 9) for c in range(n)] for f in range(n)]

def imprimirmatriz(matriz, n):
    for f in range(n):
        for c in range(n):
            print(matriz[f][c], end="\t")
        print()

tamano = int(input("Input: "))
imprimirmatriz(crearmatriz(tamano), tamano)
