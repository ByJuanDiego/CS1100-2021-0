from math import sqrt, pow
from json import dump, load
from Proyecto.variables import *


def main():
    def continuar(n):
        """ Pide que se ingrese 'C' para continuar, caso contrario te lo vuelve a pedir hasta que ingreses 'C'.
        :param n: si es 0, la función retorna sin hacer nada, caso contrario vuelve a llamar a la función main

        """
        if n == 0: return
        print()
        while True:
            c = input(f"{C}Ingrese 'C' y presione Enter para continuar: ").upper()
            if c == 'C': break
        print()
        main()

    print(f"{W}{menu}")
    opcion = str(input(f"{W}Ingrese opción: "))
    while opcion not in ('0', '1', '2', '3', '4', '5', '6'):
        opcion = str(input(f"{C}Ingrese una opción válida!: "))
    print()

    if opcion == '1':
        continuar(AgregarObjeto())
    elif opcion == '2':
        continuar(BorrarObjeto())
    elif opcion == '3':
        continuar(MostrarMapa())
    elif opcion == '4':
        continuar(MostrarPlan())
    elif opcion == '5':
        continuar(DelegarTarea())
    elif opcion == '6':
        continuar(CargarArchivo())
    elif opcion == '0':
        continuar(GuardarArchivo())


def validar(fun):
    """ Evita que el programa se detenga al encontrar un ValueError.
    :param fun: la función a validar
    :return: retorna la validacion del input

    """

    def validarInput():
        """ Intenta retornar la función (ejecutándola)
        Excepción: si encuentra un ValueError se retornará a si misma de forma recursiva
        :return: retorna la función

        """
        try:
            return fun()
        except ValueError:
            print(f"{C}(ValueError)!", end=" "); return validarInput()

    return validarInput


""" ====================================== Opcion [1] Agregar nuevo objeto ========================================= """


def AgregarObjeto():
    print(f"{W}Seleccione que quiere agregar:\nAgregar Dron\t\t[0]\nAgregar Obstáculo\t[1]")
    opcion = input(f"{W}\nIngrese opción: ")
    while opcion not in ('0', '1'): opcion = input(f"{C}Ingrese una opción válida!: ")
    print()
    x, y = pedirPosicionValida(f, c)
    while True:
        nombre = pedirNombre()
        if nombre not in objetos.keys() and nombre != '':
            break
        else:
            print(f"{C}El nombre está repetido o es muy corto!", end=' ')
    if opcion == '0':
        color = pedirColor()
        matriz[x][y] = color
        agregarDatos(nombre, x, y, color, None)
    elif opcion == '1':
        altura = pedirAltura()
        matriz[x][y] = '#'
        agregarDatos(nombre, x, y, '#', altura)
    print(f"{C}\nObjeto agregado!")
    return 1


@validar
def pedirPosicion():
    """ Nos pide ingresar cordenadas.
    :return: retorna las coordenadas como 2 enteros

    """
    x, y = [int(i) + 1 for i in input(f"{W}Ingrese las coordenadas (x,y): ").split(",")]
    return x, y


def pedirPosicionValida(f, c):
    """ Se encarga de comprobar que la posición ingresada no esté fuera de los índices de la matriz
    y que no haya ningún objeto en esa posición.
    :param f: número de filas de la matriz
    :param c: número de columnas de la matriz
    :return: retorna las coordenadas como 2 enteros

    """
    while True:
        x, y = pedirPosicion()
        posiciones = [objetos[key]['Posicion'] for key in objetos]
        if (1 > x or x > f - 1) or (1 > y or y > c - 1):
            print(f"{C}Las coordenadas estan fuera de rango, pruebe con otras!")
        elif [x, y] in posiciones:
            print(f"{C}Existe un objeto en estas coordenadas, pruebe con otras!")
        else:
            break
    return x, y


def pedirNombre():
    """ Nos pide ingresar un nombre.
    :return: retorna el nombre ingresado

    """
    return input(f"{W}Ingrese un nombre: ")


def pedirColor():
    """ Pide un carácter que representará a un dron en la matriz.
    Excepción: si la longitud del carácter ingresado es mayor a 1 o igual a '#', lo volverá a pedir
    :return: retorna el carácter que representa al dron

    """
    while True:
        color = input(f"{W}Ingrese el color: ")
        if len(color) == 1 and color != '#':
            return color
        else:
            print(f"{C}Ingrese un color válido!", end=' ')


@validar
def pedirAltura():
    """ Nos pide una altura, un entero que este entre 1 y 100 metros.
    :return: retorna la altura

    """
    while True:
        altura = int(input(f"{W}Ingresa su altura: "))
        if 1 <= altura <= 100:
            return altura
        else:
            print(f"{C}Ingresa una altura válida!(1-100)m", end=' ')


