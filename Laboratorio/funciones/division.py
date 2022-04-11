def revisionNumero(func):
    def otra_funcion():
        try:
            return func()
        except ValueError:
            print("Tipo de dato erróneo!", end=" ")
            return otra_funcion()
    return otra_funcion

@revisionNumero
def PedirNumero():
    num = int(input("Ingresa número: "))
    return num

n = PedirNumero()
print(n)
