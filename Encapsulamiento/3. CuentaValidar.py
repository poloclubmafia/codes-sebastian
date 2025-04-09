class Cuenta:
    def __init__(self, usuario, contrasena):
        self.usuario = usuario
        self.contrasena = contrasena

    def validar_acceso(self, usuario, contrasena):
        return self.usuario == usuario and self.__contrasena == contrasena

    def mostrar_usuario(self):
        return self.usuario


cuenta = Cuenta("usuario123", "segura123")


intentos = [
    ("usuario123", "segura123"),  # Correcto
    ("usuario123", "incorrecta"),  # Incorrecto
    ("otroUsuario", "segura123")   # Incorrecto
]

for usuario, contrasena in intentos:
    if cuenta.validar_acceso(usuario, contrasena):
        print(f"Acceso concedido para {cuenta.mostrar_usuario()}.")
    else:
        print("Acceso denegado.")
        