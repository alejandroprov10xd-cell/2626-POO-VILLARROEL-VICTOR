from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:
    """Centraliza las operaciones que usan las vistas de Tkinter."""

    def __init__(self, archivo_servicio: ArchivoServicio) -> None:
        self.archivo_servicio = archivo_servicio
        self.productos = self._crear_productos()
        self.usuarios = self._crear_usuarios()

    def validar_acceso(self, identificacion: str, clave: str) -> bool:
        identificacion = identificacion.strip().lower()
        clave = clave.strip()
        if not identificacion or not clave:
            return False
        return any(
            usuario.identificacion.lower() == identificacion and usuario.clave == clave
            for usuario in self.usuarios
        )

    def listar_productos(self) -> list[Producto]:
        return self.productos.copy()

    def listar_usuarios(self) -> list[Usuario]:
        return self.usuarios.copy()

    def contar_productos(self) -> int:
        return len(self.productos)

    def contar_usuarios(self) -> int:
        return len(self.usuarios)

    def _crear_productos(self) -> list[Producto]:
        productos = []
        for registro in self.archivo_servicio.cargar_productos():
            try:
                productos.append(
                    Producto(
                        registro["codigo"],
                        registro["nombre"],
                        registro["categoria"],
                        registro["precio"],
                        registro["stock"],
                    )
                )
            except (KeyError, ValueError):
                continue
        return productos

    def _crear_usuarios(self) -> list[Usuario]:
        usuarios = []
        for registro in self.archivo_servicio.cargar_usuarios():
            try:
                usuarios.append(
                    Usuario(
                        registro["identificacion"],
                        registro["nombre"],
                        registro["correo"],
                        registro.get("clave", "1234"),
                    )
                )
            except (KeyError, ValueError):
                continue
        return usuarios
