s = int(input("Ingresa el tiempo que ha pasado en segundos: "))

m = s//60
s -= m*60
h = m//60
m -= h*60

print("Horas pasadas: {}\nMinutos pasados: {}\nSegundos pasados: {}".format(h, m, s))
