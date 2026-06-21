class Restaurante:
    """Gestiona los productos y clientes registrados en el restaurante."""

    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []
        self.clientes = []

    def agregar_producto(self, producto):
        """Registra un producto en el restaurante."""
        self.productos.append(producto)

    def agregar_cliente(self, cliente):
        """Registra un cliente en el restaurante."""
        self.clientes.append(cliente)

    def mostrar_productos(self):
        """Muestra todos los productos disponibles."""
        print("\nPRODUCTOS DISPONIBLES")
        print("---------------------")
        if not self.productos:
            print("No hay productos registrados.")
            return

        for producto in self.productos:
            print(producto)

    def mostrar_clientes(self):
        """Muestra todos los clientes registrados con sus pedidos."""
        print("\nCLIENTES REGISTRADOS")
        print("--------------------")
        if not self.clientes:
            print("No hay clientes registrados.")
            return

        for cliente in self.clientes:
            print(cliente)
            print()

    def mostrar_resumen(self):
        """Muestra un resumen general del restaurante."""
        print(f"RESTAURANTE: {self.nombre}")
        print("=" * 35)
        self.mostrar_productos()
        self.mostrar_clientes()
