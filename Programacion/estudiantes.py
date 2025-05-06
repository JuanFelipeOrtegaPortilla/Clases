


import os
os.system('cls')  


with open("notasEstediante.txt", "r") as file:
    mayor = 0
    for i in range(5):  
        nombre = file.readline()
        suma = 0
        
        for j in range(1,6): 
            nota = float(file.readline().strip())  
            suma += nota
        promedio = suma / 5  

        
        print(f'{nombre} - El promedio es: {promedio:.2f}')
        if mayor < promedio:
            mayor = promedio
            nombreMayor = nombre 

    print(f'\nEl mayor es: {mayor} del estudiante {nombreMayor}')




    