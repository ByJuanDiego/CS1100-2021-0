from random import randint

def generarDatosHuella(diccionario):
    for e in diccionario:
        diccionario[e] = [randint(minimoDeValor, maximoDeValor) for _ in range(randint(minimoDeNumeros, maximoDeNumeros))]

def biometrico(vectorIngresado):
    coincidencias = 0
    vectorReal = dic_persona[mano][dedo]
    iteraciones = max(len(vectorReal), len(vectorIngresado))
    for i in range(iteraciones):
        try:
            if vectorReal[i] == vectorIngresado[i]:
                coincidencias += 1
        except IndexError:
            pass
    if coincidencias <= len(vectorReal)//2:
        return "\nLas coincidencias no son suficientes!\nLas coincidencias fueron {}".format(coincidencias)
    else:
        return "\nLas coincidencias fueron suficientes\nLas coincidencias fueron {}\n\n{}".format(coincidencias, dic_persona)

minimoDeNumeros = 4     # valor minimo de elementos por dedo
maximoDeNumeros = 6     # valor maximo de elementos por dedo
minimoDeValor = 10      # valor minimo del elemento
maximoDeValor = 15      # valor maximo del elemento

vector_huella_derecho = dict
vector_huella_derecho = {'pulgar': [], 'indice': [], 'medio': [], 'anular': [], 'meñique': []}
generarDatosHuella(vector_huella_derecho)

vector_huella_izquierdo = dict
vector_huella_izquierdo = {'pulgar': [], 'indice': [], 'medio': [], 'anular': [], 'meñique': []}
generarDatosHuella(vector_huella_izquierdo)

dic_persona = dict
dic_persona = {"DNI": "70323306", "nombre": "Juan Diego", "derecha": vector_huella_derecho, "izquierda": vector_huella_izquierdo}

print("Datos mano derecha:\n{}\n".format(dic_persona['derecha']))
print("Datos mano izquierda:\n{}\n".format(dic_persona['izquierda']))

mano = str(input("Ingrese la mano (derecha, izquierda): "))
dedo = str(input("Ingrese el dedo (pulgar, indice, medio, anular, meñique): "))

print("\nEl vector se compone de numeros que estan entre {} y {}".format(minimoDeValor, maximoDeValor))
print("además, el vector tiene entre {} y {} numeros".format(minimoDeNumeros, maximoDeNumeros))
print("Ejemplo de input: 11,15,13,14,14\n")

vectorIngresado = str(input("Ingresa el vector: "))
vectorIngresado = vectorIngresado.split(",")
for numero in range(len(vectorIngresado)):
    vectorIngresado[numero] = int(vectorIngresado[numero])

print("vector ingresado: {}".format(vectorIngresado))
print("vector real:      {}".format(dic_persona[mano][dedo]))
print(biometrico(vectorIngresado))
