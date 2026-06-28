class Cliente:
    """Representa a una persona registrada en el restaurante."""

    def __init__(self, nombre: str, edad: int, telefono: str, saldo_disponible: float, activo: bool):
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        self.saldo_disponible = saldo_disponible
        self.activo = activo

    def obtener_estado(self) -> str:
        if self.activo:
            return "Activo"
        return "Inactivo"

    def __str__(self) -> str:
        return (
            f"Cliente: {self.nombre} | Edad: {self.edad} | Telefono: {self.telefono} | "
            f"Saldo: ${self.saldo_disponible:.2f} | Estado: {self.obtener_estado()}"
        )
