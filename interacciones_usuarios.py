# Simulación de interacciones entre usuarios

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

    def crear_cliente(self, nombre_cliente):
        print(f"{self.nombre} ha creado un nuevo cliente: {nombre_cliente}")

    def actualizar_cliente(self, nombre_cliente):
        print(f"{self.nombre} ha actualizado la información del cliente: {nombre_cliente}")

    def consultar_cliente(self, nombre_cliente):
        print(f"{self.nombre} ha consultado la información del cliente: {nombre_cliente}")

# Creación de los usuarios ficticios
usuario1 = Usuario("Juan_Garcia")
usuario2 = Usuario("Pedro_Mendez")

# Simulación de acciones
usuario1.crear_cliente("Cliente1")
usuario2.actualizar_cliente("Cliente1")
usuario1.consultar_cliente("Cliente1")
