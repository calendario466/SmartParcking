import unittest
from src.smartparking.modelo.cliente import Cliente, TipoCliente

class TestSmartParking(unittest.TestCase):
    def test_creacion_cliente(self):
        c = Cliente("Juan", "11111111-1", "j@g.com", "123", TipoCliente.NORMAL)
        self.assertEqual(c.nombre, "Juan")

if __name__ == "__main__":
    unittest.main()
