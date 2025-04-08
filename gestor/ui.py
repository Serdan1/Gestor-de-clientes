from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askokcancel, WARNING
import database as db
import helpers

class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestor de Clientes")
        self.build()

    def build(self):
        # Frame superior con Treeview
        frame = Frame(self)
        frame.pack(pady=10)
        
        self.treeview = ttk.Treeview(frame, columns=("DNI", "Nombre", "Apellido"), show="headings")
        self.treeview.heading("DNI", text="DNI")
        self.treeview.heading("Nombre", text="Nombre")
        self.treeview.heading("Apellido", text="Apellido")
        self.treeview.column("DNI", width=100, anchor=CENTER)
        self.treeview.column("Nombre", width=150, anchor=CENTER)
        self.treeview.column("Apellido", width=150, anchor=CENTER)
        
        # Cargar datos iniciales
        for cliente in db.Clientes.lista:
            self.treeview.insert("", "end", iid=cliente.dni, values=(cliente.dni, cliente.nombre, cliente.apellido))
        
        # Scrollbar
        scrollbar = Scrollbar(frame, orient=VERTICAL, command=self.treeview.yview)
        self.treeview.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.treeview.pack()

        # Frame inferior con botones
        frame = Frame(self)
        frame.pack(pady=10)
        Button(frame, text="Crear", command=self.create_client_window).grid(row=0, column=0, padx=5)
        Button(frame, text="Modificar", command=self.edit_client_window).grid(row=0, column=1, padx=5)
        Button(frame, text="Borrar", command=self.delete).grid(row=0, column=2, padx=5)

    def delete(self):
        selected = self.treeview.focus()
        if selected:
            valores = self.treeview.item(selected, "values")
            if askokcancel("Confirmación", f"¿Borrar a {valores[1]} {valores[2]}?", icon=WARNING):
                self.treeview.delete(selected)
                db.Clientes.borrar(valores[0])

    def create_client_window(self):
        CreateClientWindow(self)

    def edit_client_window(self):
        selected = self.treeview.focus()
        if selected:
            EditClientWindow(self)

class CreateClientWindow(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Crear Cliente")
        self.parent = parent
        self.build()

    def build(self):
        frame = Frame(self)
        frame.pack(padx=10, pady=10)
        
        Label(frame, text="DNI (2 nums, 1 letra):").grid(row=0, column=0)
        Label(frame, text="Nombre (2-30 chars):").grid(row=0, column=1)
        Label(frame, text="Apellido (2-30 chars):").grid(row=0, column=2)
        
        self.dni = Entry(frame)
        self.dni.grid(row=1, column=0)
        self.nombre = Entry(frame)
        self.nombre.grid(row=1, column=1)
        self.apellido = Entry(frame)
        self.apellido.grid(row=1, column=2)
        
        frame = Frame(self)
        frame.pack(pady=10)
        self.crear_btn = Button(frame, text="Crear", command=self.create_client, state=DISABLED)
        self.crear_btn.grid(row=0, column=0, padx=5)
        Button(frame, text="Cancelar", command=self.destroy).grid(row=0, column=1, padx=5)
        
        self.validaciones = [False, False, False]
        self.dni.bind("<KeyRelease>", lambda ev: self.validate(ev, 0))
        self.nombre.bind("<KeyRelease>", lambda ev: self.validate(ev, 1))
        self.apellido.bind("<KeyRelease>", lambda ev: self.validate(ev, 2))

    def validate(self, event, index):
        valor = event.widget.get()
        if index == 0:
            valido = helpers.dni_valido(valor, db.Clientes.lista)
        else:
            valido = valor.isalpha() and 2 <= len(valor) <= 30
        event.widget.config(bg="green" if valido else "red")
        self.validaciones[index] = valido
        self.crear_btn.config(state=NORMAL if all(self.validaciones) else DISABLED)

    def create_client(self):
        dni, nombre, apellido = self.dni.get(), self.nombre.get(), self.apellido.get()
        db.Clientes.crear(dni, nombre, apellido)
        self.parent.treeview.insert("", "end", iid=dni, values=(dni, nombre, apellido))
        self.destroy()

class EditClientWindow(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Modificar Cliente")
        self.parent = parent
        self.build()

    def build(self):
        selected = self.parent.treeview.focus()
        valores = self.parent.treeview.item(selected, "values")
        
        frame = Frame(self)
        frame.pack(padx=10, pady=10)
        
        Label(frame, text="DNI (no editable):").grid(row=0, column=0)
        Label(frame, text="Nombre (2-30 chars):").grid(row=0, column=1)
        Label(frame, text="Apellido (2-30 chars):").grid(row=0, column=2)
        
        self.dni = Entry(frame)
        self.dni.insert(0, valores[0])
        self.dni.config(state=DISABLED)
        self.dni.grid(row=1, column=0)
        self.nombre = Entry(frame)
        self.nombre.insert(0, valores[1])
        self.nombre.grid(row=1, column=1)
        self.apellido = Entry(frame)
        self.apellido.insert(0, valores[2])
        self.apellido.grid(row=1, column=2)
        
        frame = Frame(self)
        frame.pack(pady=10)
        self.actualizar_btn = Button(frame, text="Actualizar", command=self.update_client)
        self.actualizar_btn.grid(row=0, column=0, padx=5)
        Button(frame, text="Cancelar", command=self.destroy).grid(row=0, column=1, padx=5)
        
        self.validaciones = [True, True]  # DNI no editable
        self.nombre.bind("<KeyRelease>", lambda ev: self.validate(ev, 0))
        self.apellido.bind("<KeyRelease>", lambda ev: self.validate(ev, 1))

    def validate(self, event, index):
        valor = event.widget.get()
        valido = valor.isalpha() and 2 <= len(valor) <= 30
        event.widget.config(bg="green" if valido else "red")
        self.validaciones[index] = valido
        self.actualizar_btn.config(state=NORMAL if all(self.validaciones) else DISABLED)

    def update_client(self):
        dni, nombre, apellido = self.dni.get(), self.nombre.get(), self.apellido.get()
        db.Clientes.modificar(dni, nombre, apellido)
        self.parent.treeview.item(self.parent.treeview.focus(), values=(dni, nombre, apellido))
        self.destroy()

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()