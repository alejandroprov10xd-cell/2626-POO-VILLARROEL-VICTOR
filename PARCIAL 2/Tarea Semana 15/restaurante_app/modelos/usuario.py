class Usuario:
    """Representa un usuario que puede ingresar a la aplicacion."""

    def __init__(
        self, identificacion: str, nombre: str, correo: str, clave: str = "1234"
    ) -> None:
        self.identificacion = self._validar_texto(identificacion, "identificacion")
        self.nombre = self._validar_texto(nombre, "nombre")
        self.correo = self._validar_correo(correo)
        self.clave = self._validar_texto(clave, "clave")

    def mostrar_informacion(self) -> str:
        return f"{self.identificacion} | {self.nombre} | {self.correo}"

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
