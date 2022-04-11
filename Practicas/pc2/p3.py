def precio(servicio, distancia, tiempo):
    precio = 0

    if servicio == "UBER": precio = 1.2*distancia + 0.1*tiempo

    elif servicio == "Cabify":
        if distancia <= 20: precio = 1.65*distancia
        else: precio = 1.65*20 + 1.1*(distancia-20)

    elif servicio == "TaxiBeat": precio = 2.4 + 1.05*distancia + 0.34*tiempo

    return precio


servicios = ["UBER", "Cabify", "TaxiBeat"]
distancia = 50  # valor de la distancia
tiempo = 20     # valor del tiempo

for i in servicios: print(f"{i}: {round(precio(i, distancia, tiempo), 2)}")
