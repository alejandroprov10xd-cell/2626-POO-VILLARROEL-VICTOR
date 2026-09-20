# restaurante_app - Semana 14

Proyecto grafico desarrollado con Tkinter para la Semana 14 de Programacion Orientada a Objetos. El objetivo de esta version es aplicar componentes y contenedores para mejorar la organizacion de la interfaz, manteniendo la arquitectura modular y la persistencia en archivos JSON.

## Estructura del proyecto

```text
restaurante_app/
├── datos/
│   ├── productos.json
│   └── usuarios.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
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

## Componentes y contenedores utilizados

La aplicacion conserva una ventana principal controlada desde `main.py`. La pantalla de acceso se mantiene en `LoginView` y el panel principal se organiza en `MainView`.

En la interfaz se utilizan componentes de `tkinter` y `ttk`, como `Frame`, `LabelFrame`, `Label`, `Entry`, `Button`, `Notebook`, `Treeview` y `Scrollbar`. Los contenedores separan el encabezado, las pestañas, el formulario de productos, los botones de accion y las tablas de consulta.

## Mejoras realizadas

La seccion de productos fue evolucionada para mostrar un formulario organizado junto a una tabla de datos. Desde la interfaz se pueden realizar operaciones sencillas sin escribir directamente sobre los archivos JSON desde la vista.

Operaciones implementadas sobre productos:

- Registrar un producto.
- Cargar o consultar un producto por codigo.
- Actualizar nombre, categoria, precio y stock.
- Eliminar un producto.
- Refrescar automaticamente la tabla despues de cada operacion.

La seccion de usuarios se mantiene disponible para consultar los usuarios registrados en `usuarios.json`.

## Persistencia

Los datos se guardan en archivos JSON dentro de la carpeta `datos`. La lectura y escritura se realiza mediante `ArchivoServicio`, mientras que las reglas de negocio y validaciones se mantienen en `RestauranteServicio`.

La vista coordina la interaccion con el usuario, pero no manipula directamente los archivos JSON.

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

Despues del ingreso, abra la pestaña `Productos` para registrar, consultar, actualizar o eliminar productos. Los cambios se conservan en `datos/productos.json`.
