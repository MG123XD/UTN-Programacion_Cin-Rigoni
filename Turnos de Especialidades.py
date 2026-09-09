Especialidades = []
cupos = []
cont=0
while True:
    print("""
========| Clínica-UTN |========
1. Lista de Especialidades
2. Lista de Cupos Disponibles
3. Mostrar Agenda
4. Consultar Cupos por Especialidad
5. Listar Especialidades sin cupos
6. Agregar Especialidad
7. Actualizar cupos (Reservar/Consultar)
8. Salir
""")
    opcion = input("Elija una opcion: ").strip()
    if opcion == "":
        print("Error: Éste campo es obligatorio.")
    elif not opcion.isdigit():
        print("Error: ingresó un carácter no válido.")
    else:
        match opcion:
            case "1":
                while True:
                    cant_esp = input("Ingrese cuántas especialidades quiere agregar: ")
                    if cant_esp == "":
                        print("Error: éste campo es obligatorio.")
                        print("")
                    elif not cant_esp.isdigit():
                        print("Error: ingresó un carácter no válido.")
                        print("")
                    else:
                        cant_esp = int(cant_esp)
                        break
                while cont!=cant_esp:
                    agregar_esp = input("Inserte una nueva especialidad: ").strip().capitalize()
                    if agregar_esp in Especialidades:
                        print("Error: ésta especialidad ya está registrada.")
                    elif agregar_esp == "":
                        print("Error: éste campo es obligatorio.")
                        print("")
                    elif not agregar_esp.isalpha():
                        print("Error: ingresó un carácter no válido.")
                        print("")
                    else:
                        print(f"La especialidad {agregar_esp} se ha agregado correctamente!")
                        print("")
                        Especialidades.append(agregar_esp)
                        cupos.append(0)
                        cont+=1
            case "2":
                bandera = True
                while bandera:
                    if Especialidades == []:
                        print("Error: debe ingresar una especialidad primero.")
                        break
                    agregar_cupo = input("Inserte la especialidad para agregar sus cupos: ").strip().capitalize()
                    if agregar_cupo == "":
                        print("Error: éste campo es obligatorio.")
                        print("")
                    elif not agregar_cupo.isalpha():
                        print("Error: ingresó un carácter no válido.")
                        print("")
                    elif agregar_cupo not in Especialidades:
                        print("Error: ingreso una especialidad no registrada.")
                        print("")
                    else:
                        indice_esp = Especialidades.index(agregar_cupo)
                        while True:
                            cantidad_cupos = input("Agregue la cantidad de cupos de ésta especialidad: ").strip()
                            if cantidad_cupos == "":
                                print("Error: éste campo es obligatorio.")
                                print("")
                            elif not cantidad_cupos.isdigit():
                                print("Error: ingresó un carácter no válido.")
                                print("")
                            else:
                                print(f"La especialidad {agregar_cupo} se le agregaron {cantidad_cupos} cupos correctamente!")
                                print("")
                                cantidad_cupos = int(cantidad_cupos)
                                cupos[indice_esp] = cantidad_cupos
                                bandera = False
                                break
            case "3":
                for i in range(len(Especialidades)):
                    print("===| ", Especialidades[i], "-", cupos[i],)
            case "4":
                while True:
                    consultar = input("Ingrese la especialidad para consultar sus cupos: ").strip().capitalize()
                    if consultar == "":
                        print("Error: éste campo es obligatorio.")
                        print("")
                    elif not consultar.isalpha():
                        print("Error: ingresó un carácter no válido.")
                        print("")
                    elif consultar not in Especialidades:
                        print("Error: ésta especialidad no existe.")
                        print("")
                    else:
                        cupo_cant=Especialidades.index(consultar)
                        print(f"Los cupos disponibles de {consultar} son: {cupos[cupo_cant]}.")
                        break
            case "5":
                for i in range(len(cupos)):
                    if 0 == cupos[i]:
                        print(f"{i+1}. Especialidad: {Especialidades[i]}")
            case "6":
                while True:
                    agregar_nueva_esp = input("Introduce una nueva especialidad: ").strip().capitalize()
                    if agregar_nueva_esp == "":
                        print("Error: éste campo es obligatorio.")
                        print("")
                    elif not agregar_nueva_esp.isalpha():
                        print("Error: ingresó un carácter no válido.")
                        print("")
                    elif agregar_nueva_esp in Especialidades:
                        print("Ésta especialidad ya existe.")
                        print("")
                    else:
                        agregar_nueva_cupo = input("Introduce la cantidad de cupos de la especialidad: ").strip()
                        if agregar_nueva_cupo == "":
                            print("Error: éste campo es obligatorio.")
                            print("")
                        elif not agregar_nueva_cupo.isdigit():
                            print("Error: ingresó un carácter no válido.")
                            print("")
                        else:
                            print(f"La especialidad {agregar_nueva_esp} se ha agregado correctamente con {agregar_nueva_cupo} cupos disponibles!")
                            Especialidades.append(agregar_nueva_esp)
                            cupos.append(agregar_nueva_cupo)
                            break
                    
            case "7":
                bandera = True
                while bandera:
                    mod_esp = input("Cuál especialidad quiere aumentar o disminuir sus cupos? ").strip().capitalize()
                    if mod_esp == "":
                        print("Error: éste campo es obligatorio.")
                        print("")
                    elif not mod_esp.isalpha():
                        print("Error: ingresó un carácter no válido.")
                        print("")
                    elif mod_esp not in Especialidades:
                        print("Ésta especialidad no existe.")
                        print("")
                    else:
                        indice7 = Especialidades.index(mod_esp)
                        while True:
                            cant_cupos=input("Ingrese la cantidad de cupos a actualizar: ")
                            if cant_cupos == "":
                                print("Error: éste campo es obligatorio.")
                                print("")
                            elif not cant_cupos.isdigit():
                                print("Error: ingresó un carácter no válido")
                                print("")
                            else:
                                cupos[indice7] = int(cant_cupos)
                                print(f"Los cupos de {mod_esp} han sidos actualizados a {cant_cupos}.")
                                bandera = False
                                break
            case "8":
                print("Hasta luego")
                break
            case _:
                print("Error: ingresó un valór fuera de términos.")