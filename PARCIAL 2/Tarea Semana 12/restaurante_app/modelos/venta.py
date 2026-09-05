class Venta:
    """Relaciona un usuario con un producto y la cantidad comprada."""

    def __init__(self, usuario_id: str, producto_codigo: str, cantidad: int) -> None:
        self.usuario_id = self._validar_texto(usuario_id, "usuario")
        self.producto_codigo = self._validar_texto(producto_codigo, "producto")
        if isinstance(cantidad, bool) or not isinstance(cantidad, int) or cantidad <= 0:
            raise ValueError("La cantidad vendida debe ser un entero mayor que cero.")
        self.cantidad = cantidad

    def convertir_a_diccionario(self) -> dict[str, str | int]:
        return {
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "cantidad": self.cantidad,
        }

    @staticmethod
    def _validar_texto(valor: str, campo: str) -> str:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError(f"La referencia de {campo} no puede estar vacia.")
        return valor.strip()
