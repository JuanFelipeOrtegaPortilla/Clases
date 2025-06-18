import os 
os.system('cls')
from datetime import date 
import re 

cambioUsuario = False
cambioCatalogo = False
dicLibros = {}
dicUsuario = {}
dicPrestamos = {}
def cargarArchivo():
    try:
        libros = open("libros.txt", "r", encoding="utf-8")
        usuario = open("usuario.txt", "r", encoding="utf-8")
        prestamos = open("prestamos.txt", "r", encoding="utf-8")
    except FileNotFoundError:
        print("No se pudo abrir los archivos")
    else:
        #Libros
        for linea in libros:
            partes = linea.strip().split('|')
            if len(partes) < 5:
                continue
            ide, nombre, autor, genero, disponibilidad = partes
            dicLibros[ide] = [nombre, autor, genero, disponibilidad]
        #Usuario
        for linea in usuario:
            partes = linea.strip().split('|')
            if len(partes) < 5:
                continue
            ides, nombreU, correo, prestamo, montoMulta = partes
            dicUsuario[ides] = [nombreU, correo, prestamo, montoMulta]

        #Leer Prestamos 
        for linea in prestamos:
            partes = linea.strip().split('|')
            if len(partes) < 4:
                continue
            ide, ides, fechaPrestamo, fechaEntrega = partes
            dicPrestamos[ide + ides] = [fechaPrestamo, fechaEntrega]

        libros.close()
        usuario.close()
        prestamos.close()

    return dicUsuario, dicLibros, dicPrestamos

def menuPrincipal():
    os.system('cls')
    print("----------Bienvenido a la Biblioteca-----------")
    print("1.Gestionar libros \n 2.Gestion Usuarios \n 3.Prestamo libro \n 4. Devolucion de libro \n 5. Reportes \n 6. Salir \n")
    opcion = int(input("Seleccione una opcion 1-6"))
    return opcion
    

def ejecutarAccion(opcion: int) -> int:
    salida = 0

    if opcion == 1:
        opc2 = menuGesLibro()
        while opc2 != 5:
            if opc2 == 1:
                print("agregarLibro()")
            elif opc2 == 2:
                print("consultarLibro()")
            elif opc2 == 3:
                print("modificarLibro()")
            elif opc2 == 4:
                print("eliminarLibro()")
            else:
                salida = -1
            opc2 = menuGesLibro()  # Volver a mostrar el menú

    # elif opcion == 2:
    #     opc3 = menuGesUsuario()
    #     while opc3 != 5:
    #         if opc3 == 1:
    #             print("añadirUsuario()")
    #         elif opc3 == 2:
    #             print("consultarUsuario()")
    #         elif opc3 == 3:
    #             print("modificarUsuario()")
    #         elif opc3 == 4:
    #             print("eliminarUsuario()")
    #         else:
    #             salida = -1

    elif opcion == 3:
        opc3=menuPrestamo()
        if opc3==1:
            prestamo()

    # elif opcion == 4:
    #     menuDevolucion()

    # elif opcion == 5:
    #     menuReportes()

    else:
        salida = -1

    return salida

      
def menuGesLibro():
    print("------Menu Libro-----")
    print("1. agregar \n 2.Consutar \n 3. Modificar \n 4. Eliminar \n 5.Regresar")
    opcion = int(input("Ingrese la opcion (1-5)"))
    return opcion

def MenuUsuarios():
    print("-------Menu Usuario----")
    print("1. Añadir Usuario\n 2. Consultar Usuario, 3.Modificar\n 4.Eliminarm\n 5.Regresar")
    opcion = int(input("Ingrese una opcion (1-4)"))
    return opcion
def MenuDevolucion():
    print("Menu Devolucion")
    print("1. Ingreso de fecha\ ")

def menuPrestamo():
    print("1. Hacer prestamo \n 2. Consulta multas \n 3.Regresar")
    opcion = int(input("Ingrese una opcion (1-3)"))
   
    prestamo()
    # validarMultas()
    return opcion

def prestamo():
    
    usuario = input("Ingrese el ID del usuario")
    ok = validarUsuario(usuario)
    if ok:
        libro = input("Ingrese el ID del libro")
        if validarLibro(libro):
            ahora = date.today()
            print("libro prestado")

def validarUsuario(ides):
    datoUsuario= dicUsuario.get(ides,[])
    if len(datoUsuario) > 0:
        if int(datoUsuario[2]) < 3 and int(datoUsuario[3]) <= 10 :
            return True
        else:
            return False
    else:
        print("El usuario no existe")
        return False
               
def validarLibro(ide):
    datolibro = dicLibros.get(ide)
    if int(datolibro[3]) == 0:
        return True
    return False


# def validarMultas(fechaSalida,fechaEntrega):
#     multas = dicPrestamos.get(fechaSalida, fechaEntrega)    
#     multaUsuario = dicUsuario.get(prestamos)
#     if multaUsuario < 3 :
#         return True
#     else:
#         return False
    
    

    

# def DevolucionLibro():
#     #retraso fecha 
#     #validar multa


# def reportes():
#     #libros Prestados
#     #UsuariosActivos
    

if __name__ == "__main__":
    datosUsuario, datosCatalogos, dicPrestamos = cargarArchivo()
    opcion = menuPrincipal()
    while opcion != 6 :
        edo=ejecutarAccion(opcion)
        if edo == -1:
            print("Opcion invalida")
        opcion = menuPrincipal()
    print(dicPrestamos)
    print("Adios")
    # print("Usuarios cargados:")
    # print(datosUsuario)
    # print("\nLibros cargados:")
    # print(datosCatalogos)
    # print("\nPrestamos cargados:")
    # print(dicPrestamos)