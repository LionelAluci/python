def leer_tabla():
    n = int(input("Introduce un número entre 1 y 10: "))
    nombre_archivo = f"tabla-{n}.txt"
    try:
        with open(nombre_archivo, "r") as archivo:
            contenido = archivo.read()
            print(f"Contenido de la tabla del {n}:\n{contenido}")
    except FileNotFoundError:
        print(f"No existe el archivo {nombre_archivo}")

leer_tabla()