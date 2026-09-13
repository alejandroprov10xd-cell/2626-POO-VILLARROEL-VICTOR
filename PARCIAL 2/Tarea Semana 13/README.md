# Tarea Semana 13 - Interfaces graficas con Tkinter

## Datos del estudiante

**Nombre:** Victor Villarroel

## Proposito

Esta actividad inicia la transicion de `restaurante_app` desde una aplicacion de consola hacia una aplicacion con interfaz grafica de usuario. La base se adapta al criterio del proyecto docente Biblioteca App: modelos para representar entidades, servicios para cargar y organizar la informacion, una carpeta `ui/` para las vistas y `main.py` como punto de entrada.

En esta semana no se trasladan todas las funciones de consola. La aplicacion trabaja solo con productos y usuarios, permite un acceso simulado y muestra la informacion cargada desde archivos JSON. La seccion de ventas queda marcada como pendiente para continuar en las siguientes semanas.

## Estructura

```text
README.md
restaurante_app/
|-- datos/
|   |-- productos.json
|   `-- usuarios.json
|-- modelos/
|   |-- __init__.py
|   |-- producto.py
|   `-- usuario.py
|-- servicios/
|   |-- __init__.py
|   |-- archivo_servicio.py
|   `-- restaurante_servicio.py
|-- ui/
|   |-- __init__.py
|   |-- login_view.py
|   `-- main_view.py
`-- main.py
```

## Componentes implementados

- `Producto`: representa los productos del restaurante.
- `Usuario`: representa los usuarios usados para el acceso simulado.
- `ArchivoServicio`: lee `productos.json` y `usuarios.json`.
- `RestauranteServicio`: convierte los datos JSON en objetos, valida credenciales, lista usuarios, lista productos y consulta cantidades.
- `LoginView`: muestra usuario, clave, mensajes de error y boton de ingreso.
- `MainView`: muestra productos, usuarios y una pestana de ventas pendiente.
- `main.py`: crea una unica ventana de Tkinter, prepara los servicios y cambia entre login y panel principal.

## Flujo de la aplicacion

```text
Inicio
-> main.py prepara Tkinter y servicios
-> LoginView
-> Validacion de usuario y clave
-> MainView
-> Productos | Usuarios | Ventas pendiente
-> Cerrar sesion
-> LoginView
```

## Credenciales de prueba

Los usuarios se cargan desde `restaurante_app/datos/usuarios.json`. Como los datos heredados de la semana anterior no tenian clave, la aplicacion asigna la clave por defecto `1234`.

Ejemplo:

```text
Usuario: U01
Clave: 1234
```

Si agrega un campo `clave` a un usuario dentro del JSON, esa clave sera usada por el servicio.

## Ejecucion

Desde esta carpeta:

```bash
python restaurante_app/main.py
```

Tambien puede ejecutarse `python main.py` dentro de `restaurante_app`.

## Comprobacion realizada

- La aplicacion inicia desde `main.py`.
- Se muestra primero la pantalla de acceso.
- Los campos de usuario y clave aceptan datos.
- Los campos vacios o credenciales incorrectas muestran un mensaje visual.
- Con credenciales validas se abre el panel principal.
- La pestana Productos muestra datos cargados desde `productos.json`.
- La pestana Usuarios muestra datos cargados desde `usuarios.json`.
- Las vistas solicitan informacion a `RestauranteServicio`.
- Cerrar sesion vuelve al login en la misma ventana.
