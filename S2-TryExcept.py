valor_text= input("Enter the temperature values ")
t=float(valor_text)

try:    #condiciona si la entrada es valida
    if t >= 30 :       #condicion
        print("Alerta! ALTA TEMPERATURA")

    elif t<0:
        print("Temperatura bajo cero")

    else:
        print("Temperatura normal")

except ValueError:
    print("ingrese un entrada valida(Ej.20.5")  # se ejecuta cuando la entrada no es valida