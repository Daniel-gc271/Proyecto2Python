
"""
Funcion para crear usuarios:
 Crea la tupla usuario a partir de un nombre, una edad y una ciudad
 valida que la edad sea positiva y devuelve una tupla
"""
def crearUsuario():
    print("\n--- CREAR USUARIO ---")
    #Pedir y validar el nombre
    nombre = ""
    while not nombre or nombre.isdigit():
        nombre = input("Introduce el nombre: ").strip()
        if not nombre:
            print("El nombre no puede estar vacío.")
        elif nombre.isdigit():
            print("El nombre no puede ser un numero")

    # Pedir y validar edad
    edad_invalida = True
    while edad_invalida:
        edad = input("Introduce la edad: ").strip()

        if not edad:
            print("La edad no puede estar vacía!")
            continue  

        if not edad.isdigit():
            print("La edad debe ser un número positivo mayor que cero.")

            continue  

        edad = int(edad)
        if edad <= 0:
            print("La edad debe ser un número positivo mayor que cero.")
            continue  

        """
        El continue salta este reset de bandera en caso de que la edad sea incorrecta
        """
        edad_invalida = False

    #Pedir y validar el nombre de la ciudad   
    ciudad = ""
    while not ciudad or ciudad.isdigit():
        ciudad = input("Introduce la ciudad: ").strip()
        if not ciudad:
            print("La ciudad no puede estar vacía.")
        elif ciudad.isdigit():
            print("La ciudad no puede ser un numero")
    return (nombre, edad, ciudad)

"""
Añade el usuario a la base de datos de usuarios y devuelve dicha base actulizada
la clave es numerica y la genera de manera automatica cada vez que se
añade un usuario.
Crea los usuarios a partir de la funcion "Crear usuario"
"""
def añadirUsuario(usuarios:dict):
    newKey=1
    while newKey in usuarios:
        newKey = newKey + 1
    usuarios[newKey] = crearUsuario()
    print("\n--- USUARIO AÑADIDO ---")
    return usuarios
"""
Solicita el nombre y precio del producto,
los valida y actualiza la lista
"""
def añadirProducto(productos:dict):
    print("\n--- AÑADIR PRODUCTO ---")
    #Pedir y validar el nombre
    nombre = ""
    while not nombre or nombre.isdigit():
        nombre = input("Introduce el nombre del producto: ").strip()
        if not nombre:
            print("El nombre del producto no puede estar vacío.")
        elif nombre.isdigit():
            print("El nombre del producto no puede ser un numero")
    #Pedir y validar el precio
    precio_invalido = True
    while precio_invalido:
        precio = input("Introduce el precio con punto decimal: ").strip()
        #Comprobar que no este vacio el precio
        if not precio:
            print("El precio no puede estar vacío!")
            continue  
        #Comprobar que el precio es un numero
        try:
            precio = float(precio)
            if precio <= 0:
                print("El precio debe ser un número positivo mayor que cero.")
                continue  
            precio_invalido = False
        except ValueError:
            print("El precio debe ser un número.")
    productos[nombre]=precio
    print(f"Se ha añadido: {nombre}\n"
          f"Con precio: {precio}")
    return productos
"""
Busca en la base de datos de los productos el producto a eliminar y lo borra
en caso de que no este disponible lanza un error
"""
def eliminarProducto(productos:dict):
    #Borra de la base de datos de productos un producto a partir de un key en concreto
    print("\n--- BORRAR PRODUCTO ---")
    nombre_Producto = input("Introduce el nombre del producto a borrar: ").strip()
    if nombre_Producto in productos:
        precio = productos.get(nombre_Producto)
        productos.pop(nombre_Producto)
        print("\n--- PRODUCTO BORRADO ---")
        print(f"Se ha borrado {nombre_Producto}con precio {precio}")
        return productos
    else:
        print("\n--- ERROR AL BORRAR PRODUCTO ---")
        print(f"El producto ({nombre_Producto}) no se encuentra en la base de datos")
        print("No se puede borrar un producto inexistente")
        #raise KeyError(f"El producto ({nombre_Producto}) no existe para borrarse")
        return productos
