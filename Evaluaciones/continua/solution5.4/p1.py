def agregarDatos(iteracion):
    nombre = input("\nIngresa el nombre de la persona N˚{}: ".format(iteracion+1))
    apellido = input("Ingresa el apellido de la persona: ")
    nombre_completo = "{} {}".format(nombre, apellido)
    notas = input("Ingresa las 4 notas de la persona: ")
    notas = notas.split(",")
    promedio = calcularPromedio(notas)
    dic_persona[nombre_completo] = promedio

def calcularPromedio(lista_notas):
    suma = 0
    for nota in lista_notas:
        suma += int(nota)
    promedio = round(suma/len(lista_notas), 2)
    return promedio

dic_persona = dict
dic_persona = {}
n = int(input("Ingrese el numero de personas a registrar: "))

for _ in range(n):
    agregarDatos(_)

print("\nPromedios de alumnos de CS1100:\n{}".format(dic_persona))
