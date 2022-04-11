codigo = int(input("Input: "))
digitos = 0
tanques = 0
sumaPares = 0
soldados = 0

while codigo != 0:
    digitos += 1
    digito = codigo % 10
    if digito % 2 == 0:
        sumaPares += digito
    codigo //= 10

tanques = digitos//2
soldados = sumaPares

print(f"Numero de tanques: {tanques}")
print(f"Soldados por tanque: {soldados}")
