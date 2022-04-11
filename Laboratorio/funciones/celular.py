import time
import random

estado = False
desbloqueado = False
contrasenha = "1234"
contactos = ""
bateria = random.randint(10, 20)
intento = 0


def encender():
    global estado
    estado = True
    print("Ahora el celular se encuentra encendido\n")


def apagar():
    global estado
    estado = False
    print("Ahora el celular se encuentra apagado\n")


def obtenerestado():
    return estado


def desbloquear():
    global intento
    global contrasenha
    global desbloqueado
    while True:
        if desbloqueado and obtenerestado():
            print("Su celular ya se encuentra desbloqueado !\n")
        clave = str(input("Ingresa tu contraseña: "))
        if obtenerestado():
            if clave == contrasenha:
                desbloqueado = True
                print("El dispositivo ahora esta desbloqueado\n")
                break
            else:
                intento += 1
                print("Contraseña incorrecta, ha agotado su intento N°{}".format(intento))
                if intento == 3:
                    print("Llegaste al los 3 intentos, tu cuenta se encuentra bloqueda")
                    segundos = 10
                    while True:
                        print("Intenta en {} Seg.".format(segundos))
                        segundos -= 1
                        time.sleep(1)
                        if segundos == 0:
                            intento = 0
                            break
        else:
            print("El dispositivo se encuentra Apagado, no puede desbloquearse !\n")
            break


def obtenerestadogeneral():
    return estado and desbloqueado


def cargarbateria():
    global bateria
    while True:
        carga = int(input("Cuanta carga quieres que tenga?, ahora tiene {}% : ".format(bateria)))
        if bateria <= carga <= 100:
            bateria = carga
            print("El dispositivo se ha cargado exitosamente !\n")
            break
        else:
            print("Ingresa una carga valida, la carga debe ser mayor o igual a.a la que tiene ahora!\n")


def obtenercarga():
    print("La bateria del dispositivo es de {}%\n".format(bateria))


def hora():
    hora_local = time.localtime()
    result = time.strftime("%I:%M:%S %p", hora_local)
    print("La hora actual es: {}\n".format(result))


def agregarcontacto():
    global contactos
    nombre = str(input("Ingresa el contacto a.a agregar: "))
    if estado and desbloqueado:
        contactos += "{}. ".format(nombre)
        print("Se ha agregado a.a {} exitosamente\n".format(nombre))
    elif estado:
        print("El dispositivo esta apagado, no puedes agregar contactos!\n")
    else:
        print("El dispositivo esta bloqueado, no puedes agregar contactos!\n")


def llamar():
    numero = int(input("Ingresa el numero al que quieres llamar: "))
    if obtenerestadogeneral():
        num = str(numero)
        if len(num) == 9:
            print("Llamando a.a {}...\n".format(numero))
        else:
            print("Debes llamar a.a un numero de 9 digitos !\n")
    else:
        print("El dispositivo se encuentra apagado, no puedes llamar\n")


def imprimir_contactos():
    global contactos
    print("Tus contactos son: {}\n".format(contactos))


def main():
    print("[-1]: Dejar de usar el celular\n[0]: Apagar el celular\n[1]: Encender\n[2]: Desbloquear\n[3]: Ver la hora"
          "\n[4]: Cargar la bateria\n[5]: Saber cuanta bateria tiene\n[6]: Llamar a.a un numero"
          "\n[7]: Agregar un nuevo contacto\n[8]: Imprimir tu lista de contactos\n")
    while True:
        opcion = int(input("¿Qué quiere hacer con su dispositivo?: "))
        if opcion == -1:
            print("\nUsar mucho el celular cansa la vista !\n")
            break
        if opcion == 0:
            apagar()
        if opcion == 1:
            encender()
        if opcion == 2:
            desbloquear()
        if opcion == 3:
            hora()
        if opcion == 4:
            cargarbateria()
        if opcion == 5:
            obtenercarga()
        if opcion == 6:
            llamar()
        if opcion == 7:
            agregarcontacto()
        if opcion == 8:
            imprimir_contactos()


main()
