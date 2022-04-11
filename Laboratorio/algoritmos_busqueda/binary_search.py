def binary_search(arr, n):
    # complejidad en tiempo de O(log(n))
    # complejidad en espacio de O(1)

    min_idx, max_idx = 0, len(arr) - 1
    while True:
        if max_idx < min_idx:
            return -1
        else:
            mid = (min_idx + max_idx) // 2
            if arr[mid] < n:
                min_idx = mid + 1
            elif arr[mid] > n:
                max_idx = mid - 1
            else:
                return mid


def binary_search_recursive(arr, n, start=0, stop=None):
    stop = (len(arr) - 1) if stop is None else stop
    mid = (stop - start) // 2 + start

    if start <= stop:
        if arr[mid] == n:
            return mid
        elif arr[mid] < n:
            return binary_search_recursive(arr, n, start=mid+1, stop=stop)
        elif arr[mid] > n:
            return binary_search_recursive(arr, n, start=0, stop=mid-1)
    else:
        return -1


lista = [0, 2, 4, 5, 6, 8, 10, 12, 14, 16, 18]
for i in range(20):
    var = binary_search_recursive(lista, i)
    print(f'El número {i} {f"no está en la lista" if var == (-1) else f"está en la posición [{var}]"}')
