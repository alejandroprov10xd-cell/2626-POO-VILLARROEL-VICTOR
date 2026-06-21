from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def main():
    # Se crea el restaurante principal del sistema.
    restaurante = Restaurante("Sabores del Valle")

    # Se crean productos disponibles en el restaurante.
    producto_1 = Producto("Arroz con pollo", "Plato fuerte", 4.50)
    producto_2 = Producto("Jugo natural", "Bebida", 1.25)
    producto_3 = Producto("Ensalada mixta", "Entrada", 2.00)
    producto_4 = Producto("Flan casero", "Postre", 1.75)

    # Se agregan los productos al servicio principal.
    restaurante.agregar_producto(producto_1)
    restaurante.agregar_producto(producto_2)
    restaurante.agregar_producto(producto_3)
    restaurante.agregar_producto(producto_4)

    # Se crean clientes y se registran sus pedidos.
    cliente_1 = Cliente("Victor Villarroel", "0991234567", 3)
    cliente_1.agregar_pedido(producto_1)
    cliente_1.agregar_pedido(producto_2)

    cliente_2 = Cliente("Ana Morales", "0987654321", 5)
    cliente_2.agregar_pedido(producto_3)
    cliente_2.agregar_pedido(producto_4)

    # Se agregan los clientes al restaurante.
    restaurante.agregar_cliente(cliente_1)
    restaurante.agregar_cliente(cliente_2)

    # Se muestra la informacion registrada de forma organizada.
    restaurante.mostrar_resumen()


if __name__ == "__main__":
    main()
