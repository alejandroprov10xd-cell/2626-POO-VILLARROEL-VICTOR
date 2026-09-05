class Usuario:
    """Representa una persona registrada que puede realizar compras."""

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
            f"Identificacion: {self.identificacion} | Usuario: {self.nombre} | "
            f"Correo: {self.correo}"
        )

    @staticmethod
    def _validar_texto(valor: str, campo: str) -> str:
        if not isinstance(valor, str):
            raise ValueError(f"La {campo} debe ser texto.")
        texto = valor.strip()
        if not texto:
            raise ValueError(f"La {campo} no puede estar vacia.")
        return texto

    @staticmethod
    def _validar_correo(correo: str) -> str:
        correo_limpio = Usuario._validar_texto(correo, "correo")
        if "@" not in correo_limpio or "." not in correo_limpio:
            raise ValueError("El correo debe tener un formato valido.")
        return correo_limpio
