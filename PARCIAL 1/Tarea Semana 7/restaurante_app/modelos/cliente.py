from dataclasses import dataclass


@dataclass
class Cliente:
    """Almacena los datos principales de un cliente del restaurante."""

    id_cliente: str
    nombre: str
    correo: str

    def mostrar_informacion(self) -> str:
        return (
            f"Cliente: {self.nombre} | "
            f"ID: {self.id_cliente} | "
            f"Correo: {self.correo}"
        )
