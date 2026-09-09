hamburguesa = 4500
papas = 2000
bebida = 1500
costo_final = 0
pago = 0
ticket = 0
opcion = ""
while opcion != "5":
    print("""
    -=-=-=-=-| FAST-FOOD |-=-=-=-=-

    1. Agregar Hamburguesa $4500
    2. Agregar Papas fritas $2000
    3. Agregar Bebida $1500
    4. Pagar el pedido (cierra ticket)
    5. Cancelar pedido y salir

    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    """)

    opcion = input("ingrese una opcion de la lista: ")
    match opcion:
        case "1":
            costo_final += hamburguesa
            print("")
            print("Se agrego una hamburguesa a su pedido, total actual $",costo_final)
        case "2":
            costo_final += papas
            print("")
            print("Se agrego papas fritas a su pedido, total actual $",costo_final)
        case "3":
            costo_final += bebida
            print("")
            print("se agrego bebida a su pedido, total actual $",costo_final)
        case "4":
                while True:
                    print("")
                    print("el costo del pedido es $",costo_final)
                    pago = input("Ingrese el dinero en efectivo: ")
                    if not pago.isdigit():
                        print("")
                        print("Error, ingresó un carácter no numérico")
                    else:
                        pago = int(pago)
                        if pago < costo_final:
                            costo_final = costo_final - pago
                            print("")
                            print("faltan $",costo_final,"para pagar todo")
                        elif pago == costo_final:
                            print("")
                            print("Se realizo el pago completo")
                            costo_final = 0
                            ticket = 0
                            break
                        elif pago > costo_final:
                            ticket = pago - costo_final
                            print("")
                            print("su vuelto es $",ticket)
                            costo_final = 0
                            ticket = 0
                            break
        case "5":
            print("")
            print("hasta luego!")
        case _:
            print("")
            print("Error: Ingreso un digito no válido!")