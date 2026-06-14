def registrar_mascota():
    print("Registro de mascota")
    nombre = input("Ingrese el nombre de la mascota: ")
    especie = input("Ingrese la especie de la mascota: ")
    edad = input("Ingrese la edad de la mascota: ")

    return nombre, especie, edad


def mostrar_informacion(nombre, especie, edad):
    print("\nInformacion registrada")
    print("----------------------")
    print(f"Nombre : {nombre}")
    print(f"Especie: {especie}")
    print(f"Edad   : {edad} anios")


def main():
    nombre, especie, edad = registrar_mascota()
    mostrar_informacion(nombre, especie, edad)


if __name__ == "__main__":
    main()
