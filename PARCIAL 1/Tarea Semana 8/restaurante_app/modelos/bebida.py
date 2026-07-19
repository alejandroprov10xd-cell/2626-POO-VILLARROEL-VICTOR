from modelos.producto import Producto


class Bebida(Producto):
    """Especializacion de Producto para bebidas del restaurante."""

    def __init__(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        tamano: str,
        tipo_envase: str,
    ) -> None:
        super().__init__(codigo, nombre, categoria, precio)
        self.tamano = self._validar_texto(tamano, "tamano")
        self.tipo_envase = self._validar_texto(tipo_envase, "tipo de envase")

    def mostrar_informacion(self) -> str:
        informacion_base = super().mostrar_informacion()
        return (
            f"{informacion_base} | "
            f"Tamano: {self.tamano} | "
            f"Envase: {self.tipo_envase}"
        )
