""" Se dice que un numero es tramposo cuando:
-Es negativo
-Es menor a.a 100 y es multiplo de 3 pero no de 6
-Es mayor o igual a.a 100 y termina en 1 """
n = int(input("Ingrese un numero: "))

if n < 0:
    print("Es tramposo")
elif n < 100 and n % 3 == 0 and 0 != n % 6:
    print("Es tramposo")
elif n >= 100 and n % 10 == 1:
    print("Es tramposo")
else:
    print("No es tramposo")
