def mostrar_linea():
    n = int(input("Introduce el número de la tabla (1 a 10): "))
    m = int(input("Introduce la línea que quieres ver (1 a 10): "))
    nombre_archivo = f"tabla-{n}.txt"
    try:
        with open(nombre_archivo, "r") as archivo:
            lineas = archivo.readlines()
            if 1 <= m <= 10:
                print(f"Línea {m}: {lineas[m-1]}")
            else:
                print("La línea está fuera de rango.")
    except FileNotFoundError:
        print(f"No existe el archivo {nombre_archivo}")

mostrar_linea()