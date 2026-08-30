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

    def cargar_datos(
        self, productos: list[Producto], usuarios: list[Usuario], ventas: list[Venta]
    ) -> None:
        self._productos = productos.copy()
        self._usuarios = usuarios.copy()
        self._ventas = ventas.copy()

    def registrar_producto(self, producto: Producto) -> bool:
        if self.buscar_producto(producto.codigo) is not None:
            return False
        self._productos.append(producto)
        return True

    def buscar_producto(self, codigo: str) -> Producto | None:
        codigo_normalizado = codigo.strip().lower()
        return next((p for p in self._productos if p.codigo.lower() == codigo_normalizado), None)

    def actualizar_producto(
        self, codigo: str, nombre: str, categoria: str, precio: float, stock: int
    ) -> bool:
        producto = self.buscar_producto(codigo)
        if producto is None:
            return False
        producto.actualizar(nombre, categoria, precio, stock)
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        producto = self.buscar_producto(codigo)
        if producto is None:
            return False
        self._productos.remove(producto)
        return True

    def listar_productos(self) -> list[Producto]:
        return self._productos.copy()

    def obtener_categorias(self) -> set[str]:
        return {producto.categoria for producto in self._productos}

    def registrar_usuario(self, usuario: Usuario) -> bool:
        if self.buscar_usuario(usuario.identificacion) is not None:
            return False
        self._usuarios.append(usuario)
        return True

    def buscar_usuario(self, identificacion: str) -> Usuario | None:
        identificacion_normalizada = identificacion.strip().lower()
        return next(
            (u for u in self._usuarios if u.identificacion.lower() == identificacion_normalizada),
            None,
        )

    def eliminar_usuario(self, identificacion: str) -> bool:
        usuario = self.buscar_usuario(identificacion)
        if usuario is None:
            return False
        self._usuarios.remove(usuario)
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
        self._ventas.append(Venta(usuario.identificacion, producto.codigo, cantidad))
        return True

    def consultar_ventas_usuario(self, identificacion_usuario: str) -> list[Venta]:
        identificacion = identificacion_usuario.strip().lower()
        return [v for v in self._ventas if v.usuario_id.lower() == identificacion]

    def listar_ventas(self) -> list[Venta]:
        return self._ventas.copy()
