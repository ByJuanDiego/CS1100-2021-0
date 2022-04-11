from random import randint as rd


def merge(lista, left, right):
    posL = posR = posF = 0
    while posL < len(left) and posR < len(right):
        if left[posL] < right[posR]:
            lista[posF] = left[posL]
            posL += 1
        else:
            lista[posF] = right[posR]
            posR += 1
        posF += 1
    while posL < (len(left)):
        lista[posF] = left[posL]
        posL += 1
        posF += 1
    while posR < (len(right)):
        lista[posF] = right[posR]
        posR += 1
        posF += 1


def merge_sort(lista):
    if len(lista) > 1:
        mid = len(lista) // 2
        left = lista[:mid]
        right = lista[mid:]
        merge_sort(left)
        merge_sort(right)
        merge(lista, left, right)


array = [rd(0, 100) for _ in range(10)]
merge_sort(array)
print(array)
