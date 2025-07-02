def guardar_tabla():
    n = int(input("Introduce un número entre 1 y 10: "))
    if 1 <= n <= 10:
        nombre_archivo = f"tabla-{n}.txt"
        with open(nombre_archivo, "w") as archivo:
            for i in range(1, 11):
                archivo.write(f"{n} x {i} = {n*i}\n")
        print(f"Tabla del {n} guardada en {nombre_archivo}")
    else:
        print("Número fuera de rango.")

guardar_tabla()