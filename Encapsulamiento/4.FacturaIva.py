class Factura:
    def __init__(self, producto, precio, iva= 0.12):
        self.__producto = producto
        self.__precio = precio
        self.__iva = iva  #12 %

    def calcular_total(self):
        return self.__precio * (1 + self.__iva)

    def mostrar_detalles(self):
        print(f"Producto: {self.__producto}, Precio: ${self.__precio:.2f}, Total con IVA: ${self.calcular_total():.2f}")

# Ingresar producto y precio
producto = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio del producto: "))

# Crear factura y mostrar detalles
factura = Factura(producto, precio)
factura.mostrar_detalles()