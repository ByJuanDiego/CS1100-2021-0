class Solution:

    def Pregunta1(self, data):

        ancho = data[0][0]
        alto = data[0][1]
        R = (data[len(data) - 1][0])
        S = (data[len(data) - 1][1])
        C = data[len(data) - 1][2]

        for fila in range(R, alto):
            for columna in range(S, ancho):

                if data[1][fila][columna] == 0:
                    data[1][fila][columna] = C
            S = 0

        return data[1]

    def CalcularNota(self, n):

        num = 0

        if n < 28: return n
        else:
            while not (num > n): num += 5
            if (num - n) % 2 != 0: return num
            else: return n

    def Pregunta2(self, data2):

        resultado = []
        columnas = data2[0][0]
        filas = data2[0][1]

        for fila in range(filas + 1):
            resultado.append([])
            if fila == 0:
                resultado[fila].append(data2[0][0])
                resultado[fila].append(data2[0][1])
            for columna in range(columnas):
                if fila != 0:
                    nota = data2[fila][columna]
                    nota = Solution().CalcularNota(nota)
                    resultado[fila].append(nota)
        return resultado

data1 = [[8, 5],
         [[2, 1, 1, 1, 1, 1, 1, 1],
          [2, 1, 0, 0, 0, 0, 0, 1],
          [2, 1, 0, 0, 0, 0, 0, 1],
          [2, 1, 0, 0, 0, 0, 0, 1],
          [2, 1, 1, 1, 1, 1, 1, 1]],
         [1, 2, 1]]
data1A = [[9, 6],
          [[2, 2, 1, 1, 1, 1, 3, 3, 1],
           [2, 1, 1, 0, 0, 1, 1, 3, 1],
           [2, 1, 0, 0, 0, 0, 1, 1, 2],
           [2, 1, 0, 0, 1, 1, 1, 1, 2],
           [2, 1, 1, 1, 1, 1, 1, 1, 2],
           [3, 3, 3, 3, 3, 3, 3, 3, 3]],
          [1, 3, 3]]
data2 = [[3, 9],
         [68, 32, 36],
         [46, 29, 42],
         [54, 30, 67],
         [24, 50, 19],
         [37, 27, 30],
         [23, 27, 57],
         [48, 35, 53],
         [51, 31, 45],
         [45, 67, 49]]
data2A = [[4, 10],
          [55, 49, 41, 48],
          [63, 53, 30, 67],
          [40, 26, 53, 33],
          [28, 62, 34, 27],
          [34, 32, 49, 60],
          [51, 47, 58, 50],
          [28, 42, 68, 48],
          [22, 68, 70, 49],
          [20, 54, 60, 62],
          [69, 65, 58, 48]]

for i in Solution().Pregunta1(data1):
    print(i)
print()
for i in Solution().Pregunta1(data1A):
    print(i)
print()
for i in Solution().Pregunta2(data2):
    print(i)
print()
for i in Solution().Pregunta2(data2A):
    print(i)
