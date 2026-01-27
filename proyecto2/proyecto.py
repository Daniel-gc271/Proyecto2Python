# Lista de usuarios (tuplas)
usuarios = []

# Diccionario de productos
productos = {}

#Funciones de los usuarioas
def añadirUsuario():
    print("\n--- AÑADIR USUARIO ---")

    # 1. Pedir y validar ID
    id_valido = False
    while not id_valido:
        id_usuario = input("Introduce el ID del usuario: ")

        if not id_usuario.isdigit():
            print("El ID debe ser un número.")
        else:
            id_usuario = int(id_usuario)

            # Comprobar que el ID no exista
            existe = False
            for usuario in usuarios:
                if usuario[0] == id_usuario:
                    existe = True

            if existe:
                print("Ese ID ya existe. Introduce otro.")
            else:
                id_valido = True

    # Pedir nombre
    nombre = input("Introduce el nombre: ")

    # Pedir y validar edad
    edad_valida = False
    while not edad_valida:
        edad = input("Introduce la edad: ")

        if not edad.isdigit():
            print("La edad debe ser un número.")
        else:
            edad = int(edad)
            edad_valida = True

    # Pedir ciudad
    ciudad = input("Introduce la ciudad: ")

    # Crear la tupla y añadirla a la lista
    usuario = (id_usuario, nombre, edad, ciudad)
    usuarios.append(usuario)

    print("Usuario añadido correctamente.")

def mostrarUsuarios():
    print("\n--- LISTA DE USUARIOS ---")

    # Comprobar si hay usuarios
    if len(usuarios) == 0:
        print("No hay usuarios registrados.")
    else:
        for usuario in usuarios:
            print(f"ID: {usuario[0]}")
            print(f"Nombre: {usuario[1]}")
            print(f"Edad: {usuario[2]}")
            print(f"Ciudad: {usuario[3]}")
            print("------------------------")

def buscarUsuarioPorId():
    print("\n--- BUSCAR USUARIO POR ID ---")

    # Comprobar si hay usuarios registrados
    if len(usuarios) == 0:
        print("No hay usuarios registrados.")
    else:
        # Pedir y validar ID
        id_valido = False
        while not id_valido:
            id_buscar = input("Introduce el ID del usuario: ")

            if not id_buscar.isdigit():#isdigit() asegura que solo se introduzcan números
                print("El ID debe ser un número.")
            else:
                id_buscar = int(id_buscar)
                id_valido = True

        # Buscar el usuario
        encontrado = False
        for usuario in usuarios:
            if usuario[0] == id_buscar:
                print("\nUsuario encontrado:")
                print(f"ID: {usuario[0]}")
                print(f"Nombre: {usuario[1]}")
                print(f"Edad: {usuario[2]}")
                print(f"Ciudad: {usuario[3]}")
                encontrado = True

        if not encontrado:
            print("No existe ningún usuario con ese ID.")

def buscarUsuariosPorCiudad():
    print("\n--- BUSCAR USUARIOS POR CIUDAD ---")

    # Comprobar si hay usuarios registrados
    if len(usuarios) == 0:
        print("No hay usuarios registrados.")
    else:
        ciudad_buscar = input("Introduce la ciudad: ")

        encontrado = False

        for usuario in usuarios:
            if usuario[3].lower() == ciudad_buscar.lower():
                print("\nUsuario encontrado:")
                print(f"ID: {usuario[0]}")
                print(f"Nombre: {usuario[1]}")
                print(f"Edad: {usuario[2]}")
                print(f"Ciudad: {usuario[3]}")
                print("------------------------")
                encontrado = True

        if not encontrado:
            print("No hay usuarios registrados en esa ciudad.")

#Funciones de los Productos
def añadirProducto():
    print("\n--- AÑADIR PRODUCTO ---")

    #Pedir nombre del producto, el nombre será la clave del diccionario
    nombre = input("Introduce el nombre del producto: ")

    #Comprobar si el producto ya existe
    if nombre in productos:
        print("Ese producto ya existe.")
    else:#Pedir y validar precio       
        precio_valido = False
        while not precio_valido:
            precio = input("Introduce el precio del producto: ")

            try:
                precio = float(precio)
                if precio < 0:
                    print("El precio no puede ser negativo.")
                else:
                    precio_valido = True
            except ValueError:
                print("El precio debe ser un número.")

        # Añadir producto al diccionario
        productos[nombre] = precio
        print("Producto añadido correctamente.")

def modificarPrecio():
    print("\n--- MODIFICAR PRECIO DE PRODUCTO ---")

    # Comprobar si hay productos registrados
    if len(productos) == 0:
        print("No hay productos registrados.")
    else:
        nombre = input("Introduce el nombre del producto a modificar: ")

        # Comprobar si existe el producto
        if nombre not in productos:
            print("Ese producto no existe.")
        else:
            # Pedir y validar el nuevo precio
            precio_valido = False
            while not precio_valido:
                nuevo_precio = input("Introduce el nuevo precio: ")

                try:
                    nuevo_precio = float(nuevo_precio)
                    if nuevo_precio < 0:
                        print("El precio no puede ser negativo.")
                    else:
                        precio_valido = True
                except ValueError:
                    print("El precio debe ser un número.")

            # Actualizar el precio
            productos[nombre] = nuevo_precio
            print("Precio actualizado correctamente.")

