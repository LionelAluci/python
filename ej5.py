import urllib.request

def pib_por_pais():
    url = "https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true"
    iniciales = input("Introduce las iniciales del país (por ejemplo: ES): ").upper()

    try:
        with urllib.request.urlopen(url) as response:
            datos = response.read().decode("utf-8")
            for linea in datos.splitlines():
                if linea.startswith(iniciales):
                    print(f"Datos del país {iniciales}:\n{linea}")
                    break
            else:
                print("País no encontrado.")
    except Exception as e:
        print("Error al acceder al archivo:", e)

pib_por_pais()