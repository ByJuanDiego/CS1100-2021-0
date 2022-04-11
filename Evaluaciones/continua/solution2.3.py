""" En el curso “Introducción a la Ciencia de la Computación” el profesor desea eximir del “Examen Final” a los
alumnos que tienen promedio mayor a 15, pero, siempre y cuando no haya desaprobado ninguna PC. Se sabe que el
alumno dio tres PC’s. Escriba un algoritmo que permita imprimir los alumnos eximidos con su respectivo promedio,
las notas son como sigue:

                                    PC1      PC2     PC3
                                1)  10       16      13
                                2)  17       10      11
                                3)  15       17      14
                                4)  10       16      16
                                5)  10       16      16
                                6)  10       16      16
                                7)  10       16      16 """
def eximidos():
    n_eximidos = 0
    eximidos = ""
    susNotas = ""
    for alumno in range(1, 8):

        jaladoEnPC = False
        sumaDeNotas = 0

        for notas in range(1, 4):
            nota = int(input("Ingrese la nota [{}] del alumno [{}]: ".format(notas, alumno)))
            sumaDeNotas += nota
            if nota < 10.5:
                jaladoEnPC = True

        promedio = sumaDeNotas / 3
        print("El promedio del alumno {} es: {}".format(alumno, promedio))
        if (jaladoEnPC == False) and (promedio > 15):
            n_eximidos += 1
            if n_eximidos == 1:
                eximidos += str(alumno)
                susNotas += str(round(promedio, 1))
            elif n_eximidos < 7:
                eximidos += ", " + str(alumno)
                susNotas += ", " + str(round(promedio, 1))
            elif n_eximidos == 7:
                eximidos += ", " + str(alumno) + "."
                susNotas += ", " + str(round(promedio, 1)) + "."

    if eximidos == "":
        print("No hay eximidos\n")
    elif eximidos != "":
        print("Los alumnos eximidos son: " + eximidos + ", y sus notas son: " + susNotas + "\n")


"""
    P1) Una de las políticas de la UTEC es premiar a los mejores estudiantes con BECAS para
   pasantías en Universidades Extranjeras y Alejandro es candidato para una
   pasantía en “Harvard University”. Él se averiguó las notas, de las Practicas Calificadas (pcs)
   del curso CS1100,de los 4 candidatos y quiere saber quien tiene el promedio más alto, las notas son lo siguiente:
           PC1   PC2     PC3  PC4
       1)  10     16     13     16
       2)  17     14     11     15
       3)  12     17     16     17
       4)  15     16     16     15
"""
def alumno():
    mayor = 0
    alumno = 0
    for i in range(1, 5):  # lee los alumnos
        sumanota = 0
        for j in range(1, 5):  # lee las notas de los alumnos
            nota = int(input("Ingrese la nota [{}] del alumno [{}]: ".format(j, i)))
            sumanota += nota
        promedio = sumanota / 4
        print("El promedio de alumno[{}] es : {:.2f}".format(i, promedio))
        if i == 1:
            mayor = promedio
        if promedio > mayor:
            mayor = promedio
            alumno = i
    print("El promedio mas alto es {} y es del almuno {}:".format(mayor, alumno))


eximidos()
alumno()
