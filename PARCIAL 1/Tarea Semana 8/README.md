# Tarea Semana 8 - Aplicacion de principios SOLID en restaurante_app

## Datos del estudiante

Nombre completo: Victor Villarroel

## Descripcion del sistema

Este proyecto implementa una aplicacion de consola para la gestion basica de un restaurante. El sistema permite registrar productos generales, bebidas y clientes mediante un menu interactivo. La solucion esta organizada en modelos, servicios y un archivo principal para evidenciar una distribucion clara de responsabilidades.

## Estructura del proyecto

```text
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── bebida.py
│   └── cliente.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
└── main.py
```

## Responsabilidad de cada clase

- `Producto`: representa los datos comunes de un producto del restaurante, como codigo, nombre, categoria y precio.
- `Bebida`: representa una especializacion de `Producto` e incorpora informacion propia, como tamano y tipo de envase.
- `Cliente`: representa los datos de un cliente registrado, como identificacion, nombre y correo.
- `Restaurante`: administra las colecciones de productos y clientes, valida duplicados y expone metodos de registro y listado.
- `main.py`: coordina la interaccion por consola, solicita datos al usuario, crea objetos y llama al servicio.

## Relacion entre Producto y Bebida

`Bebida` hereda de `Producto` porque una bebida es un tipo de producto del restaurante. Por esa razon, puede almacenarse en la misma lista de productos y utilizar el metodo comun `mostrar_informacion()`. La clase `Bebida` sobrescribe ese metodo para agregar sus datos especificos sin cambiar la logica general del servicio.

## Principios SOLID aplicados

- **SRP - Responsabilidad unica**: cada clase cumple una funcion concreta. Los modelos representan datos, el servicio administra colecciones y `main.py` maneja la entrada y salida por consola.
- **OCP - Abierto/cerrado**: el sistema se amplio con la clase `Bebida` sin reescribir la logica de registro y listado de productos en `Restaurante`.
- **LSP - Sustitucion de Liskov**: una `Bebida` puede usarse como un `Producto`, ya que comparte el comportamiento esperado mediante `mostrar_informacion()`.

## Instrucciones de ejecucion

Desde la carpeta `PARCIAL 1/Tarea Semana 8/restaurante_app`, ejecutar:

```bash
python main.py
```

## Reflexion

Disenar proyectos mantenibles permite que el sistema pueda crecer sin mezclar responsabilidades ni duplicar logica. Al separar modelos, servicios e interaccion por consola, el codigo resulta mas claro, facil de probar y mas sencillo de modificar cuando aparecen nuevos requerimientos, como agregar una nueva clase hija de `Producto`.
