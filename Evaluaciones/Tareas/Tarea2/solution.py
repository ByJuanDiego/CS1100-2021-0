import requests
from io import BytesIO
import numpy as np
from PIL import Image

class Solution:
    """FILTROS IMAGENES"""

    # Cuatro tonalidades
    def cuatroTonalidades(self, linkImagen):
        response = requests.get(linkImagen)
        img = Image.open(BytesIO(response.content))
        img_arr = np.array(img)
        mitad_f, mitad_c = len(img_arr)//2, len(img_arr[0])//2

        for f in range(len(img_arr)):
            for c in range(len(img_arr[0])):

                if f < mitad_f and c < mitad_c:
                    img_arr[f][c][1], img_arr[f][c][2] = 0, 0
                elif f < mitad_f and c >= mitad_c:
                    img_arr[f][c][0], img_arr[f][c][2] = 0, 0
                elif f >= mitad_f and c < mitad_c:
                    img_arr[f][c][0], img_arr[f][c][1] = 0, 0
                elif f >= mitad_f and c >= mitad_c:
                    avg = 0
                    for rgb in img_arr[f][c]:
                        avg += rgb
                    avg //= 3
                    img_arr[f][c] = [avg, avg, avg]

        return Image.fromarray(img_arr)

    # Puzzle
    def puzzle(self, linkImagen, tono='Default'):
        response = requests.get(linkImagen)
        img = Image.open(BytesIO(response.content))
        img_arr = np.array(img)
        mitad_f = len(img_arr)//2
        for f in range(len(img_arr)):
            for c in range(len(img_arr[0])):
                if tono == 'r':
                    img_arr[f][c][1], img_arr[f][c][2] = 0, 0
                elif tono == 'g':
                    img_arr[f][c][0], img_arr[f][c][2] = 0, 0
                elif tono == 'b':
                    img_arr[f][c][0], img_arr[f][c][1] = 0, 0
                else:
                    avg = 0
                    for rgb in img_arr[f][c]:
                        avg += rgb
                    avg //= 3
                    img_arr[f][c] = [avg, avg, avg]
        copia = img_arr.copy()
        for f in range(len(img_arr)):
            for c in range(len(img_arr[0])):
                if len(img_arr) % 2 == 0:
                    if f < mitad_f:
                        img_arr[f][c] = copia[f+mitad_f][c]
                    elif f >= mitad_f:
                        img_arr[f][c] = copia[f-mitad_f][c]
                elif len(img_arr) % 2 != 0:
                    if f <= mitad_f:
                        img_arr[f][c] = copia[f+mitad_f][c]
                    elif f > mitad_f:
                        img_arr[f][c] = copia[f-mitad_f-1][c]
        return Image.fromarray(img_arr)

    # Linea Vertical
    def lineaVertical(self, startAt, size, color, linkImagen):
        response = requests.get(linkImagen)
        img = Image.open(BytesIO(response.content))
        img_arr = np.array(img)

        if size < 0:
            size = size * (-1)
        if startAt < len(img_arr[0]):
            for i in range(len(img_arr)):
                j = 0
                while (j < size) and (startAt+j < len(img_arr[0])):
                    img_arr[i][startAt + j] = color
                    j += 1
        return Image.fromarray(img_arr)

    # Cruz
    def cruz(self, tamanhoCruz, color, linkImagen):
        response = requests.get(linkImagen)
        img = Image.open(BytesIO(response.content))
        img_arr = np.array(img)
        tamanhoCruz = abs(tamanhoCruz)

        if tamanhoCruz >= len(img_arr) or tamanhoCruz >= len(img_arr[0]):
            for f in range(len(img_arr)):
                for c in range(len(img_arr[0])):
                    img_arr[f][c] = color

        else:
            limiInfFils = len(img_arr)//2 - tamanhoCruz//2
            limSupFils = len(img_arr)//2 + tamanhoCruz//2
            limInfCols = len(img_arr[0])//2 - tamanhoCruz//2
            limSupCols = len(img_arr[0])//2 + tamanhoCruz//2

            for f in range(len(img_arr)):
                for c in range(len(img_arr[0])):
                    if limiInfFils <= f < limSupFils or limInfCols <= c < limSupCols:
                        pass
                    else:
                        img_arr[f][c] = color
        return Image.fromarray(img_arr)

    # Marco de imagen
    def marcoImagen(self, tamanhoMarco, color, linkImagen):
        response = requests.get(linkImagen)
        img = Image.open(BytesIO(response.content))
        img_arr = np.array(img)
        if tamanhoMarco < 0:  # Observacion
            tamanhoMarco *= (-1)
        if (tamanhoMarco >= len(img_arr)) or (tamanhoMarco >= len(img_arr[0])):  # Observacion
            return Image.fromarray(img_arr)
        else:
            for f in range(len(img_arr)):
                for c in range(len(img_arr[0])):
                    if (f < tamanhoMarco) or (f > len(img_arr)-tamanhoMarco-1):
                        pass
                    elif (c < tamanhoMarco) or (c > len(img_arr[0])-tamanhoMarco-1):
                        pass
                    else:
                        img_arr[f][c] = color
            return Image.fromarray(img_arr)

    # Marco color
    def marcoColor(self, tamanhoMarco, color, linkImagen):
        response = requests.get(linkImagen)
        img = Image.open(BytesIO(response.content))
        img_arr = np.array(img)

        if tamanhoMarco < 0:  # Observacion
            tamanhoMarco *= (-1)
        if (tamanhoMarco >= len(img_arr)) or (tamanhoMarco >= len(img_arr[0])):  # Observacion
            for f in range(len(img_arr)):
                for c in range(len(img_arr[0])):
                    img_arr[f][c] = color
            return Image.fromarray(img_arr)
        else:
            for f in range(len(img_arr)):
                for c in range(len(img_arr[0])):
                    if (f < tamanhoMarco) or (c < tamanhoMarco) or (f > len(img_arr)-tamanhoMarco-1) or (c > len(img_arr[0])-tamanhoMarco-1):
                        img_arr[f][c] = color
                    else:
                        pass
            return Image.fromarray(img_arr)

link = 'http://2.bp.blogspot.com/-sDudoynEP9I/Tbwru6HsvJI/AAAAAAAAAE0/_XZrUyCN9JA/s1600/modern-cheerful-children-room-interior-design1.jpg'
fi = Solution()
fi.cuatroTonalidades(link).save('CuatroTonalidades.jpg')
fi.puzzle(link, 'r').save('Puzzle.jpg')
fi.lineaVertical(500, 400, [220, 12, 70], link).save('LineaVertical.jpg')
fi.cruz(101, [0, 0, 0], link).save('Cruz.jpg')
fi.marcoImagen(250, [240, 200, 200], link).save('MarcoImagen.jpg')
fi.marcoColor(150, [240, 5, 240], link).save('MarcoColor.jpg')
550 , 650
