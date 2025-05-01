from datetime import date

# Superclase Persona
class Persona:
    def __init__(self, nombre: str, nif: str, fecha_nac: date):
        self.nombre = nombre
        self.nif = nif
        self.fecha_nac = fecha_nac

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"NIF: {self.nif}")
        print(f"Fecha de nacimiento: {self.fecha_nac}")

# Subclase Jugador
class Jugador(Persona):
    def __init__(self, nombre: str, nif: str, fecha_nac: date, num_fed: int):
        super().__init__(nombre, nif, fecha_nac)
        self.num_fed = num_fed

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Número de Federación: {self.num_fed}")


