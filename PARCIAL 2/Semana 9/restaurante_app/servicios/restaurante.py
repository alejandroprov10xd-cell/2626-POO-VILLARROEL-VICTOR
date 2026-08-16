from modelos.producto import Producto
from modelos.usuario import Usuario


class Restaurante:
    """Servicio encargado de administrar las colecciones del restaurante."""

    def __init__(self, nombre: str) -> None:
        self.nombre = nombre.strip()
        self._productos: list[Producto] = []
        self._usuarios: list[Usuario] = []

    def registrar_producto(self, producto: Producto) -> bool:
        if self.buscar_producto(producto.codigo) is not None:
            return False

        self._productos.append(producto)
        return True

    def buscar_producto(self, codigo: str) -> Producto | None:
        codigo_normalizado = codigo.strip().lower()
        for producto in self._productos:
            if producto.codigo.lower() == codigo_normalizado:
                return producto
        return None

    def actualizar_producto(self, codigo: str, nombre: str, categoria: str, precio: float) -> bool:
        producto = self.buscar_producto(codigo)
        if producto is None:
            return False

        producto.actualizar(nombre, categoria, precio)
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
        for usuario in self._usuarios:
            if usuario.identificacion.lower() == identificacion_normalizada:
                return usuario
        return None

    def listar_usuarios(self) -> list[Usuario]:
        return self._usuarios.copy()

    def exportar_productos_como_diccionarios(self) -> list[dict[str, str | float]]:
        return [producto.convertir_a_diccionario() for producto in self._productos]

    def exportar_usuarios_como_diccionarios(self) -> list[dict[str, str]]:
        return [usuario.convertir_a_diccionario() for usuario in self._usuarios]
