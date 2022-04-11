count1 = 0
count2 = 0


def fibonacci(n):
    global count1
    count1 += 1
    print(count1)
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci2(n):
    cache = [-1] * (n + 1)

    def fibo(k):
        global count2
        count2 += 1
        if k == 0:
            cache[0] = 0
        elif k == 1:
            cache[0] = 0
            cache[1] = 1
        else:
            fibo(k - 1)
            cache[k] = cache[k - 1] + cache[k - 2]

    fibo(n)
    return cache[n]


print(f"Recursion clasica: {fibonacci(30)}")
print(f"Numero de llamadas: {count1}")

print(f"Recursion dinamica: {fibonacci2(30)}")
print(f"Numero de llamadas: {count2}")
