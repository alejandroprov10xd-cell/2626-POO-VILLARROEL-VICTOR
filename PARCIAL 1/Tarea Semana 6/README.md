# Tarea Semana 6 - Restaurante App

## Datos del estudiante

Nombre: Victor Villarroel

## Descripcion del sistema

Este proyecto representa productos disponibles en un restaurante mediante Programacion Orientada a Objetos. El sistema permite registrar platillos y bebidas, almacenarlos en una clase de servicio y mostrar su informacion de forma organizada en consola.

## Estructura del proyecto

```text
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── platillo.py
│   └── bebida.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
└── main.py
```

- `modelos/producto.py`: contiene la clase padre `Producto`.
- `modelos/platillo.py`: contiene la clase hija `Platillo`.
- `modelos/bebida.py`: contiene la clase hija `Bebida`.
- `servicios/restaurante.py`: contiene la clase `Restaurante`, encargada de administrar la lista de productos.
- `main.py`: es el punto de arranque del programa.

## Herencia aplicada

La clase `Producto` define los atributos comunes `nombre`, `precio` y `disponible`. Las clases `Platillo` y `Bebida` heredan de `Producto` usando `super()` y agregan atributos propios:

- `Platillo`: `tipo_platillo` y `tiempo_preparacion`.
- `Bebida`: `volumen_mililitros` y `tipo_bebida`.

## Encapsulacion

El atributo `__precio` esta encapsulado dentro de la clase `Producto`. Para consultarlo se utiliza el metodo `obtener_precio()` y para modificarlo se utiliza `cambiar_precio()`. Este metodo valida que el precio sea mayor que cero.

## Polimorfismo

El metodo `mostrar_informacion()` se sobrescribe en `Platillo` y `Bebida`. La clase `Restaurante` recorre una lista de productos y ejecuta el mismo metodo en cada objeto, mostrando informacion distinta segun el tipo de producto.

## Ejecucion

Desde la carpeta `restaurante_app`, ejecutar:

```bash
python main.py
```

## Reflexion

Aplicar principios de POO en proyectos Python modulares permite organizar mejor el codigo, reutilizar atributos y metodos mediante herencia, proteger datos importantes con encapsulacion y crear comportamientos flexibles mediante polimorfismo. Esto facilita el mantenimiento y crecimiento del sistema.
