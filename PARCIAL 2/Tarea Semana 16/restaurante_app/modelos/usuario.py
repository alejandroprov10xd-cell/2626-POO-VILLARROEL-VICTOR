class Usuario:
    """Representa un usuario que puede ingresar a la aplicacion."""

    ROLES_VALIDOS = ("Administrador", "Empleado", "Cliente")

    def __init__(
        self,
        identificacion: str,
        nombre: str,
        usuario: str,
        clave: str = "1234",
        rol: str = "Cliente",
    ) -> None:
        self.identificacion = self._validar_texto(identificacion, "identificacion")
        self.nombre = self._validar_texto(nombre, "nombre")
        self.usuario = self._validar_texto(usuario, "usuario")
        self.clave = self._validar_texto(clave, "clave")
        self.rol = self._validar_rol(rol)

    def mostrar_informacion(self) -> str:
        return f"{self.identificacion} | {self.nombre} | {self.usuario} | {self.rol}"

    def convertir_a_diccionario(self) -> dict[str, str]:
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "usuario": self.usuario,
            "clave": self.clave,
            "rol": self.rol,
        }

    @staticmethod
    def _validar_texto(valor: str, campo: str) -> str:
        if not isinstance(valor, str):
            raise ValueError(f"La {campo} debe ser texto.")
        texto = valor.strip()
        if not texto:
            raise ValueError(f"La {campo} no puede estar vacia.")
        return texto

    @classmethod
    def _validar_rol(cls, rol: str) -> str:
        rol_limpio = cls._validar_texto(rol, "rol").capitalize()
        for rol_valido in cls.ROLES_VALIDOS:
            if rol_valido.lower() == rol_limpio.lower():
                return rol_valido
        raise ValueError("El rol debe ser Administrador, Empleado o Cliente.")
