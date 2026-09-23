class RepositorioMemoria: 
    """ Simula un repositorio temporal en memoria. """ 
    def __init__(self): 
        self._datos = [] 
        self._ultimo_id = 0 

    def crear(self, objeto): 
        self._ultimo_id += 1 
        objeto.id = self._ultimo_id 
        self._datos.append(objeto) 
        return objeto 

    def obtener_todos(self): 
        return self._datos 

    def actualizar(self, objeto): 
        for indice, elemento in enumerate( self._datos ): 
            if elemento.id == objeto.id: 
                self._datos[indice] = objeto 
                return objeto 
            
        return None 

    def eliminar(self, id_objeto): 
        for elemento in self._datos: 
            if elemento.id == id_objeto: 
                self._datos.remove(elemento) 
                return True 
            
        return False