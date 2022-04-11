"""Se importa la libreria de math
completa para utilizar funciones
que facilitan programar """
import math
s1 = float(input("Ingrese el primer lado: "))
s2 = float(input("Ingrese el segundo lado: "))
s3 = float(input("Ingrese el tercer lado: "))
s = (s1+s2+s3)/2
area = math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
print("El area del triangulo es: {}".format(round(area, 2)))