def eliminarProducto():
    print("\n--- ELIMINAR PRODUCTO ---")

    # Comprobar si hay productos
    if len(productos) == 0:
        print("No hay productos registrados.")
    else:
        nombre = input("Introduce el nombre del producto a eliminar: ")

        # Comprobar si el producto existe
        if nombre not in productos:
            print("Ese producto no existe.")
        else:
            # Eliminar el producto usando del
            del productos[nombre]
            print("Producto eliminado correctamente.")

def mostrarProductos():
    print("\n--- LISTA DE PRODUCTOS ---")

    # Comprobar si hay productos
    if len(productos) == 0:
        print("No hay productos registrados.")
    else:
        for nombre, precio in productos.items():
            print(f"Producto: {nombre}")
            print(f"Precio: {precio} €")
            print("------------------------")

#Funciones de las estadisticas
def mostrarEstadisticas():
    print("\n--- ESTADÍSTICAS ---")

    # ====== Estadísticas de USUARIOS ======
    print("\n[Usuarios]")
    total_usuarios = len(usuarios)
    print(f"Total de usuarios: {total_usuarios}")

    if total_usuarios == 0:
        print("No se puede calcular edad media ni extremos (no hay usuarios).")
    else:
        # Sumar edades para la media
        suma_edades = 0
        for u in usuarios:
            suma_edades += u[2]  # u[2] es la edad, por si acaso

        edad_media = suma_edades / total_usuarios

        # Encontrar más joven y más mayor
        # (recorremos una vez y vamos guardando al mejor candidato)
        mas_joven = usuarios[0]
        mas_mayor = usuarios[0]

        for u in usuarios:
            if u[2] < mas_joven[2]:
                mas_joven = u
            if u[2] > mas_mayor[2]:
                mas_mayor = u

        print(f"Edad media: {edad_media:.2f} años")
        print(f"Usuario más joven: ID {mas_joven[0]} - {mas_joven[1]} ({mas_joven[2]} años, {mas_joven[3]})")
        print(f"Usuario más mayor: ID {mas_mayor[0]} - {mas_mayor[1]} ({mas_mayor[2]} años, {mas_mayor[3]})")

    # ====== Estadísticas de PRODUCTOS ======
    print("\n[Productos]")
    total_productos = len(productos)
    print(f"Total de productos: {total_productos}")

    if total_productos == 0:
        print("No se puede calcular el precio medio (no hay productos).")
    else:
        # Sumar precios para la media
        suma_precios = 0.0
        for precio in productos.values():
            suma_precios += precio

        precio_medio = suma_precios / total_productos
        print(f"Precio medio: {precio_medio:.2f} €")

#Submenu de Productos
def menuProductos():
    volver = False
    while not volver:
        print("\n--- MENÚ DE PRODUCTOS ---")
        print("1. Añadir producto")
        print("2. Mostrar productos")
        print("3. Modificar precio")
        print("4. Eliminar producto")
        print("5. Volver al menú principal")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            añadirProducto()
        elif opcion == "2":
            mostrarProductos()
        elif opcion == "3":
            modificarPrecio()     
        elif opcion == "4":
            eliminarProducto()
        elif opcion == "5":
            volver = True
        else:
            print("Opción no válida.")

#Submenu de busquedas
def menuBusquedas():
    volver = False

    while not volver:
        print("\n--- MENÚ DE BÚSQUEDAS ---")
        print("1. Buscar usuario por ID")
        print("2. Buscar usuarios por ciudad")
        print("3. Volver al menú principal")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            buscarUsuarioPorId()
        elif opcion == "2":
            buscarUsuariosPorCiudad()
        elif opcion == "3":
            volver = True
        else:
            print("Opción no válida.")

#Menu Principal
def menuPrincipal():
    salir = False
    while not salir:
        print("\n--- GESTOR INTELIGENTE DE DATOS ---")
        print("1. Añadir usuario")
        print("2. Mostrar usuarios")
        print("3. Gestión de productos") 
        print("4. Estadísticas")
        print("5. Búsquedas")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            añadirUsuario()
        elif opcion == "2":
            mostrarUsuarios()
        elif opcion == "3":
            menuProductos()         
        elif opcion == "4":
            mostrarEstadisticas()
        elif opcion == "5":
            menuBusquedas()
        elif opcion == "6":
            print("Saliendo del programa...")
            salir = True
        else:
            print("Opción no válida. Inténtalo de nuevo.")
                      
#Funcion principal del main
def main():
    menuPrincipal()          
    
    

#main
main()               