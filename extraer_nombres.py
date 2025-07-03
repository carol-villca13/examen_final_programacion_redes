import json

with open("usuarios.json", "r") as archivo:
    datos = json.load(archivo)

for usuario in datos:
    print(usuario["nombre"])
