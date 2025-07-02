import urllib.request

def contar_palabras():
    url = input("Introduce la URL: ")
    try:
        with urllib.request.urlopen(url) as response:
            contenido = response.read().decode("utf-8")
            palabras = contenido.split()
            print(f"Número de palabras: {len(palabras)}")
    except Exception as e:
        print("Error al acceder a la URL:", e)

contar_palabras()