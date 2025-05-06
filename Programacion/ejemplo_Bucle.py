import os 
os. system('cls')
#Ejemplo
# blanco = " "
# caracter = "*"

# j =10
# for i in range(1,10,2):
#     print(blanco*j,caracter*i)
#     j=j-1
# for i in range(1,4):
#     print(blanco*10, caracter)

# for i in range(2):
#     print(blanco*7, caracter)
#     caracter='\-----/'

# print(f'El valor de i es: {i}')


for i in range( 1,10):
    print()
    print(f'\nTabla del {i}')
    print()
    for j in range(1,10):
        print(f'{i}*{j}={i*j}')
        if j == 5:
            
             break
    if i == 7:
        
         break    
print(f'\nSaiendo de Tabla \n\n\n')


for i in range(1, 10):
    print(f'\nTabla del {i}')
    print()
    
    for j in range(1, 10):  
        if i == 7: 
            continue
        if j == 5:  
            continue
        print(f'{i} * {j} = {i * j}')

print(f'\nSaliendo de la Tabla\n\n\n')

