def suma_n(n):
    if n == 1:
        return 1
    else:
        return n + suma_n(n - 1)


a = int(input("Ingrese n: "))
print(suma_n(a))
