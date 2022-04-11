
def agregarProducto(dic, i):
    producto = input("Producto [{}]: ".format(i+1))
    precio = float(input("Precio [{}]: ".format(i+1)))
    cantidad = int(input("Cantidad [{}]: ".format(i + 1)))
    dic.update({producto: {}})
    dic[producto].update({'Precio': precio})
    dic[producto].update({'Cantidad': cantidad})
    return dic

def calcularCostos(dic, IGV):
    precio_igv = 0
    precio_producto = 0
    for key in dic.keys():
        precio_producto += dic[key]['Precio'] * dic[key]['Cantidad']
        precio_igv += dic[key]['Precio'] * dic[key]['Cantidad'] * IGV
    monto_a_pagar = precio_producto + precio_igv
    return precio_igv, monto_a_pagar

IGV = 18/100
diccionario = {}
n = int(input("Input: "))
print()

for i in range(n):
    agregarProducto(diccionario, i)
    print()

precioIGV, precioTotal = calcularCostos(diccionario, IGV)
print('Output\nEl IGV es {} y el monto a pagar es {}'.format(precioIGV, precioTotal))
