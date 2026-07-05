from modelos.producto import Producto


class Platillo(Producto):
    """Clase hija que representa un platillo del restaurante."""

    def __init__(
        self,
        nombre: str,
        precio: float,
        disponible: bool,
        tipo_platillo: str,
        tiempo_preparacion: int,
    ) -> None:
        super().__init__(nombre, precio, disponible)
        self.tipo_platillo = tipo_platillo
        self.tiempo_preparacion = tiempo_preparacion

    def mostrar_informacion(self) -> str:
        return (
            f"Platillo: {self.nombre} | "
            f"Tipo: {self.tipo_platillo} | "
            f"Preparacion: {self.tiempo_preparacion} min | "
            f"Precio: ${self.obtener_precio():.2f} | "
            f"Estado: {self.obtener_estado_disponibilidad()}"
        )
