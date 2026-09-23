from tkinter import ttk 

class SelectorEntidad(ttk.Frame): 
    def __init__( self, parent, al_seleccionar, titulo="¿Qué desea crear?" ): 
        super().__init__(parent) 
        self.al_seleccionar = al_seleccionar 
        self.titulo = titulo 
        self.crear_interfaz() 

    def crear_interfaz(self): 
        titulo = ttk.Label( self, text=self.titulo, font=("Arial", 18, "bold") ) 
        titulo.pack(pady=30) 
        boton_vehiculo = ttk.Button( 
                                    self, text="Vehículo", 
                                    command=lambda: self.al_seleccionar( "vehiculo" ) 
                                    ) 
        boton_vehiculo.pack(pady=10) 
        boton_propietario = ttk.Button( self, text="Propietario", 
                                        command=lambda: self.al_seleccionar( "propietario" ) ) 
        boton_propietario.pack(pady=10)


