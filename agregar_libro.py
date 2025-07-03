import requests

url = "http://library.demo.local/api/v1/books"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Token cisco|ffgu68tXbWCyt58cCKdxrTNEX6dPOROrvDmESKeNyHc"
}

     "id":20
    "title": "exame Final ProgramacionRedes",
    "author": "erika villca gutierrez"
}

respuesta = requests.post(url, headers=headers, json=nuevo_libro)

if respuesta.status_code == 200:
    print("Libro agregado correctamente:", respuesta.json())
else:
    print("Error al agregar el libro:", respuesta.status_code, respuesta.text)
