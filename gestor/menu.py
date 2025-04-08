import os
import database as db
import helpers

def iniciar():
    while True:
        helpers.limpiar_pantalla()
        print("-----")
        print(" BIENVENIDO AL GESTOR DE CLIENTES ")
        print("[1] Listar clientes")
        print("[2] Buscar cliente")
        print("[3] Añadir cliente")
        print("[4] Modificar cliente")
        print("[5] Borrar cliente")
        print("[6] Salir")
        print("-----")
        opcion = helpers.leer_texto(1, 1, "Selecciona una opción (1-6)")

        helpers.limpiar_pantalla()
        if opcion == "1":
            print("Listando los clientes...\n")
            for cliente in db.Clientes.lista:
                print(cliente)
        elif opcion == "2":
            dni = helpers.leer_texto(3, 3, "DNI (2 números y 1 letra):").upper()
            cliente = db.Clientes.buscar(dni)
            print(cliente if cliente else "Cliente no encontrado.")
        elif opcion == "3":
            while True:
                dni = helpers.leer_texto(3, 3, "DNI (2 números y 1 letra):").upper()
                if helpers.dni_valido(dni, db.Clientes.lista):
                    break
            nombre = helpers.leer_texto(2, 30, "Nombre (2-30 caracteres):").capitalize()
            apellido = helpers.leer_texto(2, 30, "Apellido (2-30 caracteres):").capitalize()
            cliente = db.Clientes.crear(dni, nombre, apellido)
            print("Cliente añadido correctamente.")
        elif opcion == "4":
            dni = helpers.leer_texto(3, 3, "DNI (2 números y 1 letra):").upper()
            cliente = db.Clientes.buscar(dni)
            if cliente:
                nombre = helpers.leer_texto(2, 30, f"Nuevo nombre (actual: {cliente.nombre}):").capitalize()
                apellido = helpers.leer_texto(2, 30, f"Nuevo apellido (actual: {cliente.apellido}):").capitalize()
                db.Clientes.modificar(dni, nombre, apellido)
                print("Cliente modificado correctamente.")
            else:
                print("Cliente no encontrado.")
        elif opcion == "5":
            dni = helpers.leer_texto(3, 3, "DNI (2 números y 1 letra):").upper()
            cliente = db.Clientes.borrar(dni)
            print("Cliente borrado." if cliente else "Cliente no encontrado.")
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")
        
        input("\nPresiona ENTER para continuar...")