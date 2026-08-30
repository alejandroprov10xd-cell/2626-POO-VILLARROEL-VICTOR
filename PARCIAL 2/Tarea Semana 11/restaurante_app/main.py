from collections.abc import Callable
from pathlib import Path

from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante import Restaurante


RUTA_DATOS = Path(__file__).resolve().parent / "datos"
OPCIONES_MENU: tuple[str, ...] = (
    "1. Registrar producto", "2. Buscar producto", "3. Actualizar producto",
    "4. Eliminar producto", "5. Listar productos", "6. Registrar usuario",
    "7. Listar usuarios", "8. Mostrar categorias", "9. Vender producto",
    "10. Consultar ventas de un usuario", "11. Salir",
)


def mostrar_menu() -> None:
    print("\n" + "=" * 42)
    print("         SISTEMA DE RESTAURANTE")
    print("=" * 42)
    for opcion in OPCIONES_MENU:
        print(opcion)


def leer_float(mensaje: str) -> float:
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Ingrese un numero valido.")


def leer_entero(mensaje: str) -> int:
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Ingrese un numero entero valido.")


def registrar_producto(restaurante: Restaurante, archivos: ArchivoServicio) -> None:
    try:
        producto = Producto(input("Codigo: "), input("Nombre: "), input("Categoria: "),
                            leer_float("Precio: "), leer_entero("Stock: "))
    except ValueError as error:
        print(f"No se pudo crear el producto: {error}")
        return
    if restaurante.registrar_producto(producto):
        archivos.guardar_productos(restaurante.listar_productos())
        print("Producto registrado y guardado correctamente.")
    else:
        print("Ya existe un producto con ese codigo.")


def buscar_producto(restaurante: Restaurante, _: ArchivoServicio) -> None:
    producto = restaurante.buscar_producto(input("Codigo del producto: "))
    print(producto.mostrar_informacion() if producto else "Producto no encontrado.")


def actualizar_producto(restaurante: Restaurante, archivos: ArchivoServicio) -> None:
    codigo = input("Codigo del producto a actualizar: ")
    if restaurante.buscar_producto(codigo) is None:
        print("Producto no encontrado.")
        return
    try:
        restaurante.actualizar_producto(
            codigo, input("Nuevo nombre: "), input("Nueva categoria: "),
            leer_float("Nuevo precio: "), leer_entero("Nuevo stock: "),
        )
    except ValueError as error:
        print(f"No se pudo actualizar: {error}")
        return
    archivos.guardar_productos(restaurante.listar_productos())
    print("Producto actualizado y guardado correctamente.")


def eliminar_producto(restaurante: Restaurante, archivos: ArchivoServicio) -> None:
    if restaurante.eliminar_producto(input("Codigo del producto a eliminar: ")):
        archivos.guardar_productos(restaurante.listar_productos())
        print("Producto eliminado y cambio guardado.")
    else:
        print("Producto no encontrado.")


def listar_productos(restaurante: Restaurante, _: ArchivoServicio) -> None:
    productos = restaurante.listar_productos()
    if not productos:
        print("No existen productos registrados.")
    for numero, producto in enumerate(productos, start=1):
        print(f"{numero}. {producto.mostrar_informacion()}")


def registrar_usuario(restaurante: Restaurante, archivos: ArchivoServicio) -> None:
    try:
        usuario = Usuario(input("Identificacion: "), input("Nombre: "), input("Correo: "))
    except ValueError as error:
        print(f"No se pudo crear el usuario: {error}")
        return
    if restaurante.registrar_usuario(usuario):
        archivos.guardar_usuarios(restaurante.listar_usuarios())
        print("Usuario registrado y guardado correctamente.")
    else:
        print("Ya existe un usuario con esa identificacion.")


def listar_usuarios(restaurante: Restaurante, _: ArchivoServicio) -> None:
    usuarios = restaurante.listar_usuarios()
    if not usuarios:
        print("No existen usuarios registrados.")
    for numero, usuario in enumerate(usuarios, start=1):
        print(f"{numero}. {usuario.mostrar_informacion()}")


def mostrar_categorias(restaurante: Restaurante, _: ArchivoServicio) -> None:
    categorias = sorted(restaurante.obtener_categorias())
    print("\n".join(categorias) if categorias else "No existen categorias registradas.")


def vender_producto(restaurante: Restaurante, archivos: ArchivoServicio) -> None:
    identificacion = input("Identificacion del usuario: ")
    codigo = input("Codigo del producto: ")
    cantidad = leer_entero("Cantidad: ")
    if not restaurante.vender_producto(codigo, identificacion, cantidad):
        print("Venta rechazada: verifique usuario, producto, cantidad y stock.")
        return
    productos_guardados = archivos.guardar_productos(restaurante.listar_productos())
    ventas_guardadas = archivos.guardar_ventas(restaurante.listar_ventas())
    if productos_guardados and ventas_guardadas:
        print("Venta registrada; stock y ventas fueron guardados.")
    else:
        print("Venta realizada en memoria, pero ocurrio un error al guardar.")


def consultar_ventas(restaurante: Restaurante, _: ArchivoServicio) -> None:
    identificacion = input("Identificacion del usuario: ")
    ventas = restaurante.consultar_ventas_usuario(identificacion)
    if not ventas:
        print("No existen ventas para ese usuario.")
        return
    for numero, venta in enumerate(ventas, start=1):
        producto = restaurante.buscar_producto(venta.producto_codigo)
        nombre = producto.nombre if producto else "Producto no disponible"
        print(f"{numero}. Codigo: {venta.producto_codigo} | Producto: {nombre} | Cantidad: {venta.cantidad}")


def salir(_: Restaurante, __: ArchivoServicio) -> bool:
    print("Gracias por utilizar el sistema.")
    return True


def main() -> None:
    archivos = ArchivoServicio(RUTA_DATOS)
    restaurante = Restaurante("Sabores del Valle")
    restaurante.cargar_datos(
        archivos.cargar_productos(), archivos.cargar_usuarios(), archivos.cargar_ventas()
    )
    print(
        f"Datos recuperados: {len(restaurante.listar_productos())} productos, "
        f"{len(restaurante.listar_usuarios())} usuarios y "
        f"{len(restaurante.listar_ventas())} ventas."
    )
    acciones: dict[str, Callable[[Restaurante, ArchivoServicio], None | bool]] = {
        "1": registrar_producto, "2": buscar_producto, "3": actualizar_producto,
        "4": eliminar_producto, "5": listar_productos, "6": registrar_usuario,
        "7": listar_usuarios, "8": mostrar_categorias, "9": vender_producto,
        "10": consultar_ventas, "11": salir,
    }
    while True:
        mostrar_menu()
        accion = acciones.get(input("Seleccione una opcion: ").strip())
        if accion is None:
            print("Opcion invalida. Intente nuevamente.")
            continue
        if accion(restaurante, archivos):
            break


if __name__ == "__main__":
    main()
