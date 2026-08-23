from collections.abc import Callable
from pathlib import Path

from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante import Restaurante


RUTA_PRODUCTOS = Path(__file__).resolve().parent / "datos" / "productos.json"
OPCIONES_MENU: tuple[str, ...] = (
    "1. Registrar producto", "2. Buscar producto", "3. Actualizar producto",
    "4. Eliminar producto", "5. Listar productos", "6. Registrar usuario",
    "7. Listar usuarios", "8. Mostrar categorias", "9. Salir",
)


def mostrar_menu() -> None:
    print("\n" + "=" * 40)
    print("        SISTEMA DE RESTAURANTE")
    print("=" * 40)
    for opcion in OPCIONES_MENU:
        print(opcion)


def leer_precio() -> float:
    while True:
        try:
            return float(input("Precio: "))
        except ValueError:
            print("Ingrese un precio numerico valido.")


def guardar_cambios(restaurante: Restaurante, archivos: ArchivoServicio) -> None:
    if archivos.guardar_productos(restaurante.listar_productos()):
        print("Cambios guardados en productos.json.")
    else:
        print("Los cambios permanecen solo durante esta ejecucion.")


def registrar_producto(restaurante: Restaurante, archivos: ArchivoServicio) -> None:
    print("\nRegistro de producto")
    try:
        producto = Producto(input("Codigo: "), input("Nombre: "),
                            input("Categoria: "), leer_precio())
    except ValueError as error:
        print(f"No se pudo crear el producto: {error}")
        return
    if not restaurante.registrar_producto(producto):
        print("Ya existe un producto con ese codigo.")
        return
    print("Producto registrado correctamente.")
    guardar_cambios(restaurante, archivos)


def buscar_producto(restaurante: Restaurante, _: ArchivoServicio) -> None:
    producto = restaurante.buscar_producto(input("Codigo del producto: "))
    print(producto.mostrar_informacion() if producto else "Producto no encontrado.")


def actualizar_producto(restaurante: Restaurante, archivos: ArchivoServicio) -> None:
    codigo = input("Codigo del producto a actualizar: ")
    if restaurante.buscar_producto(codigo) is None:
        print("Producto no encontrado.")
        return
    try:
        actualizado = restaurante.actualizar_producto(
            codigo, input("Nuevo nombre: "), input("Nueva categoria: "), leer_precio()
        )
    except ValueError as error:
        print(f"No se pudo actualizar el producto: {error}")
        return
    if actualizado:
        print("Producto actualizado correctamente.")
        guardar_cambios(restaurante, archivos)


def eliminar_producto(restaurante: Restaurante, archivos: ArchivoServicio) -> None:
    if restaurante.eliminar_producto(input("Codigo del producto a eliminar: ")):
        print("Producto eliminado correctamente.")
        guardar_cambios(restaurante, archivos)
    else:
        print("Producto no encontrado.")


def listar_productos(restaurante: Restaurante, _: ArchivoServicio) -> None:
    productos = restaurante.listar_productos()
    if not productos:
        print("No existen productos registrados.")
        return
    for numero, producto in enumerate(productos, start=1):
        print(f"{numero}. {producto.mostrar_informacion()}")


def registrar_usuario(restaurante: Restaurante, _: ArchivoServicio) -> None:
    try:
        usuario = Usuario(input("Identificacion: "), input("Nombre: "), input("Correo: "))
    except ValueError as error:
        print(f"No se pudo crear el usuario: {error}")
        return
    mensaje = ("Usuario registrado correctamente." if restaurante.registrar_usuario(usuario)
               else "Ya existe un usuario con esa identificacion.")
    print(mensaje)


def listar_usuarios(restaurante: Restaurante, _: ArchivoServicio) -> None:
    usuarios = restaurante.listar_usuarios()
    if not usuarios:
        print("No existen usuarios registrados.")
        return
    for numero, usuario in enumerate(usuarios, start=1):
        print(f"{numero}. {usuario.mostrar_informacion()}")


def mostrar_categorias(restaurante: Restaurante, _: ArchivoServicio) -> None:
    categorias = sorted(restaurante.obtener_categorias())
    print("\n".join(categorias) if categorias else "No existen categorias registradas.")


def salir(_: Restaurante, __: ArchivoServicio) -> bool:
    print("Gracias por utilizar el sistema.")
    return True


def main() -> None:
    archivos = ArchivoServicio(RUTA_PRODUCTOS)
    restaurante = Restaurante("Sabores del Valle")
    restaurante.cargar_productos(archivos.cargar_productos())
    print(f"Se cargaron {len(restaurante.listar_productos())} producto(s).")

    acciones: dict[str, Callable[[Restaurante, ArchivoServicio], None | bool]] = {
        "1": registrar_producto, "2": buscar_producto, "3": actualizar_producto,
        "4": eliminar_producto, "5": listar_productos, "6": registrar_usuario,
        "7": listar_usuarios, "8": mostrar_categorias, "9": salir,
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
