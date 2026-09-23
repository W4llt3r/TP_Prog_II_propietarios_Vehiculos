import tkinter as tk 
from tkinter import messagebox 
from app.interfaz.dashboard import Dashboard 
from app.interfaz.selector_entidad import SelectorEntidad 
from app.interfaz.formulario_dinamico import FormularioDinamico 
from app.entidades.vehiculo import Vehiculo 
from app.entidades.propietario import Propietario 

class Aplicacion: 
    def __init__(self, servicio): 
        self.servicio = servicio 
        self.root = tk.Tk() 
        self.root.title( "Sistema de Gestión de Vehículos" ) 
        self.root.geometry( "1200x650" ) 

        #PANTALLA # ========================================== 
        self.pantalla_actual = None 

        #DATOS TEMPORALES DE CREACIÓN # ========================================== 
        self.vehiculo_temporal = None 
        self.propietario_temporal = None 

        #DATOS DE ACTUALIZACIÓN # ========================================== 
        self.registro_en_actualizacion = None 
        self.vehiculo_actualizado_temporal = None 
        self.propietario_actualizado_temporal = None 

        #INICIAR # ========================================== 
        self.mostrar_dashboard() 

    #LIMPIAR PANTALLA # ================================================== 
    def limpiar_pantalla(self): 
        if self.pantalla_actual is not None: 
            self.pantalla_actual.destroy() 

    #DASHBOARD # ================================================== 
    def mostrar_dashboard(self): 
        self.limpiar_pantalla() 
        self.pantalla_actual = Dashboard( self.root, self.servicio, 
                                        self.mostrar_selector, 
                                        self.iniciar_actualizacion, 
                                        self.eliminar_registro ) 
        self.pantalla_actual.pack( fill="both", expand=True ) 

    #CREAR # ================================================== 
    def mostrar_selector(self): 
        self.limpiar_pantalla() 
        self.pantalla_actual = SelectorEntidad( self.root, 
                                                self.seleccionar_entidad, 
                                                titulo="¿Qué desea crear?" ) 
        self.pantalla_actual.pack( fill="both", expand=True ) 

    #SELECCIONAR ENTIDAD # ================================================== 
    def seleccionar_entidad(self, entidad): 
        if entidad == "vehiculo": 
            self.mostrar_formulario_vehiculo_inicial() 
        elif entidad == "propietario": 
            self.mostrar_formulario_propietario_inicial()
    
    # Para probar la llegada de la info   
    # def seleccionar_entidad(self, entidad):
    #     if entidad == "vehiculo":
    #         print("Usuario eligió VEHÍCULO")
    #     elif entidad == "propietario":
    #         print("Usuario eligió PROPIETARIO")

    #CREAR DESDE VEHÍCULO # ================================================== 
    def mostrar_formulario_vehiculo_inicial(self): 
        campos = { "marca": "Marca", "modelo": "Modelo", 
                    "patente": "Patente", "anio": "Año" 
                    } 
        self.limpiar_pantalla() 
        self.pantalla_actual = FormularioDinamico( self.root, 
                                                    "Crear Vehículo", 
                                                    campos, 
                                                    Vehiculo, self.guardar_vehiculo_inicial 
                                                    ) 
        self.pantalla_actual.pack( fill="both", expand=True ) 

    #Guardar vehículo temporal y mostrar formulario de propietario final
    def guardar_vehiculo_inicial(self, vehiculo): 
        self.vehiculo_temporal = vehiculo 
        self.mostrar_formulario_propietario_final() 

    def mostrar_formulario_propietario_final(self): 
        campos = { "nombre": "Nombre", "apellido": "Apellido", 
                    "dni": "DNI", "telefono": "Teléfono" 
                    } 
        self.limpiar_pantalla() 
        self.pantalla_actual = FormularioDinamico( self.root, 
                                                    "Crear Propietario", 
                                                    campos, Propietario, 
                                                    self.finalizar_desde_vehiculo 
                                                    ) 
        self.pantalla_actual.pack( fill="both", expand=True ) 

    #Salir desde el formulario de propietario final y crear registro completo
    def finalizar_desde_vehiculo(self, propietario): 
        self.propietario_temporal = propietario 
        self.servicio.crear_registro_completo( self.vehiculo_temporal, 
                                                self.propietario_temporal ) 
        messagebox.showinfo( "Operación exitosa", 
                            "Vehículo y propietario creados correctamente." 
                            ) 
        self.vehiculo_temporal = None 
        self.propietario_temporal = None 
        self.mostrar_dashboard()

    #CREAR DESDE PROPIETARIO # ================================================== 
    def mostrar_formulario_propietario_inicial(self): 
        campos = { 
                    "nombre": "Nombre", "apellido": "Apellido", 
                    "dni": "DNI", "telefono": "Teléfono" 
                } 
        self.limpiar_pantalla() 
        self.pantalla_actual = FormularioDinamico(  self.root, 
                                                    "Crear Propietario", 
                                                    campos, Propietario, 
                                                    self.guardar_propietario_inicial 
                                                    ) 
        self.pantalla_actual.pack( fill="both", expand=True ) 

    #Guardar propietario temporal y mostrar formulario de vehículo final
    def guardar_propietario_inicial(self, propietario): 
        self.propietario_temporal = propietario 
        self.mostrar_formulario_vehiculo_final() 

    def mostrar_formulario_vehiculo_final(self): 
        campos = {  "marca": "Marca", "modelo": "Modelo", "patente": "Patente", "anio": "Año" 
                    } 
        self.limpiar_pantalla() 
        self.pantalla_actual = FormularioDinamico(  self.root, "Crear Vehículo", 
                                                    campos, Vehiculo, 
                                                    self.finalizar_desde_propietario 
                                                    ) 
        self.pantalla_actual.pack( fill="both", expand=True ) 

    #Salir desde el formulario de vehículo final y crear registro completo
    def finalizar_desde_propietario(self, vehiculo): 
        self.vehiculo_temporal = vehiculo 
        self.servicio.crear_registro_completo(  self.vehiculo_temporal, 
                                                self.propietario_temporal 
                                                ) 
        messagebox.showinfo( "Operación exitosa", 
                            "Propietario y vehículo creados correctamente." 
                            ) 
        self.vehiculo_temporal = None 
        self.propietario_temporal = None 
        self.mostrar_dashboard() 

    #Selector ACTUALIZAR

    #INICIAR ACTUALIZACIÓN # ================================================== 
    def iniciar_actualizacion(self, registro): 
        self.registro_en_actualizacion = registro 
        # self.vehiculo_actualizado_temporal = None 
        # self.propietario_actualizado_temporal = None 
        self.mostrar_selector_actualizar() 

    #SELECTOR DE ACTUALIZACIÓN # ================================================== 
    def mostrar_selector_actualizar(self): 
        self.limpiar_pantalla() 
        self.pantalla_actual = SelectorEntidad( self.root, 
                                                self.seleccionar_entidad_actualizar, titulo="¿Qué desea actualizar?" ) 
        self.pantalla_actual.pack( fill="both", expand=True ) 

    # def seleccionar_entidad_actualizar( self, entidad ): 
    #     if entidad == "vehiculo": 
    #         self.mostrar_formulario_vehiculo_actualizar() 
    #     elif entidad == "propietario": 
    #         self.mostrar_formulario_propietario_actualizar() 

    def seleccionar_entidad_actualizar( self, entidad ): 
        if entidad == "vehiculo": 
            self.mostrar_formulario_vehiculo_actualizar() 
        elif entidad == "propietario": 
            self.mostrar_formulario_propietario_actualizar()

            #self.finalizar_actualizacion_desde_propietario se encontraba dentro de mostrar_formulario_propietario_actualizar, pero lo moví a la función seleccionar_entidad_actualizar para que se ejecute después de seleccionar "propietario" y no antes. Esto permite que se muestre el formulario de actualización del propietario antes de finalizar la actualización desde el propietario.


    #ACTUALIZAR VEHÍCULO # ================================================== 
    def mostrar_formulario_vehiculo_actualizar(self): 
        campos = {  "marca": "Marca", "modelo": "Modelo", 
                    "patente": "Patente", "anio": "Año" 
                    } 
        vehiculo = ( self.registro_en_actualizacion["vehiculo"] ) 
        self.limpiar_pantalla() 
        self.pantalla_actual = FormularioDinamico(  self.root, "Actualizar Vehículo", 
                                                    campos, Vehiculo, self.guardar_vehiculo_actualizado, texto_boton="Actualizar", objeto_existente=vehiculo ) 
        self.pantalla_actual.pack( fill="both", expand=True ) 

    # def guardar_vehiculo_actualizado( self, vehiculo ): 
    #     self.vehiculo_actualizado_temporal = vehiculo 
    #     self.mostrar_formulario_propietario_actualizar() 

    def guardar_vehiculo_actualizado( self, vehiculo ): 
        self.vehiculo_actualizado_temporal = vehiculo 
        self.mostrar_formulario_propietario_actualizar()

    #ACTUALIZAR PROPIETARIO # ================================================== 
    
    # Script actualizado para mostrar el formulario de actualización del propietario y finalizar la actualización desde el propietario después de seleccionar "propietario" en el selector de actualización.


    # def mostrar_formulario_propietario_actualizar( self, al_finalizar=None ): 
    #     campos = { "nombre": "Nombre", "apellido": "Apellido", "dni": "DNI", "telefono": "Teléfono" } 
    #     propietario = ( self.registro_en_actualizacion["propietario"] ) 
    #     if al_finalizar is None: 
    #         al_finalizar = ( self.finalizar_actualizacion_desde_vehiculo ) 
    #         self.limpiar_pantalla() 
    #         self.pantalla_actual = FormularioDinamico( self.root, 
    #                                                     "Actualizar Propietario",
    #                                                     campos, Propietario, 
    #                                                     al_finalizar, texto_boton="Actualizar", 
    #                                                     objeto_existente=propietario ) 
    #         self.pantalla_actual.pack( fill="both", expand=True )


    def mostrar_formulario_propietario_actualizar(self):
        propietario = self.registro_en_actualizacion["propietario"]
        campos = {
                    "nombre": "Nombre",
                    "apellido": "Apellido",
                    "dni": "DNI",
                    "telefono": "Teléfono"
                }
        self.limpiar_pantalla()

        self.pantalla_actual = FormularioDinamico(
                                self.root,
                                "Actualizar Propietario",
                                campos,
                                Propietario,
                                self.finalizar_actualizacion_propietario,
                                texto_boton="Actualizar",
                                objeto_existente=propietario
                                )

        self.pantalla_actual.pack(
                    fill="both",
                    expand=True
                        )

    def finalizar_actualizacion_desde_vehiculo( self, propietario ): 
        self.propietario_actualizado_temporal = propietario 
        self.guardar_actualizacion_completa() 

