class Cliente:
    def __init__(self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
    
    def __str__(self):
        return f"({self.dni}) {self.nombre} {self.apellido}"

class Clientes:
    lista = [
        Cliente("15J", "Marta", "Pérez"),
        Cliente("48H", "Manolo", "López"),
        Cliente("28Z", "Ana", "García")
    ]

    @staticmethod
    def buscar(dni):
        for cliente in Clientes.lista:
            if cliente.dni == dni:
                return cliente
        return None

    @staticmethod
    def crear(dni, nombre, apellido):
        if Clientes.buscar(dni):
            return None  # No permitir DNIs duplicados
        cliente = Cliente(dni, nombre, apellido)
        Clientes.lista.append(cliente)
        return cliente

    @staticmethod
    def modificar(dni, nombre, apellido):
        cliente = Clientes.buscar(dni)
        if cliente:
            cliente.nombre = nombre
            cliente.apellido = apellido
            return cliente
        return None

    @staticmethod
    def borrar(dni):
        cliente = Clientes.buscar(dni)
        if cliente:
            Clientes.lista.remove(cliente)
            return cliente
        return None
    