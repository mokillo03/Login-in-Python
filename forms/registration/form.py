from forms.registration.registration_designer import formRegisterDesigner
from tkinter import ttk , messagebox
import tkinter as tk

class formRegister(formRegisterDesigner):
    
    def __init__(self):
        super().__init__()
    
    def registar(self):
        if self.confimationPassword():
            if self.userRegister():
                self.carga()
        
    def confimationPassword(self):
        status: bool = True
        if (self.password.get()!="" and self.confirmation.get()!="" ):
            if (self.password.get() != self.confirmation.get()):
                status = False
                messagebox.showerror(message="las contraseñas no coinciden", title="Mensaje")
                self.password.delete(0, tk.END)
                self.confirmation.delete(0,tk.END)
        else:
            messagebox.showerror(message="complete los campos", title="Mensaje")
            self.password.delete(0, tk.END)
            self.confirmation.delete(0,tk.END)
        return status
    
    def userRegister(self):
        usu = self.usuario.get()
        archivo = open("BD.txt","r")
        users = archivo.readlines()
        archivo.close
        for user in users:
            datos = user.strip().split(";")
            if datos[0] == usu:
                messagebox.showerror(message="usuario ya registrado",title="mensaje")
                self.usuario.delete(0, tk.END)
                return False
        return True
    
    def carga(self):
        usu = self.usuario.get()
        password = self.password.get()
        if usu != "" and password != "":
            archivo = open("BD.txt","a")
            archivo.write(f"{usu};{password}\n")
            archivo.close
            messagebox.showinfo(message="registrado con exito",title="Mensaje")
        else:
            messagebox.showerror(message="debe completar los campos",title="Mensaje")