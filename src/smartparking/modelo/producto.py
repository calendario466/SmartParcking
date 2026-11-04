from enum import Enum
from .cliente import Cliente

class TipoVehiculo(Enum):
    AUTOMOVIL = "AUTOMOVIL"
    MOTOCICLETA = "MOTOCICLETA"
    ELECTRICO = "ELECTRICO"

class Vehiculo:
    def __init__(self, patente: str, tipo_vehiculo: TipoVehiculo, cliente: Cliente):
        self.patente = patente.upper()
        self.tipo_vehiculo = tipo_vehiculo
        self.cliente = cliente

    def to_dict(self):
        return {
            "patente": self.patente,
            "tipo": self.tipo_vehiculo.value,
            "rut_cliente": self.cliente.rut
        }
