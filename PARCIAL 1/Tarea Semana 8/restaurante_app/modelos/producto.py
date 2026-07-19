class Producto:
    """Representa un producto general del restaurante."""

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float) -> None:
        self.codigo = self._validar_texto(codigo, "codigo")
        self.nombre = self._validar_texto(nombre, "nombre")
        self.categoria = self._validar_texto(categoria, "categoria")
        self.precio = self._validar_precio(precio)

    def _validar_texto(self, valor: str, campo: str) -> str:
        texto_limpio = valor.strip()
        if not texto_limpio:
            raise ValueError(f"El {campo} no puede estar vacio.")
        return texto_limpio

    def _validar_precio(self, precio: float) -> float:
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")
        return precio

    def mostrar_informacion(self) -> str:
        return (
            f"Codigo: {self.codigo} | "
            f"Producto: {self.nombre} | "
            f"Categoria: {self.categoria} | "
            f"Precio: ${self.precio:.2f}"
        )
