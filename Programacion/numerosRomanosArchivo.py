import os
import re

os.system('cls')  

archivo = input("De el nombre del archivo: ")
archivo += ".txt"

patron = r"^[IVXLCDM]+$"

try:
    with open(archivo, "r") as file:
        for line in file:
            line = line.strip().upper()
            print(f"\nCadena leída: {line}")
            valida = re.match(patron, line)

            if valida:
                print(f"Cadena '{line}' contiene solo caracteres de números Romanos")

                total = 0
                anterior = 0
                i = len(line) - 1

                while i >= 0:
                    letra = line[i]

                    if letra == 'I':
                        valor = 1
                    elif letra == 'V':
                        valor = 5
                    elif letra == 'X':
                        valor = 10
                    elif letra == 'L':
                        valor = 50
                    elif letra == 'C':
                        valor = 100
                    elif letra == 'D':
                        valor = 500
                    elif letra == 'M':
                        valor = 1000
                    else:
                        valor = 0

                    if valor < anterior:
                        total -= valor
                    else:
                        total += valor
                        anterior = valor
                    i -= 1

                print(f"Valor decimal: {total}")
            else:
                print(f"Cadena '{line}' NO contiene solo caracteres de números Romanos")

except FileNotFoundError:
    print(f'\nLo siento, el archivo "{archivo}" no existe')
finally:
    print("Bye".center(80))








