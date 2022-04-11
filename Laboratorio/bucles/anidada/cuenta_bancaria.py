import time

""" P1)  Diseñe un algoritmo que simule la autenticación de un cajero automático
y que al tercer intento bloquee la cuenta por 10seg e imprima
 los segundos  que queda para volver a.a intentar y cuando la
  autenticación sea exitosa imprima:
 ******************************
  [1] Depositar
  [2] Retirar
  [3] Salir
****************************** """


# P1:
def cuenta_bancaria(password):
    intento = 0
    contrasenaCorrecta = password

    while True:
        contrasena = int(input("Ingrese su contraseña: "))
        if contrasena == contrasenaCorrecta:
            print("Puede realizar las siguiente Operaciones")
            print("-" * 30)
            print("[1] Depositar")
            print("[2] Retirar")
            print("[3] Salir")
            print("-" * 30)
            # opciones = input("Eliga una opción: ")
            # se puede hacer mas cosas . . . . . .
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


""" P2) Se nos viene la próxima elección presidencial que se realizará en Perú
este 21 de abril del 2021 y cuando se trata de votaciones electrónicas,
la integridad de los datos es crucial. En esta oportunidad solo se
presentaron dos candidatos al cual denominaremos Candidato1 (Juan Perez)
y Candidato2 (Jorge Perez). Siendo además los electores una cantidad de N.

Se desea elaborar un algoritmo para contabilizar los votos, donde el
elector puede: elegir un candidato o votar en blanco o viciar su voto,
como resultado final se requiere saber quien fue el candidato ganador,
cantidad de votos blancos, viciados y el total de votos válidos (- viciados). """


# P2:
def elecciones(votantes):
    contador_jorge = 0
    contador_juan = 0
    voto_blanco = 0
    voto_viciado = 0
    votos_validos = 0
    ganador = ""

    print("\n""Ingrese su voto: ")
    print("Jorge Perez      [1]")
    print("Juan Perez       [2]")
    print("Voto el blanco   [enter]""\n")

    for votante in range(votantes):

        voto = str(input("Ingrese el voto del votante N˚{}: ".format(votante + 1)))

        if voto == "1":
            contador_jorge += 1
            votos_validos += 1
        elif voto == "2":
            contador_juan += 1
            votos_validos += 1
        elif voto == "":
            voto_blanco += 1
            votos_validos += 1
        else:
            voto_viciado += 1

    if contador_juan > contador_jorge:
        ganador = "Juan Perez"
    elif contador_jorge > contador_juan:
        ganador = "Jorge Perez"
    elif voto_blanco == votos_validos and voto_blanco != 0:
        ganador = "No hay ganador, todos votaron en blanco."
    elif voto_viciado == votantes:
        ganador = "No hay ganador, todos los votos fueron viciados."

    print("\n""El ganador es: " + ganador +
          "\n" + "La cantidad de votos en blanco es: " + str(voto_blanco) +
          "\n" + "La cantidad de votos viciados es: " + str(voto_viciado) +
          "\n" + "La cantidad de votos validos es: " + str(votos_validos))


n = int(input("Ingresa el numero de pregunta: "))
while n not in [1, 2]:
    n = int(input("Ingresa el numero de pregunta [1, 2]: "))

if n == 1:
    password = int(input("Registre su contraseña: "))
    print("Su contraseña ha sido guardada exitosamente" "\n")
    cuenta_bancaria(password)
elif n == 2:
    votantes = int(input("Ingresa el numero de votantes: "))
    elecciones(votantes)
