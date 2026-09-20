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

    def buscar_producto(self, codigo: str) -> Producto:
        codigo_limpio = codigo.strip().lower()
        if not codigo_limpio:
            raise ValueError("Ingrese el codigo del producto.")
        for producto in self.productos:
            if producto.codigo.lower() == codigo_limpio:
                return producto
        raise ValueError("No existe un producto con ese codigo.")

    def registrar_producto(
        self, codigo: str, nombre: str, categoria: str, precio: str, stock: str
    ) -> Producto:
        if self._existe_codigo(codigo):
            raise ValueError("Ya existe un producto con ese codigo.")
        producto = self._crear_producto_desde_texto(codigo, nombre, categoria, precio, stock)
        self.productos.append(producto)
        self._guardar_productos()
        return producto

    def actualizar_producto(
        self, codigo: str, nombre: str, categoria: str, precio: str, stock: str
    ) -> Producto:
        producto_existente = self.buscar_producto(codigo)
        producto_actualizado = self._crear_producto_desde_texto(
            producto_existente.codigo, nombre, categoria, precio, stock
        )
        indice = self.productos.index(producto_existente)
        self.productos[indice] = producto_actualizado
        self._guardar_productos()
        return producto_actualizado

    def eliminar_producto(self, codigo: str) -> Producto:
        producto = self.buscar_producto(codigo)
        self.productos.remove(producto)
        self._guardar_productos()
        return producto

    def contar_productos(self) -> int:
        return len(self.productos)

    def contar_usuarios(self) -> int:
        return len(self.usuarios)

    def _existe_codigo(self, codigo: str) -> bool:
        codigo_limpio = codigo.strip().lower()
        return any(producto.codigo.lower() == codigo_limpio for producto in self.productos)

    def _crear_producto_desde_texto(
        self, codigo: str, nombre: str, categoria: str, precio: str, stock: str
    ) -> Producto:
        try:
            precio_convertido = float(precio)
        except ValueError as error:
            raise ValueError("El precio debe ser numerico.") from error

        try:
            stock_convertido = int(stock)
        except ValueError as error:
            raise ValueError("El stock debe ser un numero entero.") from error

        return Producto(codigo, nombre, categoria, precio_convertido, stock_convertido)

    def _guardar_productos(self) -> None:
        self.archivo_servicio.guardar_productos(
            [
                {
                    "codigo": producto.codigo,
                    "nombre": producto.nombre,
                    "categoria": producto.categoria,
                    "precio": producto.precio,
                    "stock": producto.stock,
                }
                for producto in self.productos
            ]
        )

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
