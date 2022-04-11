import json


def validar(dic):
    for es, ing in dic.items():
        respuesta = input("Ingrese en ingles '{}': ".format(es))
        if respuesta == ing:
            print("Correcto.")
        else:
            print("Incorrecto, es '{}' ".format(ing))


def agregar(dic):
    esp = input("Palabra en español: ")
    ing = input("Palabra en ingles : ")
    dic[esp] = ing


def cargar_datos():
    with open("minidic.json", "r") as file:
        json_data = json.load(file)
        return json_data


def guardar_datos(dic):
    with open("minidic.json", "w") as file:
        json.dump(dic, file, indent=4, sort_keys=True)


def main():
    minidic = cargar_datos()
    menu = '''
    1. Repasar.
    2. Agregar palabra.
    3. Guardar y Salir
    '''
    while True:
        print(menu)
        elegir = input("¿Que deseas hacer? : ")
        if elegir == "1":
            validar(minidic)
        elif elegir == "2":
            agregar(minidic)
        elif elegir == "3":
            guardar_datos(minidic)
            break
        else:
            print("Opción invalida, intente nuevamente")


main()
