from math import cos, radians

print("Input:")
N = int(input("N: "))
suma = 0

while True:
    t = int(input("grado : "))
    if (-10) <= t <= 10: break
t = radians(t)

for i in range(1, N+1): suma += cos(i*t)

print("Output:")
print(suma/N)
