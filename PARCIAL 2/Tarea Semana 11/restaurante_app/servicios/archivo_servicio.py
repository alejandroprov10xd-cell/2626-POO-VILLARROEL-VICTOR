import json
from pathlib import Path
from typing import Any, Callable, TypeVar

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


T = TypeVar("T")


class ArchivoServicio:
    """Centraliza la persistencia JSON de las colecciones del sistema."""

    def __init__(self, directorio_datos: Path) -> None:
        self.directorio_datos = directorio_datos
        self.ruta_productos = directorio_datos / "productos.json"
        self.ruta_usuarios = directorio_datos / "usuarios.json"
        self.ruta_ventas = directorio_datos / "ventas.json"

    def cargar_productos(self) -> list[Producto]:
        return self._cargar(
            self.ruta_productos,
            "productos",
            lambda r: Producto(r["codigo"], r["nombre"], r["categoria"], r["precio"], r["stock"]),
            lambda producto: producto.codigo.lower(),
        )

    def cargar_usuarios(self) -> list[Usuario]:
        return self._cargar(
            self.ruta_usuarios,
            "usuarios",
            lambda r: Usuario(r["identificacion"], r["nombre"], r["correo"]),
            lambda usuario: usuario.identificacion.lower(),
        )

    def cargar_ventas(self) -> list[Venta]:
        return self._cargar(
            self.ruta_ventas,
            "ventas",
            lambda r: Venta(r["usuario_id"], r["producto_codigo"], r["cantidad"]),
        )

    def guardar_productos(self, productos: list[Producto]) -> bool:
        return self._guardar(self.ruta_productos, productos, "productos")

    def guardar_usuarios(self, usuarios: list[Usuario]) -> bool:
        return self._guardar(self.ruta_usuarios, usuarios, "usuarios")

    def guardar_ventas(self, ventas: list[Venta]) -> bool:
        return self._guardar(self.ruta_ventas, ventas, "ventas")

    def _cargar(
        self,
        ruta: Path,
        nombre: str,
        constructor: Callable[[dict[str, Any]], T],
        clave_unica: Callable[[T], str] | None = None,
    ) -> list[T]:
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                registros = json.load(archivo)
        except FileNotFoundError:
            print(f"No existe {ruta.name}; se iniciara con {nombre} vacios.")
            return []
        except json.JSONDecodeError:
            print(f"{ruta.name} no contiene un JSON valido.")
            return []
        except PermissionError:
            print(f"No hay permisos para leer {ruta.name}.")
            return []

        if not isinstance(registros, list):
            print(f"{ruta.name} debe contener una lista.")
            return []

        objetos: list[T] = []
        claves: set[str] = set()
        for numero, registro in enumerate(registros, start=1):
            try:
                if not isinstance(registro, dict):
                    raise ValueError("el registro no es un objeto JSON")
                objeto = constructor(registro)
                if clave_unica is not None:
                    clave = clave_unica(objeto)
                    if clave in claves:
                        raise ValueError("el identificador esta duplicado")
                    claves.add(clave)
                objetos.append(objeto)
            except KeyError as error:
                print(f"Registro {numero} de {ruta.name} omitido: falta {error}.")
            except ValueError as error:
                print(f"Registro {numero} de {ruta.name} omitido: {error}.")
        return objetos

    def _guardar(self, ruta: Path, objetos: list[Any], nombre: str) -> bool:
        registros = [objeto.convertir_a_diccionario() for objeto in objetos]
        try:
            self.directorio_datos.mkdir(parents=True, exist_ok=True)
            with open(ruta, "w", encoding="utf-8") as archivo:
                json.dump(registros, archivo, ensure_ascii=False, indent=4)
        except PermissionError:
            print(f"No hay permisos para guardar {nombre} en {ruta.name}.")
            return False
        return True
