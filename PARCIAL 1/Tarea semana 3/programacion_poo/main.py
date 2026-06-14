from mascota import Mascota


def main():
    mascota_1 = Mascota("Luna", "Perro", 3)
    mascota_2 = Mascota("Michi", "Gato", 2)

    mascota_1.mostrar_informacion()
    mascota_1.hacer_sonido()

    print()

    mascota_2.mostrar_informacion()
    mascota_2.hacer_sonido()


if __name__ == "__main__":
    main()
