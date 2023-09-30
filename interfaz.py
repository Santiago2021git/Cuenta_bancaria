from modelo import Cuenta

cuentas = []

def crearCuenta():
    numero_cuenta = int(input("Ingrese el número de cuenta: "))
    documento_identidad = int(input("Ingrese el documento de identidad: "))
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    saldo_actual = float(input("Ingrese el saldo actual: "))

    nueva_cuenta = Cuenta(numero_cuenta, documento_identidad, nombre_cliente, saldo_actual)
    cuentas.append(nueva_cuenta)
    print("Cuenta creada y almacenada con éxito.")

def mostrarCuentas():
    print("\nListado de Cuentas:")
    for i, cuenta in enumerate(cuentas, start=1):
        print(f"Cuenta {i}:")
        cuenta.mostrarDatos()
        print("\n")

def depositarDinero():
    if not cuentas:
        print("No hay cuentas creadas.")
        return

    mostrarCuentas()
    seleccion = int(input("Seleccione el número de cuenta en la que desea depositar dinero: ")) - 1

    if 0 <= seleccion < len(cuentas):
        cantidad = float(input("Ingrese la cantidad a depositar: "))
        cuentas[seleccion].depositarDinero(cantidad)
        print("Dinero depositado con éxito en la cuenta seleccionada.")
    else:
        print("Número de cuenta no válido.")

def retirarDinero():
    if not cuentas:
        print("No hay cuentas creadas.")
        return

    mostrarCuentas()
    seleccion = int(input("Seleccione el número de cuenta de la que desea retirar dinero: ")) - 1

    if 0 <= seleccion < len(cuentas):
        cantidad = float(input("Ingrese la cantidad a retirar: "))
        cuentas[seleccion].retirarDinero(cantidad)
        print("Dinero retirado con éxito de la cuenta seleccionada.")
    else:
        print("Número de cuenta no válido.")

def main():
    while True:
        print("\nMENU:")
        print("1. Crear nueva cuenta")
        print("2. Mostrar cuentas")
        print("3. Depositar dinero")
        print("4. Retirar dinero")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crearCuenta()
        elif opcion == "2":
            mostrarCuentas()
        elif opcion == "3":
            depositarDinero()
        elif opcion == "4":
            retirarDinero()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente nuevamente.")




