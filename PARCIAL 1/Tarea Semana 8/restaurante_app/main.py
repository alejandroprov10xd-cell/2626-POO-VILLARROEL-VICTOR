from modelos.bebida import Bebida
from modelos.cliente import Cliente
from modelos.producto import Producto
from servicios.restaurante import Restaurante


def mostrar_menu() -> None:
    print("=" * 40)
    print("        SISTEMA DE RESTAURANTE")
    print("=" * 40)
    print("1. Registrar producto")
    print("2. Registrar bebida")
    print("3. Registrar cliente")
    print("-" * 40)
    print("4. Listar productos")
    print("5. Listar clientes")
    print("-" * 40)
    print("6. Salir")


def leer_precio() -> float:
    while True:
        try:
            return float(input("Precio: "))
        except ValueError:
            print("Ingrese un precio numerico valido.")


def solicitar_datos_producto() -> tuple[str, str, str, float]:
    codigo = input("Codigo: ")
    nombre = input("Nombre: ")
    categoria = input("Categoria: ")
    precio = leer_precio()
    return codigo, nombre, categoria, precio


def registrar_producto(restaurante: Restaurante) -> None:
    print("\nRegistro de producto")
    codigo, nombre, categoria, precio = solicitar_datos_producto()

    try:
        producto = Producto(codigo, nombre, categoria, precio)
    except ValueError as error:
        print(f"No se pudo crear el producto: {error}")
        return

    if restaurante.registrar_producto(producto):
        print("Producto registrado correctamente.")
    else:
        print("No se pudo registrar: ya existe un producto con ese codigo.")


def registrar_bebida(restaurante: Restaurante) -> None:
    print("\nRegistro de bebida")
    codigo, nombre, categoria, precio = solicitar_datos_producto()
    tamano = input("Tamano: ")
    tipo_envase = input("Tipo de envase: ")

    try:
        bebida = Bebida(codigo, nombre, categoria, precio, tamano, tipo_envase)
    except ValueError as error:
        print(f"No se pudo crear la bebida: {error}")
        return

    if restaurante.registrar_producto(bebida):
        print("Bebida registrada correctamente.")
    else:
        print("No se pudo registrar: ya existe un producto con ese codigo.")


def registrar_cliente(restaurante: Restaurante) -> None:
    print("\nRegistro de cliente")
    identificacion = input("Identificacion: ")
    nombre = input("Nombre: ")
    correo = input("Correo: ")

    try:
        cliente = Cliente(identificacion=identificacion, nombre=nombre, correo=correo)
    except ValueError as error:
        print(f"No se pudo crear el cliente: {error}")
        return

    if restaurante.registrar_cliente(cliente):
        print("Cliente registrado correctamente.")
    else:
        print("No se pudo registrar: ya existe un cliente con esa identificacion.")


def listar_productos(restaurante: Restaurante) -> None:
    print("\nProductos registrados")
    print("-" * 40)

    productos = restaurante.listar_productos()
    if not productos:
        print("No existen productos registrados.")
        return

    for numero, producto in enumerate(productos, start=1):
        print(f"{numero}. {producto.mostrar_informacion()}")


def listar_clientes(restaurante: Restaurante) -> None:
    print("\nClientes registrados")
    print("-" * 40)

    clientes = restaurante.listar_clientes()
    if not clientes:
        print("No existen clientes registrados.")
        return

    for numero, cliente in enumerate(clientes, start=1):
        print(f"{numero}. {cliente.mostrar_informacion()}")


def main() -> None:
    restaurante = Restaurante("Sabores del Valle")

    while True:
        print()
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            registrar_producto(restaurante)
        elif opcion == "2":
            registrar_bebida(restaurante)
        elif opcion == "3":
            registrar_cliente(restaurante)
        elif opcion == "4":
            listar_productos(restaurante)
        elif opcion == "5":
            listar_clientes(restaurante)
        elif opcion == "6":
            print("Gracias por utilizar el sistema.")
            break
        else:
            print("Opcion invalida. Intente nuevamente.")


if __name__ == "__main__":
    main()
