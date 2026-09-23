# import tkinter as tk
# from tkinter import ttk, messagebox

# class InterfazCRUD:

#     def __init__(self, parent, titulo, campos,
#                 clase_entidad, repositorio
#                 ):

#         self.parent = parent
#         self.titulo = titulo
#         self.campos = campos
#         self.clase_entidad = clase_entidad
#         self.repositorio = repositorio

#         self.entries = {}
#         self.objeto_seleccionado = None

#         self.crear_interfaz()

#     def crear_interfaz(self):

#         self.frame = ttk.LabelFrame(
#         self.parent,
#         text=self.titulo,
#         padding=10
#         )

#         self.frame.pack(
#             fill="x",
#             padx=10,
#             pady=10
#         )

#         self.crear_formulario()
#         self.crear_botones()
#         self.crear_tabla()

#     def crear_formulario(self):

#         for fila, campo in enumerate(self.campos):

#             label = ttk.Label(
#                 self.frame,
#                 text=campo.capitalize()
#                 )

#             label.grid(
#                 row=fila,
#                 column=0,
#                 padx=5,
#                 pady=5,
#                 sticky="w"
#             )

#             entry = ttk.Entry(
#                 self.frame
#                 )

#             entry.grid(
#                 row=fila,
#                 column=1,
#                 padx=5,
#                 pady=5,
#                 sticky="ew"
#                 )

#             self.entries[campo] = entry

#     def crear_botones(self):

#         frame_botones = ttk.Frame(self.parent)

#         frame_botones.pack(
#             fill="x",
#             padx=10,
#             pady=5
#             )

#         botones = [
#             ("Crear", self.crear),
#             ("Actualizar", self.actualizar),
#             ("Eliminar", self.eliminar),
#             ("Limpiar", self.limpiar)
#             ]

#         for texto, comando in botones:

#             boton = ttk.Button(
#                 frame_botones,
#                 text=texto,
#                 command=comando
#                 )

#             boton.pack(
#                 side="left",
#                 padx=5
#                 )

#     def crear_tabla(self):

#         frame_tabla = ttk.Frame(self.parent)

#         frame_tabla.pack(
#             fill="both",
#             expand=True,
#             padx=10,
#             pady=10
#             )

#         columnas = ["id"] + self.campos

#         self.tabla = ttk.Treeview(
#             frame_tabla,
#             columns=columnas,
#             show="headings"
#             )

#         for columna in columnas:

#             self.tabla.heading(
#                 columna,
#                 text=columna.capitalize()
#                 )

#             self.tabla.column(
#                 columna,
#                 width=120
#                 )

#             self.tabla.pack(
#                 fill="both",
#                 expand=True
#                 )

#             self.tabla.bind(
#                 "<<TreeviewSelect>>", self.seleccionar
#                 )

#     def obtener_datos_formulario(self):
#         datos = {}

#         for campo, entry in self.entries.items():
#             datos[campo] = entry.get().strip()

#         return datos

#     def crear(self):
#         datos = self.obtener_datos_formulario()
#         if not all(datos.values()):
#             messagebox.showwarning(
#                 "Datos incompletos",
#                 "Debe completar todos los campos."
#                 )

#             return

#         objeto = self.clase_entidad(**datos)

#         self.repositorio.crear(objeto)
#         self.actualizar_tabla()
#         self.limpiar()

#         messagebox.showinfo(
#             "Éxito",
#             "Registro creado correctamente."
#             )


#     def actualizar_tabla(self):

#         for elemento in self.tabla.get_children():
#             self.tabla.delete(elemento)
#             registros = self.repositorio.obtener_todos()

#             for objeto in registros:
#                 valores = [objeto.id]

#                 for campo in self.campos:
#                     valores.append(
#                         getattr(objeto, campo)
#                         )

#         self.tabla.insert("", "end", values=valores)


#     def seleccionar(self, event):
#         seleccion = self.tabla.selection()

