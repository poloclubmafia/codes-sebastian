class CuentaBancaria:
    def __init__(self, numero_cuenta, saldo_inicial):
        self.__saldo = saldo_inicial
    
    def obtener_saldo(self): #getter
        return self.__saldo

    def depositar(self, monto):
        if monto > 0:
            self.__saldo = self.__saldo + monto
            print(f"Depósito existoso de $ {monto}.")
        else:
            print("El monto del depósito debe ser mayor que cero.")

cuenta = CuentaBancaria("1065566814", 1000)
print(f"Saldo inicial: $ {cuenta.obtener_saldo()}")

cuenta.depositar(500)
print(f"Saldo actual: $ {cuenta.obtener_saldo()}")
