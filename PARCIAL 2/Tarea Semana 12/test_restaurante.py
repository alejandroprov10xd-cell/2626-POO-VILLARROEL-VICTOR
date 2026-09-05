"""Pruebas de regresion sin modificar los JSON de la entrega."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

APP = Path(__file__).resolve().parent / "restaurante_app"
sys.path.insert(0, str(APP))
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.restaurante import Restaurante
from servicios.archivo_servicio import ArchivoServicio


class PruebasRestaurante(unittest.TestCase):
    def setUp(self):
        self.r = Restaurante("Prueba")
        self.p = Producto("P01", "Sopa", "Platos", 3.5, 10)
        self.u = Usuario("U01", "Usuario de prueba", "prueba@example.com")
        self.r.cargar_datos([self.p], [self.u], [])

    def test_busquedas_registro_y_duplicados(self):
        self.assertIs(self.r.buscar_producto(" p01 "), self.p)
        self.assertIs(self.r.buscar_usuario(" u01 "), self.u)
        self.assertFalse(self.r.registrar_producto(Producto("p01", "Otro", "Platos", 2, 1)))
        self.assertFalse(self.r.registrar_usuario(Usuario("u01", "Otro", "otro@example.com")))
        self.assertTrue(self.r.registrar_producto(Producto("P02", "Jugo", "Bebidas", 1, 4)))
        self.assertTrue(self.r.registrar_usuario(Usuario("U02", "Otro", "otro@example.com")))
        self.assertIsNotNone(self.r.buscar_producto("P02"))
        self.assertIsNotNone(self.r.buscar_usuario("U02"))
        self.assertIsNone(self.r.buscar_producto("ausente"))
        self.assertIsNone(self.r.buscar_usuario("ausente"))

    def test_actualizar_eliminar_y_registrar_de_nuevo(self):
        self.assertTrue(self.r.actualizar_producto("p01", "Jugo", "Bebidas", 2, 8))
        self.assertIs(self.r.buscar_producto("P01"), self.r.listar_productos()[0])
        self.assertEqual(self.r.buscar_producto("P01").stock, 8)
        self.assertEqual(self.r.obtener_categorias(), {"Bebidas"})
        self.assertTrue(self.r.vender_producto("P01", "U01", 2))
        self.assertTrue(self.r.eliminar_producto(" p01 "))
        self.assertTrue(self.r.eliminar_usuario(" u01 "))
        self.assertIsNone(self.r.buscar_producto("P01"))
        self.assertIsNone(self.r.buscar_usuario("U01"))
        self.assertEqual(self.r.listar_productos(), [])
        self.assertEqual(self.r.listar_usuarios(), [])
        self.assertEqual(len(self.r.consultar_ventas_usuario("U01")), 1)
        self.assertTrue(self.r.registrar_producto(self.p))
        self.assertTrue(self.r.registrar_usuario(self.u))

    def test_ventas_stock_y_copias(self):
        for cantidad in (0, -1, 11, True, 1.5):
            self.assertFalse(self.r.vender_producto("P01", "U01", cantidad))
        self.assertFalse(self.r.vender_producto("X", "U01", 1))
        self.assertFalse(self.r.vender_producto("P01", "X", 1))
        self.assertEqual(self.p.stock, 10)
        self.assertEqual(self.r.listar_ventas(), [])
        self.assertTrue(self.r.vender_producto(" p01 ", " u01 ", 3))
        self.assertEqual(self.p.stock, 7)
        ventas = self.r.consultar_ventas_usuario("U01")
        self.assertIs(ventas[0], self.r.listar_ventas()[0])
        ventas.clear()
        self.assertEqual(len(self.r.consultar_ventas_usuario("U01")), 1)
        self.assertEqual(self.r.consultar_ventas_usuario("X"), [])

    def test_recarga_reemplaza_indices_y_rechaza_duplicados(self):
        with self.assertRaises(ValueError):
            self.r.cargar_datos([self.p, self.p], [self.u], [])
        self.assertIs(self.r.buscar_producto("P01"), self.p)
        with self.assertRaises(ValueError):
            self.r.cargar_datos([self.p], [self.u, self.u], [])
        self.r.cargar_datos([], [], [Venta("historico", "P01", 1)])
        self.assertIsNone(self.r.buscar_producto("P01"))
        self.assertIsNone(self.r.buscar_usuario("U01"))
        self.assertEqual(len(self.r.consultar_ventas_usuario("HISTORICO")), 1)
        self.r.cargar_datos([], [], [])
        self.assertEqual(self.r.consultar_ventas_usuario("historico"), [])

    def test_persistencia_reconstruye_objetos_e_indices(self):
        with tempfile.TemporaryDirectory() as carpeta:
            archivos = ArchivoServicio(Path(carpeta))
            self.r.vender_producto("P01", "U01", 2)
            self.assertTrue(archivos.guardar_productos(self.r.listar_productos()))
            self.assertTrue(archivos.guardar_usuarios(self.r.listar_usuarios()))
            self.assertTrue(archivos.guardar_ventas(self.r.listar_ventas()))
            nuevo = Restaurante("Reinicio")
            nuevo.cargar_datos(archivos.cargar_productos(), archivos.cargar_usuarios(), archivos.cargar_ventas())
            self.assertEqual(nuevo.buscar_producto("p01").stock, 8)
            self.assertEqual(nuevo.buscar_usuario("u01").nombre, self.u.nombre)
            self.assertEqual(nuevo.consultar_ventas_usuario("u01")[0].cantidad, 2)
            self.assertTrue(nuevo.vender_producto("P01", "U01", 1))
            self.assertEqual(len(nuevo.consultar_ventas_usuario("U01")), 2)

    def test_main_en_dos_ejecuciones(self):
        with tempfile.TemporaryDirectory() as carpeta:
            copia = Path(carpeta) / "restaurante_app"
            shutil.copytree(APP, copia, ignore=shutil.ignore_patterns("__pycache__"))
            entrada = "6\nTEST12\nUsuario Prueba\nprueba@example.com\n1\nTEST12\nSopa\nPlatos\n3.5\n10\n2\ntest12\n9\nTEST12\nTEST12\n3\n10\nTEST12\n11\n"
            primera = subprocess.run([sys.executable, "-B", str(copia / "main.py")], input=entrada, text=True, capture_output=True, timeout=20)
            self.assertEqual(primera.returncode, 0, primera.stderr)
            self.assertIn("Venta registrada; stock y ventas fueron guardados.", primera.stdout)
            segunda = subprocess.run([sys.executable, "-B", str(copia / "main.py")], input="2\nTEST12\n7\n10\nTEST12\n11\n", text=True, capture_output=True, timeout=20)
            self.assertEqual(segunda.returncode, 0, segunda.stderr)
            self.assertIn("Stock: 7", segunda.stdout)
            self.assertIn("Usuario Prueba", segunda.stdout)
            self.assertIn("Cantidad: 3", segunda.stdout)
            productos = json.loads((copia / "datos/productos.json").read_text(encoding="utf-8"))
            self.assertEqual(next(p for p in productos if p["codigo"] == "TEST12")["stock"], 7)


if __name__ == "__main__":
    unittest.main()
