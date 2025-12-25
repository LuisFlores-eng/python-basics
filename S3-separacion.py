import random as rd

#-----Ejercicio-----
# crear una lista aleatoria de 10 valores
# verificar si los valores son mayores o menores a 5V
#imprimir en cada caso, voltaje alto - bajo

#solución

Vinput=[]       #lista que almacena voltaje de ingreso
Vmenor=[]
Vmayor=[]

for i in range(10):     #10 iteraciones para 10 numero aleatorios
    random= rd.randint(1,10)
    if random >5:
        Vmayor.append(random)
    else:
        Vmenor.append(random)
print(Vmenor)
print(Vmayor)

print("----------------------")
# Another way

Vinput2=[]       #lista que almacena voltaje de ingreso
Vmenor2=[]
Vmayor2=[]

for i in range(10):
    Vinput2.append(rd.randint(1,10))
print(Vinput2)   #se emprime la lista con todo sus parentesis
                            #una alternativa habría sido usar
for i in Vinput2:            #range(len(Vint)) y luego usar otro for para imprimir cada valor de la lista.

    if i>=5:
        Vmayor2.append(i)
    else:
        Vmenor2.append(i)

print(Vmayor2)
print(Vmenor2)

print("----------------------")

#-----Ejercicio-----
# Generar 20 valores hasta 30v en aleatorio
# separar en voltaje: ALTO-MEDIO-BAJO

Vinput0=[]       #lista que almacena voltaje de ingreso
low_voltage=[]
medium_voltage=[]
high_voltage=[]

for i in range(20):
    Vinput0.append(rd.randint(1,30))
print(Vinput0)   #se emprime la lista con todo sus parentesis
                            #una alternativa habría sido usar
for i in Vinput0:            #range(len(Vint)) y luego usar otro for para imprimir cada valor de la lista.

    if i<=8:
        low_voltage.append(i)
    elif i<=15:
        medium_voltage.append(i)
    else:
        high_voltage.append(i)

print(low_voltage)
print(medium_voltage)
print(high_voltage)


print("----------------------")