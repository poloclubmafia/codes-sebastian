class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    def mostrar_info(self):
        print(f"Nombre:{self.__nombre}")
        print(f"Edad:{self.__edad}")

pers1 = Persona("Sebastian", 21)

pers1.mostrar_info()