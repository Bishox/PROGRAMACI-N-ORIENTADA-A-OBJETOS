class ClimaDiario:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperatura(self, temperatura):
        self.temperaturas.append(temperatura)

    def calcular_promedio_semanal(self):
        if len(self.temperaturas) == 0:
            return 0
        return sum(self.temperaturas) / len(self.temperaturas)

    def ingresar_temperaturas(self):
        for i in range(7):
            temperatura = float(input(f"Ingrese la temperatura del día {i + 1}: "))
            self.ingresar_temperatura(temperatura)

# Función principal para coordinar la lógica del programa
def main():
    clima = ClimaDiario()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio_semanal()
    print(f"El promedio semanal de temperaturas es: {promedio:.2f}")

# Llamada a la función principal
if __name__ == "__main__":
    main()
