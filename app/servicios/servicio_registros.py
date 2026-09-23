class ServicioRegistros:

    def __init__(
        self,
        repositorio_vehiculos,
        repositorio_propietarios
    ):
        self.repositorio_vehiculos = repositorio_vehiculos
        self.repositorio_propietarios = repositorio_propietarios

    # ==========================================================
    # CREAR
    # ==========================================================

    def crear_propietario(self, propietario):
        return self.repositorio_propietarios.crear(propietario)

    def crear_vehiculo(self, vehiculo):
        return self.repositorio_vehiculos.crear(vehiculo)

    def crear_registro_completo(
        self,
        vehiculo,
        propietario
    ):
        propietario = self.repositorio_propietarios.crear(
            propietario
        )

        vehiculo.propietario_id = propietario.id

        vehiculo = self.repositorio_vehiculos.crear(
            vehiculo
        )

        return vehiculo, propietario

    # ==========================================================
    # ACTUALIZAR
    # ==========================================================

    def actualizar_vehiculo(self, vehiculo):
        return self.repositorio_vehiculos.actualizar(
            vehiculo
        )

    def actualizar_propietario(self, propietario):
        return self.repositorio_propietarios.actualizar(
            propietario
        )

    # ==========================================================
    # OBTENER REGISTROS COMPLETOS
    # ==========================================================

    def obtener_registros_completos(self):

        resultado = []

        vehiculos = self.repositorio_vehiculos.obtener_todos()

        propietarios = self.repositorio_propietarios.obtener_todos()

        for vehiculo in vehiculos:

            propietario_encontrado = None

            for propietario in propietarios:

                if propietario.id == vehiculo.propietario_id:

                    propietario_encontrado = propietario

                    break

            resultado.append(
                {
                    "vehiculo": vehiculo,
                    "propietario": propietario_encontrado
                }
            )

        return resultado

    # ==========================================================
    # ELIMINAR
    # ==========================================================

    def eliminar_registro_completo(self, registro):

        vehiculo = registro["vehiculo"]

        propietario = registro["propietario"]

        self.repositorio_vehiculos.eliminar(
            vehiculo.id
        )

        if propietario is not None:

            self.repositorio_propietarios.eliminar(
                propietario.id
            )






"""
class ServicioRegistros: 
    
    def __init__( self, repositorio_vehiculos, repositorio_propietarios ): 
        self.repositorio_vehiculos = repositorio_vehiculos 
        self.repositorio_propietarios = repositorio_propietarios 

    #CREAR # ================================================== 
    def crear_propietario(self, propietario): 
        return self.repositorio_propietarios.crear(propietario) 

    def crear_vehiculo(self, vehiculo): 
        return self.repositorio_vehiculos.crear(vehiculo) 

    def crear_registro_completo( self, vehiculo, propietario ):
    
        propietario = self.repositorio_propietarios.crear( propietario )
        
        vehiculo.propietario_id = propietario.id
        
        vehiculo = self.repositorio_vehiculos.crear( vehiculo ) 

        return vehiculo, propietario 
    
    #ACTUALIZAR # ================================================== 
    def actualizar_vehiculo(self, vehiculo): 
        return self.repositorio_vehiculos.actualizar( vehiculo ) 

    def actualizar_propietario(self, propietario): 
        return self.repositorio_propietarios.actualizar( propietario ) 

    #OBTENER REGISTROS COMPLETOS # ================================================== 
    def obtener_registros_completos(self): 
        resultado = [] 
        vehiculos = self.repositorio_vehiculos.obtener_todos() 
        propietarios = self.repositorio_propietarios.obtener_todos() 
        for vehiculo in vehiculos: 
            propietario_encontrado = None 
            for propietario in propietarios: 
                if propietario.id == vehiculo.propietario_id: 
                    propietario_encontrado = propietario 
                    break 
                resultado.append({ "vehiculo": vehiculo, "propietario": propietario_encontrado }) 
            return resultado 
    #ELIMINAR # ================================================== 
    def eliminar_registro_completo(self, registro): 
        vehiculo = registro["vehiculo"] 
        propietario = registro["propietario"] 
        self.repositorio_vehiculos.eliminar( vehiculo.id ) 
        if propietario is not None: 
            self.repositorio_propietarios.eliminar( propietario.id )
"""



#######################Archivo anterior a la modificacion 
# class ServicioRegistros:

#     def __init__(self,     
#                 repositorio_vehiculos, repositorio_propietarios):
#         self.repositorio_vehiculos = repositorio_vehiculos
#         self.repositorio_propietarios = repositorio_propietarios

#     def crear_propietario(self, propietario):
#         return self.repositorio_propietarios.crear(propietario)

#     def crear_vehiculo(self, vehiculo):
#         return self.repositorio_vehiculos.crear(vehiculo)
    
#     def actualizar_vehiculo(self, vehiculo): 
#         return self.repositorio_vehiculos.actualizar(vehiculo) 

#     def actualizar_propietario(self, propietario):
#         return self.repositorio_propietarios.actualizar(propietario)

#     def crear_registro_completo(self, 
#                                 vehiculo,         propietario):
#         propietario = self.repositorio_propietarios.crear(propietario)
#         vehiculo.propietario_id = propietario.id
#         vehiculo = self.repositorio_vehiculos.crear(vehiculo)

#         return vehiculo, propietario

#     def obtener_registros_completos(self):

#         resultado = []
#         vehiculos = self.repositorio_vehiculos.obtener_todos()
#         propietarios = self.repositorio_propietarios.obtener_todos()

#         for vehiculo in vehiculos:
#             propietario = None
#             for propietario in propietarios:

#                 if propietario.id == vehiculo.propietario_id:
#                     propietario = propietario
#                     break

#             resultado.append({
#                 "vehiculo": vehiculo,
#                 "propietario": propietario
#             })

#         return resultado

#     def eliminar_registro_completo(self, registro):

#         vehiculo = registro["vehiculo"]
#         propietario = registro["propietario"]

#         self.repositorio_vehiculos.eliminar(vehiculo.id)

#         if propietario is not None:
#             self.repositorio_propietarios.eliminar(propietario.id)