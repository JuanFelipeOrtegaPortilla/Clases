if __name__=='__main__':
    file= open("myFile.txt","w")
    file.write("Hola a todos\n")
    file.writelines(["Es un buen dia "," Para aprender"])
    cadena= "\nHasta pronto "
    file.write(cadena)
    dato=str(33)
    file.write(dato)
    file.close()


    file = open("myFile.txt","r")
    file.readline()
    lineas1= file.readline()
    linea2= file.readline()
    print("Linea1 = ",lineas1)
    print("Linea2 =",linea2)
    file.close()

    
    # salida= file.read()
    # print(salida)
    # file.close()

