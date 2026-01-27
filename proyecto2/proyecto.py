# Lista de usuarios (tuplas)
usuarios = []

# Diccionario de productos
productos = {}

#Funciones de los usuarioas
def añadir_usuario():
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

def mostrar_usuarios():
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

def buscar_usuario_por_id():
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

def buscar_usuarios_por_ciudad():
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
def añadir_producto():
    """Añade un producto al diccionario."""
    pass


def eliminar_producto():
    """Elimina un producto del diccionario."""
    pass

def mostrar_productos():
    """Muestra todos los productos disponibles."""
    pass

#Funciones de las estadisticas
def mostrar_estadisticas():
    """Muestra estadísticas de usuarios y productos."""
    pass


#Submenu de busquedas
def menu_busquedas():
    volver = False

    while not volver:
        print("\n--- MENÚ DE BÚSQUEDAS ---")
        print("1. Buscar usuario por ID")
        print("2. Buscar usuarios por ciudad")
        print("3. Volver al menú principal")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            buscar_usuario_por_id()
        elif opcion == "2":
            buscar_usuarios_por_ciudad()
        elif opcion == "3":
            volver = True
        else:
            print("Opción no válida.")

#Menu Principal
def menu_principal():
    salir = False

    while not salir:
        print("\n--- GESTOR INTELIGENTE DE DATOS ---")
        print("1. Añadir usuario")
        print("2. Mostrar usuarios")
        print("3. Añadir producto")
        print("4. Mostrar productos")
        print("5. Estadísticas")
        print("6. Búsquedas")
        print("7. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            añadir_usuario()
        elif opcion == "2":
            mostrar_usuarios()
        elif opcion == "3":
            añadir_producto()
        elif opcion == "4":
            mostrar_productos()
        elif opcion == "5":
            mostrar_estadisticas()
        elif opcion == "6":
            menu_busquedas()
        elif opcion == "7":
            print("Saliendo del programa...")
            salir = True
        else:
            print("Opción no válida. Inténtalo de nuevo.")
            
                      
#Funcion principal del main
def main():
    menu_principal()          
    
    

#main
main()               