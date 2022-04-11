class Solution:
    def __init__(self):
        self.deportefutbol = dict()
        self.deportebasket = dict()
        self.deportegolf = dict()

        solution = open("fans.csv", "r")

        for line in solution:
            if line != "":
                linea_d = line.split(",")
                self.deportefutbol[linea_d[0]] = int(linea_d[1])
                self.deportebasket[linea_d[0]] = int(linea_d[2])
                self.deportegolf[linea_d[0]] = int(linea_d[3])

    def merge_sort0(self, grup):
        if 2 > len(grup):
            return grup
        else:
            medio = (len(grup)) // 2
            der = s.merge_sort0(grup[:medio])
            izq = s.merge_sort0(grup[medio:])
            return s.merge(der, izq)

    def merge(self, grup1, grup2):
        i, j = 0, 0
        result = []
        while i < len(grup1) and j < len(grup2):
            if grup1[i][1] < grup2[j][1]:
                result.append(grup1[i])
                i += 1
            else:
                result.append(grup2[j])
                j += 1
        result += grup2[j:]
        result += grup1[i:]
        return result

    def merge_sort1(self, grup):
        if len(grup) < 2:
            return grup
        else:
            medio = len(grup) // 2
            der = s.merge_sort1(grup[:medio])
            izq = s.merge_sort1(grup[medio:])
            return s.merge1(der, izq)

    def merge1(self, grup1, grup2):
        i, j = 0, 0
        result = []
        while i < len(grup1) and j < len(grup2):
            if grup1[i][1] > grup2[j][1]:
                result.append(grup1[i])
                i += 1
            else:
                result.append(grup2[j])
                j += 1
        result = result + grup1[i:]
        result = result + grup2[j:]
        return result

    def recursivo(self, grup, nbuscado):
        medio = (len(grup)) // 2
        if grup[medio][1] == nbuscado:
            return grup[medio][0]
        elif len(grup) == 1:
            return -1
        else:
            if grup[medio][1] > nbuscado:
                izq = grup[:medio]
                return s.recursivo(izq, nbuscado)
            else:
                der = grup[medio:]
                return s.recursivo(der, nbuscado)

    def ejercicio1(self):
        a = 0
        for i in self.deportebasket:
            if self.deportebasket[i] >= a:
                a = self.deportebasket[i]
                b = i
        return b

    def ejercicio2(self):
        c = s.merge_sort0(list(self.deportefutbol.items()))
        return dict(c)

    def ejercicio3(self, nbuscado):
        g = s.merge_sort0(list(self.deportefutbol.items()))
        return s.recursivo(g, nbuscado)

    def ejercicio4(self):
        d = s.merge_sort1(list(self.deportegolf.items()))
        return dict(d)

#Ejecutamos el programa
s = Solution()
print(s.ejercicio1())
print(s.ejercicio2())
print(s.ejercicio3(20000))
print(s.ejercicio4())
