import random

random.seed(30)
MAX_LENGTH = 256
# paso 3
numeroRandom = random.randint(1000000000, 9999999999)

# paso 4
def getCadenaDeInicio(key):
    cadenaDeInicio = ""
    isKey = True
    while len(cadenaDeInicio) < MAX_LENGTH:
        cadenaDeInicio += key if isKey else str(numeroRandom)
        isKey = not isKey
    return cadenaDeInicio[0:MAX_LENGTH]


# paso 2
def toBinary(string):
    mensaje_binario = ""
    for caracter in string:
        mensaje_binario += format(ord(caracter), '08b')
    return mensaje_binario


# paso 6b
def toBinaryArray(lista):
    mensaje_binario = ""
    for numero in lista:
        mensaje_binario += format(numero, '08b')
    return mensaje_binario


# paso 5
def createList(cadenaDeInicio):
    arr = [i for i in range(MAX_LENGTH)]
    for i in range(MAX_LENGTH):
        j = int(cadenaDeInicio[i])
        arr[i], arr[(i + j) % MAX_LENGTH] = arr[(i + j) % MAX_LENGTH], arr[i]
    return arr


def numberToBinary(number):
    ans = ""
    while number > 0:
        currentDigit = number % 10;
        ans = str(format(currentDigit, '08b')) + ans;
        number //= 10
    return ans


def encriptar(key, mensaje):
    # paso 4
    ci = getCadenaDeInicio(key)
    array = createList(ci)

    # paso 2/6a
    mensajeBinario = toBinary(mensaje)
    # paso 6b
    arrayBinario = toBinaryArray(array)

    arrayBinario = arrayBinario[:len(mensajeBinario)]

    mensajeCodificado = ""
    # paso 6c
    for i in range(len(mensajeBinario)):
        mensajeCodificado += '0' if mensajeBinario[i] == arrayBinario[i] else '1'

    # paso 7
    return numberToBinary(numeroRandom) + mensajeCodificado


key = "9876543210"
mensaje_a_enviar = "#:;<>@#$&()^"
print(encriptar(key, mensaje_a_enviar))
