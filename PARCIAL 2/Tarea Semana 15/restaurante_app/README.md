# restaurante_app - Semana 15

Proyecto grafico desarrollado con Tkinter para la Semana 15 de Programacion Orientada a Objetos. Esta version continua la aplicacion del restaurante y agrega el manejo fundamental de eventos mediante una operacion de venta.

## Objetivo

La aplicacion conserva el inicio de sesion, la navegacion por pestanas, la consulta de usuarios y la gestion de productos. La nueva seccion `Ventas` permite seleccionar un usuario y un producto, registrar la venta con un boton asociado a `command=` y mostrar la respuesta en la interfaz.

Flujo aplicado:

```text
Usuario
-> Boton Registrar venta
-> command=
-> callback _registrar_venta
-> RestauranteServicio
-> ventas.json
-> actualizacion del Treeview
```

## Estructura del proyecto

```text
restaurante_app/
├── assets/
│   ├── logo.ppm
│   └── venta.ppm
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── main.py
└── README.md
```

## Funcionalidades

- Inicio de sesion validado desde `RestauranteServicio`.
- Consulta de usuarios registrados en `usuarios.json`.
- Registro, consulta, actualizacion y eliminacion de productos.
- Nueva pestana `Ventas` con seleccion de usuario y producto mediante `ttk.Combobox`.
- Boton `Registrar venta` conectado con `command=self._registrar_venta`.
- Callback que solicita la operacion al servicio y actualiza la tabla de ventas.
- Persistencia de ventas en `datos/ventas.json`.
- Uso de recursos visuales desde la carpeta `assets/`.

## Responsabilidades

La interfaz coordina la interaccion visual, pero no escribe directamente en los archivos JSON. Las validaciones, busquedas y registro de ventas se realizan en `RestauranteServicio`, mientras que `ArchivoServicio` centraliza la lectura y escritura de los archivos.

## Ejecutar la aplicacion

Desde la carpeta `restaurante_app`, ejecute:

```bash
python main.py
```

Credencial inicial:

```text
Usuario: U01
Clave: 1234
```

Despues del ingreso, abra la pestana `Ventas`, seleccione un usuario y un producto, y pulse `Registrar venta`. La venta se mostrara en la tabla y quedara guardada en `datos/ventas.json`.
