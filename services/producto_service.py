from database import Productos
from models.productos import Producto

def crear_producto(nombre,descripcion,precio,imagen):
    Producto = Productos(nombre,descripcion,precio,imagen)
    Producto.insert_one(Producto.on_dict())
    print("Producto creado correctamente.")

def listar_productos():
    return Productos.find()