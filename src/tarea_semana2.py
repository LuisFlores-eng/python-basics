MODE1="UMBRAL_BAJO"
MODE2="UMBRAL_MEDIO"
MODE3="UMBRAL_ALTO"
STUDENT="lUIS"
accumulate=0                #Declarar variable como número

str1=input("Enter your name ")
str2=input("Enter the name of the electronic device ")
num_samples=int(input("Enter the number of samples "))
user_choice=int(input("choose an option 1- VOLTAGE OR 2- TEMPERATURE "))

try:
    if user_choice==1:
        for i in range(0,2):
            voltage=float(input(f"Enter the first voltage value {i+1}: " ))
            accumulate=accumulate + voltage


        if accumulate<10:
            print(f"Stutus: {MODE1}")
        elif accumulate<20:
            print(f"Stutus: {MODE2}")
        else:
            print(f"Stutus: {MODE3}")


        print(f"student : {STUDENT} | Device: {str2}" )   
        print(f"Readings: {voltage} ") 
        print(f"Average: {(accumulate/2):.2f}")
    else:
        for i in range(0,2):
            temperature=float(input(f"Enter the first temperature value {i+1}: " ))
            accumulate=accumulate + temperature

        if accumulate<10:
            print(f"Stutus: {MODE1}")
        elif accumulate<20:
            print(f"Stutus: {MODE2}")
        else:
            print(f"Stutus: {MODE3}")


        print(f"student : {STUDENT} | Device: {str2}" )   
        print(f"Readings: {temperature} ") 
        print(f"Average: {(accumulate/2):.2f}")

except ValueError:
    print("Invalid input. Choose an option from the menu(e.g. 1 or 2)")


