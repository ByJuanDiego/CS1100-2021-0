"""Para no llenar toda la memoria
con una libreria, importamos
unicamente las funciones que
queremos usar"""
from math import pi, tan
n = int(input("Ingresa el numero de lados: "))
s = float(input("Ingresa la longitud de los lados: "))
area = (n*(s**2))/(4*tan(pi/n))
print("El area es: {}".format(round(area, 3)))
