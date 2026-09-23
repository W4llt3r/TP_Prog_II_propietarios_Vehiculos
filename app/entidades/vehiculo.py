class Vehiculo:
    #Solo objeto 
    def __init__(self, marca, modelo, patente, anio,
        propietario_id=None
                ):
        self.id = None
        self.marca = marca
        self.modelo = modelo
        self.patente = patente
        self.anio = anio
        self.propietario_id = propietario_id

    #Propiedades del Vehiculo
    #def set_marca(self, marca):
        # self.set_marca(marca) = marca
        # self.set_modelo(modelo) = modelo
        # self.set_patente(patente) = patente
        # self.set_anio(anio) = anio
        # self.set_propietario_id(propietario_id) = propietario_id

#     # ======================================
#     #               SETTERS
#     # ======================================

#     def set_marca(self, marca):
#         if not isinstance(marca, str):
#             raise TypeError("La marca debe ser texto")

#         if marca.strip() == "":
#             raise ValueError("La marca debe contener texto")

#         self.__marca = marca

#     def set_modelo(self, modelo):
#         if not isinstance(modelo, str):
#             raise TypeError("El modelo debe ser texto")

#         if modelo.strip() == "":
#             raise ValueError("El modelo debe contener texto")

#         self.__modelo = modelo

#     def set_patente(self, patente):
#         if not isinstance(patente, str):
#             raise TypeError("La patente debe ser letras y numeros")

#         if patente.strip() == "":
#             raise ValueError("La patente debe contener letras y numeros")

#         if not patente.replace(" ", "").isalnum():
#             raise ValueError(
#                 "La patente solo puede contener letras y numeros."
#             )

#         self.__patente = patente

    # def set_anio(self, anio):
#         if not isinstance(anio, int):
#             raise TypeError("El año debe ser un número entero")

#         if anio.strip() == "":
#             raise ValueError("El año no puede estar vacio")
#         
#         if anio < 0:
#             raise ValueError("El año debe ser un número positivo entero")

    #     if anio <1970 and anio > 2027:
    #         raise ValueError("El año debe ser un número válido de modelo desde 1970 en  adelante hasta el año actual)")

    #     self.__anio = anio



    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.patente}"



    """
    Propuesta con property para la marca del vehiculo
    @marca.setter
    def marca(self, valor):

        if not isinstance(valor, str):
            raise ValueError("La marca debe ser texto.")

        valor = valor.strip()

        if not valor:
            raise ValueError("La marca no puede estar vacía.")

        if not valor.replace(" ", "").isalpha():
            raise ValueError(
                "La marca solo puede contener letras y espacios."
            )

        self.__marca = valor
    """


# from errores import LibroNoDisponibleError

# class Libro:
#     def __init__(self, titulo, autor, isbn):
#         self.set_titulo(titulo)
#         self.set_autor(autor)
#         self.set_isbn(isbn)

#         self.__disponible = True
#         self.__prestado_a = None

#     # ======================================
#     #               SETTERS
#     # ======================================

#     def set_titulo(self, titulo):
#         if not isinstance(titulo, str):
#             raise TypeError("El titulo debe ser texto")

#         if titulo.strip() == "":
#             raise ValueError("Titulo vacio")

#         self.__titulo = titulo

#     def set_autor(self, autor):
#         if not isinstance(autor, str):
#             raise TypeError("El autor debe ser texto")

#         if autor.strip() == "":
#             raise ValueError("Autor vacio")

#         self.__autor = autor

#     def set_isbn(self, isbn):
#         if not isinstance(isbn, str):
#             raise TypeError("El ISBN debe ser texto")

#         if isbn.strip() == "":
#             raise ValueError("ISBN vacio")

#         if not isbn.isdigit():
#             raise ValueError("El ISBN debe contener solo numeros")

#         if len(isbn) != 13 :
#             raise ValueError("El ISBN debe tener 13 numeros")

#         self.__isbn = isbn

#     # ======================================
#     #               GETTERS
#     # ======================================

#     def get_titulo(self):
#         return self.__titulo

#     def get_autor(self):
#         return self.__autor

#     def get_isbn(self):
#         return self.__isbn

#     def get_disponible(self):
#         return self.__disponible

#     def get_prestado_a(self):
#         return self.__prestado_a

#     # ======================================
#     #               METODOS
#     # ======================================

#     def prestar(self, miembro):
#         if not self.__disponible:
#             raise LibroNoDisponibleError(
#                 self.__titulo
#             )

#         self.__disponible = False
#         self.__prestado_a = miembro

#     def devolver(self):
#         self.__disponible = True
#         self.__prestado_a = None

#     # ======================================
#     #               STR
#     # ======================================

#     def __str__(self):
#         estado = "Disponible"

#         if not self.__disponible:
#             estado = (
#                 f"Prestado a "
#                 f"{self.__prestado_a.get_nombre()}"
#             )

#         return (
#             f"Titulo: {self.__titulo} | "
#             f"Autor: {self.__autor} | "
#             f"ISBN: {self.__isbn} | "
#             f"Estado: {estado}"
#         )