import tkinter as tk
from tkinter import ttk

from servicios.restaurante_servicio import RestauranteServicio


class LoginView(ttk.Frame):
    """Pantalla de acceso simulado para iniciar la aplicacion."""

    def __init__(
        self,
        master: tk.Tk,
        restaurante_servicio: RestauranteServicio,
        on_login_correcto,
    ) -> None:
        super().__init__(master, padding=30)
        self.restaurante_servicio = restaurante_servicio
        self.on_login_correcto = on_login_correcto
        self.usuario_var = tk.StringVar()
        self.clave_var = tk.StringVar()
        self.mensaje_var = tk.StringVar()
        self._crear_componentes()

    def _crear_componentes(self) -> None:
        self.columnconfigure(0, weight=1)

        titulo = ttk.Label(
            self,
            text="Restaurante App",
            font=("Segoe UI", 20, "bold"),
            anchor="center",
        )
        titulo.grid(row=0, column=0, sticky="ew", pady=(20, 6))

        subtitulo = ttk.Label(
            self,
            text="Ingreso de usuario",
            font=("Segoe UI", 11),
            anchor="center",
        )
        subtitulo.grid(row=1, column=0, sticky="ew", pady=(0, 24))

        formulario = ttk.Frame(self)
        formulario.grid(row=2, column=0)
        formulario.columnconfigure(1, weight=1)

        ttk.Label(formulario, text="Usuario").grid(row=0, column=0, sticky="w", pady=5)
        usuario_entry = ttk.Entry(formulario, textvariable=self.usuario_var, width=30)
        usuario_entry.grid(row=0, column=1, sticky="ew", pady=5)
        usuario_entry.focus()

        ttk.Label(formulario, text="Clave").grid(row=1, column=0, sticky="w", pady=5)
        clave_entry = ttk.Entry(
            formulario, textvariable=self.clave_var, width=30, show="*"
        )
        clave_entry.grid(row=1, column=1, sticky="ew", pady=5)
        clave_entry.bind("<Return>", lambda _: self._intentar_ingreso())

        ttk.Button(
            formulario, text="Ingresar", command=self._intentar_ingreso
        ).grid(row=2, column=0, columnspan=2, sticky="ew", pady=(18, 8))

        mensaje = ttk.Label(
            formulario,
            textvariable=self.mensaje_var,
            foreground="#b00020",
            anchor="center",
        )
        mensaje.grid(row=3, column=0, columnspan=2, sticky="ew")

    def _intentar_ingreso(self) -> None:
        usuario = self.usuario_var.get()
        clave = self.clave_var.get()
        if not usuario.strip() or not clave.strip():
            self.mensaje_var.set("Ingrese usuario y clave.")
            return
        if not self.restaurante_servicio.validar_acceso(usuario, clave):
            self.mensaje_var.set("Credenciales incorrectas.")
            return
        self.mensaje_var.set("")
        self.clave_var.set("")
        self.on_login_correcto()
