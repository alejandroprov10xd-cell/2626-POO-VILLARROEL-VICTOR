from modelos.cliente import Cliente
from modelos.producto import Producto


class Restaurante:
    """Servicio encargado de administrar productos y clientes."""

    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self.productos: list[Producto] = []
        self.clientes: list[Cliente] = []

    def registrar_producto(self, producto: Producto) -> None:
        self.productos.append(producto)

    def listar_productos(self) -> list[Producto]:
        return self.productos

    def buscar_producto(self, nombre: str) -> Producto | None:
        nombre_buscado = nombre.strip().lower()
        for producto in self.productos:
            if producto.nombre.lower() == nombre_buscado:
                return producto
        return None

    def registrar_cliente(self, cliente: Cliente) -> None:
        self.clientes.append(cliente)

    def listar_clientes(self) -> list[Cliente]:
        return self.clientes

    def buscar_cliente(self, id_cliente: str) -> Cliente | None:
        id_buscado = id_cliente.strip().lower()
        for cliente in self.clientes:
            if cliente.id_cliente.lower() == id_buscado:
                return cliente
        return None
