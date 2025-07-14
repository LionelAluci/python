def ej2():
    n = int(input("Número (1-10): "))
    try:
        archivo = open("tabla-" + str(n) + ".txt", "r")
        print(archivo.read())
        archivo.close()
    except:
        print("El archivo no existe.")

ej2()
