def formatear_moneda(monto: float) -> str:
    return f"${monto:,.0f}".replace(",", ".")

def limpiar_rut(rut: str) -> str:
    return rut.strip().replace(".", "").replace("-", "").lower() if rut else ""

def buscar_por_rut(clientes, rut: str):
    clave = limpiar_rut(rut)
    if not clave:
        return None
    if rut in clientes:
        return clientes[rut]
    directo = clientes.get(clave)
    if directo is not None:
        return directo
    for cliente in clientes.values():
        if limpiar_rut(cliente.rut) == clave:
            return cliente
    return None
