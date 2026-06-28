from modelos.cliente import Cliente
from modelos.producto import Producto
from servicios.restaurante import Restaurante


def main() -> None:
    # Se crea el servicio principal del sistema.
    restaurante = Restaurante("Sabores del Valle", "Av. Principal 123")

    # Se crean productos con tipos de datos str, int, float y bool.
    producto_entrada = Producto("Empanada de verde", "Entrada", 12, 1.50, True)
    producto_bebida = Producto("Jugo natural", "Bebida", 8, 2.25, True)

    # Se crean clientes registrados en el restaurante.
    cliente_frecuente = Cliente("Ana Torres", 28, "0987654321", 15.75, True)
    cliente_nuevo = Cliente("Carlos Mendez", 35, "0991234567", 8.50, True)

    # Se agregan los objetos a las listas administradas por Restaurante.
    restaurante.agregar_producto(producto_entrada)
    restaurante.agregar_producto(producto_bebida)
    restaurante.agregar_cliente(cliente_frecuente)
    restaurante.agregar_cliente(cliente_nuevo)

    # Se muestra la informacion registrada de forma organizada.
    restaurante.mostrar_informacion()


if __name__ == "__main__":
    main()
