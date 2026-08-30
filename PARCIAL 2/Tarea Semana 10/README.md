# Semana 10 - Persistencia JSON en Restaurante App

## Datos del estudiante

**Nombre:** Victor Villarroel

## Descripcion

Esta entrega evoluciona `restaurante_app` de la Semana 9. El programa administra productos y usuarios de un restaurante mediante un menu de consola. La mejora principal es la persistencia de productos en JSON: los productos registrados, actualizados o eliminados permanecen disponibles despues de cerrar y volver a ejecutar la aplicacion. Los usuarios se conservan solamente en memoria, como solicita la actividad.

## Estructura

```text
restaurante_app/
|-- datos/
|   `-- productos.json
|-- modelos/
|   |-- __init__.py
|   |-- producto.py
|   `-- usuario.py
|-- servicios/
|   |-- __init__.py
|   |-- archivo_servicio.py
|   `-- restaurante.py
`-- main.py
```

## Responsabilidad de los componentes

- `Producto`: valida codigo, nombre, categoria y precio; tambien convierte cada objeto a diccionario.
- `Usuario`: conserva el registro y validacion de usuarios de la semana anterior.
- `Restaurante`: administra las colecciones y las operaciones de registro, busqueda, actualizacion, eliminacion y listado.
- `ArchivoServicio`: centraliza la lectura con `json.load()` y la escritura con `json.dump()`, usando `with open()` y UTF-8.
- `main.py`: carga al iniciar, coordina el menu y guarda despues de cada cambio exitoso en los productos.
- `productos.json`: almacena una lista de diccionarios, pero durante la ejecucion cada registro valido se reconstruye como un objeto `Producto`.

## Flujo de carga y guardado

Al iniciar, `main.py` solicita a `ArchivoServicio` la lectura del JSON. El servicio valida que exista una lista, reconstruye cada registro valido con `Producto(...)` y omite solo los registros defectuosos. Luego entrega los objetos a `Restaurante`.

Al registrar, actualizar o eliminar correctamente, `main.py` obtiene una copia de la coleccion desde `Restaurante` y solicita el guardado. `ArchivoServicio` convierte los objetos a diccionarios y actualiza el JSON con formato legible.

## Excepciones controladas

- `FileNotFoundError`: permite iniciar con una coleccion vacia si el archivo no existe.
- `json.JSONDecodeError`: informa que el contenido no es JSON valido.
- `PermissionError`: informa problemas de permisos durante lectura o escritura.
- `KeyError`: omite registros que no poseen alguna clave requerida.
- `ValueError`: controla productos invalidos y entradas numericas incorrectas.

No se utiliza `except: pass`; los errores esperados muestran mensajes comprensibles.

## Ejecucion

Desde la carpeta `restaurante_app` ejecute:

```bash
python main.py
```

No requiere librerias externas.

## Comprobacion de persistencia

Se probo el siguiente ciclo: iniciar el programa, registrar productos desde el menu, cerrar, volver a iniciar y listarlos. Despues se actualizo y elimino un producto, reiniciando nuevamente para confirmar que `datos/productos.json` conservaba cada cambio. Tambien se verificaron un archivo inexistente, JSON invalido y registros incompletos.
