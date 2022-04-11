import csv

with open('Diccionario_Datos.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0].split(";")[0])
