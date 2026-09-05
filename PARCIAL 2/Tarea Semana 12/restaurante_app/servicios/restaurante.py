from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class Restaurante:
    """Administra colecciones y reglas de negocio del restaurante."""

    def __init__(self, nombre: str) -> None:
        self.nombre = nombre.strip()
        self._productos: list[Producto] = []
        self._usuarios: list[Usuario] = []
        self._ventas: list[Venta] = []
        self._productos_por_codigo: dict[str, Producto] = {}
        self._usuarios_por_id: dict[str, Usuario] = {}
        self._ventas_por_usuario: dict[str, list[Venta]] = {}

    @staticmethod
    def _normalizar(clave: str) -> str:
        return clave.strip().lower()

    def cargar_datos(
        self, productos: list[Producto], usuarios: list[Usuario], ventas: list[Venta]
    ) -> None:
        # Preparar todo antes de reemplazar el estado; no aceptar claves repetidas.
        productos_por_codigo = {self._normalizar(p.codigo): p for p in productos}
        usuarios_por_id = {self._normalizar(u.identificacion): u for u in usuarios}
        if len(productos_por_codigo) != len(productos):
            raise ValueError("Existen codigos de productos duplicados.")
        if len(usuarios_por_id) != len(usuarios):
            raise ValueError("Existen identificaciones de usuarios duplicadas.")
        ventas_por_usuario: dict[str, list[Venta]] = {}
        for venta in ventas:
            ventas_por_usuario.setdefault(self._normalizar(venta.usuario_id), []).append(venta)
        self._productos = productos.copy()
        self._usuarios = usuarios.copy()
        self._ventas = ventas.copy()
        self._productos_por_codigo = productos_por_codigo
        self._usuarios_por_id = usuarios_por_id
        self._ventas_por_usuario = ventas_por_usuario

    def registrar_producto(self, producto: Producto) -> bool:
        if self.buscar_producto(producto.codigo) is not None:
            return False
        self._productos.append(producto)
        self._productos_por_codigo[self._normalizar(producto.codigo)] = producto
        return True

    def buscar_producto(self, codigo: str) -> Producto | None:
        return self._productos_por_codigo.get(self._normalizar(codigo))

    def actualizar_producto(
        self, codigo: str, nombre: str, categoria: str, precio: float, stock: int
    ) -> bool:
        producto = self.buscar_producto(codigo)
        if producto is None:
            return False
        producto.actualizar(nombre, categoria, precio, stock)
        # Lista e indice comparten el mismo objeto; el codigo no cambia.
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        producto = self.buscar_producto(codigo)
        if producto is None:
            return False
        self._productos.remove(producto)
        del self._productos_por_codigo[self._normalizar(producto.codigo)]
        return True

    def listar_productos(self) -> list[Producto]:
        return self._productos.copy()

    def obtener_categorias(self) -> set[str]:
        return {producto.categoria for producto in self._productos}

    def registrar_usuario(self, usuario: Usuario) -> bool:
        if self.buscar_usuario(usuario.identificacion) is not None:
            return False
        self._usuarios.append(usuario)
        self._usuarios_por_id[self._normalizar(usuario.identificacion)] = usuario
        return True

    def buscar_usuario(self, identificacion: str) -> Usuario | None:
        return self._usuarios_por_id.get(self._normalizar(identificacion))

    def eliminar_usuario(self, identificacion: str) -> bool:
        usuario = self.buscar_usuario(identificacion)
        if usuario is None:
            return False
        self._usuarios.remove(usuario)
        del self._usuarios_por_id[self._normalizar(usuario.identificacion)]
        # Las ventas historicas se conservan, igual que en la Semana 11.
        return True

    def listar_usuarios(self) -> list[Usuario]:
        return self._usuarios.copy()

    def vender_producto(
        self, codigo_producto: str, identificacion_usuario: str, cantidad: int
    ) -> bool:
        usuario = self.buscar_usuario(identificacion_usuario)
        producto = self.buscar_producto(codigo_producto)
        if usuario is None or producto is None:
            return False
        if isinstance(cantidad, bool) or not isinstance(cantidad, int):
            return False
        if cantidad <= 0 or producto.stock < cantidad:
            return False
        producto.vender(cantidad)
        venta = Venta(usuario.identificacion, producto.codigo, cantidad)
        self._ventas.append(venta)
        self._ventas_por_usuario.setdefault(
            self._normalizar(usuario.identificacion), []
        ).append(venta)
        return True

    def consultar_ventas_usuario(self, identificacion_usuario: str) -> list[Venta]:
        identificacion = self._normalizar(identificacion_usuario)
        return self._ventas_por_usuario.get(identificacion, []).copy()

    def listar_ventas(self) -> list[Venta]:
        return self._ventas.copy()