#ACTUALIZAR DESDE PROPIETARIO # ==================================================


    def mostrar_formulario_vehiculo_actualizar_desde_propietario( self ): 
        campos = { "marca": "Marca", "modelo": "Modelo", 
                "patente": "Patente", "anio": "Año" 
                } 
        vehiculo = ( self.registro_en_actualizacion["vehiculo"] ) 
        self.limpiar_pantalla() 
        self.pantalla_actual = FormularioDinamico(  
                            self.root, "Actualizar Vehículo", 
                            campos, Vehiculo, 
                            self.finalizar_actualizacion_desde_propietario, 
                            texto_boton="Actualizar", 
                            objeto_existente=vehiculo 
                            ) 
        self.pantalla_actual.pack( fill="both", expand=True ) 


    def mostrar_formulario_vehiculo_actualizar(self):

        vehiculo = self.registro_en_actualizacion["vehiculo"]
        campos = {
            "marca": "Marca",
            "modelo": "Modelo",
            "patente": "Patente",
            "anio": "Año"
            }

        self.limpiar_pantalla()

        self.pantalla_actual = FormularioDinamico(
                                self.root,
                                "Actualizar Vehículo",
                                campos,
                                Vehiculo,
                                self.finalizar_actualizacion_vehiculo,
                                texto_boton="Actualizar",
                                objeto_existente=vehiculo
                                )

        self.pantalla_actual.pack(
            fill="both",
            expand=True
            )

    def finalizar_actualizacion_vehiculo(self, vehiculo):

        self.servicio.actualizar_vehiculo(
                                vehiculo
                                    )

        messagebox.showinfo(
            "Actualización exitosa",
            "Los datos del vehículo fueron actualizados correctamente."
            )

        self.registro_en_actualizacion = None

        self.mostrar_dashboard()



    # def guardar_propietario_actualizado( self, propietario ): 
    #   self.propietario_actualizado_temporal = propietario 
    #   self.mostrar_formulario_vehiculo_actualizar_desde_propietario() 
    
    def guardar_propietario_actualizado( self, propietario ): 
        self.propietario_actualizado_temporal = propietario 
        self.mostrar_formulario_vehiculo_actualizar_desde_propietario()

    def finalizar_actualizacion_desde_propietario( self, vehiculo ): 
        self.vehiculo_actualizado_temporal = vehiculo 
        self.guardar_actualizacion_completa() 


    #GUARDAR ACTUALIZACIÓN COMPLETA # ================================================== 
    def guardar_actualizacion_completa(self): 
        if ( self.vehiculo_actualizado_temporal is None or self.propietario_actualizado_temporal is None ): 
            return 
        self.servicio.actualizar_vehiculo( self.vehiculo_actualizado_temporal ) 
        self.servicio.actualizar_propietario( self.propietario_actualizado_temporal ) 
        messagebox.showinfo( "Operación exitosa", 
                            "Vehículo y propietario actualizados correctamente." ) 
        self.registro_en_actualizacion = None 
        self.vehiculo_actualizado_temporal = None 
        self.propietario_actualizado_temporal = None 
        self.mostrar_dashboard() 

    def finalizar_actualizacion_vehiculo(self, vehiculo):
        self.servicio.actualizar_vehiculo(
                                        vehiculo
                                        )

        messagebox.showinfo(
                    "Actualización exitosa",
                    "Los datos del vehículo fueron actualizados correctamente."
                            )

        self.registro_en_actualizacion = None

        self.mostrar_dashboard()

    def finalizar_actualizacion_propietario(self, propietario):

        self.servicio.actualizar_propietario(
                                            propietario
                                            )
        messagebox.showinfo(
                    "Actualización exitosa",
                    "Los datos del propietario fueron actualizados correctamente."
                            )
        self.registro_en_actualizacion = None
        self.mostrar_dashboard()

#ELIMINAR # ================================================== 
    def eliminar_registro(self, registro): 
        self.servicio.eliminar_registro_completo( registro ) 
        messagebox.showinfo( "Operación exitosa", "Vehículo y propietario eliminados correctamente." ) 
        self.mostrar_dashboard() 
#EJECUTAR # ================================================== 
    def ejecutar(self): 
        self.root.mainloop()




