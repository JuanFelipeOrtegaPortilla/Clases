import os 
os.system('cls')  

#Ejercicio 1
n = int(input("Ingrese el valor de n: "))
while n <= 0:
    print("Error, ingrese un entero positivo")
    n = int(input("Ingrese el valor de n: "))


a = int(input("Ingrese el primer termino: "))
while a < 0:
    print("Ingrese un número mayor o igual a 0")
    a = int(input("Ingrese el primer termino: "))


r = int(input("Ingrese la razon: "))
while r < 0:
    print("Ingrese un número mayor o igual a 0")
    r = int(input("Ingrese la razon: "))


suma = 0
for i in range(n):
    suma += a * (r ** i)  


print(f"La suma de la progresión geométrica es: {suma}")


#Ejercicio 2 
binario = input("Ingrese un número binario: ")
decimal = 0
i = 0

for digito in reversed(binario):
    decimal += int(digito) * (2 ** i)
    i += 1

print("Decimal:", decimal)




