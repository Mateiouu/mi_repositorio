class Persona():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def hablar(self):
        return f"Hola, me llamo {self.nombre} {self.apellido}"