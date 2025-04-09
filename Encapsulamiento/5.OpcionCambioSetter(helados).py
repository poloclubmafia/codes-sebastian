class Helado:
    def __init__(self):
        self._sabor = "Vainilla"
        self._sabores_disponibles = ["Vainilla", "Fresa", "Galleta"]

    @property
    def sabor(self):
        return self._sabor

    @sabor.setter
    def sabor(self, nuevo_sabor):
        if nuevo_sabor in self._sabores_disponibles:
            self._sabor = nuevo_sabor
            print(f"Sabor cambiado a: {self._sabor}")
        else:
            print("Sabor no disponible. Elija entre: Vainilla, Fresa o Galleta.")

    def servir(self):
        print(f"Sirviendo un helado de {self._sabor} 🍦")


mi_helado = Helado()
mi_helado.servir()

# Cambiar con setter.
mi_helado.sabor = "Fresa"
mi_helado.servir()

mi_helado.sabor = "Galleta"
mi_helado.servir()

#sabor no valido.
mi_helado.sabor = "Chocolate"