from database import Usuarios
from usuarios import Usuario

def crear_ususario(nombre,email,password,rol):
    Usuario= Usuarios(nombre,email,password,rol)
    Usuarios.insart_one(Usuario.to_dict())
    print("Usuario creado correctamente")

def  buscar_usuario(email):
    return Usuarios.find_one({"email",email})

def login(email,password):
    Usuario = buscar_usuario(email)
    if Usuario and Usuarios ("password") == password:
        print("login exitoso")
        return Usuario
    else:
        print("credenciales incorrectas.")
        return None