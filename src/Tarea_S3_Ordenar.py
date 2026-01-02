#Generar un grupo de 10 números aleatorios
#Ordenar lista de mayor a menor usando algoritmo de ordenamiento
#Mostrar la lista ordenada en ascendente y descendente

import random as rd

list=[]

for i in range(10):
    v=rd.randint(1,20)
    list.append(v)

# otra forma de agrgar lista elmentos

list1=[rd.randint(1,20) for i in range(10)]

print(list)
print(list1)

#algoritmo ordenamiento metodo burbuja

for i in range(len(list)-1):       #Recorre la lista hasta el penultimo elemento
    
   for j in range (len(list)-1-i):
    if list[j]<list[j+1]:
        temp=list[j]
        list[j]=list[j+1]
        list[j+1]=temp

print(list)
print("descendente: ", list[::-1])      #invierte la lista original  ordenada