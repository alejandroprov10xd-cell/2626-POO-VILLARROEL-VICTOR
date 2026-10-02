import tkinter as tk
from pathlib import Path
from tkinter import messagebox, ttk

from modelos.usuario import Usuario
from servicios.restaurante_servicio import RestauranteServicio


class MainView(ttk.Frame):
    """Panel principal con secciones organizadas mediante contenedores."""

    def __init__(
        self,
        master: tk.Tk,
        restaurante_servicio: RestauranteServicio,
        usuario_actual: Usuario,
        on_cerrar_sesion,
    ) -> None:
        super().__init__(master, padding=18)
        self.restaurante_servicio = restaurante_servicio
        self.usuario_actual = usuario_actual
        self.on_cerrar_sesion = on_cerrar_sesion
        self.codigo_var = tk.StringVar()
        self.nombre_var = tk.StringVar()
        self.categoria_var = tk.StringVar()
        self.precio_var = tk.StringVar()
        self.stock_var = tk.StringVar()
        self.estado_productos_var = tk.StringVar()
        self.estado_ventas_var = tk.StringVar()
        self.estado_usuarios_var = tk.StringVar()
        self.contador_productos_var = tk.StringVar()
        self.contador_usuarios_var = tk.StringVar()
        self.usuario_venta_var = tk.StringVar()
        self.producto_venta_var = tk.StringVar()
        self.usuario_identificacion_var = tk.StringVar()
        self.usuario_nombre_var = tk.StringVar()
        self.usuario_cuenta_var = tk.StringVar()
        self.usuario_clave_var = tk.StringVar()
        self.usuario_rol_var = tk.StringVar(value="Cliente")
        self.usuario_seleccionado_id: str | None = None
        self.opciones_usuarios: dict[str, str] = {}
        self.opciones_productos: dict[str, str] = {}
        self.logo_imagen = self._cargar_imagen("logo.ppm")
        self.venta_imagen = self._cargar_imagen("venta.ppm")
        self._crear_componentes()
        self._actualizar_tabla_productos()
        self._actualizar_tabla_usuarios()
        self._actualizar_tabla_ventas()

    def _crear_componentes(self) -> None:
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        encabezado = ttk.Frame(self)
        encabezado.grid(row=0, column=0, sticky="ew", pady=(0, 14))
        encabezado.columnconfigure(0, weight=1)

        marca = ttk.Frame(encabezado)
        marca.grid(row=0, column=0, rowspan=2, sticky="w")
        marca.columnconfigure(1, weight=1)

        if self.logo_imagen is not None:
            ttk.Label(marca, image=self.logo_imagen).grid(
                row=0, column=0, rowspan=2, sticky="w", padx=(0, 10)
            )

        ttk.Label(
            marca,
            text="Panel del restaurante",
            font=("Segoe UI", 18, "bold"),
        ).grid(row=0, column=1, sticky="w")
        ttk.Label(
            marca,
            text="Semana 16 - Manejo de eventos en usuarios",
            font=("Segoe UI", 10),
        ).grid(row=1, column=1, sticky="w", pady=(4, 0))
        ttk.Label(
            encabezado,
            text=f"Sesion: {self.usuario_actual.nombre} ({self.usuario_actual.rol})",
            font=("Segoe UI", 10, "bold"),
        ).grid(row=0, column=1, sticky="e", padx=(0, 10))
        ttk.Button(
            encabezado, text="Cerrar sesion", command=self.on_cerrar_sesion
        ).grid(row=1, column=1, sticky="e")

        self.notebook = ttk.Notebook(self)
        self.notebook.grid(row=1, column=0, sticky="nsew")

        self._crear_tab_productos()
        if self.restaurante_servicio.usuario_es_administrador(self.usuario_actual):
            self._crear_tab_usuarios()
        else:
            self._crear_tab_usuarios_restringida()
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
        tab.columnconfigure(0, weight=0)
        tab.columnconfigure(1, weight=1)
        tab.rowconfigure(1, weight=1)
        self.notebook.add(tab, text="Usuarios")

        ttk.Label(
            tab,
            textvariable=self.contador_usuarios_var,
            font=("Segoe UI", 11, "bold"),
        ).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 10))

        formulario = ttk.LabelFrame(tab, text="Formulario de usuario", padding=12)
        formulario.grid(row=1, column=0, sticky="ns", padx=(0, 12))
        formulario.columnconfigure(1, weight=1)

        ttk.Label(formulario, text="Identificacion").grid(
            row=0, column=0, sticky="w", pady=5
        )
        self.usuario_identificacion_entry = ttk.Entry(
            formulario, textvariable=self.usuario_identificacion_var, width=28
        )
        self.usuario_identificacion_entry.grid(row=0, column=1, sticky="ew", pady=5)

        ttk.Label(formulario, text="Nombre").grid(row=1, column=0, sticky="w", pady=5)
        usuario_nombre_entry = ttk.Entry(
            formulario, textvariable=self.usuario_nombre_var, width=28
        )
        usuario_nombre_entry.grid(row=1, column=1, sticky="ew", pady=5)

        ttk.Label(formulario, text="Usuario").grid(row=2, column=0, sticky="w", pady=5)
        usuario_cuenta_entry = ttk.Entry(
            formulario, textvariable=self.usuario_cuenta_var, width=28
        )
        usuario_cuenta_entry.grid(row=2, column=1, sticky="ew", pady=5)

        ttk.Label(formulario, text="Clave").grid(row=3, column=0, sticky="w", pady=5)
        usuario_clave_entry = ttk.Entry(
            formulario, textvariable=self.usuario_clave_var, width=28, show="*"
        )
        usuario_clave_entry.grid(row=3, column=1, sticky="ew", pady=5)

        ttk.Label(formulario, text="Rol").grid(row=4, column=0, sticky="w", pady=5)
        self.combo_roles = ttk.Combobox(
            formulario,
            textvariable=self.usuario_rol_var,
            values=Usuario.ROLES_VALIDOS,
            state="readonly",
            width=25,
        )
        self.combo_roles.grid(row=4, column=1, sticky="ew", pady=5)
        self.combo_roles.bind("<<ComboboxSelected>>", self._evento_cambiar_rol)

        acciones = ttk.Frame(formulario)
        acciones.grid(row=5, column=0, columnspan=2, sticky="ew", pady=(12, 0))
        acciones.columnconfigure((0, 1), weight=1)

        ttk.Button(acciones, text="Registrar", command=self._registrar_usuario).grid(
            row=0, column=0, sticky="ew", padx=(0, 4), pady=4
        )
        ttk.Button(acciones, text="Actualizar", command=self._actualizar_usuario).grid(
            row=0, column=1, sticky="ew", padx=(4, 0), pady=4
        )
        ttk.Button(acciones, text="Eliminar", command=self._eliminar_usuario).grid(
            row=1, column=0, sticky="ew", padx=(0, 4), pady=4
        )
        ttk.Button(
            acciones, text="Limpiar", command=self._limpiar_formulario_usuario
        ).grid(row=1, column=1, sticky="ew", padx=(4, 0), pady=4)

        ttk.Label(
            formulario,
            textvariable=self.estado_usuarios_var,
            foreground="#0f766e",
            wraplength=250,
        ).grid(row=6, column=0, columnspan=2, sticky="ew", pady=(10, 0))

        contenedor_tabla = ttk.Frame(tab)
        contenedor_tabla.grid(row=1, column=1, sticky="nsew")
        contenedor_tabla.columnconfigure(0, weight=1)
        contenedor_tabla.rowconfigure(0, weight=1)

        columnas = ("identificacion", "nombre", "usuario", "rol")
        self.tabla_usuarios = ttk.Treeview(
            contenedor_tabla, columns=columnas, show="headings", height=14
        )
        self.tabla_usuarios.grid(row=0, column=0, sticky="nsew")
        self.tabla_usuarios.bind("<<TreeviewSelect>>", self._evento_seleccionar_usuario)
        self.tabla_usuarios.bind("<Escape>", self._evento_limpiar_usuario)

        scroll_y = ttk.Scrollbar(
            contenedor_tabla, orient="vertical", command=self.tabla_usuarios.yview
        )
        scroll_y.grid(row=0, column=1, sticky="ns")
        self.tabla_usuarios.configure(yscrollcommand=scroll_y.set)

        self.tabla_usuarios.heading("identificacion", text="Identificacion")
        self.tabla_usuarios.heading("nombre", text="Nombre")
        self.tabla_usuarios.heading("usuario", text="Usuario")
        self.tabla_usuarios.heading("rol", text="Rol")
        self.tabla_usuarios.column("identificacion", width=120, anchor="center")
        self.tabla_usuarios.column("nombre", width=200)
        self.tabla_usuarios.column("usuario", width=160)
        self.tabla_usuarios.column("rol", width=130, anchor="center")

        self._vincular_eventos_usuario(
            self.usuario_identificacion_entry,
            usuario_nombre_entry,
            usuario_cuenta_entry,
            usuario_clave_entry,
            self.combo_roles,
        )

    def _crear_tab_usuarios_restringida(self) -> None:
        tab = ttk.Frame(self.notebook, padding=24)
        tab.columnconfigure(0, weight=1)
        self.notebook.add(tab, text="Usuarios")

        ttk.Label(
            tab,
            text="Gestion de usuarios",
            font=("Segoe UI", 14, "bold"),
        ).grid(row=0, column=0, sticky="w", pady=(0, 8))
        ttk.Label(
            tab,
            text=(
                "Esta seccion esta disponible solo para usuarios con rol "
                "Administrador."
            ),
            font=("Segoe UI", 10),
        ).grid(row=1, column=0, sticky="w")

    def _crear_tab_ventas(self) -> None:
        tab = ttk.Frame(self.notebook, padding=12)
        tab.columnconfigure(0, weight=0)
        tab.columnconfigure(1, weight=1)
        tab.rowconfigure(0, weight=1)
        self.notebook.add(tab, text="Ventas")

        formulario = ttk.LabelFrame(tab, text="Registro de venta", padding=12)
        formulario.grid(row=0, column=0, sticky="ns", padx=(0, 12))
        formulario.columnconfigure(1, weight=1)

        if self.venta_imagen is not None:
            ttk.Label(formulario, image=self.venta_imagen).grid(
                row=0, column=0, columnspan=2, pady=(0, 10)
            )

        ttk.Label(formulario, text="Usuario").grid(row=1, column=0, sticky="w", pady=5)
        self.combo_usuarios = ttk.Combobox(
            formulario,
            textvariable=self.usuario_venta_var,
            state="readonly",
            width=32,
        )
        self.combo_usuarios.grid(row=1, column=1, sticky="ew", pady=5)

        ttk.Label(formulario, text="Producto").grid(row=2, column=0, sticky="w", pady=5)
        self.combo_productos = ttk.Combobox(
            formulario,
            textvariable=self.producto_venta_var,
            state="readonly",
            width=32,
        )
        self.combo_productos.grid(row=2, column=1, sticky="ew", pady=5)

        ttk.Button(
            formulario,
            text="Registrar venta",
            command=self._registrar_venta,
        ).grid(row=3, column=0, columnspan=2, sticky="ew", pady=(14, 8))

        ttk.Label(
            formulario,
            textvariable=self.estado_ventas_var,
            foreground="#0f766e",
            wraplength=260,
        ).grid(row=4, column=0, columnspan=2, sticky="ew", pady=(6, 0))

        contenedor_tabla = ttk.Frame(tab)
        contenedor_tabla.grid(row=0, column=1, sticky="nsew")
        contenedor_tabla.columnconfigure(0, weight=1)
        contenedor_tabla.rowconfigure(0, weight=1)

        columnas = ("usuario", "producto", "fecha")
        self.tabla_ventas = ttk.Treeview(
            contenedor_tabla, columns=columnas, show="headings", height=14
        )
        self.tabla_ventas.grid(row=0, column=0, sticky="nsew")

        scroll_y = ttk.Scrollbar(
            contenedor_tabla, orient="vertical", command=self.tabla_ventas.yview
        )
        scroll_y.grid(row=0, column=1, sticky="ns")
        self.tabla_ventas.configure(yscrollcommand=scroll_y.set)

        self.tabla_ventas.heading("usuario", text="Usuario")
        self.tabla_ventas.heading("producto", text="Producto")
        self.tabla_ventas.heading("fecha", text="Fecha")
        self.tabla_ventas.column("usuario", width=190)
        self.tabla_ventas.column("producto", width=210)
        self.tabla_ventas.column("fecha", width=150, anchor="center")
        self._actualizar_opciones_venta()

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
        self._actualizar_opciones_venta()
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
        self._actualizar_opciones_venta()
        self.estado_productos_var.set(f"Producto actualizado: {producto.nombre}.")

    def _eliminar_producto(self) -> None:
        try:
            producto = self.restaurante_servicio.eliminar_producto(self.codigo_var.get())
        except ValueError as error:
            self._mostrar_error(error)
            return
        self._limpiar_formulario()
        self._actualizar_tabla_productos()
        self._actualizar_opciones_venta()
        self.estado_productos_var.set(f"Producto eliminado: {producto.nombre}.")

    def _registrar_usuario(self) -> None:
        try:
            usuario = self.restaurante_servicio.registrar_usuario(
                self.usuario_identificacion_var.get(),
                self.usuario_nombre_var.get(),
                self.usuario_cuenta_var.get(),
                self.usuario_clave_var.get(),
                self.usuario_rol_var.get(),
            )
        except ValueError as error:
            self._mostrar_error_usuario(error)
            return
        self._actualizar_tabla_usuarios()
        self._actualizar_opciones_venta()
        self._limpiar_formulario_usuario(mostrar_mensaje=False)
        self.estado_usuarios_var.set(f"Usuario registrado: {usuario.nombre}.")

    def _actualizar_usuario(self) -> None:
        identificacion = self.usuario_seleccionado_id or self.usuario_identificacion_var.get()
        try:
            usuario = self.restaurante_servicio.actualizar_usuario(
                identificacion,
                self.usuario_nombre_var.get(),
                self.usuario_cuenta_var.get(),
                self.usuario_clave_var.get(),
                self.usuario_rol_var.get(),
            )
        except ValueError as error:
            self._mostrar_error_usuario(error)
            return
        self._actualizar_tabla_usuarios()
        self._actualizar_opciones_venta()
        self._limpiar_formulario_usuario(mostrar_mensaje=False)
        self.estado_usuarios_var.set(f"Usuario actualizado: {usuario.nombre}.")

    def _eliminar_usuario(self) -> None:
        identificacion = self.usuario_seleccionado_id or self.usuario_identificacion_var.get()
        if not identificacion.strip():
            self._mostrar_error_usuario(ValueError("Seleccione un usuario."))
            return
        confirmar = messagebox.askyesno(
            "Confirmar eliminacion",
            "Desea eliminar el usuario seleccionado?",
        )
        if not confirmar:
            return
        try:
            usuario = self.restaurante_servicio.eliminar_usuario(
                identificacion,
                self.usuario_actual.identificacion,
            )
        except ValueError as error:
            self._mostrar_error_usuario(error)
            return
        self._actualizar_tabla_usuarios()
        self._actualizar_opciones_venta()
        self._limpiar_formulario_usuario(mostrar_mensaje=False)
        self.estado_usuarios_var.set(f"Usuario eliminado: {usuario.nombre}.")

    def _registrar_venta(self) -> None:
        usuario = self.opciones_usuarios.get(self.usuario_venta_var.get(), "")
        producto = self.opciones_productos.get(self.producto_venta_var.get(), "")
        try:
            venta = self.restaurante_servicio.registrar_venta(usuario, producto)
            nombre_usuario, nombre_producto, _ = self.restaurante_servicio.obtener_detalle_venta(
                venta
            )
        except ValueError as error:
            self.estado_ventas_var.set(str(error))
            messagebox.showwarning("Venta no registrada", str(error))
            return
        self._actualizar_tabla_ventas()
        self.estado_ventas_var.set(
            f"Venta registrada: {nombre_usuario} compro {nombre_producto}."
        )

    def _evento_seleccionar_usuario(self, event) -> None:
        seleccion = self.tabla_usuarios.selection()
        if not seleccion:
            return
        valores = self.tabla_usuarios.item(seleccion[0], "values")
        if not valores:
            return
        identificacion = valores[0]
        try:
            usuario = self.restaurante_servicio.buscar_usuario(identificacion)
        except ValueError as error:
            self._mostrar_error_usuario(error)
            return
        self.usuario_seleccionado_id = usuario.identificacion
        self._bloquear_identificacion_usuario(False)
        self.usuario_identificacion_var.set(usuario.identificacion)
        self.usuario_nombre_var.set(usuario.nombre)
        self.usuario_cuenta_var.set(usuario.usuario)
        self.usuario_clave_var.set(usuario.clave)
        self.usuario_rol_var.set(usuario.rol)
        self._bloquear_identificacion_usuario(True)
        self.estado_usuarios_var.set("Usuario cargado desde la tabla.")

    def _evento_registrar_usuario(self, event):
        self._registrar_usuario()
        return "break"

    def _evento_limpiar_usuario(self, event):
        self._limpiar_formulario_usuario()
        return "break"

    def _evento_cambiar_rol(self, event) -> None:
        self.estado_usuarios_var.set(f"Rol seleccionado: {self.usuario_rol_var.get()}.")

    def _vincular_eventos_usuario(self, *widgets) -> None:
        for widget in widgets:
            widget.bind("<Return>", self._evento_registrar_usuario)
            widget.bind("<Escape>", self._evento_limpiar_usuario)

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

    def _actualizar_tabla_usuarios(self) -> None:
        if not hasattr(self, "tabla_usuarios"):
            return
        self.tabla_usuarios.delete(*self.tabla_usuarios.get_children())
        for usuario in self.restaurante_servicio.listar_usuarios():
            self.tabla_usuarios.insert(
                "",
                "end",
                iid=usuario.identificacion,
                values=(
                    usuario.identificacion,
                    usuario.nombre,
                    usuario.usuario,
                    usuario.rol,
                ),
            )
        self.contador_usuarios_var.set(
            f"Usuarios registrados: {self.restaurante_servicio.contar_usuarios()}"
        )

    def _actualizar_tabla_ventas(self) -> None:
        self.tabla_ventas.delete(*self.tabla_ventas.get_children())
        for venta in self.restaurante_servicio.listar_ventas():
            try:
                nombre_usuario, nombre_producto, fecha = (
                    self.restaurante_servicio.obtener_detalle_venta(venta)
                )
            except ValueError:
                continue
            self.tabla_ventas.insert(
                "",
                "end",
                values=(nombre_usuario, nombre_producto, fecha),
            )

    def _actualizar_opciones_venta(self) -> None:
        self.opciones_usuarios = {
            f"{usuario.identificacion} - {usuario.nombre} ({usuario.rol})": (
                usuario.identificacion
            )
            for usuario in self.restaurante_servicio.listar_usuarios()
        }
        self.opciones_productos = {
            f"{producto.codigo} - {producto.nombre}": producto.codigo
            for producto in self.restaurante_servicio.listar_productos()
        }
        self.combo_usuarios["values"] = list(self.opciones_usuarios)
        self.combo_productos["values"] = list(self.opciones_productos)
        if self.combo_usuarios["values"] and not self.usuario_venta_var.get():
            self.combo_usuarios.current(0)
        if self.combo_productos["values"] and not self.producto_venta_var.get():
            self.combo_productos.current(0)

    def _cargar_imagen(self, nombre_archivo: str) -> tk.PhotoImage | None:
        ruta = Path(__file__).resolve().parent.parent / "assets" / nombre_archivo
        try:
            return tk.PhotoImage(file=ruta)
        except tk.TclError:
            return None

    def _limpiar_formulario(self) -> None:
        self.codigo_var.set("")
        self.nombre_var.set("")
        self.categoria_var.set("")
        self.precio_var.set("")
        self.stock_var.set("")

    def _limpiar_formulario_usuario(self, mostrar_mensaje: bool = True) -> None:
        self._bloquear_identificacion_usuario(False)
        self.usuario_seleccionado_id = None
        self.usuario_identificacion_var.set("")
        self.usuario_nombre_var.set("")
        self.usuario_cuenta_var.set("")
        self.usuario_clave_var.set("")
        self.usuario_rol_var.set("Cliente")
        if hasattr(self, "tabla_usuarios"):
            self.tabla_usuarios.selection_remove(self.tabla_usuarios.selection())
        if mostrar_mensaje:
            self.estado_usuarios_var.set("Formulario de usuario limpio.")

    def _bloquear_identificacion_usuario(self, bloquear: bool) -> None:
        if hasattr(self, "usuario_identificacion_entry"):
            estado = "readonly" if bloquear else "normal"
            self.usuario_identificacion_entry.configure(state=estado)

    def _mostrar_error(self, error: ValueError) -> None:
        self.estado_productos_var.set(str(error))
        messagebox.showwarning("Operacion no realizada", str(error))

    def _mostrar_error_usuario(self, error: ValueError) -> None:
        self.estado_usuarios_var.set(str(error))
        messagebox.showwarning("Operacion no realizada", str(error))
