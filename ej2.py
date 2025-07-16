def ej2():
    n = int(input("numero (1-10): "))
    try:
        archivo = open("tabla-" + str(n) + ".txt", "r")
        print(archivo.read())
        archivo.close()
    except ValueError:
        print("ingresa un numero valido")
    except FileNotFoundError:
        print("el archivo no existe")

ej2()
