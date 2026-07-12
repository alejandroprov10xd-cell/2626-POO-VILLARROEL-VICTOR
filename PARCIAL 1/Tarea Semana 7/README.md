# Tarea Semana 7 - Sistema de Restaurante

## Datos del estudiante

Nombre: Victor Villarroel

## Descripcion del sistema

Este proyecto implementa una aplicacion de consola para la gestion basica de un restaurante. El sistema permite registrar, listar y buscar productos y clientes mediante un menu interactivo. Los datos se ingresan por teclado y se transforman en objetos de Python utilizando Programacion Orientada a Objetos.

## Estructura del proyecto

```text
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── cliente.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
└── main.py
```

- `modelos/producto.py`: contiene la clase `Producto`.
- `modelos/cliente.py`: contiene la clase `Cliente`.
- `servicios/restaurante.py`: contiene la clase `Restaurante`, que administra las listas de productos y clientes.
- `main.py`: contiene el menu interactivo y es el punto de inicio del programa.

## Constructor en Producto

La clase `Producto` utiliza el constructor tradicional `__init__()` para recibir el nombre, la categoria, el precio y la disponibilidad. Estos datos ingresados por el usuario permiten crear objetos reales del sistema.

## Uso de @property y @setter

En la clase `Producto` se aplican `@property` y `@setter` para controlar el acceso y la modificacion de los atributos. Los setters validan que el nombre y la categoria no esten vacios, y que el precio sea mayor que cero.

## Uso de @dataclass en Cliente

La clase `Cliente` utiliza el decorador `@dataclass` para definir de forma sencilla los atributos `id_cliente`, `nombre` y `correo`. Esto reduce codigo repetitivo y mantiene clara la estructura de datos del cliente.

## Menu interactivo

El archivo `main.py` presenta un menu con las opciones para registrar, listar y buscar productos y clientes. El programa se mantiene en ejecucion hasta que el usuario selecciona la opcion de salir.

## Reflexion

Crear objetos a partir de datos ingresados por el usuario es importante porque permite que el programa trabaje con informacion dinamica. De esta manera, la aplicacion no depende de datos quemados en el codigo y puede representar situaciones reales mediante objetos almacenados y consultados en el sistema.

## Ejecucion

Desde la carpeta `restaurante_app`, ejecutar:

```bash
python main.py
```
