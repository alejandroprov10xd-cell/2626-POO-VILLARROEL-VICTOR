class Producto:
    """Representa un producto disponible en el restaurante."""

    def __init__(self, nombre: str, categoria: str, cantidad_disponible: int, precio: float, activo: bool):
        self.nombre = nombre
        self.categoria = categoria
        self.cantidad_disponible = cantidad_disponible
        self.precio = precio
        self.activo = activo

    def obtener_estado(self) -> str:
        if self.activo and self.cantidad_disponible > 0:
            return "Disponible"
        return "No disponible"

    def __str__(self) -> str:
        return (
            f"Producto: {self.nombre} | Categoria: {self.categoria} | "
            f"Cantidad: {self.cantidad_disponible} | Precio: ${self.precio:.2f} | "
            f"Estado: {self.obtener_estado()}"
        )
