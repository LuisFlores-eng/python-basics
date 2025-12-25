import random as rd
list=[]        #lista vacia

#//////-----numeros aleatorios agregar a list-----
for i in range(5):  # 5 iteraciones 
    num=rd.randint(1,10)    #Aleatorios del 1-10
    list.append(num)
print(list)

#----- imprimir los valores de la lista V elevado al cudrado-----

V=[4.5, 2.32, 4.88]

for i in V:
    a=i*i                                                       #los valores son: 23.8144, 23.8144, 23.8144
print(f"los valores son: {', '.join([f'{a}' for i in V ])}")    # Se usa JOIN para juntar los valore de la lista con ","
print("---------------------------")

#-----enumerar los de V-----
#idx es el numero de orden que le corresponde
#voltatge es la variable de salida correspondiente a la posicion del idx
#"enumerate" es fijo, V se refiere a la ,lista en que buscará y start=1 significa que comienze desde 1
for idx, voltage in enumerate(V, start=1):
    print(f"{idx}: {voltage:.2f}")
for idx, voltaje in enumerate(V, start=1):
    print(f"{idx}: {voltaje:.2f}")

print("---------------")
#-----Ejercicio-----
# crear una lista aleatoria de 10 valores
# verificar si los valores son mayores o menores a 5V
#imprimir en cada caso, voltaje alto - bajo

#solución
#Este codigo está bine sin embargo no es reutilizable. Tú idea es hacer el codigo
#lo más simple y corto(está bien) pero esta muy anidadado es decir muchas líneas
#depende de otros y al momento de querer cambiar algo tendras que cambiar todo
# VER NUEVAS ALTERNATIVAS ARCHIVO S3-separacion.py

list_eg=[]      #creaer lista vacia que almacene los nuemro aleatorios

for i in range(10):         #10 iteraciones para 10 aleatorios
    random=rd.randint(0,10)
    list_eg.append(random)
    print(f"volataje medido:{'VOLTAJE ALTO ' if random>5 else 'VOLTAJE BAJO'}")
print(list_eg)



print("---------------")