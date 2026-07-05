from modelos.producto import Producto


class Bebida(Producto):
    """Clase hija que representa una bebida del restaurante."""

    def __init__(
        self,
        nombre: str,
        precio: float,
        disponible: bool,
        volumen_mililitros: int,
        tipo_bebida: str,
    ) -> None:
        super().__init__(nombre, precio, disponible)
        self.volumen_mililitros = volumen_mililitros
        self.tipo_bebida = tipo_bebida

    def mostrar_informacion(self) -> str:
        return (
            f"Bebida: {self.nombre} | "
            f"Tipo: {self.tipo_bebida} | "
            f"Volumen: {self.volumen_mililitros} ml | "
            f"Precio: ${self.obtener_precio():.2f} | "
            f"Estado: {self.obtener_estado_disponibilidad()}"
        )
