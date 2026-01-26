


usuarios = {}
productos = {}
productos.po
def crearUsuario():
    #Crea la tupla para el nuevo usuario
    nombre = input("Introduce el nombre: ")
    edad = input("Introduce la edad: ")
    ciudad = input("Introduce la ciudad: ")
    return (nombre, edad, ciudad)

def addUsuario(USR_data):
    #Añade la tupla del usuario a la base de datos de usuarios calculando el nuevo key
    newKey = len(USR_data) + 1
    USR_data[newKey] = crearUsuario()
    return USR_data

def processProduct(productos,name,price):
    #Añade productos si el nombre es nuevo y sobreescribe el precio en caso contrario
    
    productos[name] = price
    return productos
def delProduct(productos, key):
    #Borra de la base de datos de productos un producto a partir de un key en concreto
    if key in productos:
        precio = productos.get(key)
        productos.pop(key,f"Se ha borrado {key}con precio {precio}")
        return productos
    else:
        #print("No se puede borrar un producto inexistentes")
        raise KeyError(f"La clave ({key}) no existe para borrarse")
        return productos
        



# def procesar_diccionario(datos):
#     print("El diccionario tiene:", len(datos), "elementos")
#     # También puedes acceder a claves, valores, etc.
#     print("Claves:", datos.keys())

# mi_dic = {"a": 1, "b": 2, "c": 3}
# procesar_diccionario(mi_dic)



usuarios = addUsuario(usuarios)
usuarios = addUsuario(usuarios)

print(usuarios)
