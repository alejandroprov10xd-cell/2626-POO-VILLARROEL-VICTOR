from collections.abc import Callable

from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante


OPCIONES_MENU: tuple[str, ...] = (
    "1. Registrar producto",
    "2. Buscar producto",
    "3. Actualizar producto",
    "4. Eliminar producto",
    "5. Listar productos",
    "----------------------------------------",
    "6. Registrar usuario",
    "7. Listar usuarios",
    "----------------------------------------",
    "8. Mostrar categorias",
    "9. Salir",
)


def mostrar_menu() -> None:
    print("=" * 40)
    print("        SISTEMA DE RESTAURANTE")
    print("=" * 40)
    for opcion in OPCIONES_MENU:
        print(opcion)


def leer_precio() -> float:
    while True:
        try:
            precio = float(input("Precio: "))
            if precio <= 0:
                print("El precio debe ser mayor que cero.")
                continue
            return precio
        except ValueError:
            print("Ingrese un precio numerico valido.")


def solicitar_datos_producto() -> dict[str, str | float]:
    return {
        "codigo": input("Codigo: "),
        "nombre": input("Nombre: "),
        "categoria": input("Categoria: "),
        "precio": leer_precio(),
    }


def solicitar_datos_actualizacion_producto() -> dict[str, str | float]:
    return {
        "nombre": input("Nombre: "),
        "categoria": input("Categoria: "),
        "precio": leer_precio(),
    }


def registrar_producto(restaurante: Restaurante) -> None:
    print("\nRegistro de producto")
    datos_producto = solicitar_datos_producto()

    try:
        producto = Producto(
            codigo=str(datos_producto["codigo"]),
            nombre=str(datos_producto["nombre"]),
            categoria=str(datos_producto["categoria"]),
            precio=float(datos_producto["precio"]),
        )
    except ValueError as error:
        print(f"No se pudo crear el producto: {error}")
        return

    if restaurante.registrar_producto(producto):
        print("Producto registrado correctamente.")
    else:
        print("No se pudo registrar: ya existe un producto con ese codigo.")


def buscar_producto(restaurante: Restaurante) -> None:
    print("\nBusqueda de producto")
    codigo = input("Codigo del producto: ")
    producto = restaurante.buscar_producto(codigo)

    if producto is None:
        print("No existe un producto con ese codigo.")
        return

    print(producto.mostrar_informacion())
    print(f"Datos en diccionario: {producto.convertir_a_diccionario()}")


def actualizar_producto(restaurante: Restaurante) -> None:
    print("\nActualizacion de producto")
    codigo = input("Codigo del producto a actualizar: ")

    if restaurante.buscar_producto(codigo) is None:
        print("No existe un producto con ese codigo.")
        return

    print("Ingrese los nuevos datos del producto.")
    datos_producto = solicitar_datos_actualizacion_producto()

    try:
        restaurante.actualizar_producto(
            codigo=codigo,
            nombre=str(datos_producto["nombre"]),
            categoria=str(datos_producto["categoria"]),
            precio=float(datos_producto["precio"]),
        )
    except ValueError as error:
        print(f"No se pudo actualizar el producto: {error}")
        return

    print("Producto actualizado correctamente.")


def eliminar_producto(restaurante: Restaurante) -> None:
    print("\nEliminacion de producto")
    codigo = input("Codigo del producto a eliminar: ")

    if restaurante.eliminar_producto(codigo):
        print("Producto eliminado correctamente.")
    else:
        print("No existe un producto con ese codigo.")


def listar_productos(restaurante: Restaurante) -> None:
    print("\nProductos registrados")
    print("-" * 40)

    productos = restaurante.listar_productos()
    if not productos:
        print("No existen productos registrados.")
        return

    for numero, producto in enumerate(productos, start=1):
        print(f"{numero}. {producto.mostrar_informacion()}")

    print("\nProductos como diccionarios:")
    for datos_producto in restaurante.exportar_productos_como_diccionarios():
        print(datos_producto)


def registrar_usuario(restaurante: Restaurante) -> None:
    print("\nRegistro de usuario")
    datos_usuario: dict[str, str] = {
        "identificacion": input("Identificacion: "),
        "nombre": input("Nombre: "),
        "correo": input("Correo: "),
    }

    try:
        usuario = Usuario(
            identificacion=datos_usuario["identificacion"],
            nombre=datos_usuario["nombre"],
            correo=datos_usuario["correo"],
        )
    except ValueError as error:
        print(f"No se pudo crear el usuario: {error}")
        return

    if restaurante.registrar_usuario(usuario):
        print("Usuario registrado correctamente.")
    else:
        print("No se pudo registrar: ya existe un usuario con esa identificacion.")


def listar_usuarios(restaurante: Restaurante) -> None:
    print("\nUsuarios registrados")
    print("-" * 40)

    usuarios = restaurante.listar_usuarios()
    if not usuarios:
        print("No existen usuarios registrados.")
        return

    for numero, usuario in enumerate(usuarios, start=1):
        print(f"{numero}. {usuario.mostrar_informacion()}")

    print("\nUsuarios como diccionarios:")
    for datos_usuario in restaurante.exportar_usuarios_como_diccionarios():
        print(datos_usuario)


def mostrar_categorias(restaurante: Restaurante) -> None:
    print("\nCategorias registradas")
    print("-" * 40)

    categorias = restaurante.obtener_categorias()
    if not categorias:
        print("No existen categorias registradas.")
        return

    for numero, categoria in enumerate(sorted(categorias), start=1):
        print(f"{numero}. {categoria}")


def salir(_: Restaurante) -> bool:
    print("Gracias por utilizar el sistema.")
    return True


def main() -> None:
    restaurante = Restaurante("Sabores del Valle")

    acciones_menu: dict[str, Callable[[Restaurante], None | bool]] = {
        "1": registrar_producto,
        "2": buscar_producto,
        "3": actualizar_producto,
        "4": eliminar_producto,
        "5": listar_productos,
        "6": registrar_usuario,
        "7": listar_usuarios,
        "8": mostrar_categorias,
        "9": salir,
    }

    while True:
        print()
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()
        accion = acciones_menu.get(opcion)

        if accion is None:
            print("Opcion invalida. Intente nuevamente.")
            continue

        debe_salir = accion(restaurante)
        if debe_salir:
            break


if __name__ == "__main__":
    main()
