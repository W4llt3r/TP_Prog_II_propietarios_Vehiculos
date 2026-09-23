from tkinter import ttk, messagebox


class Dashboard(ttk.Frame):

    def __init__(
        self,
        parent,
        servicio,
        al_crear,
        al_actualizar,
        al_eliminar
    ):
        super().__init__(parent)

        self.servicio = servicio
        self.al_crear = al_crear
        self.al_actualizar = al_actualizar
        self.al_eliminar = al_eliminar

        self.registro_seleccionado = None

        # Primero construimos la interfaz
        self.crear_interfaz()

        # Después cargamos los datos
        self.cargar_datos()

    # ==========================================================
    # CREAR INTERFAZ
    # ==========================================================

    def crear_interfaz(self):

        titulo = ttk.Label(
            self,
            text="Sistema de Gestión de Vehículos",
            font=("Arial", 18, "bold")
        )

        titulo.pack(pady=20)

        # ------------------------------------------------------
        # CONTENEDOR DE LA TABLA
        # ------------------------------------------------------

        contenedor_tabla = ttk.Frame(self)

        contenedor_tabla.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        # ------------------------------------------------------
        # COLUMNAS
        # ------------------------------------------------------

        columnas = (
            "id_vehiculo",
            "marca",
            "modelo",
            "patente",
            "anio",
            "id_propietario",
            "nombre",
            "apellido",
            "dni",
            "telefono"
        )

        # ------------------------------------------------------
        # TREEVIEW
        # ------------------------------------------------------

        self.tabla = ttk.Treeview(
            contenedor_tabla,
            columns=columnas,
            show="headings"
        )

        encabezados = {
            "id_vehiculo": "ID Vehículo",
            "marca": "Marca",
            "modelo": "Modelo",
            "patente": "Patente",
            "anio": "Año",
            "id_propietario": "ID Propietario",
            "nombre": "Nombre",
            "apellido": "Apellido",
            "dni": "DNI",
            "telefono": "Teléfono"
        }

        for columna in columnas:

            self.tabla.heading(
                columna,
                text=encabezados[columna]
            )

            self.tabla.column(
                columna,
                width=110,
                anchor="center"
            )

        # ------------------------------------------------------
        # SCROLLBAR
        # ------------------------------------------------------

        scrollbar_vertical = ttk.Scrollbar(
            contenedor_tabla,
            orient="vertical",
            command=self.tabla.yview
        )

        self.tabla.configure(
            yscrollcommand=scrollbar_vertical.set
        )

        self.tabla.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar_vertical.pack(
            side="right",
            fill="y"
        )

        # ------------------------------------------------------
        # DETECTAR SELECCIÓN
        # ------------------------------------------------------

        self.tabla.bind(
            "<<TreeviewSelect>>",
            self.seleccionar_registro
        )

        # ------------------------------------------------------
        # BOTONES
        # ------------------------------------------------------

        contenedor_botones = ttk.Frame(self)

        contenedor_botones.pack(pady=20)

        self.boton_crear = ttk.Button(
            contenedor_botones,
            text="Crear",
            command=self.al_crear
        )

        self.boton_actualizar = ttk.Button(
            contenedor_botones,
            text="Actualizar",
            command=self.actualizar
        )

        self.boton_eliminar = ttk.Button(
            contenedor_botones,
            text="Eliminar",
            command=self.eliminar
        )

        self.boton_limpiar = ttk.Button(
            contenedor_botones,
            text="Limpiar",
            command=self.limpiar_seleccion
        )

        self.boton_crear.pack(
            side="left",
            padx=5
        )

        self.boton_actualizar.pack(
            side="left",
            padx=5
        )

        self.boton_eliminar.pack(
            side="left",
            padx=5
        )

        self.boton_limpiar.pack(
            side="left",
            padx=5
        )

    # ==========================================================
    # CARGAR DATOS
    # ==========================================================

    def cargar_datos(self):

        # Limpiar tabla antes de cargar
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        registros = self.servicio.obtener_registros_completos()

        for registro in registros:
            vehiculo = registro["vehiculo"]
            propietario = registro["propietario"]

            if propietario is not None:
                valores = (
                    vehiculo.id,
                    vehiculo.marca,
                    vehiculo.modelo,
                    vehiculo.patente,
                    vehiculo.anio,
                    propietario.id,
                    propietario.nombre,
                    propietario.apellido,
                    propietario.dni,
                    propietario.telefono
                )

            else:

                valores = (
                    vehiculo.id,
                    vehiculo.marca,
                    vehiculo.modelo,
                    vehiculo.patente,
                    vehiculo.anio,
                    "",
                    "",
                    "",
                    "",
                    ""
                )

            self.tabla.insert(
                "",
                "end",
                values=valores
            )

    # ==========================================================
    # SELECCIONAR REGISTRO
    # ==========================================================

    def seleccionar_registro(self, evento):
        seleccion = self.tabla.selection()

        if not seleccion:
            return

        item = seleccion[0]
        valores = self.tabla.item(
            item,
            "values"
        )

        id_vehiculo = int(valores[0])
        registros = self.servicio.obtener_registros_completos()

        for registro in registros:
            vehiculo = registro["vehiculo"]

            if vehiculo.id == id_vehiculo:
                self.registro_seleccionado = registro

                print("Registro seleccionado:")
                print(self.registro_seleccionado)

                break

    # ==========================================================
    # LIMPIAR SELECCIÓN
    # ==========================================================

    def limpiar_seleccion(self):
        seleccion = self.tabla.selection()

        if seleccion:
            self.tabla.selection_remove(seleccion)
        self.registro_seleccionado = None

        print("Selección limpiada")

    # ==========================================================
    # ACTUALIZAR
    # ==========================================================

    def actualizar(self):

        if self.registro_seleccionado is None:
            messagebox.showwarning(
                "Selección requerida",
                "Debe seleccionar un registro antes de actualizar."
            )
            return

        self.al_actualizar(
            self.registro_seleccionado
        )

    # ==========================================================
    # ELIMINAR
    # ==========================================================

    def eliminar(self):

        if self.registro_seleccionado is None:
            messagebox.showwarning(
                "Selección requerida",
                "Debe seleccionar un registro antes de eliminar."
            )
            return

        confirmar = messagebox.askyesno(
            "Confirmar eliminación",
            "¿Desea eliminar el vehículo y su propietario relacionado?"
        )

        if confirmar:
            self.al_eliminar(
                self.registro_seleccionado
            )


            
