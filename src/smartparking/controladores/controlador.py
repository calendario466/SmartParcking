from ..persistencia.repositorio_json import RepositorioJSON
from ..modelo.cliente import Cliente, TipoCliente
from ..modelo.producto import Vehiculo, TipoVehiculo
from ..modelo.repartidor import EspacioAuto, EspacioMoto, EspacioElectrico, Estado
from ..modelo.pedido import RegistroEstacionamiento, EstadoEstacionamiento

class ControladorPrincipal:
    def __init__(self):
        self.repo = RepositorioJSON()
        self.clientes = self.repo.cargar_clientes()
        self.vehiculos = self.repo.cargar_vehiculos(self.clientes)
        self.espacios = self.repo.cargar_espacios()
        self.registros = self.repo.cargar_registros(self.clientes, self.vehiculos, self.espacios)
        self.contador_registros = (max((r.id_registro for r in self.registros), default=0) + 1)

    def registrar_cliente(self, nombre, rut, email, telefono, tipo_str):
        if rut in self.clientes: return False, "El cliente ya existe."
        tipo = TipoCliente.PREMIUM if tipo_str == "PREMIUM" else TipoCliente.NORMAL
        c = Cliente(nombre, rut, email, telefono, tipo)
        self.clientes[rut] = c
        self.repo.guardar_clientes(self.clientes)
        return True, "Cliente registrado con éxito."

    def registrar_vehiculo(self, rut, patente, tipo_str):
        patente = patente.upper()
        if patente in self.vehiculos: return False, "El vehículo ya existe."
        c = self.clientes.get(rut)
        if not c: return False, "Cliente no encontrado."
        tipo = TipoVehiculo.MOTOCICLETA if tipo_str == "MOTOCICLETA" else (TipoVehiculo.ELECTRICO if tipo_str == "ELECTRICO" else TipoVehiculo.AUTOMOVIL)
        v = Vehiculo(patente, tipo, c)
        self.vehiculos[patente] = v
        self.repo.guardar_vehiculos(self.vehiculos)
        return True, "Vehículo registrado."

    def get_clientes_lista(self): return [c.to_dict() for c in self.clientes.values()]
    def get_espacios_lista(self): return [e.to_dict() for e in self.espacios.values()]
    def get_registros_lista(self): return [r.to_dict() for r in self.registros]

    def registrar_ingreso(self, patente, fecha):
        patente = patente.upper()
        v = self.vehiculos.get(patente)
        if not v: return False, "Vehículo no registrado."
        for r in self.registros:
            if r.vehiculo.patente == patente and r.estado_estacionamiento == EstadoEstacionamiento.ACTIVO:
                return False, "Vehículo ya está dentro del estacionamiento."
        espacio_libre = None
        for e in self.espacios.values():
            if e.estado == Estado.DISPONIBLE:
                if v.tipo_vehiculo == TipoVehiculo.AUTOMOVIL and isinstance(e, EspacioAuto): espacio_libre = e; break
                elif v.tipo_vehiculo == TipoVehiculo.MOTOCICLETA and isinstance(e, EspacioMoto): espacio_libre = e; break
                elif v.tipo_vehiculo == TipoVehiculo.ELECTRICO and isinstance(e, EspacioElectrico): espacio_libre = e; break
        if not espacio_libre: return False, "No hay espacios disponibles para este tipo de vehículo."
        espacio_libre.cambiar_estado(Estado.OCUPADO)
        nuevo_registro = RegistroEstacionamiento(self.contador_registros, v.cliente, v, espacio_libre, fecha)
        self.contador_registros += 1
        self.registros.append(nuevo_registro)
        self.repo.guardar_espacios(self.espacios)
        self.repo.guardar_registros(self.registros)
        return True, f"Ingreso exitoso. Espacio {espacio_libre.numero} asignado."

    def registrar_salida(self, id_registro, dias, fecha, metodo_pago):
        reg = next((r for r in self.registros if r.id_registro == id_registro), None)
        if not reg: return False, "Registro no encontrado."
        if reg.estado_estacionamiento == EstadoEstacionamiento.FINALIZADO: return False, "El registro ya está finalizado."
        exito = reg.finalizar_estacionamiento(dias, fecha, metodo_pago)
        if exito:
            self.repo.guardar_espacios(self.espacios)
            self.repo.guardar_registros(self.registros)
            return True, f"Salida exitosa. Total a pagar: ${reg.valor_total:,.0f}"
        return False, "Error al procesar pago."

    def gestionar_mantenimiento(self, numero_espacio, enviar, motivo=""):
        e = self.espacios.get(numero_espacio)
        if not e: return False, "Espacio no existe."
        if enviar:
            if e.estado == Estado.OCUPADO: return False, "No se puede enviar a mantenimiento un espacio OCUPADO."
            e.cambiar_estado(Estado.MANTENIMIENTO)
        else:
            if e.estado != Estado.MANTENIMIENTO: return False, "El espacio no está en mantenimiento."
            e.cambiar_estado(Estado.DISPONIBLE)
        self.repo.guardar_espacios(self.espacios)
        return True, "Estado de mantenimiento actualizado."
