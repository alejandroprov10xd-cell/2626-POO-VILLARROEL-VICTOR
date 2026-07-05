class Producto:
    """Clase padre que representa un producto general del restaurante."""

    def __init__(self, nombre: str, precio: float, disponible: bool) -> None:
        self.nombre = nombre
        self.__precio = 0.0
        self.disponible = disponible
        self.cambiar_precio(precio)

    def obtener_precio(self) -> float:
        """Devuelve el precio encapsulado del producto."""
        return self.__precio

    def cambiar_precio(self, nuevo_precio: float) -> None:
        """Modifica el precio solo si es mayor que cero."""
        if nuevo_precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")

        self.__precio = nuevo_precio

    def obtener_estado_disponibilidad(self) -> str:
        return "Disponible" if self.disponible else "No disponible"

    def mostrar_informacion(self) -> str:
        return (
            f"Producto: {self.nombre} | "
            f"Precio: ${self.obtener_precio():.2f} | "
            f"Estado: {self.obtener_estado_disponibilidad()}"
        )
