from random import *

num_digitos = 6             # el numero de digitos del token
num_letras = 3              # el número de letras que debe tener el token
posiciones_letras = ""      # el string con las posiciones en las que iran las letras
posicion = None             # las pociciones donde iran las letras
token = ""                  # la clave del token
letras = "abcdefghijklmñnopqrstuvwxyz"            # abecedario
count = 0                   # contador para cuando tengamos las posiciones

while count < num_letras:
    posicion = randint(0, num_digitos-1)
    if str(posicion) not in posiciones_letras:
        posiciones_letras += str(posicion)
        count += 1

print(", ".join(posiciones_letras))

for digitos in range(num_digitos):
    if digitos in (int(posiciones_letras[0]), int(posiciones_letras[1]), int(posiciones_letras[2])):
        token += str(choice(letras))
    else:
        token += str(randint(0, 9))

print(token)
