class Producto:
    """Representa un producto disponible en el restaurante."""

    def __init__(self, nombre: str, categoria: str, precio: float, disponible: bool) -> None:
        self._nombre = ""
        self._categoria = ""
        self._precio = 0.0
        self._disponible = True

        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.disponible = disponible

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        if not nuevo_nombre or not nuevo_nombre.strip():
            raise ValueError("El nombre del producto no puede estar vacio.")
        self._nombre = nuevo_nombre.strip()

    @property
    def categoria(self) -> str:
        return self._categoria

    @categoria.setter
    def categoria(self, nueva_categoria: str) -> None:
        if not nueva_categoria or not nueva_categoria.strip():
            raise ValueError("La categoria del producto no puede estar vacia.")
        self._categoria = nueva_categoria.strip()

    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, nuevo_precio: float) -> None:
        if nuevo_precio <= 0:
            raise ValueError("El precio del producto debe ser mayor que cero.")
        self._precio = nuevo_precio

    @property
    def disponible(self) -> bool:
        return self._disponible

    @disponible.setter
    def disponible(self, nuevo_estado: bool) -> None:
        self._disponible = bool(nuevo_estado)

    def mostrar_informacion(self) -> str:
        estado = "Disponible" if self.disponible else "No disponible"
        return (
            f"Producto: {self.nombre} | "
            f"Categoria: {self.categoria} | "
            f"Precio: ${self.precio:.2f} | "
            f"Estado: {estado}"
        )
