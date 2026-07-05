from modelos.producto import Producto


class Restaurante:
    """Servicio que administra los productos registrados."""

    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto: Producto) -> None:
        self.productos.append(producto)

    def mostrar_productos(self) -> None:
        print(f"Productos registrados en {self.nombre}")
        print("-" * 50)

        if not self.productos:
            print("No existen productos registrados.")
            return

        # Polimorfismo: cada objeto ejecuta su propia version del metodo.
        for numero, producto in enumerate(self.productos, start=1):
            print(f"{numero}. {producto.mostrar_informacion()}")
