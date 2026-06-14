class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def mostrar_informacion(self):
        print("Informacion de la mascota")
        print("-------------------------")
        print(f"Nombre : {self.nombre}")
        print(f"Especie: {self.especie}")
        print(f"Edad   : {self.edad} anios")

    def hacer_sonido(self):
        especie = self.especie.lower()

        if especie == "perro":
            sonido = "Guau guau"
        elif especie == "gato":
            sonido = "Miau"
        elif especie == "ave":
            sonido = "Pio pio"
        else:
            sonido = "Sonido de mascota"

        print(f"{self.nombre} hace: {sonido}")
