import tkinter as tk
from pathlib import Path
from tkinter import ttk

from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView


RUTA_DATOS = Path(__file__).resolve().parent / "datos"


class RestauranteApp:
    """Controla una sola ventana y el cambio entre vistas."""

    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Restaurante App")
        self.root.geometry("760x480")
        self.root.minsize(680, 420)
        self._configurar_estilo()

        archivo_servicio = ArchivoServicio(RUTA_DATOS)
        self.restaurante_servicio = RestauranteServicio(archivo_servicio)
        self.vista_actual: ttk.Frame | None = None
        self.mostrar_login()

    def ejecutar(self) -> None:
        self.root.mainloop()

    def mostrar_login(self) -> None:
        self._cambiar_vista(
            LoginView(self.root, self.restaurante_servicio, self.mostrar_panel)
        )

    def mostrar_panel(self) -> None:
        self._cambiar_vista(
            MainView(self.root, self.restaurante_servicio, self.mostrar_login)
        )

    def _cambiar_vista(self, nueva_vista: ttk.Frame) -> None:
        if self.vista_actual is not None:
            self.vista_actual.destroy()
        self.vista_actual = nueva_vista
        self.vista_actual.pack(fill="both", expand=True)

    def _configurar_estilo(self) -> None:
        estilo = ttk.Style()
        estilo.theme_use("clam")
        estilo.configure("TFrame", background="#f7f7f7")
        estilo.configure("TLabel", background="#f7f7f7", font=("Segoe UI", 10))
        estilo.configure("TButton", font=("Segoe UI", 10), padding=6)
        estilo.configure("Treeview", rowheight=26, font=("Segoe UI", 10))
        estilo.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))


def main() -> None:
    app = RestauranteApp()
    app.ejecutar()


if __name__ == "__main__":
    main()