def modificarPrecio(productos:dict):
    print("\n--- MODIFICAR PRECIO DE PRODUCTO ---")

    # Comprobar si hay productos registrados
    if not productos:
        print("No hay productos registrados.")
    else:
        nombre = input("Introduce el nombre del producto a modificar: ")

        # Comprobar si existe el producto
        if nombre not in productos:
            print("Ese producto no existe.")
        else:
           #Pedir y validar el precio
            precio_invalido = True
            while precio_invalido:
                precio = input("Introduce el precio con punto decimal: ").strip()
                #Comprobar que no este vacio el precio
                if not precio:
                    print("El precio no puede estar vacío!")
                    continue  
                #Comprobar que el precio es un numero
                try:
                    precio = float(precio)
                    if precio <= 0:
                        print("El precio debe ser un número positivo mayor que cero.")
                        continue  
                    precio_invalido = False
                except ValueError:
                    print("El precio debe ser un número.")
                    # Actualizar el precio
            productos[nombre] = precio
            print("Precio actualizado correctamente.")
            return productos
"""
Funcion imprimir usuarios:
Imprime los usuarios presentes en la base de datos
"""
def imprimirUsuarios(usuarios:dict):
    if not usuarios: 
        print("No hay usuarios para mostrar")
    else:
        for usuario in usuarios:
            currentUser= usuarios.get(usuario)
            nombre, edad, ciudad = currentUser[0], currentUser[1], currentUser[2]
            print(
                "-------------------------\n"
                f"Usuario #{usuario}\n"
                f"Nombre: {nombre}\n"
                f"Edad: {edad}\n"
                f"Ciudad: {ciudad}\n"
            )
"""
Funcion imprimir productos:
Imprime los productos presentes en la base de datos
"""
def imprimirProductos(productos:dict):
    if not productos: 
        print("No hay productos para mostrar")
    else:
        """
        La funcion .items de los diccionarios devuelve sus contenidos
        en forma de pseudolista (gracias chatgpt x decirme que existe)
        """
        for nombre, precio in productos.items():
            print(
            "-------------------------\n"
            f"Nombre: {nombre}\n"
            f"Precio: {precio}\n"
            )
"""
Funcion buscar usuarios por ciudad, DEVUELVE TODOS LOS USUARIOS QUE COINCIDAN
"""
def buscarUsuariosPorCiudad(usuarios: dict):
    print("\n--- BUSCAR USUARIOS POR CIUDAD ---")

    # Comprobar si hay usuarios registrados
    if len(usuarios) == 0:
        print("No hay usuarios registrados.")
    else:
        #solicita la ciudad y normaliza el formato en BBDD y la busqueda
        ciudad_buscar = input("Introduce la ciudad: ")
        #Muestra los usuarios encontrados que coincidan con el criterio
        for usuario in usuarios:
            currentUser= usuarios.get(usuario)
            nombre, edad, ciudad = currentUser[0], currentUser[1], currentUser[2]
            if (ciudad_buscar.strip().lower()==ciudad.lower()):
                print(
                    "-------------------------\n"
                    f"Usuario #{usuario}\n"
                    f"Nombre: {nombre}\n"
                    f"Edad: {edad}\n"
                    f"Ciudad: {ciudad}\n"
                )           
