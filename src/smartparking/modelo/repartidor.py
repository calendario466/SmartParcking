from enum import Enum
from abc import ABC, abstractmethod

class Estado(Enum):
    DISPONIBLE = "DISPONIBLE"
    OCUPADO = "OCUPADO"
    MANTENIMIENTO = "MANTENIMIENTO"

class Espacio(ABC):
    def __init__(self, numero: str, ubicacion: str, tamano: str, valor_fijo_dia: float):
        self.numero = numero
        self.ubicacion = ubicacion
        self.tamano = tamano
        self.estado = Estado.DISPONIBLE
        self.valor_fijo_dia = valor_fijo_dia

    @abstractmethod
    def calcular_precio_total(self, dias: int) -> float: pass

    def cambiar_estado(self, nuevo_estado: Estado):
        self.estado = nuevo_estado

    @abstractmethod
    def to_dict(self) -> dict: pass

class EspacioAuto(Espacio):
    def __init__(self, numero: str, ubicacion: str): super().__init__(numero, ubicacion, "Grande", 8000.0)
    def calcular_precio_total(self, dias: int) -> float: return self.valor_fijo_dia * (1 if dias <= 0 else dias)
    def to_dict(self): return {"tipo": "Auto", "numero": self.numero, "ubicacion": self.ubicacion, "estado": self.estado.value}

class EspacioMoto(Espacio):
    def __init__(self, numero: str, ubicacion: str): super().__init__(numero, ubicacion, "Reducido", 5000.0)
    def calcular_precio_total(self, dias: int) -> float: return self.valor_fijo_dia * (1 if dias <= 0 else dias)
    def to_dict(self): return {"tipo": "Moto", "numero": self.numero, "ubicacion": self.ubicacion, "estado": self.estado.value}

class EspacioElectrico(Espacio):
    def __init__(self, numero: str, ubicacion: str, potencia_carga: float = 50.0):
        super().__init__(numero, ubicacion, "Especial EV", 10000.0)
        self.potencia_carga = potencia_carga
    def calcular_precio_total(self, dias: int) -> float: return self.valor_fijo_dia * (1 if dias <= 0 else dias)
    def to_dict(self): return {"tipo": "Electrico", "numero": self.numero, "ubicacion": self.ubicacion, "potencia": self.potencia_carga, "estado": self.estado.value}
