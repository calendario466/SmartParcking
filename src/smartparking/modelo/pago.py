from abc import ABC, abstractmethod

class MetodoPago(ABC):
    @abstractmethod
    def procesar_pago(self, monto: float) -> bool: pass

class PagoTarjetaCredito(MetodoPago):
    def __init__(self, numero_tarjeta: str): self.numero_tarjeta = numero_tarjeta
    def procesar_pago(self, monto: float) -> bool: return True

class PagoTarjetaDebito(MetodoPago):
    def __init__(self, numero_tarjeta: str): self.numero_tarjeta = numero_tarjeta
    def procesar_pago(self, monto: float) -> bool: return True

class PagoTransferencia(MetodoPago):
    def __init__(self, banco_origen: str): self.banco_origen = banco_origen
    def procesar_pago(self, monto: float) -> bool: return True
