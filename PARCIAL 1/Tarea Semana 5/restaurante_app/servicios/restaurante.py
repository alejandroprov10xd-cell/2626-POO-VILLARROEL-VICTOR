from modelos.cliente import Cliente
from modelos.producto import Producto


class Restaurante:
    """Administra los productos y clientes registrados."""

    def __init__(self, nombre: str, direccion: str):
        self.nombre = nombre
        self.direccion = direccion
        self.productos: list[Producto] = []
        self.clientes: list[Cliente] = []

    def agregar_producto(self, producto: Producto) -> None:
        self.productos.append(producto)

    def agregar_cliente(self, cliente: Cliente) -> None:
        self.clientes.append(cliente)

    def mostrar_productos(self) -> None:
        print("PRODUCTOS REGISTRADOS")
        for producto in self.productos:
            print(f"- {producto}")

    def mostrar_clientes(self) -> None:
        print("CLIENTES REGISTRADOS")
        for cliente in self.clientes:
            print(f"- {cliente}")

    def mostrar_informacion(self) -> None:
        print(f"Restaurante: {self.nombre}")
        print(f"Direccion: {self.direccion}")
        print()
        self.mostrar_productos()
        print()
        self.mostrar_clientes()
