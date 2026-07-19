from dataclasses import dataclass


@dataclass
class Cliente:
    """Representa la informacion de un cliente registrado."""

    identificacion: str
    nombre: str
    correo: str

    def __post_init__(self) -> None:
        self.identificacion = self._validar_texto(self.identificacion, "identificacion")
        self.nombre = self._validar_texto(self.nombre, "nombre")
        self.correo = self._validar_texto(self.correo, "correo")

    def _validar_texto(self, valor: str, campo: str) -> str:
        texto_limpio = valor.strip()
        if not texto_limpio:
            raise ValueError(f"La {campo} no puede estar vacia.")
        return texto_limpio

    def mostrar_informacion(self) -> str:
        return (
            f"Identificacion: {self.identificacion} | "
            f"Cliente: {self.nombre} | "
            f"Correo: {self.correo}"
        )
