import os 

os.system('çls')
lista_vacia = []
lista_numeros = [1,2,3,4,5]
lista_mixta = [1, "Dos",3.5, True]
print(lista_vacia)
print(lista_numeros)
print(lista_mixta)    
#Acceso a los elementos de una lista
print(f'3er elemento de la lista = {lista_numeros[2]}',"\n")
num0 = lista_mixta[0]
num1 = lista_mixta[1]
print(f'1er elemento = {num0} \n 2do elemento = {num1}', "\n")
#Asignar un valor a elemtnos de la lista_numeros [1,2,3,4,5]
lista_numeros [2] = lista_numeros[2]*2
print(f'3er elemnto de la lista [1,2,3,4,5] ACTUALIZADO = {lista_numeros[2]}',"\n")

#Agregar un elemento a la lista
frutas = ["manzana", "banana"]
frutas.append("naranja")
print(frutas, "\n")

#Insertar (pos, elemento): agregar un elemento en pos de la lista
frutas = ["manzana", "banana"]
frutas.insert(1, "kiwi")
print(frutas, "\n")

#Eliminar un elemento de la lista
frutas = ["manzana", "banana", "kiwi", "naaranja"]
frutas.remove("kiwi")
print("Eliminado Kiwi",frutas, "\n")
ultima = frutas.pop()
print("Ultimo elemento eliminado", frutas, "\nElemtno eliminado:", ultima, "\n")
print("\nImprime lista de numero =", lista_numeros)
buscaElemento  =lista_numeros.pop(2)
print("ELiminado elmento 2 = ", lista_numeros, "\nElemento eliminado:", buscaElemento, "\n")

#operacion con listas
#Concatenar 
lista1 = [1,2,3]
lista2 = [4,5,6]
print("Lista concatenada", lista1 + lista2, "\n")

#Repetir
lista_repetida = lista1 * 3
print("Lista repetida", lista_repetida, "\n")

#Contar elementos 
print("Cantidad de elementos en lista1", len(lista1), "\n")

#recorrer una lista

for num in lista_numeros:
    print(num)
    print("")

#Recorrer un lista modo 2 
for i in range(len(lista_numeros)):
    print(lista_numeros[i])


nums = [10, 20, 30, 40, 50]
print(nums[1:4]) # [20, 30, 40]
print(nums[:3]) # [10, 20, 30]
print(nums[3:]) # [40, 50]
print(nums[::2]) # [10, 30, 50]
print(nums[::-1]) # [50, 40, 30, 20, 10]
print(nums[-1]) # 50
print(nums[-5]) # 10
print(nums[-3:]) # [30, 40, 50]
print(nums[-3:-1]) # [30, 40]
print(nums[-1:-3]) # [] (no devuelve nada porque el rango es inválido)
print(nums[-3::-1])

#lista por comprensión
cuadrados = [x**2 for x in range(5)]
print(cuadrados) # [0, 1, 4, 9, 16]
pares = [x for x in range(10) if x % 2 == 0]
print(pares) # [0, 2, 4, 6, 8]

#Manejo de ecxcepciones
pares = [x for x in range(10)]
try:
    pares [10] = 100
except IndexError:
    print("\n Error: no se puede asignar un valor a un indice fuera de rango")

#Metodos utiles
print("\n",pares)
pos=pares.index(8)
print(f"\nPosición del elemento 8 en la lista = {pos}")
pares.append(5) #print(f'\n{pares}')
ocurrencia=pares.count(5)
print(f"\nCantidad de veces que aparece el elemento 5en la lista = {ocurrencia}")
print("\nlista sin ordenar", pares)
pares.sort()
print("\nlista ordenada", pares)
pares.sort(reverse=True) # Ordenar en orden descendente
print("\nlista ordenada de forma descendente", pares)
pares.sort(reverse=False)
pares.reverse()
print("\nlista invertida", pares)
pares.clear() # Limpiar la lista
print("\nlista limpia", pares)