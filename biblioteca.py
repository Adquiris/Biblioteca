from basededatos import BaseDeDatos
import os


def menuLibros():
    os.system('cls')
    print("\nHorizonte Literario")
    print("\nMenu")
    
    print("1. Ingresar un libro.")
    print("2. Informacion de un libro.")
    print("3. Lista de libros.")
    print("4. Cambiar la informacion del libro.")
    print("5. Eliminar un libro registrado.")
    print("6. Eliminar los libros registrados.")
    print("7. Para volver al menu principal.")
    decision2 = int(input("\nIngresa la opcion que desees ingresar: "))
    os.system('cls')

    if decision2 == 1:
        titulo = input("\nIngrese el titulo: ")
        genero = input("\nIngrese el genero del libro: ")
        anio = int(input("\nIngrese el año de publicacion: "))

        bd.insertarLibro(titulo, genero, anio)
        os.system('cls')

    elif decision2 == 2:
        id = int(input("Ingrese el ID del libro que deseas consultar: "))

        bd.imprimirLibro(id)
        os.system('pause')
        
    elif decision2 == 3:
        bd.imprimirTabla('LIBROS')
        os.system('pause')

    elif decision2 == 4:
        id = input("Ingrese el id del libro: ")
        titulo = input("\nIngrese el titulo: ")
        anio = int(input("\nIngrese el año de publicacion: "))
        genero = input("\nIngrese el genero del libro: ")
        disponible = bool(input("Esta disponible? 1. Si 2. No: "))

        bd.actualizarLibro(id, titulo, anio, genero, disponible)

    elif decision2 == 5:
        id = input("Ingrese el id del libro que desea eliminar: ")
        bd.eliminarLibro(id)

    elif decision2 == 6:
        respuesta = int(input("Estas seguro que deseas eliminar todos los regirtros? 1.Si 2.No:  "))
        if respuesta == 1:
            bd.eliminarRegistros('LIBROS')
        else:
            return False

    else:
        return True
    return False


#-------------------------------------------------------------------------------------------------------------------

def menuUsuarios():
    os.system('cls')
    print("\nHorizonte Literario")
    print("\nMenu")
    
    print("1. Ingresar un usuario.")
    print("2. Informacion de un usuario.")
    print("3. Lista de usuarios.")
    print("4. Cambiar la informacion del usuario.")
    print("5. Eliminar un usuario registrado.")
    print("6. Eliminar los usuarios registrados.")
    print("7. Para volver al menu principal.")
    decision2 = int(input("\nIngresa la opcion que desees ingresar: "))
    os.system('cls')

    if decision2 == 1:
        nombre = input("\nIngrese el nombre del usuario: ")
        correo = input("\nIngrese el correo del usuario: ")
        num_contacto = int(input("\nIngrese el numero de contacto: "))

        bd.insertarUsuario(nombre, correo, num_contacto)
        os.system('cls')

    elif decision2 == 2:
        id = int(input("Ingrese el ID del usuario que deseas consultar: "))

        bd.imprimirUsuario(id)
        os.system('pause')
        
    elif decision2 == 3:
        bd.imprimirTabla('USUARIOS')
        os.system('pause')

    elif decision2 == 4:
        id = input("Ingrese el id del usuario: ")
        nombre = input("\nIngrese el titulo: ")
        correo = int(input("\nIngrese el año de publicacion: "))
        contacto = input("\nIngrese el genero del usuario: ")
        
        bd.actualizarUsuario (id, nombre, correo, contacto)

    elif decision2 == 5:
        id = input("Ingrese el id del usuario que desea eliminar: ")
        bd.eliminarUsuario(id)
        
    elif decision2 == 6:
        respuesta = int(input("Estas seguro que deseas eliminar todos los regirtros? 1. Si 2. No:  "))
        if respuesta == 1:
            bd.eliminarRegistros('USUARIOS')
        else:
            return False

    else:
        return True
    return False


#-------------------------------------------------------------------------------------------------------------------

bd = BaseDeDatos()
bd.crearTablaLibros()
bd.crearTablaUsuarios()


while True:
    os.system('cls')
    print("\nHorizonte Literario")
    print("\nMenu")
    print("1. Libros")
    print("2. Usuarios")
    print("3. Para salir del programa.")
    decision = int(input("\nIngresa la opcion que desees realizar: "))

    if decision == 3:
        break
    salir = False
    while not salir:
        if decision == 1:
            salir = menuLibros()
        elif decision == 2:
            salir = menuUsuarios()

        else:
            salir = True
