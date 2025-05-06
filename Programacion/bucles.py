import os
os.system('cls')

#for ( repita para n valores)
for i in range(5):
    print(f'\nEl valor de i es: {i}')

#For (reputa desde hasta)
for i in range (3,6):
    print(f'\nEl valor de i es: {i}')

#For (repita desde hasta de salto en salto)
for i in range (1,10,2):
    print(f'\n El valor de i es: {i}')

#For(repita para n valores desendentes)
for i in range (10,1,-2):
        print(f'\n El valor de i es: {i}')

#For (cadenas)
cadena = "Hola mundo"
for i in cadena:
     print(f'\nEl carcter es: {i}')

#For (cadena y for)
for i in range (1,5): 
     caracter = str(i)
     print(f'EL caracter: {caracter*i}')

