import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
from forms.master.form_master import MasterPanel
from forms.login.from_login_designer import formLoginDesigner
from forms.registration.form import formRegister
class formLogin(formLoginDesigner):
    
    def registrar(self):
       formRegister()
       
    
    def verificar(self):
        ban=0
        archivo = open("BD.txt","r")
        usu = self.usuario.get()
        password = self.password.get()
        users = archivo.readlines()
        archivo.close()
        for user in users:
            datos = user.strip().split(";") 
            if usu == datos[0]:
                ban = 1
                if password == datos[1]:
                    self.ventana.destroy()
                    MasterPanel()
                else:
                    messagebox.showerror(message="Contraseña incorrecta",title="Mensaje")
                
        if ban == 0 :
            messagebox.showerror(message="usuario inexistente",title="Mensaje")
        
            
        
    
        