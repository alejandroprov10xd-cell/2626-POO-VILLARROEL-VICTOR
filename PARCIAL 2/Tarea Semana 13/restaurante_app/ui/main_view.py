import tkinter as tk
from tkinter import ttk

from servicios.restaurante_servicio import RestauranteServicio


class MainView(ttk.Frame):
    """Panel principal para consultar productos y usuarios cargados."""

    def __init__(
        self,
        master: tk.Tk,
        restaurante_servicio: RestauranteServicio,
        on_cerrar_sesion,
    ) -> None:
        super().__init__(master, padding=18)
        self.restaurante_servicio = restaurante_servicio
        self.on_cerrar_sesion = on_cerrar_sesion
        self._crear_componentes()

    def _crear_componentes(self) -> None:
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        encabezado = ttk.Frame(self)
        encabezado.grid(row=0, column=0, sticky="ew", pady=(0, 12))
        encabezado.columnconfigure(0, weight=1)

        ttk.Label(
            encabezado,
            text="Panel del restaurante",
            font=("Segoe UI", 18, "bold"),
        ).grid(row=0, column=0, sticky="w")
        ttk.Button(
            encabezado, text="Cerrar sesion", command=self.on_cerrar_sesion
        ).grid(row=0, column=1, sticky="e")

        self.notebook = ttk.Notebook(self)
        self.notebook.grid(row=1, column=0, sticky="nsew")

        self._crear_tab_productos()
        self._crear_tab_usuarios()
        self._crear_tab_ventas()

    def _crear_tab_productos(self) -> None:
        tab = ttk.Frame(self.notebook, padding=12)
        tab.columnconfigure(0, weight=1)
        tab.rowconfigure(1, weight=1)
        self.notebook.add(tab, text="Productos")

        ttk.Label(
            tab,
            text=f"Productos registrados: {self.restaurante_servicio.contar_productos()}",
            font=("Segoe UI", 11, "bold"),
        ).grid(row=0, column=0, sticky="w", pady=(0, 8))

        columnas = ("codigo", "nombre", "categoria", "precio", "cantidad")
        tabla = ttk.Treeview(tab, columns=columnas, show="headings", height=12)
        tabla.grid(row=1, column=0, sticky="nsew")
        tabla.heading("codigo", text="Codigo")
        tabla.heading("nombre", text="Producto")
        tabla.heading("categoria", text="Categoria")
        tabla.heading("precio", text="Precio")
        tabla.heading("cantidad", text="Cantidad")
        tabla.column("codigo", width=90, anchor="center")
        tabla.column("nombre", width=180)
        tabla.column("categoria", width=130)
        tabla.column("precio", width=90, anchor="e")
        tabla.column("cantidad", width=90, anchor="center")

        for producto in self.restaurante_servicio.listar_productos():
            tabla.insert(
                "",
                "end",
                values=(
                    producto.codigo,
                    producto.nombre,
                    producto.categoria,
                    f"${producto.precio:.2f}",
                    producto.cantidad,
                ),
            )

    def _crear_tab_usuarios(self) -> None:
        tab = ttk.Frame(self.notebook, padding=12)
        tab.columnconfigure(0, weight=1)
        tab.rowconfigure(1, weight=1)
        self.notebook.add(tab, text="Usuarios")

        ttk.Label(
            tab,
            text=f"Usuarios registrados: {self.restaurante_servicio.contar_usuarios()}",
            font=("Segoe UI", 11, "bold"),
        ).grid(row=0, column=0, sticky="w", pady=(0, 8))

        columnas = ("identificacion", "nombre", "correo")
        tabla = ttk.Treeview(tab, columns=columnas, show="headings", height=12)
        tabla.grid(row=1, column=0, sticky="nsew")
        tabla.heading("identificacion", text="Identificacion")
        tabla.heading("nombre", text="Usuario")
        tabla.heading("correo", text="Correo")
        tabla.column("identificacion", width=130, anchor="center")
        tabla.column("nombre", width=180)
        tabla.column("correo", width=220)

        for usuario in self.restaurante_servicio.listar_usuarios():
            tabla.insert(
                "",
                "end",
                values=(usuario.identificacion, usuario.nombre, usuario.correo),
            )

    def _crear_tab_ventas(self) -> None:
        tab = ttk.Frame(self.notebook, padding=20)
        self.notebook.add(tab, text="Ventas")
        ttk.Label(
            tab,
            text="Ventas mediante interfaz grafica: pendiente para proximas semanas.",
            font=("Segoe UI", 11),
        ).pack(anchor="w")
