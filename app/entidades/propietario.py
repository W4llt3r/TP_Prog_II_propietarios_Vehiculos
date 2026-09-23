class Propietario: 
    """ Representa un propietario dentro del sistema. """ 
    def __init__(self, nombre, apellido, dni, telefono): 
        self.id = None 
        self.nombre = nombre 
        self.apellido = apellido 
        self.dni = dni 
        self.telefono = telefono 

    def __str__(self):
        return f"{self.nombre} {self.apellido}"