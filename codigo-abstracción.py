from abc import ABC, abstractmethod

class metododepago(ABC):
    def __init__(self, nombre, numerocuenta, monto):
        self.nombre = nombre
        self.numerocuenta = numerocuenta
        self.monto = monto

    @abstractmethod
    def pagar(self):
        pass

class Nequi(metododepago):
    def __init__(self, nombre, numerocuenta, monto, numcerocelular):
        super().__init__(nombre, numerocuenta, monto)
        self.numcerocelular = numcerocelular

    def pagar(self):
        print(f"Pagando {self.monto} a través de Nequi, número de celular: {self.numcerocelular}")

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Numero de cuenta: {self.numerocuenta}, Monto: {self.monto}, Numero de celular: {self.numcerocelular}"

class Daviplata(metododepago):
    def __init__(self, nombre, numerocuenta, monto, pin):
        super().__init__(nombre, numerocuenta, monto)
        self.pin = pin

    def pagar(self):
        print(f"Pagando {self.monto} a través de Daviplata, con pin: {self.pin}")

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Numero de cuenta: {self.numerocuenta}, Monto: {self.monto}, Pin: {self.pin}"

class PSE(metododepago):
    def __init__(self, nombre, numerocuenta, monto, codigoseguridad):
        super().__init__(nombre, numerocuenta, monto)
        self.codigoseguridad = codigoseguridad

    def pagar(self):
        print(f"Pagando {self.monto} a través de PSE, con código de seguridad: {self.codigoseguridad}")

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Numero de cuenta: {self.numerocuenta}, Monto: {self.monto}, Codigo de seguridad: {self.codigoseguridad}"

class tarjetacredito(metododepago):
    def __init__(self, nombre, numerocuenta, monto, pin):
        super().__init__(nombre, numerocuenta, monto)
        self.pin = pin

    def pagar(self):
        print(f"Pagando {self.monto} a través de Tarjeta de Crédito, con pin: {self.pin}")

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Numero de cuenta: {self.numerocuenta}, Monto: {self.monto}, Pin: {self.pin}"

class tarjetadebito(metododepago):
    def __init__(self, nombre, numerocuenta, monto, pin):
        super().__init__(nombre, numerocuenta, monto)
        self.pin = pin

    def pagar(self):
        print(f"Pagando {self.monto} a través de Tarjeta Débito, con pin: {self.pin}")

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Numero de cuenta: {self.numerocuenta}, Monto: {self.monto}, Pin: {self.pin}"

class Efectivo(metododepago):
    def __init__(self, nombre, monto, moneda):
        super().__init__(nombre, "", monto)  
        self.moneda = moneda

    def pagar(self):
        print(f"Pagando {self.monto} en efectivo, en moneda: {self.moneda}")

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Monto: {self.monto}, Moneda: {self.moneda}"

# Instancias
nequi = Nequi("Sebastian Negrette", "123456789", 500000, "3208825418")
daviplata = Daviplata("Antony Delon", "987654321", 1300000, "1234")
pse = PSE("Luis García", "456789123", 2000000, "5678")
credit = tarjetacredito("Juan Medina", "5555666677778888", 3000000, "9876")
debit = tarjetadebito("María Callas", "9999888877776666", 2500000, "5432")
efectivo = Efectivo("Aristóteles Onassis", 1000000, "USD")

#informacion
print(nequi.mostrar_informacion())
nequi.pagar()

print(daviplata.mostrar_informacion())
daviplata.pagar()

print(pse.mostrar_informacion())
pse.pagar()

print(credit.mostrar_informacion())
credit.pagar()

print(debit.mostrar_informacion())
debit.pagar()

print(efectivo.mostrar_informacion())
efectivo.pagar()
