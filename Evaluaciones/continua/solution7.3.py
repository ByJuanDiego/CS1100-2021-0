# Pregunta N˚2:
def p2(n):
    if n == 1:
        return 1
    else:
        return 1/n + p2(n-1)

# Pregunta N˚3:
def p3(n):
    if n == 1:
        return 1
    else:
        return n*p3(n-1)

# Pregunta N˚4:
def p4(n, x):
    if n-x <= 0:
        print('Fin\n')
    else:
        print(n, end=" ")
        return p4(n-x, x)

# Pregunta N˚10:
def p10(start, stop):
    if start < stop:
        return start * p10(start+1, stop)
    else:
        return stop

# Pregunta N˚11:
def p11(start, stop):
    if start < stop:
        return start + p11(start+1, stop)
    else:
        return stop

# Pregunta N˚12:
def p12(n):
    if n == 1:
        return n
    else:
        return n + p12(n-1)

# Pregunta N˚15:
def p15(n, d):
    if n == 1:
        return 1/d
    else:
        return n/d + p15(n-1, d)

# Pregunta N˚16:
def p16(n, p):
    if n == 1:
        return p*1
    else:
        return n*p + p16(n-1, p)

# Pregunta N˚17:
def p17(num):
    def suma_digitos(n):
        if n == 0:
            return n
        else:
            return n % 10 + suma_digitos(n//10)
    suma = suma_digitos(num)
    if suma % 3 == 0:
        return "La suma de los digitos es: {}\nEl numero SI es divisible por 3".format(suma)
    else:
        return "La suma de los digitos es: {}\nEl numero NO es divisible por 3".format(suma)

# Pregunta N˚19:
def p19(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        arr[len(arr)-2] += arr[len(arr)-1]
        del arr[len(arr)-1]
        return p19(arr)

# ----------------------------------------------------------------------------

print("P2:\n{}\n".format(round(p2(10), 3)))       # P2

print("P3:\n{}\n".format(p3(5)))           # P3

print("P4:")
p4(40, 5)                                  # P4

print("P10:\n{}\n".format(p10(30, 35)))    # P10

print("P11:\n{}\n".format(p11(30, 35)))    # P11

print("P12:\n{}\n".format(p12(30)))        # P12

print("P15:\n{}\n".format(p15(3, 2)))      # P15

print("P16:\n{}\n".format(p16(5, 2)))      # P16

print("P17:\n{}\n".format(p17(14587629)))  # P17

print("P19:\n{}\n".format(p19([1.2, 1.0, 1.0, 1.0, 1.0])))  # P19
