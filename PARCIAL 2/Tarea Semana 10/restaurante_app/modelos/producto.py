class Producto:
    """Representa un producto del restaurante."""

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float) -> None:
        self.codigo = self._validar_texto(codigo, "codigo")
        self.nombre = self._validar_texto(nombre, "nombre")
        self.categoria = self._validar_texto(categoria, "categoria")
        self.precio = self._validar_precio(precio)

    def actualizar(self, nombre: str, categoria: str, precio: float) -> None:
        nombre_validado = self._validar_texto(nombre, "nombre")
        categoria_validada = self._validar_texto(categoria, "categoria")
        precio_validado = self._validar_precio(precio)
        self.nombre = nombre_validado
        self.categoria = categoria_validada
        self.precio = precio_validado

    def convertir_a_diccionario(self) -> dict[str, str | float]:
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
        }

    def mostrar_informacion(self) -> str:
        return (
            f"Codigo: {self.codigo} | Producto: {self.nombre} | "
            f"Categoria: {self.categoria} | Precio: ${self.precio:.2f}"
        )

    @staticmethod
    def _validar_texto(valor: str, campo: str) -> str:
        if not isinstance(valor, str):
            raise ValueError(f"El {campo} debe ser texto.")
        texto_limpio = valor.strip()
        if not texto_limpio:
            raise ValueError(f"El {campo} no puede estar vacio.")
        return texto_limpio

    @staticmethod
    def _validar_precio(precio: float) -> float:
        if isinstance(precio, bool) or not isinstance(precio, (int, float)):
            raise ValueError("El precio debe ser numerico.")
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")
        return float(precio)
