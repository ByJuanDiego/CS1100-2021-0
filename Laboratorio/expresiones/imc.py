import math
peso_gr = float(input("Ingrese el peso en gr: "))
altura_cm = float(input("Ingrese la altura en cm: "))
peso_kg = peso_gr/1000
altura_m = altura_cm/100
BMI = peso_kg/math.pow(altura_m, 2)
print("El BMI es de: {}".format(round(BMI, 3)))
