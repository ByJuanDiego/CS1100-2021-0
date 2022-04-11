def linealSearch(arr, n):
    # Complejidad en tiempo de O(n)
    # Complejidad en espacio de O(1)

    for i in range(len(arr)):
        if arr[i] == n:
            return i
    return -1


lista = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
n = 20
print(linealSearch(lista, n))
