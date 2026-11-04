from .controladores.controlador import ControladorPrincipal
from .modelo.pago import PagoTarjetaCredito

def main():
    print("=== MODO DEMO DE SMARTPARKING ===")
    ctrl = ControladorPrincipal()
    print("Clientes en sistema:", len(ctrl.get_clientes_lista()))
    print("Espacios cargados:", len(ctrl.get_espacios_lista()))

if __name__ == "__main__":
    main()
