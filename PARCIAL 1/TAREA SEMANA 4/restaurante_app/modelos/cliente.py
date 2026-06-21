class Cliente:
    """Representa a un cliente que consume en el restaurante."""

    def __init__(self, nombre, telefono, mesa):
        self.nombre = nombre
        self.telefono = telefono
        self.mesa = mesa
        self.pedidos = []

    def agregar_pedido(self, producto):
        """Agrega un producto al pedido del cliente."""
        self.pedidos.append(producto)

    def calcular_total(self):
        """Calcula el total a pagar por los productos pedidos."""
        total = 0
        for producto in self.pedidos:
            total += producto.precio
        return total

    def mostrar_pedidos(self):
        """Devuelve los productos solicitados por el cliente."""
        if not self.pedidos:
            return "Sin pedidos registrados"

        detalle = ""
        for producto in self.pedidos:
            detalle += f"\n    - {producto.nombre}: ${producto.precio:.2f}"
        return detalle

    def __str__(self):
        return (
            f"Cliente: {self.nombre} | Telefono: {self.telefono} | Mesa: {self.mesa}"
            f"\n  Pedidos:{self.mostrar_pedidos()}"
            f"\n  Total a pagar: ${self.calcular_total():.2f}"
        )
