from enum import Enum

class TipoCliente(Enum):
    NORMAL = "NORMAL"
    PREMIUM = "PREMIUM"

class Cliente:
    def __init__(self, nombre: str, rut: str, email: str, telefono: str, tipo_cliente: TipoCliente):
        self.nombre = nombre
        self.rut = rut
        self.email = email
        self.telefono = telefono
        self.tipo_cliente = tipo_cliente

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "rut": self.rut,
            "email": self.email,
            "telefono": self.telefono,
            "tipo": self.tipo_cliente.value
        }
