from modelos.bebida import Bebida
from modelos.platillo import Platillo
from servicios.restaurante import Restaurante


def main() -> None:
    # Se crea el servicio principal del restaurante.
    restaurante = Restaurante("Sabores del Valle")

    # Se crean platillos con atributos heredados y propios.
    encebollado = Platillo("Encebollado", 3.50, True, "Plato fuerte", 18)
    bolon = Platillo("Bolon de verde", 2.25, True, "Desayuno", 12)

    # Se crean bebidas con atributos heredados y propios.
    jugo_natural = Bebida("Jugo natural", 1.75, True, 350, "Fria")
    cafe = Bebida("Cafe pasado", 1.25, False, 200, "Caliente")

    # Se modifica un precio mediante el metodo de acceso controlado.
    cafe.cambiar_precio(1.50)

    restaurante.agregar_producto(encebollado)
    restaurante.agregar_producto(bolon)
    restaurante.agregar_producto(jugo_natural)
    restaurante.agregar_producto(cafe)

    restaurante.mostrar_productos()


if __name__ == "__main__":
    main()
