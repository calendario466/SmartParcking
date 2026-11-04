import tkinter as tk
from tkinter import ttk, messagebox

class VistaMantenimiento(ttk.Frame):
    def __init__(self, parent, controlador):
        super().__init__(parent)
        self.controlador = controlador
        f = ttk.LabelFrame(self, text="Mantenimiento de Espacios")
        f.pack(fill='x', padx=10, pady=10)
        ttk.Label(f, text="N° Espacio:").grid(row=0, column=0, padx=5, pady=5)
        self.ent_esp = ttk.Entry(f); self.ent_esp.grid(row=0, column=1, padx=5, pady=5)
        ttk.Label(f, text="Motivo:").grid(row=0, column=2, padx=5, pady=5)
        self.ent_motivo = ttk.Entry(f); self.ent_motivo.grid(row=0, column=3, padx=5, pady=5)
        ttk.Button(f, text="Enviar a Mantenimiento", command=lambda: self.mant(True)).grid(row=1, column=0, columnspan=2, pady=10)
        ttk.Button(f, text="Finalizar Mantenimiento", command=lambda: self.mant(False)).grid(row=1, column=2, columnspan=2, pady=10)

    def mant(self, enviar):
        exito, msg = self.controlador.gestionar_mantenimiento(self.ent_esp.get().strip().upper(), enviar, self.ent_motivo.get().strip())
        if exito: messagebox.showinfo("Éxito", msg)
        else: messagebox.showerror("Error", msg)
