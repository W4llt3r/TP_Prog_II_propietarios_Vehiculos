from tkinter import ttk, messagebox

class FormularioDinamico(ttk.Frame): 
    def __init__( self, parent, titulo, campos, clase_entidad, al_guardar, texto_boton="Crear", objeto_existente=None ): 
        super().__init__(parent) 
        self.titulo = titulo 
        self.campos = campos 
        self.clase_entidad = clase_entidad 
        self.al_guardar = al_guardar 
        self.texto_boton = texto_boton 
        self.objeto_existente = objeto_existente 
        self.entries = {} 
        self.crear_interfaz() 

    def crear_interfaz(self): 
        titulo = ttk.Label( self, text=self.titulo, font=("Arial", 18, "bold") ) 
        titulo.pack(pady=20) 

    #GENERAR CAMPOS DINÁMICAMENTE # ========================================== 
        for nombre_campo, texto_campo in self.campos.items(): 
            label = ttk.Label( self, text=texto_campo ) 
            label.pack(pady=5) 
            entry = ttk.Entry(self) 
            entry.pack(pady=5) 

    #PRECARGAR DATOS PARA ACTUALIZACIÓN # ====================================== 
            if self.objeto_existente is not None: 
                valor_existente = getattr( self.objeto_existente, nombre_campo ) 
                entry.insert( 0, str(valor_existente) ) 
            self.entries[nombre_campo] = entry 

    #BOTÓN # ========================================== 
        boton = ttk.Button(
                    self, text=self.texto_boton,
                    command=self.obtener_datos 
                    ) 
        boton.pack(pady=20) 

    def obtener_datos(self): 
        datos = {} 

    #OBTENER DATOS # ========================================== 
        for nombre_campo, entry in self.entries.items(): 
            valor = entry.get().strip() 
            datos[nombre_campo] = valor 

    #VALIDAR # ========================================== 
    
        if not all(datos.values()): 
            messagebox.showwarning( "Datos incompletos", 
                                    "Debe completar todos los campos." ) 
            return 

    #CREAR OBJETO # ========================================== 
        objeto = self.clase_entidad(**datos) 

    #CONSERVAR ID # ========================================== 
        if self.objeto_existente is not None: 
            objeto.id = self.objeto_existente.id 

    # El vehículo tiene una relación con el propietario. 
            if hasattr( self.objeto_existente, "propietario_id" ): 
                objeto.propietario_id = ( self.objeto_existente.propietario_id ) 
    #ENVIAR OBJETO A APLICACION # ========================================== 
        self.al_guardar(objeto)



