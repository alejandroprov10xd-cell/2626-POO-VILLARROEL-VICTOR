# Tarea Semana 11 - Colecciones, ventas y persistencia JSON

## Datos del estudiante

**Nombre:** Victor Villarroel

## Descripcion

Esta entrega continua `restaurante_app` de la Semana 10. Conserva la administracion de productos y usuarios, agrega stock a cada producto e incorpora la entidad `Venta`, que relaciona un usuario registrado con un producto existente. Las tres colecciones se reconstruyen desde JSON al iniciar.

## Estructura

```text
restaurante_app/
|-- datos/
|   |-- productos.json
|   |-- usuarios.json
|   `-- ventas.json
|-- modelos/
|   |-- __init__.py
|   |-- producto.py
|   |-- usuario.py
|   `-- venta.py
|-- servicios/
|   |-- __init__.py
|   |-- archivo_servicio.py
|   `-- restaurante.py
`-- main.py
```

## Mejoras de Semana 11

- `Producto` valida que el stock sea entero y nunca negativo, y su metodo `vender()` descuenta una cantidad valida.
- `Venta` guarda identificacion del usuario, codigo del producto y cantidad adquirida.
- `Restaurante` administra colecciones privadas, valida cada venta y permite filtrarlas por usuario.
- `ArchivoServicio` carga y guarda productos, usuarios y ventas con `json.load()`, `json.dump()`, `with open()` y UTF-8.
- El menu guarda productos despues de registrarlos, actualizarlos o eliminarlos; usuarios despues de registrarlos; y productos junto con ventas despues de vender.

## Reglas de venta

La venta se acepta solamente si existen el usuario y el producto, la cantidad es un entero mayor que cero y hay stock suficiente. Una venta rechazada no modifica la coleccion ni el stock. Al aceptarla se crea un objeto `Venta`, se descuenta el stock y se actualizan `productos.json` y `ventas.json`.

## Excepciones controladas

La persistencia controla `FileNotFoundError`, `json.JSONDecodeError`, `PermissionError`, `KeyError` y los `ValueError` de los modelos. Un archivo inexistente inicia su coleccion vacia; los registros incompletos o invalidos se informan y se omiten.

## Ejecucion

Desde la carpeta `restaurante_app`:

```bash
python main.py
```

No se necesitan librerias externas.

## Comprobacion

1. Registre un usuario y un producto con stock.
2. Venda una cantidad disponible y confirme el nuevo stock al listar productos.
3. Consulte las ventas usando la identificacion del usuario.
4. Revise `datos/ventas.json` y `datos/productos.json`.
5. Salga, ejecute nuevamente y confirme que se recuperaron las tres colecciones.
6. Intente vender cero, una cantidad negativa o mas unidades que el stock: la venta debe rechazarse sin alterar los archivos.
