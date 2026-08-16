# Semana 9 - Sistema de Restaurante

## Datos del estudiante

Nombre: Victor Villarroel

## Descripcion del sistema

Este proyecto continua la evolucion de `restaurante_app` desarrollado en semanas anteriores. El sistema administra productos y usuarios de un restaurante desde consola, manteniendo separadas las entidades, el servicio y el archivo principal.

La mejora de esta semana es el uso funcional de estructuras de datos de Python para organizar informacion del sistema, con especial atencion al uso de diccionarios para representar datos en formato clave-valor.

## Estructura del proyecto

```text
restaurante_app/
+-- modelos/
|   +-- __init__.py
|   +-- producto.py
|   +-- usuario.py
+-- servicios/
|   +-- __init__.py
|   +-- restaurante.py
+-- main.py
```

## Responsabilidad de los componentes

- `modelos/producto.py`: contiene la clase `Producto`, con codigo, nombre, categoria y precio.
- `modelos/usuario.py`: contiene la clase `Usuario`, con identificacion, nombre y correo.
- `servicios/restaurante.py`: contiene la clase `Restaurante`, encargada de registrar, buscar, actualizar, eliminar y listar informacion.
- `main.py`: contiene el menu interactivo, solicita datos por consola y llama a los metodos del servicio.

## Uso de estructuras de datos

- `list`: se usa en `Restaurante` para almacenar colecciones dinamicas de objetos `Producto` y `Usuario`.
- `tuple`: se usa en `main.py` para definir las opciones estables del menu principal.
- `dict`: se usa para guardar datos en modo clave-valor, convertir productos y usuarios a diccionarios, y asociar opciones del menu con funciones.
- `set`: se usa en `Restaurante.obtener_categorias()` para obtener categorias unicas sin duplicados.

## Funcionalidades

- Registrar productos.
- Buscar productos por codigo.
- Actualizar productos.
- Eliminar productos.
- Listar productos.
- Registrar usuarios.
- Listar usuarios.
- Mostrar categorias unicas.
- Evitar codigos de productos duplicados.
- Evitar identificaciones de usuarios duplicadas.

## Ejecucion

Desde la carpeta `PARCIAL 2/Semana 9/restaurante_app`, ejecutar:

```bash
python main.py
```

## Reflexion

Seleccionar una estructura de datos adecuada ayuda a resolver cada necesidad del programa de forma ordenada. Las listas permiten manejar colecciones que crecen durante la ejecucion, los diccionarios organizan informacion mediante claves descriptivas, las tuplas conservan datos estables y los conjuntos eliminan duplicados. Usarlas correctamente mejora la claridad del codigo y facilita el mantenimiento del sistema.
