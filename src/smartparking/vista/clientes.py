import tkinter as tk
from tkinter import ttk, messagebox

class VistaClientes(ttk.Frame):
    def __init__(self, parent, controlador):
        super().__init__(parent)
        self.controlador = controlador
        
        f = ttk.LabelFrame(self, text="Registrar Cliente")
        f.pack(fill='x', padx=10, pady=10)
        
        ttk.Label(f, text="RUT:").grid(row=0, column=0, padx=5, pady=5)
        self.ent_rut = ttk.Entry(f); self.ent_rut.grid(row=0, column=1, padx=5, pady=5)
        ttk.Label(f, text="Nombre:").grid(row=0, column=2, padx=5, pady=5)
        self.ent_nombre = ttk.Entry(f); self.ent_nombre.grid(row=0, column=3, padx=5, pady=5)
        ttk.Label(f, text="Tipo:").grid(row=1, column=0, padx=5, pady=5)
        self.cb_tipo = ttk.Combobox(f, values=["NORMAL", "PREMIUM"], state="readonly")
        self.cb_tipo.current(0); self.cb_tipo.grid(row=1, column=1, padx=5, pady=5)
        ttk.Button(f, text="Guardar", command=self.guardar).grid(row=1, column=2, columnspan=2, pady=10)
        
        self.tree = ttk.Treeview(self, columns=("RUT", "Nombre", "Tipo"), show="headings")
        self.tree.heading("RUT", text="RUT"); self.tree.heading("Nombre", text="Nombre"); self.tree.heading("Tipo", text="Tipo")
        self.tree.pack(fill='both', expand=True, padx=10, pady=10)
        self.actualizar()

    def guardar(self):
        exito, msg = self.controlador.registrar_cliente(self.ent_nombre.get().strip(), self.ent_rut.get().strip(), "correo@ej.com", "123", self.cb_tipo.get())
        if exito: messagebox.showinfo("Éxito", msg); self.actualizar()
        else: messagebox.showerror("Error", msg)

    def actualizar(self):
        for item in self.tree.get_children(): self.tree.delete(item)
        for c in self.controlador.get_clientes_lista(): self.tree.insert("", 'end', values=(c['rut'], c['nombre'], c['tipo']))
