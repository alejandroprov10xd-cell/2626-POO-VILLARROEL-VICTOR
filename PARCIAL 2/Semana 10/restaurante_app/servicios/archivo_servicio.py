import json
from pathlib import Path

from modelos.producto import Producto


class ArchivoServicio:
    """Carga y guarda productos en un archivo JSON."""

    def __init__(self, ruta_archivo: Path) -> None:
        self.ruta_archivo = ruta_archivo

    def cargar_productos(self) -> list[Producto]:
        try:
            with open(self.ruta_archivo, "r", encoding="utf-8") as archivo:
                registros = json.load(archivo)
        except FileNotFoundError:
            print("No existe un archivo previo. Se iniciara con productos vacios.")
            return []
        except json.JSONDecodeError:
            print("El archivo de productos no contiene un JSON valido.")
            return []
        except PermissionError:
            print("No hay permisos para leer el archivo de productos.")
            return []

        if not isinstance(registros, list):
            print("El JSON debe contener una lista de productos.")
            return []

        productos: list[Producto] = []
        codigos_cargados: set[str] = set()
        for numero, registro in enumerate(registros, start=1):
            try:
                if not isinstance(registro, dict):
                    raise ValueError("el registro no es un objeto JSON")
                producto = Producto(
                    codigo=registro["codigo"],
                    nombre=registro["nombre"],
                    categoria=registro["categoria"],
                    precio=registro["precio"],
                )
                codigo_normalizado = producto.codigo.lower()
                if codigo_normalizado in codigos_cargados:
                    raise ValueError("el codigo esta duplicado")
                productos.append(producto)
                codigos_cargados.add(codigo_normalizado)
            except KeyError as error:
                print(f"Registro {numero} omitido: falta la clave {error}.")
            except ValueError as error:
                print(f"Registro {numero} omitido: {error}.")

        return productos

    def guardar_productos(self, productos: list[Producto]) -> bool:
        registros = [producto.convertir_a_diccionario() for producto in productos]
        try:
            self.ruta_archivo.parent.mkdir(parents=True, exist_ok=True)
            with open(self.ruta_archivo, "w", encoding="utf-8") as archivo:
                json.dump(registros, archivo, ensure_ascii=False, indent=4)
        except PermissionError:
            print("No hay permisos para guardar el archivo de productos.")
            return False
        return True
