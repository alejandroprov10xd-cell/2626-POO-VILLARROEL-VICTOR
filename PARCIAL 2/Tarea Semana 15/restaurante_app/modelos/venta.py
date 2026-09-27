from datetime import datetime


class Venta:
    """Representa una venta simple entre un usuario y un producto."""

    def __init__(self, usuario_id: str, producto_codigo: str, fecha: str) -> None:
        self.usuario_id = self._validar_texto(usuario_id, "usuario")
        self.producto_codigo = self._validar_texto(producto_codigo, "producto")
        self.fecha = self._validar_fecha(fecha)

    def convertir_a_diccionario(self) -> dict[str, str]:
        return {
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "fecha": self.fecha,
        }

    @staticmethod
    def crear(usuario_id: str, producto_codigo: str) -> "Venta":
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return Venta(usuario_id, producto_codigo, fecha_actual)

    @staticmethod
    def _validar_texto(valor: str, campo: str) -> str:
        if not isinstance(valor, str):
            raise ValueError(f"La referencia de {campo} debe ser texto.")
        texto = valor.strip()
        if not texto:
            raise ValueError(f"La referencia de {campo} no puede estar vacia.")
        return texto

    @staticmethod
    def _validar_fecha(fecha: str) -> str:
        if not isinstance(fecha, str) or not fecha.strip():
            raise ValueError("La fecha de la venta no puede estar vacia.")
        return fecha.strip()
