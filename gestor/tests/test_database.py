import unittest
import copy
import os
from gestor import database as db

class TestDatabase(unittest.TestCase):
    def setUp(self):
        # Configurar datos de prueba antes de cada test
        db.Clientes.lista = [
            db.Cliente("15J", "Marta", "Pérez"),
            db.Cliente("48H", "Manolo", "López"),
            db.Cliente("28Z", "Ana", "García")
        ]
        # Guardar una copia inicial para restaurar después
        self.lista_inicial = copy.deepcopy(db.Clientes.lista)

    def tearDown(self):
        # Restaurar la lista y el archivo después de cada test
        db.Clientes.lista = self.lista_inicial
        db.Clientes.guardar()

    def test_buscar_cliente(self):
        cliente_existente = db.Clientes.buscar("15J")
        cliente_no_existente = db.Clientes.buscar("99X")
        self.assertIsNotNone(cliente_existente)
        self.assertEqual(cliente_existente.nombre, "Marta")
        self.assertIsNone(cliente_no_existente)

    def test_crear_cliente(self):
        nuevo_cliente = db.Clientes.crear("39X", "Héctor", "Costa")
        self.assertEqual(len(db.Clientes.lista), 4)
        self.assertEqual(nuevo_cliente.dni, "39X")
        self.assertEqual(nuevo_cliente.nombre, "Héctor")
        self.assertEqual(nuevo_cliente.apellido, "Costa")
        # Verificar que no se puede duplicar DNI
        duplicado = db.Clientes.crear("39X", "Otro", "Nombre")
        self.assertIsNone(duplicado)

    def test_modificar_cliente(self):
        cliente_modificado = db.Clientes.modificar("28Z", "Mariana", "Pérez")
        self.assertEqual(cliente_modificado.nombre, "Mariana")
        self.assertEqual(cliente_modificado.apellido, "Pérez")
        # Verificar que no modifica si no existe
        no_existente = db.Clientes.modificar("99X", "Nadie", "Nada")
        self.assertIsNone(no_existente)

    def test_borrar_cliente(self):
        cliente_borrado = db.Clientes.borrar("48H")
        self.assertEqual(len(db.Clientes.lista), 2)
        self.assertEqual(cliente_borrado.dni, "48H")
        # Verificar que no encuentra el cliente borrado
        cliente_rebuscado = db.Clientes.buscar("48H")
        self.assertIsNone(cliente_rebuscado)
        # Verificar que no borra si no existe
        no_existente = db.Clientes.borrar("99X")
        self.assertIsNone(no_existente)

    def test_persistencia_csv(self):
        db.Clientes.crear("39X", "Héctor", "Costa")
        db.Clientes.guardar()
        # Simular recarga desde el archivo
        db.Clientes.cargar()
        cliente = db.Clientes.buscar("39X")
        self.assertIsNotNone(cliente)
        self.assertEqual(cliente.nombre, "Héctor")

if __name__ == "__main__":
    unittest.main()