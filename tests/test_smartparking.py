import json
import os
import shutil
import tempfile
import unittest
from src.smartparking.controladores.controlador import ControladorPrincipal
from src.smartparking.modelo.cliente import Cliente, TipoCliente
from src.smartparking.modelo.sistema import SistemaEstacionamiento
from src.smartparking.persistencia.repositorio_json import RepositorioJSON

class TestSmartParking(unittest.TestCase):
    def test_creacion_cliente(self):
        c = Cliente("Juan", "11111111-1", "j@g.com", "123", TipoCliente.NORMAL)
        self.assertEqual(c.nombre, "Juan")

    def test_buscar_cliente_ignora_puntos_guion_y_k(self):
        sistema = SistemaEstacionamiento()
        juan = Cliente("Juan", "11.111.111-1", "j@g.com", "123", TipoCliente.NORMAL)
        luis = Cliente("Luis", "21212236-k", "l@g.com", "123", TipoCliente.PREMIUM)
        sistema.clientes[juan.rut] = juan
        sistema.clientes[luis.rut] = luis
        self.assertIs(sistema.buscar_cliente("11111111-1"), juan)
        self.assertIs(sistema.buscar_cliente("11.111.111-1"), juan)
        self.assertIs(sistema.buscar_cliente("21212236-K"), luis)
        self.assertIsNone(sistema.buscar_cliente(""))

    def test_registrar_vehiculo_encuentra_cliente_con_otro_formato_de_rut(self):
        tmp = tempfile.mkdtemp()
        try:
            with open(os.path.join(tmp, "clientes.json"), "w", encoding="utf-8") as f:
                json.dump([{
                    "nombre": "Juan Pérez",
                    "rut": "11111111-1",
                    "email": "juan@gmail.com",
                    "telefono": "1",
                    "tipo": "NORMAL"
                }], f)
            ctrl = ControladorPrincipal(RepositorioJSON(tmp))
            ok, msg = ctrl.registrar_vehiculo("11.111.111-1", "cd1234", "AUTOMOVIL")
            self.assertTrue(ok, msg)
            self.assertIn("CD1234", ctrl.vehiculos)
            duplicado, aviso = ctrl.registrar_cliente("Otro", "11.111.111-1", "a@b.c", "9", "PREMIUM")
            self.assertFalse(duplicado)
            self.assertIn("ya existe", aviso)
            vacio, aviso_vacio = ctrl.registrar_cliente("Nadie", "---", "a@b.c", "9", "NORMAL")
            self.assertFalse(vacio)
            self.assertIn("vacío", aviso_vacio)
            self.assertEqual(len(ctrl.clientes), 1)
        finally:
            shutil.rmtree(tmp)

if __name__ == "__main__":
    unittest.main()
