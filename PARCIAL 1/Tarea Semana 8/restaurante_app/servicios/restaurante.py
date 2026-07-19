from modelos.cliente import Cliente
from modelos.producto import Producto


class Restaurante:
    """Servicio encargado de administrar productos y clientes."""

    def __init__(self, nombre: str) -> None:
        self.nombre = nombre.strip()
        self._productos: list[Producto] = []
        self._clientes: list[Cliente] = []

    def registrar_producto(self, producto: Producto) -> bool:
        if self._existe_codigo_producto(producto.codigo):
            return False

        self._productos.append(producto)
        return True

    def listar_productos(self) -> list[Producto]:
        return self._productos.copy()

    def registrar_cliente(self, cliente: Cliente) -> bool:
        if self._existe_identificacion_cliente(cliente.identificacion):
            return False

        self._clientes.append(cliente)
        return True

    def listar_clientes(self) -> list[Cliente]:
        return self._clientes.copy()

    def _existe_codigo_producto(self, codigo: str) -> bool:
        codigo_normalizado = codigo.strip().lower()
        return any(
            producto.codigo.lower() == codigo_normalizado
            for producto in self._productos
        )

    def _existe_identificacion_cliente(self, identificacion: str) -> bool:
        identificacion_normalizada = identificacion.strip().lower()
        return any(
            cliente.identificacion.lower() == identificacion_normalizada
            for cliente in self._clientes
        )
