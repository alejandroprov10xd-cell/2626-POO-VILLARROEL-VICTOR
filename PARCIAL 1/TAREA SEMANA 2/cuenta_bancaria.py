class CuentaBancaria:
    """Representa una cuenta bancaria simple.

    Atributos:
        titular (str): Nombre del dueño de la cuenta.
        saldo (float): Saldo actual de la cuenta.
    """

    def __init__(self, titular: str, saldo: float = 0.0):
        self.titular = str(titular)
        self.saldo = float(saldo)

    def depositar(self, monto: float) -> None:
        """Deposita `monto` en la cuenta.

        Lanza ValueError si el monto no es positivo.
        """
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser positivo")
        self.saldo += monto

    def retirar(self, monto: float) -> None:
        """Retira `monto` de la cuenta.

        Lanza ValueError si el monto no es positivo o si fondos insuficientes.
        """
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser positivo")
        if monto > self.saldo:
            raise ValueError("Fondos insuficientes")
        self.saldo -= monto

    def transferir(self, otra_cuenta: "CuentaBancaria", monto: float) -> None:
        """Transfiere `monto` desde esta cuenta a `otra_cuenta`.

        Usa `retirar` y `depositar` para mantener las reglas.
        """
        self.retirar(monto)
        otra_cuenta.depositar(monto)

    def __str__(self) -> str:
        return f"Cuenta(titular={self.titular}, saldo={self.saldo:.2f})"
