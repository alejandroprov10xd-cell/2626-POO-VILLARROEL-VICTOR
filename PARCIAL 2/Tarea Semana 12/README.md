# Tarea Semana 12 - Rendimiento mediante colecciones

## Datos del estudiante

**Nombre:** Victor Villarroel

## Descripcion y continuidad

Esta entrega continua el restaurante_app funcional de la Semana 11. La Semana 9 incorporo colecciones para productos y usuarios; la Semana 10 agrego persistencia de productos; la Semana 11 incorporo ventas, stock y JSON para las tres entidades. La Semana 12 mejora las busquedas dentro de Restaurante y conserva los modelos, el menu y la persistencia anteriores.

## Estructura

```text
README.md
test_restaurante.py
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
|-- README.md
`-- main.py
```

## Mejoras implementadas

| Operacion | Semana 11 | Semana 12 |
|---|---|---|
| Buscar producto por codigo | Recorrido O(P) | dict `_productos_por_codigo`: O(1) promedio |
| Buscar usuario por identificacion | Recorrido O(U) | dict `_usuarios_por_id`: O(1) promedio |
| Validar duplicados y existencia al vender | Busquedas en listas | Reutiliza los dos indices anteriores |
| Consultar ventas de un usuario | Filtrado O(V) | dict `_ventas_por_usuario`: O(1) promedio para localizar el grupo y O(k) para copiar sus k ventas |

P, U y V representan las cantidades totales de productos, usuarios y ventas. Los diccionarios usan claves sin espacios externos y en minusculas, conservando la busqueda sin distinguir mayusculas.

Las listas `_productos`, `_usuarios` y `_ventas` siguen siendo las colecciones principales de objetos para almacenar, listar y persistir. Los indices contienen referencias a esos mismos objetos, no modelos convertidos a diccionarios. Se mantiene el set de categorias unicas y el set temporal que evita identificadores repetidos al cargar JSON. No se agregan conjuntos redundantes para claves ya presentes en los indices.

## Sincronizacion

- Al iniciar, ArchivoServicio reconstruye objetos desde JSON y Restaurante.cargar_datos reconstruye todos los indices en O(P + U + V). Repetir la carga reemplaza el estado anterior; no acumula referencias antiguas. El servicio rechaza claves duplicadas antes de reemplazar su estado.
- Registrar un producto o usuario actualiza su lista e indice.
- Actualizar nombre, categoria, precio o stock modifica el mismo producto referenciado en lista e indice. El servicio no cambia codigos ni identificaciones; los objetos recuperados deben modificarse mediante las operaciones del servicio.
- Eliminar productos o usuarios retira sus referencias de la lista y del indice. Se conservan las ventas historicas y su consulta por identificacion, como en la Semana 11.
- Una venta valida descuenta stock y agrega el mismo objeto Venta a la lista general y al grupo del usuario. Las ventas rechazadas no alteran el estado.
- Consultar ventas devuelve una copia de la lista del grupo para que quitar elementos del resultado no altere el indice.

Los indices solo existen en memoria: los tres JSON conservan su formato anterior. Eliminar elementos de las listas sigue siendo O(n); listar y guardar siguen recorriendo las colecciones. Los indices requieren memoria adicional O(P + U + V). No se afirma que toda la aplicacion sea O(1).

## Ejecucion

Requiere Python 3.10 o posterior, sin dependencias externas. Desde esta carpeta:

```bash
python restaurante_app/main.py
```

Tambien puede ejecutarse `python main.py` dentro de restaurante_app. Las rutas de datos se resuelven respecto a main.py. Se conserva el producto P01 de la Semana 11 y los archivos de usuarios y ventas inicialmente vacios.

## Pruebas realizadas

Desde esta carpeta:

```bash
python -B -m unittest discover -s . -p "test_*.py" -v
```

Se ejecutaron seis pruebas satisfactorias con Python 3.14.5:

1. Busqueda de producto y usuario, claves normalizadas, registros y rechazo de duplicados.
2. Actualizacion de producto, categorias, eliminacion, nuevo registro e historial conservado.
3. Venta valida, descuento de stock, rechazo de cantidades invalidas o referencias inexistentes y copia independiente de resultados.
4. Recarga que reemplaza indices anteriores y rechazo de claves duplicadas.
5. Guardado y recuperacion de los tres JSON en un servicio nuevo, seguido de otra venta.
6. Dos ejecuciones de main.py en procesos separados: registrar usuario y producto, buscar, vender tres unidades de diez, consultar, salir y volver a comprobar usuario, venta y stock de siete.

Las pruebas utilizan carpetas temporales y no modifican los JSON entregados. La busqueda directa de usuario se comprueba mediante Restaurante.buscar_usuario, ya existente en la Semana 11.

Para comprobar manualmente: registre un usuario con la opcion 6, busque P01 con la opcion 2, venda con la opcion 9, consulte con la opcion 10 y revise el stock con la opcion 5. Salga con la opcion 11 y ejecute nuevamente para confirmar la recuperacion.
