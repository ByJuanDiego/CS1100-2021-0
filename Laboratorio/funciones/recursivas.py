# Created by JD y Sam

def suma_pares_lista(lista, contador=0):
    if not lista:
        return contador
    else:
        return suma_pares_lista(lista[1::], contador+(1 if lista[0] % 2 == 0 else 0))


print(suma_pares_lista([1, 2, 3, 3, 2, 4]))
print(suma_pares_lista([1]))
print(suma_pares_lista([2]))
