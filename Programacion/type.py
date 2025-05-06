import os 
os.system('cls')
my_var = 10
print(f'El tipo es: {type(my_var)}')
print(f'\nEl Id: {id(my_var)}')

my_var = 20 
print(f'El tipo es: {type(my_var)}')
print(f'\nEl Id: {id(my_var)}')
print()

my_var = int(input("ingrese un numero: "))
my_var1 = int(input("ingrese un numero: "))
#if corto 
mayor =  my_var if my_var > my_var1 else my_var1
print(f'\nEl mayor es: {mayor}\n')

menor = my_var if my_var < my_var1 else my_var1
print(f'\nEl menor es: {menor}\n')

    


