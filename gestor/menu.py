import os
import database as db

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def iniciar():
    while True:
        limpiar_pantalla()
        print("-----")
        print(" BIENVENIDO AL GESTOR DE CLIENTES ")
        print("[1] Listar clientes")
        print("[2] Buscar cliente")
        print("[3] Añadir cliente")
        print("[4] Modificar cliente")
        print("[5] Borrar cliente")
        print("[6] Salir")
        print("-----")
        opcion = input("> ")

        limpiar_pantalla()
        if opcion == "1":
            print("Listando los clientes...\n")
            for cliente in db.Clientes.lista:
                print(cliente)
        elif opcion == "2":
            dni = input("DNI del cliente a buscar: ").upper()
            cliente = db.Clientes.buscar(dni)
            print(cliente if cliente else "Cliente no encontrado.")
        elif opcion == "3":
            dni = input("DNI (2 números y 1 letra): ").upper()
            nombre = input("Nombre: ").capitalize()
            apellido = input("Apellido: ").capitalize()
            cliente = db.Clientes.crear(dni, nombre, apellido)
            print("Cliente añadido." if cliente else "DNI ya existe.")
        elif opcion == "4":
            dni = input("DNI del cliente a modificar: ").upper()
            nombre = input("Nuevo nombre: ").capitalize()
            apellido = input("Nuevo apellido: ").capitalize()
            cliente = db.Clientes.modificar(dni, nombre, apellido)
            print("Cliente modificado." if cliente else "Cliente no encontrado.")
        elif opcion == "5":
            dni = input("DNI del cliente a borrar: ").upper()
            cliente = db.Clientes.borrar(dni)
            print("Cliente borrado." if cliente else "Cliente no encontrado.")
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")
        
        input("\nPresiona ENTER para continuar...")