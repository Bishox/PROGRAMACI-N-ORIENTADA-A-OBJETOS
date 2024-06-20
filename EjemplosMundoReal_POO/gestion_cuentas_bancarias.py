class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Se han depositado ${cantidad}. Nuevo saldo: ${self.saldo}")

    def retirar(self, cantidad):
        if self.saldo >= cantidad:
            self.saldo -= cantidad
            print(f"Se han retirado ${cantidad}. Nuevo saldo: ${self.saldo}")
        else:
            print("Fondos insuficientes. No se puede realizar la operación.")

    def mostrar_informacion(self):
        print(f"Titular: {self.titular}, Saldo actual: ${self.saldo}")


# Función para interactuar con el usuario
def interactuar_con_usuario():
    print("Bienvenido al sistema de gestión de cuentas bancarias.")

    # Solicitar información del titular y saldo inicial
    titular = input("Ingrese el nombre del titular de la cuenta: ")
    saldo_inicial = float(input("Ingrese el saldo inicial de la cuenta (si no ingresa nada, será 0): ") or 0)

    # Crear la cuenta bancaria
    cuenta = CuentaBancaria(titular, saldo_inicial)
    print(f"\nCuenta creada para {titular} con un saldo inicial de ${saldo_inicial}\n")

    # Ciclo de interacción con el usuario
    while True:
        print("Opciones:")
        print("1. Mostrar información de la cuenta")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Salir")

        opcion = input("Ingrese el número de la opción que desea realizar: ")

        if opcion == "1":
            cuenta.mostrar_informacion()
        elif opcion == "2":
            cantidad = float(input("Ingrese la cantidad que desea depositar: "))
            cuenta.depositar(cantidad)
        elif opcion == "3":
            cantidad = float(input("Ingrese la cantidad que desea retirar: "))
            cuenta.retirar(cantidad)
        elif opcion == "4":
            print("Gracias por utilizar nuestro sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 4.")


# Ejecutar la interacción con el usuario
interactuar_con_usuario()