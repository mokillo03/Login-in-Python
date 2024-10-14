def userRegister(usu):
        
    archivo = open("BD.txt","r")
    lineas = archivo.readlines()
    for linea in lineas:
        usuario = linea.strip().split(";")
        if usuario[0] == usu:
            print("usuario existente")
            return False   
    return True
def cargar(usu,contra):
    archivo = open("BD.txt","a")
    archivo.write(f"{usu};{contra}\n")

                
              
usuario = input("ingres usuario: ")
contraseña = input("ingres contraseña: ")

if userRegister(usuario):
    cargar(usuario,contraseña)
else:
    print("ya existe")