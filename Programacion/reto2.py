if __name__ == "__main__":
    
    file = open("misDatos.txt", "r+")
    
 
    nombre = file.readline().strip()
    
   
    nota1 = int(file.readline().strip())
    nota2 = int(file.readline().strip())
    nota3 = int(file.readline().strip())
    
 
    file.close()
    
    
    if nota1 > nota2 and nota1 > nota3:
        num_Mayor = nota1
        if nota2 > nota3:
            num_medio = nota2
            num_bajo = nota3
        else:
            num_medio = nota3
            num_bajo = nota2
    elif nota2 > nota1 and nota2 > nota3:
        num_Mayor = nota2
        if nota1 > nota3:
            num_medio = nota1
            num_bajo = nota3
        else:
            num_medio = nota3
            num_bajo = nota1
    else:
        num_Mayor = nota3
        if nota1 > nota2:
            num_medio = nota1
            num_bajo = nota2
        else:
            num_medio = nota2
            num_bajo = nota1

   
    file = open("datos_Salida.txt", "w")
    
    file.write(str(num_Mayor) + "\n")
    file.write(str(num_medio) + "\n")
    file.write(str(num_bajo) + "\n")
    
    
    file.close()













































