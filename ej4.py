import urllib.request

def ejercicio4():
    url = input("URL: ")
    try:
        pagina = urllib.request.urlopen(url)
        texto = pagina.read().decode("utf-8")
        palabras = texto.split()
        print("Cantidad de palabras:", len(palabras))
    except:
        print("No se pudo acceder a la URL.")

ejercicio4()
