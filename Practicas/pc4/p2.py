alumnos = ['Juan', 'Pedro', 'Maria', 'Diego', 'Alessia', 'Luis']

def entrega_de_oculus(arr):
    if len(arr) == 1: print(f'Entregando Oculus a {arr[0]}')
    else: return entrega_de_oculus(arr[:len(arr)//2]), entrega_de_oculus(arr[len(arr)//2:])

entrega_de_oculus(alumnos)
