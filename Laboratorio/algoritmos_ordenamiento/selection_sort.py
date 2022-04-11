from random import randint as rd


def selection_sort(arr):
    # Complejidad en tiempo de O(n**(2))

    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


array = [rd(0, 100) for _ in range(10)]
print(selection_sort(array))
