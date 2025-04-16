class Estudiante:
    def __init__(self):
      self.__nota = 0

    def establecer_nota(self, nota):
        if 0 <= nota <= 5:
            self.__nota = nota
            print(f"Nota establecida: en {nota}.")
        else:
            print("Error: la nota debe estar entre 0 y 5.")
    def obtener_nota(self):
        return self.__nota

estudianteA = Estudiante()
estudianteA.establecer_nota(3.5)
print(f"Nota del estudiante: {estudianteA.obtener_nota()}")
estudianteA.establecer_nota(7)