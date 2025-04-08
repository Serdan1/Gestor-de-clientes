import csv

class Cliente:
    def __init__(self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
    
    def __str__(self):
        return f"({self.dni}) {self.nombre} {self.apellido}"

class Clientes:
    lista = []

    @staticmethod
    def cargar():
        try:
            with open("clientes.csv", newline="\n") as fichero:
                reader = csv.reader(fichero, delimiter=";")
                Clientes.lista = [Cliente(dni, nombre, apellido) for dni, nombre, apellido in reader]
        except FileNotFoundError:
            # Si no existe el archivo, inicializamos con datos de prueba
            Clientes.lista = [
                Cliente("15J", "Marta", "Pérez"),
                Cliente("48H", "Manolo", "López"),
                Cliente("28Z", "Ana", "García")
            ]
            Clientes.guardar()

    @staticmethod
    def guardar():
        with open("clientes.csv", "w", newline="\n") as fichero:
            writer = csv.writer(fichero, delimiter=";")
            for cliente in Clientes.lista:
                writer.writerow([cliente.dni, cliente.nombre, cliente.apellido])

    @staticmethod
    def buscar(dni):
        for cliente in Clientes.lista:
            if cliente.dni == dni:
                return cliente
        return None

    @staticmethod
    def crear(dni, nombre, apellido):
        if Clientes.buscar(dni):
            return None
        cliente = Cliente(dni, nombre, apellido)
        Clientes.lista.append(cliente)
        Clientes.guardar()
        return cliente

    @staticmethod
    def modificar(dni, nombre, apellido):
        cliente = Clientes.buscar(dni)
        if cliente:
            cliente.nombre = nombre
            cliente.apellido = apellido
            Clientes.guardar()
            return cliente
        return None

    @staticmethod
    def borrar(dni):
        cliente = Clientes.buscar(dni)
        if cliente:
            Clientes.lista.remove(cliente)
            Clientes.guardar()
            return cliente
        return None

# Cargar datos al iniciar el módulo
Clientes.cargar()