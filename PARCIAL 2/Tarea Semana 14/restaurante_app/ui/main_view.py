import tkinter as tk
from tkinter import messagebox, ttk

from servicios.restaurante_servicio import RestauranteServicio


class MainView(ttk.Frame):
    """Panel principal con secciones organizadas mediante contenedores."""

    def __init__(
        self,
        master: tk.Tk,
        restaurante_servicio: RestauranteServicio,
        on_cerrar_sesion,
    ) -> None:
        super().__init__(master, padding=18)
        self.restaurante_servicio = restaurante_servicio
        self.on_cerrar_sesion = on_cerrar_sesion
        self.codigo_var = tk.StringVar()
        self.nombre_var = tk.StringVar()
        self.categoria_var = tk.StringVar()
        self.precio_var = tk.StringVar()
        self.stock_var = tk.StringVar()
        self.estado_productos_var = tk.StringVar()
        self.contador_productos_var = tk.StringVar()
        self._crear_componentes()
        self._actualizar_tabla_productos()

    def _crear_componentes(self) -> None:
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        encabezado = ttk.Frame(self)
        encabezado.grid(row=0, column=0, sticky="ew", pady=(0, 14))
        encabezado.columnconfigure(0, weight=1)

        ttk.Label(
            encabezado,
            text="Panel del restaurante",
            font=("Segoe UI", 18, "bold"),
        ).grid(row=0, column=0, sticky="w")
        ttk.Label(
            encabezado,
            text="Semana 14 - Componentes y contenedores",
            font=("Segoe UI", 10),
        ).grid(row=1, column=0, sticky="w", pady=(4, 0))
        ttk.Button(
            encabezado, text="Cerrar sesion", command=self.on_cerrar_sesion
        ).grid(row=0, column=1, rowspan=2, sticky="e")

        self.notebook = ttk.Notebook(self)
        self.notebook.grid(row=1, column=0, sticky="nsew")

        self._crear_tab_productos()
        self._crear_tab_usuarios()
        self._crear_tab_ventas()

    def _crear_tab_productos(self) -> None:
        tab = ttk.Frame(self.notebook, padding=12)
        tab.columnconfigure(0, weight=0)
        tab.columnconfigure(1, weight=1)
        tab.rowconfigure(1, weight=1)
        self.notebook.add(tab, text="Productos")

        ttk.Label(
            tab,
            textvariable=self.contador_productos_var,
            font=("Segoe UI", 11, "bold"),
        ).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 10))

        formulario = ttk.LabelFrame(tab, text="Formulario de producto", padding=12)
        formulario.grid(row=1, column=0, sticky="ns", padx=(0, 12))
        formulario.columnconfigure(1, weight=1)

        campos = (
            ("Codigo", self.codigo_var),
            ("Nombre", self.nombre_var),
            ("Categoria", self.categoria_var),
            ("Precio", self.precio_var),
            ("Stock", self.stock_var),
        )
        for fila, (etiqueta, variable) in enumerate(campos):
            ttk.Label(formulario, text=etiqueta).grid(
                row=fila, column=0, sticky="w", pady=5
            )
            ttk.Entry(formulario, textvariable=variable, width=28).grid(
                row=fila, column=1, sticky="ew", pady=5
            )

        acciones = ttk.Frame(formulario)
        acciones.grid(row=len(campos), column=0, columnspan=2, sticky="ew", pady=(12, 0))
        acciones.columnconfigure((0, 1), weight=1)

        ttk.Button(acciones, text="Registrar", command=self._registrar_producto).grid(
            row=0, column=0, sticky="ew", padx=(0, 4), pady=4
        )
        ttk.Button(acciones, text="Cargar", command=self._cargar_producto).grid(
            row=0, column=1, sticky="ew", padx=(4, 0), pady=4
        )
        ttk.Button(acciones, text="Actualizar", command=self._actualizar_producto).grid(
            row=1, column=0, sticky="ew", padx=(0, 4), pady=4
        )
        ttk.Button(acciones, text="Eliminar", command=self._eliminar_producto).grid(
            row=1, column=1, sticky="ew", padx=(4, 0), pady=4
        )
        ttk.Button(acciones, text="Limpiar", command=self._limpiar_formulario).grid(
            row=2, column=0, columnspan=2, sticky="ew", pady=4
        )

        ttk.Label(
            formulario,
            textvariable=self.estado_productos_var,
            foreground="#0f766e",
            wraplength=240,
        ).grid(row=len(campos) + 1, column=0, columnspan=2, sticky="ew", pady=(10, 0))

        contenedor_tabla = ttk.Frame(tab)
        contenedor_tabla.grid(row=1, column=1, sticky="nsew")
        contenedor_tabla.columnconfigure(0, weight=1)
        contenedor_tabla.rowconfigure(0, weight=1)

        columnas = ("codigo", "nombre", "categoria", "precio", "stock")
        self.tabla_productos = ttk.Treeview(
            contenedor_tabla, columns=columnas, show="headings", height=14
        )
        self.tabla_productos.grid(row=0, column=0, sticky="nsew")

        scroll_y = ttk.Scrollbar(
            contenedor_tabla, orient="vertical", command=self.tabla_productos.yview
        )
        scroll_y.grid(row=0, column=1, sticky="ns")
        self.tabla_productos.configure(yscrollcommand=scroll_y.set)

        self.tabla_productos.heading("codigo", text="Codigo")
        self.tabla_productos.heading("nombre", text="Producto")
        self.tabla_productos.heading("categoria", text="Categoria")
        self.tabla_productos.heading("precio", text="Precio")
        self.tabla_productos.heading("stock", text="Stock")
        self.tabla_productos.column("codigo", width=90, anchor="center")
        self.tabla_productos.column("nombre", width=210)
        self.tabla_productos.column("categoria", width=150)
        self.tabla_productos.column("precio", width=90, anchor="e")
        self.tabla_productos.column("stock", width=80, anchor="center")

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
        tabla.column("correo", width=260)

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

    def _registrar_producto(self) -> None:
        try:
            producto = self.restaurante_servicio.registrar_producto(
                self.codigo_var.get(),
                self.nombre_var.get(),
                self.categoria_var.get(),
                self.precio_var.get(),
                self.stock_var.get(),
            )
        except ValueError as error:
            self._mostrar_error(error)
            return
        self._actualizar_tabla_productos()
        self.estado_productos_var.set(f"Producto registrado: {producto.nombre}.")

    def _cargar_producto(self) -> None:
        try:
            producto = self.restaurante_servicio.buscar_producto(self.codigo_var.get())
        except ValueError as error:
            self._mostrar_error(error)
            return
        self.codigo_var.set(producto.codigo)
        self.nombre_var.set(producto.nombre)
        self.categoria_var.set(producto.categoria)
        self.precio_var.set(f"{producto.precio:.2f}")
        self.stock_var.set(str(producto.stock))
        self.estado_productos_var.set("Producto cargado en el formulario.")

    def _actualizar_producto(self) -> None:
        try:
            producto = self.restaurante_servicio.actualizar_producto(
                self.codigo_var.get(),
                self.nombre_var.get(),
                self.categoria_var.get(),
                self.precio_var.get(),
                self.stock_var.get(),
            )
        except ValueError as error:
            self._mostrar_error(error)
            return
        self._actualizar_tabla_productos()
        self.estado_productos_var.set(f"Producto actualizado: {producto.nombre}.")

    def _eliminar_producto(self) -> None:
        try:
            producto = self.restaurante_servicio.eliminar_producto(self.codigo_var.get())
        except ValueError as error:
            self._mostrar_error(error)
            return
        self._limpiar_formulario()
        self._actualizar_tabla_productos()
        self.estado_productos_var.set(f"Producto eliminado: {producto.nombre}.")

    def _actualizar_tabla_productos(self) -> None:
        self.tabla_productos.delete(*self.tabla_productos.get_children())
        for producto in self.restaurante_servicio.listar_productos():
            self.tabla_productos.insert(
                "",
                "end",
                values=(
                    producto.codigo,
                    producto.nombre,
                    producto.categoria,
                    f"${producto.precio:.2f}",
                    producto.stock,
                ),
            )
        self.contador_productos_var.set(
            f"Productos registrados: {self.restaurante_servicio.contar_productos()}"
        )

    def _limpiar_formulario(self) -> None:
        self.codigo_var.set("")
        self.nombre_var.set("")
        self.categoria_var.set("")
        self.precio_var.set("")
        self.stock_var.set("")

    def _mostrar_error(self, error: ValueError) -> None:
        self.estado_productos_var.set(str(error))
        messagebox.showwarning("Operacion no realizada", str(error))
