class Estudiante:
    def __init__(self, nombre, edad,):
        self.__nombre = nombre
        self.__edad = edad
        self.__notas = []

    def agregar_nota(self, nota):
        if nota < 1 or nota > 5:
            self.__notas.append(nota)
        else:
            print("Nota fuera de rango, digita una nota entre 1 y 5")

    def obtener_promedio(self):
        if self.__notas:
            return sum(self.__notas) / len(self.__notas)
        else:
            return 0

    def mostrar_datos(self):
        print(f"Nombre: {self.__nombre}")
        print(f"Edad: {self.__edad}")
        print(f" Promedio: {self.obtener_promedio()}")

est1 = Estudiante("Juan", 20)
est2 = Estudiante("María", 22)
est3 = Estudiante("Carlos", 19)

est1.agregar_nota(8)
est1.agregar_nota(9)
est2.agregar_nota(7)
est2.agregar_nota(10)
est3.agregar_nota(6)
est3.agregar_nota(8)

est1.mostrar_datos()
est2.mostrar_datos()
est3.mostrar_datos()