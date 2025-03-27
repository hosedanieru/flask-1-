import pymongo

#conexion a mongodb
cliente = pymongo.MongoClient("mongodb://localhost:27017/")
db = cliente("ADSO_SENA_CBA")

#colecciones
Usuarios = db["usuarios"]
Productos = db["productos"]
Inventarios = db ["inventarios"]
Ventas = db ["ventas"]

print("conexion exitosa a la base de datos")

