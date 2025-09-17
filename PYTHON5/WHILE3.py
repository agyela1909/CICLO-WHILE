#WHILE3
#CarolAgyelaGonzalezOchoa

calificaciones = []
continuar = 'S'

respuesta="calificacion"
while (respuesta!="N") or (respuesta!="n"):
    # Leer calificación
    calificacion = float(input("Ingrese la calificación: "))
    calificaciones.append(calificacion)

    # Preguntar si desea continuar
    continuar = input("¿Desea continuar? [S/N]: ")

# Calcular y mostrar el promedio
if calificaciones:
    promedio = sum(calificaciones) / len(calificaciones)
    print(f"El promedio de las calificaciones es: {promedio:.2f}")
else:
    print("No se ingresaron calificaciones.")
