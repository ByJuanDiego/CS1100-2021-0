# Contadores de numeros
n_num = 0   # contador de numeros
n_imp = 0   # contador de impares
n_pares = 0     # contador de numeros pares
sum_pares = 0       # suma de numeros pares
prom_pares = 0      # promedio de numeros pares
n_menor_impar = 0       # numero menor impar
n_mayor_impar = 0       # numero mayor impar

while True:

    num = int(input("Ingrese numero: "))

    if (n_imp == 0) and (num % 2 != 0) and (num >= 0):
        n_menor_impar = num
        n_imp += 1

    elif (n_imp > 0) and (num % 2 != 0) and (num >= 0):
        n_imp += 1
        if num < n_menor_impar:
            n_menor_impar = num

    if (num > n_mayor_impar) and (num % 2 != 0) and (num >= 0):
        n_mayor_impar = num

    if num % 2 == 0:
        n_pares += 1
        sum_pares += num

    if num < 0:
        break

    elif not num < 0:
        n_num += 1

prom_pares = sum_pares / n_pares

print("Cantidad de numeros: {}".format(n_num))
print("Promedio pares: {}".format(prom_pares))
print("Mayor numero impar: {}".format(n_mayor_impar))
print("Menor numero impar: {}".format(n_menor_impar))