"""
Busca un usuario por su id y muetra los valores asociados, en caso de que no este,
avisa por la consola que dicho usuario no existe.
"""
def buscarUsuarioPorId(usuarios:dict):
    print("\n--- BUSCAR USUARIO POR ID ---")

    # Comprobar si hay usuarios registrados
    if len(usuarios) == 0:
        print("No hay usuarios registrados.")
    else:
        id_valido = True
        while id_valido:
            # Pedir y validar ID
            id_buscar = input("Introduce el ID: ").strip()

            if not id_buscar:
                print("El ID no puede estar vacía!")
                continue  

            if not id_buscar.isdigit():
                print("El ID debe ser un número positivo mayor que cero.")

                continue  

            id_buscar = int(id_buscar)
            if id_buscar <= 0:
                print("El ID debe ser un número positivo mayor que cero.")
                continue  

            
            #El continue salta este reset de bandera en caso de que el ID seea incorrecta
            
            id_valido = False
            
        if id_buscar in usuarios:
            currentUser= usuarios.get(id_buscar)
            nombre, edad, ciudad = currentUser[0], currentUser[1], currentUser[2]
            print(
                    "-------------------------\n"
                    f"Usuario #{id_buscar}\n"
                    f"Nombre: {nombre}\n"
                    f"Edad: {edad}\n"
                    f"Ciudad: {ciudad}\n"
                )
            #return True
        else: 
            print(f"El usuario con ID: {id_buscar} no está en la base de datos")
            #return False
####Stats####
"""
Devuelve el conteo total de usuarios
"""
def totUsuarios(usuarios:dict):
    num_Usuarios= len(usuarios)
    return f"En la base de datos hay: {num_Usuarios} usuarios"     
    #return num_Usuarios
"""
Devuelve el conteo total de productos
"""
def totProductos(productos:dict):
    num_Productos= len(productos)
    return f"En la base de datos hay: {num_Productos} productos"    
    #return num_Productos
"""
Devuelve la edad mas alta
"""   
def maxEdad(usuarios:dict):
    print("\n--- EDAD MÁXIMA ---")

    # Comprobar si hay usuarios registrados
    if len(usuarios) == 0:
        print("No hay usuarios registrados.")
    else:
        #Buscar la edad mas alta
        edad_mas_baja = max(usuario[1] for usuario in usuarios.values())
        #en este caso recorre las tuplas del dicionario
    for usuario in usuarios:
        #Imprimir al usuario(s) con la edad mas alta
            currentUser= usuarios.get(usuario)
            nombre, edad, ciudad = currentUser[0], currentUser[1], currentUser[2]
            if (edad==edad_mas_baja):
                
                print(
                    "-------------------------\n"
                    f"Usuario #{usuario}\n"
                    f"Nombre: {nombre}\n"
                    f"Edad: {edad}\n"
                    f"Ciudad: {ciudad}\n"
                )  
    print("\nBusqueda terminada")       
"""
Devuelve la edad mínima
"""
def minEdad(usuarios:dict):
    print("\n--- EDAD MÍNIMA ---")

    # Comprobar si hay usuarios registrados
    if len(usuarios) == 0:
        print("No hay usuarios registrados.")
    else:
        #Buscar la edad mas baja
        edad_mas_baja = min(usuario[1] for usuario in usuarios.values())
        #en este caso recorre las tuplas del dicionario
    for usuario in usuarios:
        #Imprimir al usuario(s) con la edad mas baja
            currentUser= usuarios.get(usuario)
            nombre, edad, ciudad = currentUser[0], currentUser[1], currentUser[2]
            if (edad==edad_mas_baja):
                print(
                    "-------------------------\n"
                    f"Usuario #{usuario}\n"
                    f"Nombre: {nombre}\n"
                    f"Edad: {edad}\n"
                    f"Ciudad: {ciudad}\n"
                )  
    print("\nBusqueda terminada")                             
"""
Devuelve la edad media
"""

def medEdad(usuarios: dict):
    print("\n--- EDAD MEDIA ---")

    if not usuarios:
        print("No hay usuarios registrados.")
        return

    sigmaEdades = 0
    contUsuarios = 0

    for datos in usuarios.values():
        # datos es una tupla: (nombre, edad, ciudad)
        sigmaEdades = datos[1] + sigmaEdades
        contUsuarios = 1 + contUsuarios

    media = sigmaEdades / contUsuarios
    return(f"Edad media: {media:.2f}")

"""
Devuelve la media del precio de los productos
"""
def medPrecioProductos(productos:dict):
    return sum(productos.values())/len(productos)

