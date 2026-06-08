from cuenta_bancaria import CuentaBancaria


def main():
    cuenta_victor = CuentaBancaria("Víctor Villarroel", 1000.0)
    cuenta_ana = CuentaBancaria("Ana", 200.0)

    print("Cuentas iniciales:")
    print(cuenta_victor)
    print(cuenta_ana)

    cuenta_victor.depositar(150.0)
    print("\nDespués de depositar 150 en la cuenta de Víctor:")
    print(cuenta_victor)

    try:
        cuenta_victor.transferir(cuenta_ana, 500.0)
        print("\nTras transferir 500 de Víctor a Ana:")
    except ValueError as e:
        print("Error en transferencia:", e)

    print(cuenta_victor)
    print(cuenta_ana)


if __name__ == "__main__":
    main()
