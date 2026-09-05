class Producto:
    """Representa un producto disponible en el restaurante."""

    def __init__(
        self, codigo: str, nombre: str, categoria: str, precio: float, stock: int
    ) -> None:
        self.codigo = self._validar_texto(codigo, "codigo")
        self.nombre = self._validar_texto(nombre, "nombre")
        self.categoria = self._validar_texto(categoria, "categoria")
        self.precio = self._validar_precio(precio)
        self.stock = self._validar_stock(stock)

    def actualizar(
        self, nombre: str, categoria: str, precio: float, stock: int
    ) -> None:
        self.nombre = self._validar_texto(nombre, "nombre")
        self.categoria = self._validar_texto(categoria, "categoria")
        self.precio = self._validar_precio(precio)
        self.stock = self._validar_stock(stock)

    def vender(self, cantidad: int) -> None:
        cantidad_validada = self._validar_cantidad(cantidad)
        if cantidad_validada > self.stock:
            raise ValueError("No existe stock suficiente.")
        self.stock -= cantidad_validada

    def convertir_a_diccionario(self) -> dict[str, str | float | int]:
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "stock": self.stock,
        }

    def mostrar_informacion(self) -> str:
        return (
            f"Codigo: {self.codigo} | Producto: {self.nombre} | "
            f"Categoria: {self.categoria} | Precio: ${self.precio:.2f} | "
            f"Stock: {self.stock}"
        )

    @staticmethod
    def _validar_texto(valor: str, campo: str) -> str:
        if not isinstance(valor, str):
            raise ValueError(f"El {campo} debe ser texto.")
        texto = valor.strip()
        if not texto:
            raise ValueError(f"El {campo} no puede estar vacio.")
        return texto

    @staticmethod
    def _validar_precio(precio: float) -> float:
        if isinstance(precio, bool) or not isinstance(precio, (int, float)):
            raise ValueError("El precio debe ser numerico.")
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")
        return float(precio)

    @staticmethod
    def _validar_stock(stock: int) -> int:
        if isinstance(stock, bool) or not isinstance(stock, int):
            raise ValueError("El stock debe ser un numero entero.")
        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")
        return stock

    @staticmethod
    def _validar_cantidad(cantidad: int) -> int:
        if isinstance(cantidad, bool) or not isinstance(cantidad, int):
            raise ValueError("La cantidad debe ser un numero entero.")
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        return cantidad
