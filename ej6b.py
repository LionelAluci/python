def resumen_columnas(diccionario, salida="resumen.csv"):
    with open(salida, "w", newline="") as f:
        escritor = csv.writer(f)
        escritor.writerow(["Columna", "Mínimo", "Máximo", "Media"])
        for clave, valores in diccionario.items():
            if all(isinstance(x, (int, float)) for x in valores):
                minimo = min(valores)
                maximo = max(valores)
                media = sum(valores) / len(valores)
                escritor.writerow([clave, minimo, maximo, media])
    print(f"Resumen guardado en {salida}")