def menuPrincipal(usuarios:dict, productos:dict):
    
    salir = False
    while not salir:
        print("\n--- GESTOR INTELIGENTE DE DATOS ---")
        print("0. Salir")
        print("1. Añadir usuario")
        print("2. Mostrar usuarios")
        print("3. Gestión de productos")
        print("4. Estadísticas")
        print("5. Búsquedas")

        opcion = input("Elige una opción: ").strip()
        if opcion == "1":
            print("Añadir usuario")
            print(">>")
            usuarios=añadirUsuario(usuarios)
        elif opcion == "2":
            print("Mostrar usuarios")
            print(">>")
            imprimirUsuarios(usuarios)
        elif opcion == "3":
            print("Abrir submenu productos")
            print(">>")
            menuProductos(productos)  
        elif opcion == "4":
            print("Abrir submenu estadisticas")
            print(">>")
            menuEstadisticas(productos, usuarios) 
        elif opcion == "5":
            print("Abrir submenu busquedas")
            print(">>")
            menuBusquedas(usuarios)  
        elif opcion == "0":
            print("Salir")
            print(">>")
            print("Saliendo del programa...")
            salir = True
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Submenu de búsquedas
def menuBusquedas(usuarios:dict):
    menuBusqueda = False

    while not menuBusqueda:
        print("\n--- MENÚ DE BÚSQUEDAS ---")
        print("0. Volver al menú principal")
        print("1. Buscar usuario por ID")
        print("2. Buscar usuarios por ciudad")
        

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            print("Buscar usuario por ID")
            print(">>")
            buscarUsuarioPorId(usuarios)
        elif opcion == "2":
            print("Buscar usuario por ciudad")
            print(">>")
            buscarUsuariosPorCiudad(usuarios)
        elif opcion == "0":
            menuBusqueda = True
        else:
            print("Opción no válida.")

# Submenu de Productos
def menuProductos(productos:dict):
    menuproductos = False
    while not menuproductos:
        print("\n--- MENÚ DE PRODUCTOS ---")
        print("0. Volver al menú principal")
        print("1. Añadir producto")
        print("2. Mostrar productos")
        print("3. Modificar precio")
        print("4. Eliminar producto")
        

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            print("Añadir productos")
            print(">>")
            productos=añadirProducto(productos)
        elif opcion == "2":
            print("Mostrar productos")
            print(">>")
            imprimirProductos(productos)
        elif opcion == "3":
            print("Modificar precio")
            print(">>")
            productos= modificarPrecio(productos)
        elif opcion == "4":
            print("Eliminar producto")
            print(">>")
            productos= eliminarProducto(productos)
        elif opcion == "0":
            menuproductos = True
        else:
            print("Opción no válida.")
def menuEstadisticas( productos:dict,usuarios:dict ):
    menuestadisticas = False
    while not menuestadisticas:
        print("\n--- MENÚ DE ESTADÍSTICAS ---")
        print("0. Volver al menú principal")
        print("1. Estadísticas de usuarios")
        print("2. Estadísticas de productos")
        

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            print("Estadísticas de usuarios")
            print(">>")
            subMenuestadisticasUsuarios(usuarios)
        elif opcion == "2":
            print("Estadísticas de productos")
            print(">>")
            subMenuestadisticasProductos(productos)
        elif opcion == "0":
            menuestadisticas = True
        else:
            print("Opción no válida.")
def subMenuestadisticasUsuarios(usuarios:dict):
    menuEstadisticasUsuarios = False
    while not menuEstadisticasUsuarios:
        print("\n--- ESTADÍSTICAS DE USUARIOS ---")
        print("0. Volver al menú principal")
        print("1. Total de usuarios")
        print("2. Edad media de usuarios")
        print("3. Edad mas baja")
        print("4. Edad mas alta")
        
        opcion=input("Elige una opción: ").strip()
        if opcion == "1":
            print("Total de usuarios") 
            print(totUsuarios(usuarios))
        elif opcion == "2":
            print("Edad media de usuarios")
            print(medEdad(usuarios))
        elif opcion == "3":
            print("Edad mas baja")
            print(minEdad(usuarios))
        elif opcion == "4":
            print("Edad mas alta")
            print(maxEdad(usuarios))
        elif opcion == "0":
            print("Volver al menú principal")
            menuEstadisticasUsuarios = True
        else:
            print("Opción no válida.")  
