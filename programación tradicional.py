# Función para ingresar temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    for i in range(7):
        temperatura = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        temperaturas.append(temperatura)
    return temperaturas


# Función para calcular el promedio semanal
def calcular_promedio_semanal(temperaturas):
    return sum(temperaturas) / len(temperaturas)


# Función principal para coordinar la lógica del programa
def main():
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio_semanal(temperaturas)
    print(f"El promedio semanal de temperaturas es: {promedio:.2f}")


# Llamada a la función principal
if __name__ == "__main__":
    main()
