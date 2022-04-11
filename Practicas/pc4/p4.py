def binarySearch(arr, n):
    i = 0
    min, max = 0, len(arr)-1

    while True:
        if max<min: return 'No se encontró la bola'
        mid = (min+max)//2
        if arr[mid]>n:
            min = mid+1
            i += 1
        elif arr[mid]<n:
            max = mid-1
            i += 1
        else: return i+1

arr = input("Input:\n").split(',')
arr = [int(arr[i]) for i in range(len(arr))]

n = int(input(""))
print(binarySearch(arr, n))
