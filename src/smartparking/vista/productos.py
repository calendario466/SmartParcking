import tkinter as tk
from tkinter import ttk, messagebox

class VistaVehiculos(ttk.Frame):
    def __init__(self, parent, controlador):
        super().__init__(parent)
        self.controlador = controlador
        f = ttk.LabelFrame(self, text="Registrar Vehículo")
        f.pack(fill='x', padx=10, pady=10)
        ttk.Label(f, text="Patente:").grid(row=0, column=0, padx=5, pady=5)
        self.ent_pat = ttk.Entry(f); self.ent_pat.grid(row=0, column=1, padx=5, pady=5)
        ttk.Label(f, text="RUT Dueño:").grid(row=0, column=2, padx=5, pady=5)
        self.ent_rut = ttk.Entry(f); self.ent_rut.grid(row=0, column=3, padx=5, pady=5)
        ttk.Label(f, text="Tipo:").grid(row=1, column=0, padx=5, pady=5)
        self.cb_tipo = ttk.Combobox(f, values=["AUTOMOVIL", "MOTOCICLETA", "ELECTRICO"], state="readonly")
        self.cb_tipo.current(0); self.cb_tipo.grid(row=1, column=1, padx=5, pady=5)
        ttk.Button(f, text="Guardar Vehículo", command=self.guardar).grid(row=1, column=2, columnspan=2, pady=10)

    def guardar(self):
        exito, msg = self.controlador.registrar_vehiculo(self.ent_rut.get().strip(), self.ent_pat.get().strip(), self.cb_tipo.get())
        if exito: messagebox.showinfo("Éxito", msg)
        else: messagebox.showerror("Error", msg)
