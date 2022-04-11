from turtle import lt, fd, done, pencolor

n = int(input("Ingresa el numero de lados: "))
l = int(input("Ingresa la longitud del lado: "))
ø = int((180 * (n - 2)) / n)
pencolor(str(input("Ingresa el color: ")))

for lado in range(n):
    fd(l)
    lt(180 - ø)
done()
