import os 
import re
os.system('cls')
intentos = 3 

while intentos > 0 :
    archivo =  input("\nDe el nombre del archivo: ")
    archivo += ".txt"
    patron = r"^[IVXLCDM]+$"

    try: 
        archivo = open(archivo, "r")

    except FileNotFoundError: 
        print(f'\nLo siento, el archivo "{archivo}" no existe')
        intentos -=  1
    else:
        break

if intentos > 0: 
    try: 
        archivo2 = open("archivo2" , "w")
    except IOError:
        print("No se pudo crear el archivo")
        exit()
    else:
        print("Se arbio el archivo correctamente ")
        for line in archivo:
         archivo2.write(line) 

else:
    print("\nSe agotaron los intentos")





 