def subMenuestadisticasProductos(productos:dict):

    print("\n--- ESTADÍSTICAS DE PRODUCTOS ---")
    menuEstadisticasProductos = False
    while not menuEstadisticasProductos:
        print("0. Volver al menú principal")
        print("1. Total de productos")
        print("2. Precio medio de productos")
        
        opcion=input("Elige una opción: ").strip()
        if opcion == "1":
            print("Total de productos")
            print(totProductos(productos))
        elif opcion == "2":
            print("Precio medio de productos")
            print(medPrecioProductos(productos))
        elif opcion == "0":
            print("Volver al menú principal")
            menuEstadisticasProductos = True
        else:
            print("Opción no válida.")
def main():
     # Datos de prueba
        usuarios = {
        1: ("Daniel", 32, "Valladolid"),
        2: ("Lucía", 18, "Zaragoza"),
        3: ("Pablo", 40, "Valladolid"),
        4: ("Pedro", 45, "Madrid"),
        5: ("Valeria", 28, "Zaragoza"),
        6: ("Carlos", 55, "Barcelona"),
        7: ("Marta", 22, "Sevilla"),
        8: ("Javier", 35, "Valencia"),
        9: ("Isabel", 50, "Bilbao"),
        10: ("Roberto", 29, "Málaga"),
        }

        productos = {
        "Manzana": 0.75,
        "Pan": 1.10,
        "Leche": 1.35,
        "Huevos": 2.20,
        "Arroz": 1.50,
        "Pollo": 8.50,
        "Tomate": 0.99,
        "Queso": 3.25,
        "Yogur": 1.80,
        "Aceite": 5.40,
        "Café": 4.20,
        "Chocolate": 2.15,
        "Pasta": 0.95,
        "Jamón": 6.75,
        }
        menuPrincipal(usuarios, productos)
# main
main()


########
#
# Ultima revisión: 29/01/2026
#
#
########
# Validaciones en el programa:

# 1. VALIDACIÓN DE NOMBRES (crearUsuario, añadirProducto)
# - Comprueba que el nombre no esté vacío con: if not nombre
# - Comprueba que no sea un número con: nombre.isdigit()
# - Esto asegura que los nombres sean valores alfanuméricos válidos

# 2. VALIDACIÓN DE EDAD (crearUsuario)
# - Verifica que no esté vacío: if not edad
# - Verifica que sea un número entero: edad.isdigit()
# - Verifica que sea positivo: if edad <= 0
# - Uso de try-except para capturar errores de conversión de tipos

# 3. VALIDACIÓN DE PRECIO (añadirProducto, modificarPrecio)
# - Verifica que el precio no esté vacío: if not precio
# - Intenta convertirlo a float dentro de un try-except
# - Verifica que sea positivo: if precio <= 0
# - Captura ValueError si no es convertible a número

# 4. VALIDACIÓN DE ID (buscarUsuarioPorId)
# - Verifica que el ID no esté vacío
# - Verifica que sea un número entero: id_buscar.isdigit()
# - Verifica que sea positivo: if id_buscar <= 0
# - Usa bandera id_valido para controlar el flujo del loop
# - El id siepre es un entero positivo válido al salir del loop

# 5. VALIDACIÓN DE EXISTENCIA
# - En buscarUsuariosPorCiudad: comprueba if len(usuarios) == 0
# - En modificarPrecio: comprueba if not productos
# - En eliminarProducto: comprueba if nombre_Producto in productos
# - En medPrecioProductos: usaría len(productos) > 0 para evitar división por cero

# 6. NORMALIZACIÓN DE DATOS
# - .strip() elimina espacios en blanco al inicio y final
# - .lower() normaliza mayúsculas/minúsculas en búsquedas de ciudad
# - Esto evita inconsistencias en los datos almacenados