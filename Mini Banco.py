saldo=50000
opcion=""

while opcion!="4":
    print("""
====| MINI-BANK |=====
    
1. Consultar dinero
2. Ingresar dnero
3. Retirar dinero
4. Salir

======================
    """)
    opcion = input("Elija una opción: ")
    match opcion:
        case "1":  
            print(f"Su saldo actúal es de: ${saldo}")
        case "2":
            while True:
                dinero=input("Ingrese la cantidad que desee guardar: ").strip()
                if not dinero.isdigit():
                    print("Error: Ingresó un carácter no numérico.")
                    print("")
                else:
                    dinero = int(dinero)
                    if dinero <= 0:
                        print("Error: no puede ingresar cantidades negativas.")
                        print("")
                    else:
                        saldo+=dinero
                        print(f"Se ha agregado correctamente ${dinero} a su cuenta. Saldo actual: ${saldo}")
                        print("")
                        break
        case "3":
            while True:
                dinero_retiro = (input("Ingrese la cantidad que desea retirar: ")).strip()
                if not dinero_retiro.isdigit():
                    print("Error: ingresó un carácter no numérico.")
                    print("")
                else:
                    dinero_retiro = int(dinero_retiro)
                    if dinero_retiro > saldo:
                        print("Error: el dinero a retirar es mayor que su saldo.")
                        print("")
                    elif dinero_retiro <= 0:
                        print("El dinero a retirar es negativo u es 0.")
                        print("")
                    else:
                        saldo-=dinero_retiro
                        print(f"Se ha retirado ${dinero_retiro} de su cuenta. Saldo actual: ${saldo}")
                        print("")
                        break
        case "4":
            print("hasta luego!")
        case _:
            print("Error: Ingresó una opcion no válida.")