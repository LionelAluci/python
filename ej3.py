def ejercicio3():
    n = int(input("Número (1-10): "))
    m = int(input("Línea (1-10): "))
    try:
        archivo = open("tabla-" + str(n) + ".txt", "r")
        lineas = archivo.readlines()
        print("Línea", m, ":", lineas[m - 1])
        archivo.close()
    except:
        print("El archivo no existe o la línea es incorrecta.")

ejercicio3()
