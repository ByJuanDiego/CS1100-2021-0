def func(arr):
    del arr[1]
    arr.insert(1, arr.pop(len(arr)-2))
    return arr

arr = [4, 15, 25, 35, 14, 48, 86, 48, 14, 16, 80]

print(f"input {arr}")
print(f"output: {func(arr)}")
