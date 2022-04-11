from json import load

def selectionSort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j]['nombre'] < arr[min]['nombre']: min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr

def binarySearch1(arr, nombre):
    min, max = 0, len(arr)-1
    while True:
        if max < min:  return "No se encontró al candidato"
        mid = (min + max) // 2
        if quitarTildes(arr[mid]['nombres']) < nombre: min = mid+1
        elif quitarTildes(arr[mid]['nombres']) > nombre: max = mid-1
        else: return f"{arr[mid]['partido']}"

def binarySearch2(arr, nombre):
    min, max = 0, len(arr)-1
    while True:
        if max < min: return "No se encontró al candidato"
        mid = (min + max) // 2
        if arr[mid]['nombre'] < nombre: min = mid+1
        elif arr[mid]['nombre'] > nombre: max = mid-1
        else: return f"{arr[mid]['partido']}"

def quitarTildes(nombre):
    candidato = ''
    for char in nombre:
        if char == 'á': candidato += 'a'
        if char == 'é': candidato += 'e'
        else: candidato += char
    return candidato

#=======================================================================================================================
nombre = input("Ingresa el congresista de su preferencia: ")
with open('Congresista2020.json', 'r', encoding='utf-8') as file:
    print(binarySearch1(load(file), quitarTildes(nombre)))

nombre = input("Ingrese el presidente de su preferencia: ")
with open('elecciones2021.json', 'r', encoding='utf-8') as file:
    arr = load(file)['candidato']
    print(binarySearch2(selectionSort(arr), nombre))
