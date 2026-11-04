import tkinter as tk
from tkinter import ttk, messagebox
from ..modelo.pago import PagoTarjetaCredito, PagoTarjetaDebito, PagoTransferencia

class VistaOperaciones(ttk.Frame):
    def __init__(self, parent, controlador):
        super().__init__(parent)
        self.controlador = controlador
        
        f1 = ttk.LabelFrame(self, text="Registrar Ingreso")
        f1.pack(fill='x', padx=10, pady=5)
        ttk.Label(f1, text="Patente:").grid(row=0, column=0, padx=5)
        self.ent_ing_pat = ttk.Entry(f1); self.ent_ing_pat.grid(row=0, column=1, padx=5)
        ttk.Button(f1, text="Ingresar", command=self.ingreso).grid(row=0, column=2, padx=5)

        f2 = ttk.LabelFrame(self, text="Registrar Salida y Pago")
        f2.pack(fill='x', padx=10, pady=5)
        ttk.Label(f2, text="ID Reg:").grid(row=0, column=0, padx=5)
        self.ent_sal_id = ttk.Entry(f2); self.ent_sal_id.grid(row=0, column=1, padx=5)
        ttk.Label(f2, text="Pago:").grid(row=0, column=2, padx=5)
        self.cb_pago = ttk.Combobox(f2, values=["Tarjeta de Crédito", "Tarjeta de Débito", "Transferencia Bancaria"], state="readonly")
        self.cb_pago.current(0); self.cb_pago.grid(row=0, column=3, padx=5)
        ttk.Button(f2, text="Pagar y Salir", command=self.salida).grid(row=0, column=4, padx=5)

        self.tree = ttk.Treeview(self, columns=("ID", "Patente", "Espacio", "Estado", "Total"), show="headings")
        for col in self.tree["columns"]: self.tree.heading(col, text=col)
        self.tree.pack(fill='both', expand=True, padx=10, pady=10)
        self.actualizar()

    def ingreso(self):
        exito, msg = self.controlador.registrar_ingreso(self.ent_ing_pat.get().strip(), "2026-11-02 10:00")
        if exito: messagebox.showinfo("Éxito", msg); self.actualizar()
        else: messagebox.showerror("Error", msg)

    def salida(self):
        try: id_r = int(self.ent_sal_id.get().strip())
        except: messagebox.showerror("Error", "ID inválido"); return
        pago = PagoTarjetaCredito("1234") if self.cb_pago.get() == "Tarjeta de Crédito" else (PagoTarjetaDebito("1234") if self.cb_pago.get() == "Tarjeta de Débito" else PagoTransferencia("Banco"))
        exito, msg = self.controlador.registrar_salida(id_r, 1, "2026-11-02 18:00", pago)
        if exito: messagebox.showinfo("Éxito", msg); self.actualizar()
        else: messagebox.showerror("Error", msg)

    def actualizar(self):
        for item in self.tree.get_children(): self.tree.delete(item)
        for r in self.controlador.get_registros_lista(): self.tree.insert("", 'end', values=(r['id_registro'], r['patente_vehiculo'], r['numero_espacio'], r['estado'], f"${r['total']:,.0f}"))
