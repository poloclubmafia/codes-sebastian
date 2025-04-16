class Inventario:
    def __init__(self):
        self.__cantidad = 0

    def agregar(self, unidades):
      if unidades > 0:
        self.__cantidad += unidades
        print(f"Se agregaron {unidades} unidades al inventario.")
      else:
        print("Error: la cantidad que va a agregar debe ser mayor que cero.")

    def retirar(self, unidades):
        if unidades > self.__cantidad:
            print("Error: No hay suficientes unidades para retirar.")
        elif unidades <= 0:
            print("Error: La cantidad a retirar debe ser mayor que cero.")
        else:
            self.__cantidad -= unidades
            print(f"Se retiraron {unidades} unidades.")

    def consultar_cantidad(self):
        return self.__cantidad

inventario = Inventario()
inventario.agregar(200)
print(f"Cantidad actual: {inventario.consultar_cantidad()}")

inventario.retirar(100)
print(f"Cantidad en inventario: {inventario.consultar_cantidad()}")

inventario.retirar(200)
