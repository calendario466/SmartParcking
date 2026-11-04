from typing import Dict, List
from .cliente import Cliente, TipoCliente
from .producto import Vehiculo, TipoVehiculo
from .repartidor import Espacio, EspacioAuto, EspacioMoto, EspacioElectrico, Estado
from .pedido import RegistroEstacionamiento, EstadoEstacionamiento
from .formato import limpiar_rut

class SistemaEstacionamiento:
    def __init__(self):
        self.clientes: Dict[str, Cliente] = {}
        self.vehiculos: Dict[str, Vehiculo] = {}
        self.espacios: Dict[str, Espacio] = {}
        self.registros: List[RegistroEstacionamiento] = []
        self.contador_registros = 1

    def buscar_cliente(self, rut: str):
        return self.clientes.get(limpiar_rut(rut))

    def buscar_vehiculo(self, patente: str):
        return self.vehiculos.get(patente.upper() if patente else "")
