import datetime as dt       #Para fecha y hora actualizada
import random as rd         #IMPORTAR FUNCIONES- MODULO ALEATORIO

nombre="Luis"               #CONSTANTE
fecha1="2023-10-12"         #CONSTANTE
print("Hi Ing:Electrónico " + nombre + " " + fecha1)       #too print("Hi Ing:Electrónico " , nombre)


#fUNCION DE FECHA AUTUALIZADA
fecha2= dt.datetime.now().strftime("%Y-%m-%d %H: %M: %S")
print( fecha2)              #salida de variable fecha2     

#IMPRIMIR PARTE: FUNCION- MODULO ALEATORIO
# cambiar de posicion: v=rd.randint(0,15)                        #VALORES ALEATORIOS ENTRE 0- 1023
#print("voltaje medido1: " + str(v))         #SALIDA USANDO STR, PARA CONVERTIR V A TEXTO
                                            #SI NO USAS EL STR NO COMPILA
#print(f"volataje medido2 {v}")              #OTRA FORMA

#TAREA1 GENERAR UN CORREO ELECTRONICO CON NAME AND DATE QUE MUESTRE AL INGENIERO EN JEFE
#VALORES MEDIDOS POR EL SENSOR Y LA FECHA DE MEDICION

#Esta solo envia un valor
print("fecha: "+fecha2)
print("Ingeniero Joko buenos días. Mi nombre es :"+nombre)
print("A continuacion le envio los datos obtenidos del sensor")

#AHORA PARA ENVIAR VARIOS

for data in range(10):
    #agregamos aqui el random para que cambie cada vez.

    v=rd.randint(0,1023) 
    if v <100:
        print("voltaje medido: " +str(v) + "V : Bajo")
    elif v<500:
        print("voltaje medido:"+ str(v) + " V: Medio")
    else:
        print("voltaje medido:"+ str(v)+ " V: Alto")


    #antes: print("voltaje medido : "+ str(data+1) + ": " + str(v) + " " + "V")

    # sino colocamos STR a dta a V no compila ya que data y v son numeros
    # y no se puede concatenar numeros (int) con texto STR
    #otra forma
    #print(f"voltaje medido:  {data+1} -> {v} v ")


