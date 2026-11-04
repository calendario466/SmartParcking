from .errores import ErrorValidacion

def validar_texto_no_vacio(texto: str, campo: str):
    if not texto or not texto.strip():
        raise ErrorValidacion(f"El campo '{campo}' no puede estar vacío.")

def validar_rut(rut: str):
    validar_texto_no_vacio(rut, "RUT")
