class Solution:
    def desencriptar(self, clave, mensajeAEnviarEncriptado):
        mensajeDesencriptado = ""

        cadenaAleatoria = mensajeAEnviarEncriptado[0:80]
        numeroRandom = binaryToDecimal(cadenaAleatoria)
        mensajeCodificado = mensajeAEnviarEncriptado[80:]

        cadenaDeInicio = getCadenaDeInicio(clave, numeroRandom)
        cadenaBinaria = toBinaryArray(createList(cadenaDeInicio))

        mensajeBinario = ""

        for i in range(len(mensajeCodificado)):
            if mensajeCodificado[i] == "0" and cadenaBinaria[i] == "0":
                mensajeBinario += "0"
            elif mensajeCodificado[i] == "1" and cadenaBinaria[i] == "1":
                mensajeBinario += "0"
            elif mensajeCodificado[i] == "0" and cadenaBinaria[i] == "1":
                mensajeBinario += "1"
            elif mensajeCodificado[i] == "1" and cadenaBinaria[i] == "0":
                mensajeBinario += "1"

        mensajeDesencriptado += binaryToText(mensajeBinario)
        return mensajeDesencriptado

def binaryToDecimal(string):
    numero = ""
    for i in range(0, 80, 8):
        i = str(int(string[i:i + 8], 2))
        numero += i
    return numero  # lo devuelve como string

def getCadenaDeInicio(key, numeroRandom):
    cadenaDeInicio = ""
    isKey = True
    while len(cadenaDeInicio) < MAX_LENGTH:
        cadenaDeInicio += key if isKey else str(numeroRandom)
        isKey = not isKey
    return cadenaDeInicio[0:MAX_LENGTH]

def createList(cadenaDeInicio):
    arr = [i for i in range(MAX_LENGTH)]
    for i in range(MAX_LENGTH):
        j = int(cadenaDeInicio[i])
        arr[i], arr[(i + j) % MAX_LENGTH] = arr[(i + j) % MAX_LENGTH], arr[i]
    return arr

def toBinaryArray(lista):
    mensaje_binario = ""
    for numero in lista:
        mensaje_binario += format(numero, '08b')
    return mensaje_binario

def binaryToText(string):
    numero = ""
    for i in range(0, len(string), 8):
        i = chr(int(string[i:i + 8], 2))
        numero += i
    return numero

MAX_LENGTH = 256
clave = "9876543210"
mensajeAEnviarEncriptado = "00001001000001110000000100001000000010010000010000000010000000010000000100000101001010100011101011000000110000110011110110111100001001101101101000100001001000000011101001001100"
print(Solution().desencriptar(clave, mensajeAEnviarEncriptado))
