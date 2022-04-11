from colorama import init, Fore

init(autoreset=True)

G = Fore.WHITE
W = Fore.LIGHTWHITE_EX
C = Fore.LIGHTCYAN_EX

f = 22
c = 18

matriz = [[' ' if x == y == 0 else str(y - 1) if x == 0 else str(x - 1) if y == 0 else '.'
           for y in range(c)] for x in range(f)]

objetos = {}

menu = """MENU
--------
1. Agrega nuevo objeto
2. Borrar objeto
3. Mostrar Mapa
4. Mostrar plan de navegación
5. Delegar Tarea
6. Cargar Archivo
0. Guardar y salir
"""

guardar = """Seleccione el archivo donde lo quiere guardar:
No guardar [0]
caso1.json [1]
caso2.json [2]"""

cargar = """Seleccione el archivo a cargar:
caso1.json [1]
caso2.json [2]
"""
