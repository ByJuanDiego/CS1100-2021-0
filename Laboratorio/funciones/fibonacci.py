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

    def fibo(n):
        global count2
        count2 += 1
        if n == 0 or n == 1:
            cache[0] = 0
            cache[1] = 1
        else:
            fibo(n - 1)
            cache[n] = cache[n - 1] + cache[n - 2]

    fibo(n)
    return cache[n]


print("Con recursividad clasico:", fibonacci(30))
print("Cantidad de llamadas:", count1)

print("Con recursividad PD:", fibonacci2(30))
print("Cantidad de llamadas:", count2)
