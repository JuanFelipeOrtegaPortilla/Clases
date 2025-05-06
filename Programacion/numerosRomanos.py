import os  
os.system ('cls')
import re
numero = input("Ingrese un numero romano")
numero = numero.upper
valida = True
for caracter in numero:
    if caracter != "I" and caracter != "V" and caracter != "X" and caracter != "L" and caracter != "C" and caracter != "D" and caracter != "M":
        valida = False
        break
if valida:
    print("Es un numero romano")
else:
    print("No es un numero romano")

#---------------------------------------------------------------
#Patron regular
#---------------------------------------------------------------
patron = r'^[IVXLCDM] + $'
numero = input("Ingrese el numero romano")
valida = re.search(patron, numero)
if valida:
    print(f"Cadena {numero} contiene solo  caracters de numero Romano")
else: 
    print(f"Cadena {numero} No contiene solo caracteres de numero Romano")
    

