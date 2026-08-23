class Usuario:
    """Representa una persona registrada en el sistema."""

    def __init__(self, identificacion: str, nombre: str, correo: str) -> None:
        self.identificacion = self._validar_texto(identificacion, "identificacion")
        self.nombre = self._validar_texto(nombre, "nombre")
        self.correo = self._validar_correo(correo)

    def convertir_a_diccionario(self) -> dict[str, str]:
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "correo": self.correo,
        }

    def mostrar_informacion(self) -> str:
        return (
            f"Identificacion: {self.identificacion} | "
            f"Usuario: {self.nombre} | Correo: {self.correo}"
        )

    @staticmethod
    def _validar_texto(valor: str, campo: str) -> str:
        texto_limpio = valor.strip()
        if not texto_limpio:
            raise ValueError(f"La {campo} no puede estar vacia.")
        return texto_limpio

    @staticmethod
    def _validar_correo(correo: str) -> str:
        correo_limpio = correo.strip()
        if "@" not in correo_limpio or "." not in correo_limpio:
            raise ValueError("El correo debe tener un formato valido.")
        return correo_limpio
