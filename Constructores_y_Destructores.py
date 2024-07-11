class Archivo:
    def __init__(self, nombre):
        self.nombre = nombre
        print(f"Se ha abierto el archivo '{self.nombre}'.")

    def operar(self):
        print(f"Operando con el archivo '{self.nombre}'.")

    def __del__(self):
        print(f"Se ha cerrado el archivo '{self.nombre}'.")


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print(f"Se ha creado a la persona '{self.nombre}' de {self.edad} años.")

    def __del__(self):
        print(f"Se ha eliminado a la persona '{self.nombre}'.")


# Ejemplo de uso de las clases

# Creando objetos Archivo y Persona
archivo1 = Archivo("datos.txt")
persona1 = Persona("Juan", 30)

# Operando con el archivo
archivo1.operar()

# Eliminando objetos (provocará la ejecución de los destructores)
del archivo1
del persona1
