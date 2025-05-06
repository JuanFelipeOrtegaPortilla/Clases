import os 
os.system('cls')
#Excepcion con ValueError
# try:
#     num =int(input("Ingrese un numero: "))
#     print(num)
# except ValueError:
#     print("Error")

# else: 
#     num = num +10 
# finally:
#     print("El numeor finas es: ",  num)
#----------------------------------------------------------
# Excepcion con  el TypeError
#----------------------------------------------------------
    
# a = 10 
# b = '20'

# try: 
#     c= a + b
# except TypeError:
#     print("Error, los argumentos deben ser numeros")
# else:
#     print(f"El resultado de la suma es: {c}")
#----------------------------------------------------------
#Excepcion DivisionZero 
#----------------------------------------------------------

# try :
#     10/0
# except Exception as e:
#     print("Error")


# try: 
#     10/0 
# except ZeroDivisionError:
#     print("Division por cero")

#----------------------------------------------------------
#Excepcion File not found 
#----------------------------------------------------------
# try:
#     mi_archivo = open("myfile.txt","r")
# except FileNotFoundError:
#     print("Lo siento el archivo no existe ")
# else: 
#     contenido = mi_archivo.read() 
#     print(contenido)
#     mi_archivo.close()
# finally:
#     print("Hola - Bye ".center(80))

#----------------------------------------------------------
#Excepcion Name Error
#----------------------------------------------------------
# try: 
#     print("La variable no existe")
#     a = 4-d
# except NameError: 
#     print("Variable no definida")

# try: 
#     with open('archivo.text',"r") as file:
#         data  = file.read()
#         print(data)

#----------------------------------------------------------
# except FileNotFoundError:
#----------------------------------------------------------

#     print("Error, archivo no encontrado")
# except IOError:
#     print("Error: No se pudo leer el archivo")
# finally: 
#     print("Fin  del bloque try-except")

#----------------------------------------------------------
#Lectura de archivo por lineas 
#----------------------------------------------------------

# archivo = input("De el nombre del archivo: ")
# archivo = archivo +"txt"
# file = open(archivo, "r")

# for line in file:
#     print(line)
intentos = 3
while intentos > 0:

    try: 
        archivo = input("De el nombre del archivo: ")
        archivo = archivo +".txt"
        file = open(archivo ,"r")
    except FileNotFoundError:
        print(f"Lo siento {archivo} no existe")
        intentos -=1

    else: 
        for line in file:
            print(line)
        file.close()
        break
    finally: 
        print("\n\n Bye \n\n")
    
    


