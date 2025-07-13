def ejercicio1():
    n = int(input("Número (1-10): "))
    archivo = open("tabla-" + str(n) + ".txt", "w")
    for i in range(1, 11):
        archivo.write(str(n) + " x " + str(i) + " = " + str(n * i) + "\n")
    archivo.close()
    print("Tabla guardada.")

ejercicio1()
