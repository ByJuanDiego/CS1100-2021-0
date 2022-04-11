def suma(a, b):
    if b == 0:
        return a
    else:
        return 1 + suma(a, b - 1)


print(suma(21, 3))
