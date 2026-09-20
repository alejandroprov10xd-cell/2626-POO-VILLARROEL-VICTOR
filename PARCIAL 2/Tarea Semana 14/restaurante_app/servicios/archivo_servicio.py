import json
from pathlib import Path
from typing import Any


class ArchivoServicio:
    """Lee y guarda los archivos JSON usados como datos locales de la aplicacion."""

    def __init__(self, directorio_datos: Path) -> None:
        self.directorio_datos = directorio_datos

    def cargar_productos(self) -> list[dict[str, Any]]:
        return self._cargar_json("productos.json")

    def cargar_usuarios(self) -> list[dict[str, Any]]:
        return self._cargar_json("usuarios.json")

    def guardar_productos(self, productos: list[dict[str, Any]]) -> None:
        self._guardar_json("productos.json", productos)

    def _cargar_json(self, nombre_archivo: str) -> list[dict[str, Any]]:
        ruta = self.directorio_datos / nombre_archivo
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

        if not isinstance(datos, list):
            return []
        return [registro for registro in datos if isinstance(registro, dict)]

    def _guardar_json(self, nombre_archivo: str, datos: list[dict[str, Any]]) -> None:
        self.directorio_datos.mkdir(parents=True, exist_ok=True)
        ruta = self.directorio_datos / nombre_archivo
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
