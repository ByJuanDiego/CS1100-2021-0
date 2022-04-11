from random import choice, randint

letras = "abcdefghijklmnoprqstvwxyz"

def generarToken():
    token = ""
    numeroRandom = randint(0, 9)

    for i in range(6):
        if i in [0, 5]: token += choice(letras).upper()
        elif i in [2, 4]: token += choice(letras)
        elif i in [1, 3]: token += str(numeroRandom)
    return token

print(generarToken())
