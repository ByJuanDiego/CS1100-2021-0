from turtle import *
from random import randint, randrange, choice


def variarColor(color, var):
    R, G, B = color
    R, G, B = randint(R - var, R + var), randint(G - var, G + var), randint(B - var, B + var)
    while 255 < R or R < 0:
        R = color[0]
        R = randint(R - var, R + var)
    while 255 < G or G < 0:
        G = color[1]
        G = randint(G - var, G + var)
    while 255 < B or B < 0:
        B = color[2]
        B = randint(B - var, B + var)
    return R, G, B


def generarHoja():
    miTurtle.color(variarColor(cHojas, var))
    miTurtle.begin_fill()
    miTurtle.right(180 / 2)
    miTurtle.circle(4, 180)
    miTurtle.circle(4, 180)
    miTurtle.left(180 - 180 / 2)
    miTurtle.end_fill()


def generarArbol(t, d):
    if d != 0:
        angulo1 = Ramas + randrange(-var, var + 1)
        angulo2 = Ramas + randrange(-var, var + 1)
        colortronco = variarColor(cTronco, var)
        miTurtle.color(colortronco)
        miTurtle.pensize(d)
        miTurtle.forward(t)
        miTurtle.left(angulo1)
        generarArbol(t * proporcion, d - 1)  # recursividad
        miTurtle.right(angulo1 + angulo2)
        generarArbol(t * proporcion, d - 1)  # recursividad
        miTurtle.color(colortronco)
        miTurtle.left(angulo2)
        miTurtle.penup()
        miTurtle.back(t)
        miTurtle.pendown()

    else:
        miTurtle.forward(t)
        generarHoja()
        miTurtle.penup()
        miTurtle.back(t)
        miTurtle.pendown()
        miTurtle.color(cTronco)
        return


def principal(nivel):
    colormode(255)
    miTurtle.shape('turtle')
    miTurtle.speed('fastest')
    miTurtle.color(cTronco)

    bgcolor(70, 200, 80)
    miTurtle.hideturtle()
    miTurtle.color(cFondo)
    miTurtle.goto(-675, -120)
    miTurtle.begin_fill()
    for i in range(2):
        miTurtle.forward(1500)
        miTurtle.left(90)
        miTurtle.forward(600)
        miTurtle.left(90)
    miTurtle.end_fill()

    miTurtle.showturtle()
    miTurtle.home()
    miTurtle.left(90)
    miTurtle.back(200)
    miTurtle.pendown()
    generarArbol(altura, nivel)
    miTurtle.color(0, 143, 57)
    done()


ventana = Screen()
ventana.title('Recursividad y números aleatorios')
miTurtle = Turtle()

var = 27  # variable de aleatoriedad para colores y angulos
proporcion = 0.8  # relación entre la rama y las sub ramas
Ramas = 20  # ángulo de inclinación para las ramas
altura = 200  # altura del tronco
cTronco = (90, 60, 30)  # color inicial del tronco
cHojas = (0, 100, 0)  # color de las hojas
cFondo = (150, 200, 255)  # color de fondo

i = choice([9, 10, 11])  # nivel de ramificaciones del arbol
print("Nivel {} de arbol".format(i))

principal(i)
