from modelos.cliente import Cliente
from modelos.producto import Producto
from servicios.restaurante import Restaurante


def mostrar_menu() -> None:
    print("=" * 40)
    print("        SISTEMA DE RESTAURANTE")
    print("=" * 40)
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("-" * 40)
    print("4. Registrar cliente")
    print("5. Listar clientes")
    print("6. Buscar cliente")
    print("-" * 40)
    print("7. Salir")


def leer_estado_disponible() -> bool:
    while True:
        respuesta = input("Disponible (s/n): ").strip().lower()
        if respuesta == "s":
            return True
        if respuesta == "n":
            return False
        print("Ingrese 's' para si o 'n' para no.")


def leer_precio() -> float:
    while True:
        try:
            return float(input("Precio: "))
        except ValueError:
            print("Ingrese un precio numerico valido.")


def registrar_producto(restaurante: Restaurante) -> None:
    print("\nRegistro de producto")
    nombre = input("Nombre: ")
    categoria = input("Categoria: ")
    precio = leer_precio()
    disponible = leer_estado_disponible()

    try:
        # Los datos ingresados se transforman en un objeto mediante el constructor.
        producto = Producto(nombre, categoria, precio, disponible)
        restaurante.registrar_producto(producto)
        print("Producto registrado correctamente.")
    except ValueError as error:
        print(f"No se pudo registrar el producto: {error}")


def listar_productos(restaurante: Restaurante) -> None:
    print("\nProductos registrados")
    print("-" * 40)

    productos = restaurante.listar_productos()
    if not productos:
        print("No existen productos registrados.")
        return

    for numero, producto in enumerate(productos, start=1):
        print(f"{numero}. {producto.mostrar_informacion()}")


def buscar_producto(restaurante: Restaurante) -> None:
    nombre = input("\nNombre del producto a buscar: ")
    producto = restaurante.buscar_producto(nombre)

    if producto is None:
        print("No se encontro un producto con ese nombre.")
    else:
        print(producto.mostrar_informacion())


def registrar_cliente(restaurante: Restaurante) -> None:
    print("\nRegistro de cliente")
    id_cliente = input("Identificador: ").strip()
    nombre = input("Nombre: ").strip()
    correo = input("Correo: ").strip()

    if not id_cliente or not nombre or not correo:
        print("Todos los datos del cliente son obligatorios.")
        return

    cliente = Cliente(id_cliente=id_cliente, nombre=nombre, correo=correo)
    restaurante.registrar_cliente(cliente)
    print("Cliente registrado correctamente.")


def listar_clientes(restaurante: Restaurante) -> None:
    print("\nClientes registrados")
    print("-" * 40)

    clientes = restaurante.listar_clientes()
    if not clientes:
        print("No existen clientes registrados.")
        return

    for numero, cliente in enumerate(clientes, start=1):
        print(f"{numero}. {cliente.mostrar_informacion()}")


def buscar_cliente(restaurante: Restaurante) -> None:
    id_cliente = input("\nIdentificador del cliente a buscar: ")
    cliente = restaurante.buscar_cliente(id_cliente)

    if cliente is None:
        print("No se encontro un cliente con ese identificador.")
    else:
        print(cliente.mostrar_informacion())


def main() -> None:
    restaurante = Restaurante("Sabores del Valle")

    while True:
        print()
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            registrar_producto(restaurante)
        elif opcion == "2":
            listar_productos(restaurante)
        elif opcion == "3":
            buscar_producto(restaurante)
        elif opcion == "4":
            registrar_cliente(restaurante)
        elif opcion == "5":
            listar_clientes(restaurante)
        elif opcion == "6":
            buscar_cliente(restaurante)
        elif opcion == "7":
            print("Gracias por utilizar el sistema.")
            break
        else:
            print("Opcion invalida. Intente nuevamente.")


if __name__ == "__main__":
    main()
