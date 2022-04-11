def binarySearch(arr, n):
    # complejidad en tiempo  de O(log(n))
    # complejidad en espacio de O(1)

    min, max = 0, len(arr) - 1
    while True:
        if max < min: return -1
        mid = (min + max) // 2
        if arr[mid] < n:
            min = mid + 1
        elif arr[mid] > n:
            max = mid - 1
        else:
            return mid


def binarySearch_recursive(arr, n):
    mid = len(arr) // 2
    if arr[mid] > n:
        return binarySearch_recursive(arr[:mid], n)
    elif arr[mid] < n:
        return binarySearch_recursive(arr[mid:], n)

# lista = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# n = 20
# print(binarySearch(lista, n))
# print(binarySearch_recursive(lista, n))
# print(binarySearch_recursive(lista, 4))
