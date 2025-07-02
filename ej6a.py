import csv

def leer_cotizaciones(nombre_archivo):
    columnas = {}
    with open(nombre_archivo, "r") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            for clave, valor in fila.items():
                if clave not in columnas:
                    columnas[clave] = []
                try:
                    columnas[clave].append(float(valor.replace(",", "").replace("€", "")))
                except:
                    columnas[clave].append(valor)
    return columnas