def ejercicio6_parte1():
    archivo = open("cotizacion.csv", "r")
    lineas = archivo.readlines()
    archivo.close()

    columnas = lineas[0].strip().split(",")
    datos = {}

    for col in columnas:
        datos[col] = []

    for linea in lineas[1:]:
        partes = linea.strip().split(",")
        for i in range(len(columnas)):
            datos[columnas[i]].append(partes[i])

    return datos

def ejercicio6_parte2():
    datos = ejercicio6_parte1()
    archivo = open("resumen.csv", "w")
    archivo.write("Columna,Mínimo,Maximo,Media\n")

    for clave in datos:
        try:
            numeros = [float(x) for x in datos[clave]]
            minimo = min(numeros)
            maximo = max(numeros)
            media = sum(numeros) / len(numeros)
            archivo.write(f"{clave},{minimo},{maximo},{media}\n")
        except:
            pass  # salta columnas con texto

    archivo.close()
    print("Resumen guardado.")

ejercicio6_parte2()
