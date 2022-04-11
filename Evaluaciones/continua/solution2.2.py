def descuento(c, n, r):
    if r == "A":
        return int(c * n - (30 / 100) * (c * n))
    elif r == "B":
        return int(c * n - (20 / 100) * (c * n))
    elif r == "C":
        return int(c * n - (10 / 100) * (c * n))
    elif r == "D":
        return int(c * n - (30 / 100) * (c * n))


def latex(texto):
    result = ''

    for i in texto:
        if i == "4":
            i = "a"
        elif i == "1":
            i = "i"
        elif i == "3":
            i = "e"
        elif i == "0":
            i = "o"
        elif i == ",":
            i = " "
        elif i == " ":
            i = ""
        else:
            i = i
        result += i
    return result


def redondearnota(notas0):
    result = []

    for nota in notas0:

        n = 0
        while n <= nota:
            n = n + 5

        resta = int(nota - n)

        if 0 <= nota < 30:
            result.append(nota)
        elif (resta % 2) != 0:
            nota = n
            result.append(nota)
        elif (resta % 2) == 0:
            result.append(nota)

    return result


x = 10
y = 2
a = 'A'
text = "U n 1 v 3 r s 1 d 4 d, d 3, 1 n g 3 n 1 3 r 1 4, y, t 3 c n 0 l 0 g 1 4,"
notas = [68, 46, 54, 24, 37, 23, 48, 51, 45]


print(descuento(x, y, a))
print(latex(text))
print(redondearnota(notas))
