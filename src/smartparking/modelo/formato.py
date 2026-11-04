def formatear_moneda(monto: float) -> str:
    return f"${monto:,.0f}".replace(",", ".")

def limpiar_rut(rut: str) -> str:
    return rut.strip().replace(".", "").replace("-", "").lower() if rut else ""
