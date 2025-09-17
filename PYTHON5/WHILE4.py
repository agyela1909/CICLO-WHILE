#WHILE4
#CarolAgyelaGonzalezOchoa

respuesta="doble"
while (respuesta!="N") or (respuesta!="n"):
    # Leer un número
    numero = float(input("Ingrese un número: "))

    # Calcular el doble
    doble = numero * 2

    # Mostrar el resultado
    print(f"El doble de {numero} es: {doble}")

    # Preguntar si desea continuar
    continuar = input("¿Desea continuar? [S/N]: ")

print("Programa finalizado.")