#         if not seleccion:
#             return

#         valores = self.tabla.item(
#             seleccion[0],"values"
#             )

#         id_objeto = int(valores[0])
#         registros = self.repositorio.obtener_todos()

#         for objeto in registros:

#             if objeto.id == id_objeto:
#                 self.objeto_seleccionado = objeto

#                 for campo in self.campos:
#                     self.entries[campo].delete(
#                     0,
#                     tk.END
#                 )

#                 self.entries[campo].insert(0,
#                     getattr(objeto, campo)
#                     )

#             break

#     def actualizar(self):

#         if self.objeto_seleccionado is None:
#             messagebox.showwarning(
#                 "Selección requerida",
#                 "Debe seleccionar un registro antes de actualizar."
#             )

#             return

#         datos = self.obtener_datos_formulario()

#         if not all(datos.values()):
#             messagebox.showwarning(
#                     "Datos incompletos",
#                     "Debe completar todos los campos."
#                 )

#             return

#         for campo, valor in datos.items():
#             setattr(
#                 self.objeto_seleccionado,
#                 campo,
#                 valor
#                 )

#         self.repositorio.actualizar(
#             self.objeto_seleccionado
#             )

#         self.actualizar_tabla()
#         self.limpiar()

#         messagebox.showinfo(
#             "Éxito",
#             "Registro actualizado correctamente."
#             )

#     def eliminar(self):

#         if self.objeto_seleccionado is None:

#             messagebox.showwarning(
#                 "Selección requerida",
#                 "Debe seleccionar un registro antes de eliminar."
#             )

#             return

#         confirmar = messagebox.askyesno(
#             "Confirmar eliminación",
#             "¿Está seguro de eliminar el registro?"
#             )

#         if not confirmar:
#             return

#         self.repositorio.eliminar(
#             self.objeto_seleccionado.id
#             )

#         self.objeto_seleccionado = None

#         self.actualizar_tabla()
#         self.limpiar()

#         messagebox.showinfo(
#             "Éxito",
#             "Registro eliminado correctamente."
#             )


#     def limpiar(self):

#         for entry in self.entries.values():

#             entry.delete(
#             0,
#             tk.END
#             )

#         self.objeto_seleccionado = None

#         seleccion = self.tabla.selection()

#         if seleccion:
#             self.tabla.selection_remove(seleccion
#             )

