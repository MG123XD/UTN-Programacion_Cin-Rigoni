lista_temp = []

while True:
    temperatura = input("Ingrese una temperatura, si desea finalizar escriba FIN: ").strip().upper()
    if temperatura == "":
        print("Error: éste campo es obligatorio.")
        print("")
        continue
    elif temperatura == "FIN":
        print("Sesión Finalizada.")
        break

    puntos = 0
    es_digito = True
    for caracter in temperatura:
        if caracter == ".":
            puntos += 1
            if puntos > 1:
                print("Error: ingrese un solo punto para números decimales.")
                print("")
                break
        elif not caracter.isdigit():
            es_digito = False

    if es_digito == False:
        print("Error: ingresó un carácter no válido.")
        print("")
        continue

    temperatura = float(temperatura)
    if temperatura > 500 or temperatura < 100:
        lista_temp.append(temperatura)
        print("¡ADVERTENCIA! Temperatura fuera de rango!")
    else:
        lista_temp.append(temperatura)

    print(f"Se ha agregado la temperatura: {temperatura}°C")
    print("")

        
