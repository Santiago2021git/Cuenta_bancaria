class Cuenta:
    def __init__(self, numero_cuenta, documento_identidad, nombre_cliente, saldo_actual):
        self.numero_cuenta = numero_cuenta
        self.documento_identidad = documento_identidad
        self.nombre_cliente = nombre_cliente
        self.saldo_actual = saldo_actual

    def depositarDinero(self, cantidad):
        retencion = cantidad * 0.19
        monto_depositado = cantidad - retencion
        self.saldo_actual += monto_depositadoD

    def retirarDinero(self, cantidad):
        if cantidad <= self.saldo_actual:
            self.saldo_actual -= cantidad
        else:
            print("Cuenta con saldo insuficiente, no se puede retirar.")

    def mostrarDatos(self):
        print("Número de cuenta:", self.numero_cuenta)
        print("Documento de Identidad:", self.documento_identidad)
        print("Nombre del cliente:", self.nombre_cliente)
        print("Saldo actual:", self.saldo_actual)
