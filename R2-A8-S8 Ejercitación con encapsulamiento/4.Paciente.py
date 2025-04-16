class Paciente:
    def __init__(self):
        self.__nombre = ""
        self.__edad = 0
        self.__historial_medico = []

  
    def establecer_nombre(self, nombre):
        self.__nombre = nombre

    def obtener_nombre(self):
        return self.__nombre


    def establecer_edad(self, edad):
        if edad > 0:
            self.__edad = edad
        else:
            print("Error: la edad debe ser un número positivo.")

    def obtener_edad(self):
        return self.__edad

    
    def agregar_diagnostico(self, diagnostico):
        self.__historial_medico.append(diagnostico)

    def obtener_historial_medico(self):
        return self.__historial_medico


#paciente
paciente1 = Paciente()


paciente1.establecer_nombre("Sebastian Negrette")
paciente1.establecer_edad(21)

paciente1.establecer_edad(-10)


paciente1.agregar_diagnostico("Altos niveles de azucar en la sangre")
paciente1.agregar_diagnostico("Mala circulación")


print(f"Nombre: {paciente1.obtener_nombre()}")
print(f"Edad: {paciente1.obtener_edad()}")
print("Historial médico:", paciente1.obtener_historial_medico())