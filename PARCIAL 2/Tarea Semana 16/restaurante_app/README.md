# restaurante_app - Semana 16

Proyecto grafico desarrollado con Tkinter para la Semana 16 de Programacion
Orientada a Objetos. Esta version continua la aplicacion del restaurante creada
en semanas anteriores y evoluciona la seccion de usuarios para aplicar manejo de
eventos.

## Proposito

La aplicacion conserva el inicio de sesion, la navegacion por pestanas, la
gestion de productos, el registro de ventas y la persistencia en archivos JSON.
La mejora principal esta en la pestana `Usuarios`, disponible para cuentas con
rol `Administrador`.

Desde esa seccion el administrador puede registrar, consultar, actualizar y
eliminar usuarios del restaurante. Cada usuario tiene identificacion, nombre,
usuario, clave y rol.

## Roles

- `Administrador`: puede ingresar a la gestion de usuarios.
- `Empleado`: puede usar la aplicacion, pero no administra usuarios.
- `Cliente`: puede usar la aplicacion, pero no administra usuarios.

La cuenta administrativa autenticada no puede eliminarse desde la propia
interfaz.

## Eventos implementados

```text
Treeview
-> <<TreeviewSelect>>
-> bind()
-> _evento_seleccionar_usuario(event)
-> RestauranteServicio.buscar_usuario()
-> carga del formulario
```

```text
Teclado
-> <Return>
-> bind()
-> _evento_registrar_usuario(event)
-> reutiliza _registrar_usuario()
```

```text
Teclado
-> <Escape>
-> bind()
-> _evento_limpiar_usuario(event)
-> limpia formulario y seleccion
```

```text
Combobox
-> <<ComboboxSelected>>
-> bind()
-> _evento_cambiar_rol(event)
-> actualiza respuesta visual
```

Los botones principales usan `command=`:

- `Registrar`
- `Actualizar`
- `Eliminar`
- `Limpiar`

## Responsabilidades

La interfaz captura eventos, actualiza campos y muestra mensajes. Las reglas de
negocio, validaciones, busquedas y persistencia se mantienen en
`RestauranteServicio`. La lectura y escritura de archivos JSON se centraliza en
`ArchivoServicio`.

## Persistencia

Los datos se guardan en la carpeta `datos/`:

- `productos.json`
- `usuarios.json`
- `ventas.json`

El archivo `usuarios.json` persiste el nuevo atributo `rol`.

## Estructura

```text
restaurante_app/
|-- assets/
|   |-- logo.ppm
|   `-- venta.ppm
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
|   `-- restaurante_servicio.py
|-- ui/
|   |-- __init__.py
|   |-- login_view.py
|   `-- main_view.py
|-- main.py
`-- README.md
```

## Ejecutar

Desde la carpeta `restaurante_app`, ejecute:

```bash
python main.py
```

Credenciales de prueba:

```text
Administrador: admin / 1234
Empleado: empleado / 1234
Cliente: cliente / 1234
```

Tambien se puede ingresar con la identificacion del usuario, por ejemplo
`U01 / 1234`.
