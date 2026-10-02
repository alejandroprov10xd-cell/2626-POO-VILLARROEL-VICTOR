class Producto:
    """Representa un producto del restaurante mostrado en la interfaz."""

    def __init__(
        self, codigo: str, nombre: str, categoria: str, precio: float, stock: int
    ) -> None:
        self.codigo = self._validar_texto(codigo, "codigo")
        self.nombre = self._validar_texto(nombre, "nombre")
        self.categoria = self._validar_texto(categoria, "categoria")
        self.precio = self._validar_precio(precio)
        self.stock = self._validar_stock(stock)

    @property
    def cantidad(self) -> int:
        return self.stock

    def mostrar_informacion(self) -> str:
        return (
            f"{self.codigo} | {self.nombre} | {self.categoria} | "
            f"${self.precio:.2f} | Cantidad: {self.stock}"
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
