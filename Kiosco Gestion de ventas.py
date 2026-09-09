lista_compras = []

while True:
    opcion = input("¿Quiere ingresar al Kiosco? (si/no) ").strip().lower()
    if opcion == 'si':
        while True:
            print(""" 
===== KIOSCO - GESTIÓN DE VENTAS =====

1. Registrar venta
2. Ver listado de ventas del turno
3. Ver total recaudado
4. Cerrar caja y salir
""")
            opcion = input("Elija una opción: ")

            match opcion:
                case '1':
                    producto = input("¿Qué producto desea comprar? ")
                    while True:
                        precio = input("¿Cuál es el precio de este producto? ")
                        if precio.isalpha():
                            print("Error: ingreso un caracter no numérico")
                            continue
                        precio = int(precio)
                        if precio < 0:
                            print("Error: ingreso un digito negativo")
                            continue
                        if precio > 0:
                            break
                    while True:
                        cantidad = input("¿Cuantas unidades desea comprar de éste producto? ")
                        if cantidad.isalpha():
                            print("Error: ingreso un caracter no numérico")
                            continue
                        cantidad = int(cantidad)
                        if cantidad < 0:
                            print("Error: ingreso un digito negativo")
                            continue
                        if cantidad > 0:
                            break

                    precio = int(precio)
                    cantidad = int(cantidad)
                    subtotal = precio * cantidad
                    if subtotal > 10000:
                        descuento = 10 / 100 * subtotal
                        desc_subtotal = subtotal - descuento
                    productos += 1
                    print(" ")
                    print("El producto se ha registrado correctamente!")
                    print(" ")


                case '2':
                    for lista in range(productos):
                        print(f"{productos}. ")
                case '3':
                    break
                case '4':
                    break

    elif opcion == 'no':
        break
    else:
        print("Error: ingreso un valor no especificado.")

