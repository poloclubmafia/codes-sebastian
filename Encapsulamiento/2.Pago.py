class Pago:
    def __init__(self, monto, metodo, nombre):
        self.__monto = monto
        self.__metodo = metodo
        self.__nombre = nombre
        self.__estado = "Pendiente"

    def procesar_pago(self):
        if self.__monto > 0:
            self.__estado = "Completado"
        else:
            self.__estado = "Fallido"

    def obtener_estado(self):
        return self.__estado

    def censurar_nombre(self):
        return self.__nombre[:3] + "*" * (len(self.__nombre) - 3)

    def mostrar_detalles(self):
        print(f"Nombre: {self.censurar_nombre()}, Método: {self.__metodo}, Monto: ${self.__monto:.2f}, Estado: {self.__estado}")

# Simular pagos
pago1 = Pago(100, "Tarjeta de Crédito", "Juan Pérez")
pago2 = Pago(50, "PayPal", "María González")
pago3 = Pago(20, "Efectivo", "Carlos Ramírez")


pago1.procesar_pago()
pago2.procesar_pago()
pago3.procesar_pago()

#Mostrar
pago1.mostrar_detalles()
pago2.mostrar_detalles()
pago3.mostrar_detalles()