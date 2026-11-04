import tkinter as tk
from tkinter import ttk
from ..controladores.controlador import ControladorPrincipal
from .clientes import VistaClientes
from .productos import VistaVehiculos
from .pedidos import VistaOperaciones
from .seguimiento import VistaMantenimiento

class AplicacionEscritorio:
    def __init__(self, root):
        self.root = root
        self.root.title("SmartParking — Gestión de Estacionamientos")
        self.root.geometry("850x650")
        self.controlador = ControladorPrincipal()

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill='both', padx=10, pady=12)

        self.tab_clientes = VistaClientes(self.notebook, self.controlador)
        self.tab_vehiculos = VistaVehiculos(self.notebook, self.controlador)
        self.tab_operaciones = VistaOperaciones(self.notebook, self.controlador)
        self.tab_mantenimiento = VistaMantenimiento(self.notebook, self.controlador)

        self.notebook.add(self.tab_clientes, text="Clientes")
        self.notebook.add(self.tab_vehiculos, text="Vehículos")
        self.notebook.add(self.tab_operaciones, text="Ingresos / Salidas")
        self.notebook.add(self.tab_mantenimiento, text="Mantenimiento")