def agregarDatos(nombre, x, y, color, altura):
    """ Añade un dron u obstáculo al diccionario.
    Excepciones: Solo añadirá la altura cuando su valor ingresado en la función no sea None
    :param nombre: la llave principal cuyo valor guardará los demás datos del objeto como un diccionario
    :param x: la posición vertical del objeto en el mapa
    :param y: la posicion horizontal del objeto en el mapa
    :param color: el carácter que representa al objeto en el mapa
    :param altura: la altura de objetos de tipo obstáculo

    """
    objetos.update({nombre: {}})
    objetos[nombre]['Posicion'] = [x, y]
    objetos[nombre]['Color'] = color
    if altura is not None: objetos[nombre]['Altura'] = altura


""" ========================================= Opcion [2] Borrar objeto ============================================= """


def BorrarObjeto():
    if len(objetos.keys()) == 0:
        print(f"{C}No hay objetos en el plano, no se puede borrar nada!");
        return
    nombre = pedirNombre()
    while nombre not in objetos.keys():
        print(f"{C}Este nombre no está en el plano!", end=' ')
        nombre = pedirNombre()
    x, y = objetos[nombre]['Posicion']
    matriz[x][y] = '.'
    del objetos[nombre]
    print(f"{C}\nObjeto eliminado!")
    return 1


""" =========================================== Opcion [3] Mostrar Mapa ============================================ """


def MostrarMapa():
    imprimirPlano()
    imprimirDatos(objetos)
    return 1


def imprimirPlano():
    """ Recorre la matriz del mapa e imprime los carácteres en forma de tablero.

    """
    for f in range(len(matriz)):
        for c in range(len(matriz[0])):
            char = matriz[f][c]
            if f == 0 or c == 0 or char == '#':
                print(f"{W}{char}", end='\t')
            elif char != '.':
                print(f"{C}{char}", end='\t')
            else:
                print(f"{G}{char}", end='\t')
        print()
    print()


def imprimirDatos(dic):
    """ Imprime los datos de cada nombre en el diccionario.
    :param dic: es la estructura de datos donde se almacena la información de todos los objetos del proyecto

    """
    keys = [key for key in dic.keys()]
    for i in range(len(keys)):
        key = keys[i]
        x, y = dic[key]['Posicion']
        color = dic[key]['Color']
        print(f"{C}* * * * * * {W}[{i}] Nombre = {key}  Posición ({x - 1},{y - 1})  Color = {color}")


""" ==================================== Opcion [4] Mostrar plan de navegación ===================================== """


def MostrarPlan():
    drones = [key for key in objetos if objetos[key]['Color'] != '#']
    if len(drones) == 0:
        print(f"{C}Para generar un plan de navegación debe haber un dron!");
        return
    x, y = pedirPosicionValida(f, c)
    while True:
        nombre = pedirNombreValido(objetos.keys())
        if objetos[nombre]['Color'] != '#':
            break
        else:
            print(f"{C}Ingrese el nombre de un dron, no obstáculo!", end=' ')
    color = objetos[nombre]['Color']
    ox, oy = objetos[nombre]['Posicion']
    oxf, oyf, distancia = trazarTrayectoria(x, y, ox, oy)
    imprimirPlano()
    print(f"{W}La distancia total recorrida es de: {C}{distancia} km")
    objetos[nombre]['Posicion'] = [oxf, oyf]
    borrarTrayectoria(oxf, oyf, color)
    return 1


def pedirNombreValido(nombres):
    """ Pide un nombre, si es el nombre de un objeto ya ingresado, retorna el nombre.
    Excepción: Si el nombre no está en la lista de nombres, lo pedirá hasta que sea el de un objeto existente.
    :param nombres: lista con los nombres de cada objeto existente
    :return: retorna el nombre del dron validado

    """
    while True:
        nombre = pedirNombre()
        if nombre in nombres:
            return nombre
        else:
            print(f"{C}No hay ningun objeto con este nombre!")


def trazarTrayectoria(xf, yf, ox, oy):
    """ Siempre y cuando la posición del objeto ingresado no sea igual a la de su posición de destino,
    comparará las posiciones alrededor del objeto y cambiará sus posición a la que tenga una menor
    distancia a su posición de destino.
    Excepción: si el dron no puede cambiar sus posición porque se quedó sin posiciones válidas,
    imprime el mensaje 'El dron no pudo llegar a su destino!'
    
    :param xf: la posición en x donde debe terminar el objeto
    :param yf: la posición en y donde debe terminar el objeto
    :param ox: la posición en x donde se encuentra el objeto
    :param oy: la posición en y donde se encuentra el objeto
    :return: retorna las posiciones donde terminó el objeto y la distancia que recorrió

    """
    matriz[ox][oy] = '*'
    distancia, recorridas = 0, []
    while [ox, oy] != [xf, yf]:
        oxI, oyI = ox, oy
        posiciones = [[ox - 1, oy - 1], [ox - 1, oy], [ox - 1, oy + 1],
                      [ox, oy - 1], [ox, oy + 1],
                      [ox + 1, oy - 1], [ox + 1, oy], [ox + 1, oy + 1]]
        posicionesValidas, distancias = [], []
        for xy in posiciones:
            x, y = xy
            try:
                if matriz[x][y] == '.' and xy not in recorridas:
                    posicionesValidas.append(xy), distancias.append(d(xf, yf, x, y))
                elif matriz[x][y] == '#':
                    altura = encontrarAltura(x, y)
                    if altura <= 50:
                        posicionesValidas.append(xy), distancias.append(d(xf, yf, x, y))
            except IndexError:
                pass
        if len(posicionesValidas) == 0:
            print(f"{C}\nEl dron no pudo llegar a su destino!\n");
            return ox, oy, round(distancia, 4)
        ox, oy = posicionesValidas[distancias.index(min(distancias))]
        distancia += d(oxI, oyI, ox, oy)
        recorridas.append([oxI, oyI])
        matriz[ox][oy] = '*'
    print(f"{W}\nEl recorrido mínimo es el siguiente:\n")
    return ox, oy, round(distancia, 4)


