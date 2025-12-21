
import random as rd




NOMBRE="Luis"        #constante - convencion str
edad=20              #int 
voltaje=3.1415       #float
activo= True         #bool

print(type(voltaje))        #sirve para verificar variables

# para concatenar sin usar str
print(f"hola, {NOMBRE}")
#ANTES
print("hola "+ NOMBRE)       #O STR(NOMBRE) SI ES QUE FUESE UNA VARIABLE O UN NUMERO
print(f"voltaje medido: {voltaje:.3f}") #:.2f sirve para acotar decimales

#///////////////////-----Correo-----/////////////////////
print(f"Bueno días ingeniero Joko le saluda {NOMBRE} edad: {edad}")
print(f" a continuacion le envio los datos obtenidos durate la semana")

dias={"Lunes", "Martes", "Miercoles", "Jueves", "viernes", "Sabado", "Domingo"}

for i in dias:
    print(f"{i}")
    v=rd.randint(0,1023)
    print(f"voltaje medido: {v} {'Activo' if v>0 else 'Off'  }")    #operador ternario bloque true IF condicion ELSE bloque false
    print