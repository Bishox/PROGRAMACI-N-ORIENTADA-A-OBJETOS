# Definición de la clase base Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca    # Atributo público
        self.modelo = modelo  # Atributo público
        self.__encendido = False  # Atributo privado (encapsulado)

    def encender(self):
        self.__encendido = True

    def apagar(self):
        self.__encendido = False

    def conducir(self):
        raise NotImplementedError("Método conducir() no implementado en la clase base")

    def __str__(self):
        estado = "encendido" if self.__encendido else "apagado"
        return f"{self.marca} {self.modelo} - Estado: {estado}"


# Definición de la clase derivada Coche
class Coche(Vehiculo):
    def __init__(self, marca, modelo, color):
        super().__init__(marca, modelo)
        self.color = color  # Atributo específico de Coche (público)

    def conducir(self):
        return "El coche está en movimiento"

    def __str__(self):
        return f"Coche {self.marca} {self.modelo}, Color: {self.color}"


if __name__ == "__main__":
    # Crear instancia de Vehiculo
    vehiculo_generico = Vehiculo("MarcaX", "ModeloY")
    print(vehiculo_generico)  # Imprime: MarcaX ModeloY - Estado: apagado
    vehiculo_generico.encender()
    print(vehiculo_generico)  # Imprime: MarcaX ModeloY - Estado: encendido
    vehiculo_generico.apagar()
    print(vehiculo_generico)  # Imprime: MarcaX ModeloY - Estado: apagado

    # Crear instancia de Coche
    mi_coche = Coche("Toyota", "Corolla", "Rojo")
    print(mi_coche)  # Imprime: Coche Toyota Corolla, Color: Rojo
    mi_coche.encender()
    print(mi_coche.conducir())  # Imprime: El coche está en movimiento
    mi_coche.apagar()
    print(mi_coche)  # Imprime: Coche Toyota Corolla, Color: Rojo
