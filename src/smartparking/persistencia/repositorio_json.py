import json
import os
from ..modelo.cliente import Cliente, TipoCliente
from ..modelo.formato import buscar_por_rut
from ..modelo.producto import Vehiculo, TipoVehiculo
from ..modelo.repartidor import EspacioAuto, EspacioMoto, EspacioElectrico, Estado
from ..modelo.pedido import RegistroEstacionamiento, EstadoEstacionamiento

class RepositorioJSON:
    def __init__(self, ruta_data=None):
        if ruta_data is None:
            ruta_data = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'data')
        self.ruta_data = ruta_data
        self.archivo_clientes = os.path.join(self.ruta_data, 'clientes.json')
        self.archivo_vehiculos = os.path.join(self.ruta_data, 'vehiculos.json')
        self.archivo_espacios = os.path.join(self.ruta_data, 'espacios.json')
        self.archivo_registros = os.path.join(self.ruta_data, 'registros.json')

    def _cargar(self, ruta):
        if os.path.exists(ruta):
            with open(ruta, 'r', encoding='utf-8') as f: return json.load(f)
        return []

    def _guardar(self, ruta, datos):
        with open(ruta, 'w', encoding='utf-8') as f: json.dump(datos, f, indent=4)

    def cargar_clientes(self):
        datos = self._cargar(self.archivo_clientes)
        return {d['rut']: Cliente(d['nombre'], d['rut'], d['email'], d['telefono'], TipoCliente(d['tipo'])) for d in datos}

    def guardar_clientes(self, clientes):
        self._guardar(self.archivo_clientes, [c.to_dict() for c in clientes.values()])

    def cargar_vehiculos(self, clientes):
        datos = self._cargar(self.archivo_vehiculos)
        vehiculos = {}
        for d in datos:
            c = buscar_por_rut(clientes, d.get('rut_cliente'))
            if c:
                v = Vehiculo(d['patente'], TipoVehiculo(d['tipo']), c)
                vehiculos[v.patente] = v
        return vehiculos

    def guardar_vehiculos(self, vehiculos):
        self._guardar(self.archivo_vehiculos, [v.to_dict() for v in vehiculos.values()])

    def cargar_espacios(self):
        datos = self._cargar(self.archivo_espacios)
        espacios = {}
        for d in datos:
            if d['tipo'] == 'Auto': e = EspacioAuto(d['numero'], d['ubicacion'])
            elif d['tipo'] == 'Moto': e = EspacioMoto(d['numero'], d['ubicacion'])
            else: e = EspacioElectrico(d['numero'], d['ubicacion'], d.get('potencia', 50.))
            if 'estado' in d: e.estado = Estado(d['estado'])
            espacios[e.numero] = e
        return espacios

    def guardar_espacios(self, espacios):
        self._guardar(self.archivo_espacios, [e.to_dict() for e in espacios.values()])

    def cargar_registros(self, clientes, vehiculos, espacios):
        datos = self._cargar(self.archivo_registros)
        registros = []
        for d in datos:
            c = buscar_por_rut(clientes, d.get('rut_cliente'))
            v = vehiculos.get(d['patente_vehiculo'])
            e = espacios.get(d['numero_espacio'])
            if c and v and e:
                r = RegistroEstacionamiento(d['id_registro'], c, v, e, d['fecha_entrada'])
                r.fecha_hora_salida = d['fecha_salida']
                r.estado_estacionamiento = EstadoEstacionamiento(d['estado'])
                r.valor_total = d['total']
                registros.append(r)
        return registros

    def guardar_registros(self, registros):
        self._guardar(self.archivo_registros, [r.to_dict() for r in registros])