def d(x1, y1, x2, y2):
    """ Obtiene la distancia entre dos puntos en un plano.
    :param x1: posición en x del primer punto
    :param y1: posición en y del primer punto
    :param x2: posición en x del segundo punto
    :param y2: posición en y del segundo punto
    :return: retorna la distancia entre los dos puntos del plano.

    """
    return sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2))


def encontrarAltura(x, y):
    """ Obtiene la altura de un obstáculo mediante su posición.
    :param x: posicion vertical del obstáculo
    :param y: posicion horizontal del obstáculo
    :return: retorna la altura del obstáculo

   """
    return [objetos[key]['Altura'] for key in objetos if objetos[key]['Posicion'] == [x, y]][0]


def borrarTrayectoria(oxf, oyf, color):
    """ Reemplaza las coordenadas donde terminó el dron por su color,
    reasigna las posiciones que contienen un '*' por un '.',
    si la posición '*' contenía a un '#', lo devuelve a un '#'.
    :param oxf: posición vertical final del dron en el mapa
    :param oyf: posición horizontal final del dron en el mapa
    :param color: carácter que representa al dron en el mapa

    """

    matriz[oxf][oyf] = color
    posiciones = [objetos[key]['Posicion'] for key in objetos
                  if objetos[key]['Color'] == '#' and objetos[key]['Altura'] <= 50]
    for f in range(len(matriz)):
        for c in range(len(matriz[0])):
            if matriz[f][c] == '*':
                if [f, c] in posiciones:
                    matriz[f][c] = '#'
                else:
                    matriz[f][c] = '.'


""" ======================================== Opcion [5] Delegar Tarea ============================================== """


def DelegarTarea():
    drones = [key for key in objetos if objetos[key]['Color'] != '#']
    if len(drones) < 2:
        print(f"{C}Para delegar una tarea deben existir al menos 2 drones!");
        return

    while True:
        d1 = input(f"{W}Ingrese al dron delegador: ")
        if d1 in drones: break
        print(f"{C}El dron ingresado no existe!", end=" ")
    while True:
        d2 = input(f"{W}Ingrese al dron delegado: ")
        if d2 in drones and d2 != d1: break
        print(f"{C}El dron ingresado no existe o ya lo ingresaste!", end=" ")

    x1, y1 = objetos[d1]['Posicion']
    x2, y2 = objetos[d2]['Posicion']
    distancia = d(x1, y1, x2, y2)

    print(f"{W}El dron {d1}{' no' * (distancia > 5)} pudo establecer comunicación con el dron {d2}!")
    print(f"{W}La distancia entre ellos es de: {C}{round(distancia, 4)} km")
    return 1


""" ========================================= Opcion [6] Cargar Archivo ============================================ """


def CargarArchivo():
    print(f"{W}{cargar}")
    i = input(f"{W}Ingrese opción: ")
    while i not in ('1', '2'): i = input(f"{C}Ingrese una opción válida!: ")
    if i == '1':
        with open('caso1.json', 'r') as file:
            cargarData(load(file))
    elif i == '2':
        with open('caso2.json', 'r') as file:
            cargarData(load(file))
    print(f"{C}\nArchivo cargado exitosamente!...")
    return 1


def cargarData(dic):
    """ Reasigna la matriz de eventos por una sin objetos y lo llena con nuevos datos,
    reasigna el valor del diccionario por el diccionario cargado.
    :param dic: diccionario con los datos a reasignar

    """
    global matriz, objetos
    matriz = [[' ' if x == y == 0 else str(y - 1) if x == 0 else str(x - 1) if y == 0 else '.'
               for y in range(c)] for x in range(f)]
    objetos = dic.copy()
    for key in objetos:
        x, y = objetos[key]['Posicion']
        color = objetos[key]['Color']
        matriz[x][y] = color


""" ======================================= Opcion [0] Guardar y salir ============================================= """


def GuardarArchivo():
    print(f"{W}{guardar}")
    i = input(f"{W}\nIngrese opción: ")
    while i not in ('0', '1', '2'): i = input(f"{C}Ingrese una opción válida!: ")
    if i == '0':
        return 0
    elif i == '1':
        with open('caso1.json', 'w') as file:
            dump(objetos, file, indent=4, sort_keys=True)
    elif i == '2':
        with open('caso2.json', 'w') as file:
            dump(objetos, file, indent=4, sort_keys=True)
    print(f"{C}\nArchivo guardado exitosamente!...")
    return 0
