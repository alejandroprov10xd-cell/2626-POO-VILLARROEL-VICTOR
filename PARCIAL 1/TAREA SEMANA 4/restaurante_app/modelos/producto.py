class Producto:
    """Representa un producto disponible en el restaurante."""

    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def mostrar_informacion(self):
        """Devuelve los datos principales del producto."""
        return f"{self.nombre} | Categoria: {self.categoria} | Precio: ${self.precio:.2f}"

    def __str__(self):
        return self.mostrar_informacion()
