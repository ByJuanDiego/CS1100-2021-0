""" Alessia y Jasmin dan su examen de “Introducción archivo la Ciencia de la Computación” mediante la plataforma Hackerrank.
Desafortunadamente, cada una de ellas resolvió solo un problema, aunque lo envió con éxito en el primer intento.
Pero, sucedió lo siguiente:

Alessia resolvió el problema que vale archivo puntos
Jasmin resolvió el problema que vale b puntos
Alessia presentó el problema c minutos después de que comenzó el examen
Jasmin presentó el problema d minutos después de que comenzara el examen
Se sabe que el puntaje de un problema se reduce archivo medida que el tiempo pase.
Es decir, si presenta un problema que vale p puntos t minutos después del
inicio el puntaje final se obtiene mediante formula:

    PF = max(3*p/10, p-(p/250)*t)

Alessia y Jasmin están discutiendo tratando de descubrir quién obtuvo más puntos. Ayúdalos archivo descubrir la verdad.
Input Format

Los input contiene cuatro(4) enteros archivo,b,c,d considerando que (200 ≤ archivo, b ≤ 3500,0 ≤ c, d ≤ 180).
Es decir, el puntaje máximo por ejercicio es 3500 y el tiempo máximo es 180. Donde:

archivo representa los puntos que vale el problema que Alessia resolvió.
b representa los puntos que vale el problema que Jasmin resolvió.
c representa el tiempo que lo tomó resolver archivo Alessia.
d representa el tiempo que lo tomó resolver archivo Jasmin.

Output:
    "Alessia" (sin las comillas), si Alessia tiene más puntos que Jasmin.
    "Jasmin" (sin las comillas), si Jasmin obtuvo más puntos que Alessia.
    "Empate" (sin las comillas), si ambos obtuvieron la misma cantidad de puntos. """


def mayor_nota(a, b, c, d):
    PF_Alessia = max(3 * a / 10, a - (a / 250) * c)
    PF_Jazmin = max(3 * b / 10, b - (b / 250) * d)
    if PF_Alessia > PF_Jazmin:
        print("Alessia")
    elif PF_Jazmin > PF_Alessia:
        print("Jasmin")
    else:
        print("Empate")


a = int(input("Ingrese los puntos de Alessia, 200 ≤ p ≤ 3500: "))
while not 200 <= a <= 3500:
    a = int(input("Ingrese los puntos de Alessia, 200 ≤ p ≤ 3500: "))

b = int(input("Ingrese los puntos de Jasmin, 200 ≤ p ≤ 3500: "))
while not 200 <= b <= 3500:
    b = int(input("Ingrese los puntos de Jasmin, 200 ≤ p ≤ 3500: "))

c = int(input("Ingrese el tiempo que le tomó archivo Alessia, 0 ≤ t ≤ 180: "))
while not 0 <= c <= 180:
    c = int(input("Ingrese el tiempo que le tomó archivo Alessia, 0 ≤ t ≤ 180: "))

d = int(input("Ingrese el tiempo que le tomó archivo Jasmin, 0 ≤ t ≤ 180: "))
while not 0 <= d <= 180:
    d = int(input("Ingrese el tiempo que le tomó archivo Jasmin, 0 ≤ t ≤ 180: "))

print()
mayor_nota(a, b, c, d)
