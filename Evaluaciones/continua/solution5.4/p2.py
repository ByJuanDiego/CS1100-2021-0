def agregarDatos(iteracion):
    nombre = input("\nIngresa el nombre de la persona N˚{}: ".format(iteracion+1))
    vector_huella = str(input("Ingrese su vector huella: "))
    vector_huella = vector_huella.split(',')
    for i in range(len(vector_huella)):
        vector_huella[i] = int(vector_huella[i])
    dic_persona[nombre] = vector_huella

dic_persona = dict
dic_persona = {}

n = int(input("Ingrese el numero de personas a registrar: "))
for _ in range(n):
    agregarDatos(_)

nombre = input("\nIngrese el nombre de la persona de la cual quieres los datos: ")
print(dic_persona[nombre])
