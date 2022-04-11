import json
import urllib.request

pagina = urllib.request.urlopen("http://fspreset.minagri.gob.pe:5000/datos_abiertos_ne")
data = pagina.read()
jsons = json.loads(data)

for i in range(len(jsons)):
    for key, value in jsons[i].items():
        print("{}: {}".format(key, value))
    print()