######################################
# from tkinter import ttk, messagebox 

# class Dashboard(ttk.Frame): 
#     def __init__( self, parent, servicio, al_crear, al_actualizar, al_eliminar ): 
#         super().__init__(parent) 
#         self.servicio = servicio 
#         self.al_crear = al_crear 
#         self.al_actualizar = al_actualizar 
#         self.al_eliminar = al_eliminar 
#         self.registro_seleccionado = None 
#         self.crear_interfaz() 
#         self.cargar_datos() 

#     #INTERFAZ # ================================================== 
#     def crear_interfaz(self): 
#         titulo = ttk.Label( self, text="Sistema de Gestión de Vehículos", font=("Arial", 18, "bold") ) 
#         titulo.pack(pady=20) 

#     #TABLA # ============================================== 
#         contenedor_tabla = ttk.Frame(self) 
#         contenedor_tabla.pack( fill="both", expand=True, padx=20, pady=10 ) 

#     #BOTONES # ============================================== 
#         contenedor_botones = ttk.Frame(self) 
#         contenedor_botones.pack( pady=20 ) 

#     #CARGAR DATOS # ================================================== 
#     def cargar_datos(self): 
#         for fila in self.tabla.get_children(): 
#             self.tabla.delete(fila) 

#     #SELECCIONAR # ================================================== 
#     def seleccionar_registro(self, evento): 
#         seleccion = self.tabla.selection() 
#         if not seleccion: 
#             return 

#     #ACTUALIZAR # ================================================== 
#     def actualizar(self): 
#         if self.registro_seleccionado is None: 
#             messagebox.showwarning( "Selección requerida", "Debe seleccionar un registro antes de actualizar." ) 
#             return 

#     #ELIMINAR # ================================================== 
#     def eliminar(self): 
#         if self.registro_seleccionado is None: 
#             messagebox.showwarning( "Selección requerida", "Debe seleccionar un registro antes de eliminar." ) 
#             return 

#     #LIMPIAR # ================================================== 
#     def limpiar_seleccion(self): 
#         seleccion = self.tabla.selection() 
#         if seleccion: 
#             self.tabla.selection_remove( seleccion ) 
#             self.registro_seleccionado = None 
#             self.boton_actualizar.config( state="disabled" ) 
#             self.boton_eliminar.config( state="disabled" )


