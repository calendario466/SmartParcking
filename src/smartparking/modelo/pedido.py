from enum import Enum
from .cliente import Cliente, TipoCliente
from .producto import Vehiculo
from .repartidor import Espacio, Estado
from .pago import MetodoPago

class EstadoEstacionamiento(Enum):
    ACTIVO = "ACTIVO"
    FINALIZADO = "FINALIZADO"

class RegistroEstacionamiento:
    def __init__(self, id_registro: int, cliente: Cliente, vehiculo: Vehiculo, espacio: Espacio, fecha_hora_entrada: str):
        self.id_registro = id_registro
        self.cliente = cliente
        self.vehiculo = vehiculo
        self.espacio = espacio
        self.fecha_hora_entrada = fecha_hora_entrada
        self.fecha_hora_salida = "Pendiente"
        self.estado_estacionamiento = EstadoEstacionamiento.ACTIVO
        self.valor_total = 0.0

    def finalizar_estacionamiento(self, dias_permanencia: int, fecha_salida: str, metodo_pago: MetodoPago) -> bool:
        if self.estado_estacionamiento == EstadoEstacionamiento.FINALIZADO: return False
        subtotal = self.espacio.calcular_precio_total(dias_permanencia)
        if self.cliente.tipo_cliente == TipoCliente.PREMIUM: subtotal *= 0.90
        self.valor_total = subtotal
        if metodo_pago.procesar_pago(self.valor_total):
            self.fecha_hora_salida = fecha_salida
            self.estado_estacionamiento = EstadoEstacionamiento.FINALIZADO
            self.espacio.cambiar_estado(Estado.DISPONIBLE)
            return True
        return False

    def to_dict(self):
        return {
            "id_registro": self.id_registro,
            "rut_cliente": self.cliente.rut,
            "patente_vehiculo": self.vehiculo.patente,
            "numero_espacio": self.espacio.numero,
            "fecha_entrada": self.fecha_hora_entrada,
            "fecha_salida": self.fecha_hora_salida,
            "estado": self.estado_estacionamiento.value,
            "total": self.valor_total
        }
