import urllib.request
import gzip

def ejercicio5():
    url = "https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true"
    pais = input("Iniciales del país (ej: ES): ")
    try:
        datos = urllib.request.urlopen(url).read()
        texto = datos.decode("utf-8")
        for linea in texto.split("\n"):
            if linea.startswith(pais):
                print(linea)
                return
        print("País no encontrado.")
    except:
        print("No se pudo acceder al archivo.")

ejercicio5()
