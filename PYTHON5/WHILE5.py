#WHILE5
#CarolAgyelaGonzalezOchoa

respuesta="MESES"
while (respuesta!="N") or (respuesta!="n"):
    meses = []
    entrada = ""

    while entrada.lower() != "ninguno":
        entrada = input("Ingrese el nombre de un mes (o 'ninguno' para terminar): ")

        if entrada.lower() != "ninguno":
            meses.append(entrada)

    # Mostrar los meses ingresados
    print("\nMeses ingresados:")
    for mes in meses:
        print(mes)

    print("Programa finalizado.")

