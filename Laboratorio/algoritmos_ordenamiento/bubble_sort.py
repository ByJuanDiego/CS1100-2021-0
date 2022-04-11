from random import randint as rd


def bubble_sort(arr):
    # Complejidad en tiempo de O(n**(2))

    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


array = [rd(0, 100) for _ in range(10)]
print(bubble_sort(array))
