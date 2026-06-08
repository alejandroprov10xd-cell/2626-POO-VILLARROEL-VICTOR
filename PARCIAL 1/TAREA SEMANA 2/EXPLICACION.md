# Explicación del código

## Introducción
Este documento explica cada parte del programa entregado en la carpeta `PARCIAL 1/TAREA SEMANA 2`.

## `cuenta_bancaria.py`

- **Descripción general:** contiene la clase `CuentaBancaria` que modela una cuenta bancaria simple con operaciones básicas.

- **`class CuentaBancaria`**: la definición de la clase que agrupa estado (atributos) y comportamiento (métodos).

- **`__init__(self, titular: str, saldo: float = 0.0)`**:
  - Inicializa una nueva cuenta.
  - `titular`: nombre del dueño (se convierte a `str`).
  - `saldo`: saldo inicial (se convierte a `float`).

- **`depositar(self, monto: float) -> None`**:
  - Suma `monto` al saldo.
  - Valida que `monto` sea mayor que 0, si no lanza `ValueError` con mensaje claro.

- **`retirar(self, monto: float) -> None`**:
  - Resta `monto` del saldo.
  - Valida que `monto` sea mayor que 0 y que haya fondos suficientes; en caso contrario lanza `ValueError`.

- **`transferir(self, otra_cuenta: "CuentaBancaria", monto: float) -> None`**:
  - Transfiere dinero usando `retirar` de la cuenta origen y `depositar` en la cuenta destino.
  - Reutiliza la validación de `retirar` y `depositar` para mantener reglas coherentes.

- **`__str__(self) -> str`**:
  - Representación legible de la cuenta, útil para imprimir estado.

## `main.py`

- **Importación:** `from cuenta_bancaria import CuentaBancaria` — importa la clase desde el módulo local.

- **`main()`**:
  - Crea dos instancias de `CuentaBancaria` con saldos iniciales.
  - Imprime el estado inicial de ambas cuentas.
  - Realiza un depósito en una cuenta y vuelve a imprimir para mostrar el cambio.
  - Intenta una transferencia dentro de un bloque `try/except` para capturar posibles `ValueError` (por ejemplo, fondos insuficientes) y mostrar un mensaje de error en caso necesario.

- **Guardia `if __name__ == "__main__":`**:
  - Permite ejecutar `main()` cuando el script se corre directamente, pero evita ejecutar el demo si el módulo se importa desde otro script.

## Comportamiento ante errores

- Si se intenta depositar o retirar un monto no positivo, se lanza `ValueError`.
- Si se intenta retirar más de lo disponible, se lanza `ValueError` con el mensaje "Fondos insuficientes".

## Cómo ejecutar

Abrir una terminal en la raíz del proyecto y ejecutar:

```bash
python "PARCIAL 1/TAREA SEMANA 2/main.py"
```

Esto imprimirá el estado inicial, el estado tras el depósito y el resultado de la transferencia.

## Posibles mejoras (sugerencias)

- Añadir validación de tipos más estricta o uso de `dataclasses` para simplificar la clase.
- Registrar operaciones (historial de transacciones) dentro de la clase.
- Añadir tests unitarios (por ejemplo, con `unittest` o `pytest`).
- Implementar límites de sobregiro o comisiones.
