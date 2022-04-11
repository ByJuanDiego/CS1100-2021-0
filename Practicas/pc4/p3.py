from math import pow, sqrt

def d(x1, y1, x2, y2): return sqrt(pow((x1-x2), 2) + pow((y1-y2), 2))

def agregarPokemon(lista, i):
    pos = [int(x) for x in input(f"Coordenada del pokemon {i+1} (X, Y): ").split(',')]
    lista.append(pos)

def ordenar(arr):   # usamos bubble sort
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print('Input:')
x = int(input("Coordenada de jugador X: "))
y = int(input("Coordenada de jugador Y: "))
n = int(input("N de pokemones: "))

pos = []
for i in range(n): agregarPokemon(pos, i)

distancias = []
for i in range(len(pos)):
    x1, y1 = pos[i][0], pos[i][1]
    distancias.append(d(x, y, x1, y1))

distancias = ordenar(distancias)
menor = distancias[0]

nombres = ""
for i in range(len(pos)):
    x1, y1 = pos[i][0], pos[i][1]
    if d(x, y, x1, y1) == menor: nombres += f" pokemon {i + 1},"
nombres = nombres[:len(nombres)-1]

b = distancias.count(menor)==1 # booleano para identificar si solo hay 1 pokemon con la minima distancia

print("\nOutput")
print(f"{('El'*b)+('Los'*(not b))} pokemon{'s'*(not b)} mas cercano{'s'*(not b)} {('es'*b)+('son'*(not b))}: {nombres}")
