MODE1="UMBRAL_BAJO"
MODE2="UMBRAL_MEDIO"
MODE3="UMBRAL_ALTO"
STUDENT="lUIS"
accumulate=0                #Declarar variable como número
list=[]                     # Variable como lista que almacena valores de voltaje o tempertura 

str1=input("Enter your name ")
str2=input("Enter the name of the electronic device ")
num_samples=int(input("Enter the number of samples "))
user_choice=int(input("choose an option 1- VOLTAGE OR 2- TEMPERATURE "))

try:
    # logica condicional segun la leccion del usuario 1-2
    if user_choice==1:
        
        
        for i in range(0,2):
            voltage=float(input(f"Enter the first voltage value {i+1}: " ))
            list.append(voltage)
            accumulate=accumulate + voltage # variable que acumula valores de volataje
        if accumulate<10:
            print(f"Stutus: {MODE1}")
        elif accumulate<20:
            print(f"Stutus: {MODE2}")
        else:
            print(f"Stutus: {MODE3}")


        print(f"student : {STUDENT} | Device: {str2}" ) 
        # Bulce que imprime los valores almacenados en la lista 
        for i in list:
             print(f"Voltaje reading: {i}")
        print(f"Average: {(accumulate/2):.2f}")
    else:
        for i in range(0,2):
            temperature=float(input(f"Enter the first temperature value {i+1}: " ))
        
            accumulate=accumulate + temperature # variable que acumula valores de temperatura

        if accumulate<10:
            print(f"Stutus: {MODE1}")
        elif accumulate<20:
            print(f"Stutus: {MODE2}")
        else:
            print(f"Stutus: {MODE3}")


        print(f"student : {STUDENT} | Device: {str2}" ) 
        # Bulce que imprime los valores almacenados en la lista 
        for i in list:
            print(f"Temperature reading: {i}")

        print(f"Readings: {temperature} ") 
        print(f"Average: {(accumulate/2):.2f}")

except ValueError:
    # Salida si la variable user_choice no es un numero entero
    print("Invalid input. Choose an option from the menu(e.g. 1 or 2)")