"""
import tkinter as tk
from tkinter import ttk, messagebox


class InterfazCRUD:

    def __init__(
        self,
        parent,
        titulo,
        campos,
        clase_entidad,
        repositorio
    ):

        self.parent = parent
        self.titulo = titulo
        self.campos = campos
        self.clase_entidad = clase_entidad
        self.repositorio = repositorio

        self.entries = {}
        self.objeto_seleccionado = None

        self.crear_interfaz()

    def crear_interfaz(self):

        self.frame = ttk.LabelFrame(
            self.parent,
            text=self.titulo,
            padding=10
        )

        self.frame.pack(
            fill="x",
            padx=10,
            pady=10
        )

        self.crear_formulario()
        self.crear_botones()
        self.crear_tabla()

    def crear_formulario(self):

        for fila, campo in enumerate(self.campos):

            label = ttk.Label(
                self.frame,
                text=campo.capitalize()
            )

            label.grid(
                row=fila,
                column=0,
                padx=5,
                pady=5,
                sticky="w"
            )

            entry = ttk.Entry(
                self.frame
            )

            entry.grid(
                row=fila,
                column=1,
                padx=5,
                pady=5,
                sticky="ew"
            )

            self.entries[campo] = entry

    def crear_botones(self):

        frame_botones = ttk.Frame(self.parent)

        frame_botones.pack(
            fill="x",
            padx=10,
            pady=5
        )

        botones = [
            ("Crear", self.crear),
            ("Actualizar", self.actualizar),
            ("Eliminar", self.eliminar),
            ("Limpiar", self.limpiar)
        ]

        for texto, comando in botones:

            boton = ttk.Button(
                frame_botones,
                text=texto,
                command=comando
            )

            boton.pack(
                side="left",
                padx=5
            )

    def crear_tabla(self):

        frame_tabla = ttk.Frame(self.parent)

        frame_tabla.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        columnas = ["id"] + self.campos

        self.tabla = ttk.Treeview(
            frame_tabla,
            columns=columnas,
            show="headings"
        )

        for columna in columnas:

            self.tabla.heading(
                columna,
                text=columna.capitalize()
            )

            self.tabla.column(
                columna,
                width=120
            )

        self.tabla.pack(
            fill="both",
            expand=True
        )

        self.tabla.bind(
            "<<TreeviewSelect>>",
            self.seleccionar
        )

    def obtener_datos_formulario(self):

        datos = {}

        for campo, entry in self.entries.items():

            datos[campo] = entry.get().strip()

        return datos

    def crear(self):

        datos = self.obtener_datos_formulario()

        if not all(datos.values()):

            messagebox.showwarning(
                "Datos incompletos",
                "Debe completar todos los campos."
            )

            return

        objeto = self.clase_entidad(
            **datos
        )

        self.repositorio.crear(objeto)

        self.actualizar_tabla()
        self.limpiar()

        messagebox.showinfo(
            "Éxito",
            "Registro creado correctamente."
        )

    def actualizar_tabla(self):

        for elemento in self.tabla.get_children():

            self.tabla.delete(elemento)

        registros = self.repositorio.obtener_todos()

        for objeto in registros:

            valores = [objeto.id]

            for campo in self.campos:

                valores.append(
                    getattr(objeto, campo)
                )

            self.tabla.insert(
                "",
                "end",
                values=valores
            )

    def seleccionar(self, event):

        seleccion = self.tabla.selection()

        if not seleccion:
            return

        valores = self.tabla.item(
            seleccion[0],
            "values"
        )

        id_objeto = int(valores[0])

        registros = self.repositorio.obtener_todos()

        for objeto in registros:

            if objeto.id == id_objeto:

                self.objeto_seleccionado = objeto

                for campo in self.campos:

                    self.entries[campo].delete(
                        0,
                        tk.END
                    )

                    self.entries[campo].insert(
                        0,
                        getattr(objeto, campo)
                    )

                break

    def actualizar(self):

        if self.objeto_seleccionado is None:

            messagebox.showwarning(
                "Selección requerida",
                "Debe seleccionar un registro antes de actualizar."
            )

            return

        datos = self.obtener_datos_formulario()

        if not all(datos.values()):

            messagebox.showwarning(
                "Datos incompletos",
                "Debe completar todos los campos."
            )

            return

        for campo, valor in datos.items():

            setattr(
                self.objeto_seleccionado,
                campo,
                valor
            )

        self.repositorio.actualizar(
            self.objeto_seleccionado
        )

        self.actualizar_tabla()
        self.limpiar()

        messagebox.showinfo(
            "Éxito",
            "Registro actualizado correctamente."
        )

    def eliminar(self):

        if self.objeto_seleccionado is None:

            messagebox.showwarning(
                "Selección requerida",
                "Debe seleccionar un registro antes de eliminar."
            )

            return

        confirmar = messagebox.askyesno(
            "Confirmar eliminación",
            "¿Está seguro de eliminar el registro?"
        )

        if not confirmar:
            return

        self.repositorio.eliminar(
            self.objeto_seleccionado.id
        )

        self.objeto_seleccionado = None

        self.actualizar_tabla()
        self.limpiar()

        messagebox.showinfo(
            "Éxito",
            "Registro eliminado correctamente."
        )

    def limpiar(self):

        for entry in self.entries.values():

            entry.delete(
                0,
                tk.END
            )

        self.objeto_seleccionado = None

        seleccion = self.tabla.selection()

        if seleccion:

            self.tabla.selection_remove(
                seleccion
            )
"""