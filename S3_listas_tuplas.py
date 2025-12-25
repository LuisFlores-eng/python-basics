#lISTAS

Cod22561=[35, "Ing Ambiental", 978546744, "Juan"]

print(f"la edad de {Cod22561[3]} es : {Cod22561[0]} y su numero es: {Cod22561[2]}")

#cambiar valores en la lista
Cod22561[2]=int(input("ingrese nuevo número"))     #se cambio su número

print(f"la edad de {Cod22561[3]} es : {Cod22561[0]} y su numero es: {Cod22561[2]}")

#TUPLAS
CodJefe=("Luis",65, "Administrador", 985631245)
print(f"la edad de {CodJefe[0]} es : {CodJefe[1]} y su número de telefono es : {CodJefe[3]}")

#Esta nunca cambiará puestao que una tupla nunca cambia
#CodJefe[1]=62
#print(f"la edad de {CodJefe[0]} es : {CodJefe[1]} y su número de telefono es : {CodJefe[3]}")

#Dirrectorio: En lugra de buscar en la lista con una posición lo busac con un nombre que ha sido asignado

CodNuevo={"Nombre": "Ricardo", "Edad": 19, "Carrera":"Programador", "Telefono": 986421356}

print(CodNuevo["Nombre"])
print(CodNuevo["Edad"])
CodNuevo["Nombre"]="Luis"       #Cambiamos nombre
print(CodNuevo["Nombre"])

#Diccionarios anidados

Cod001={"Nombre": "Ricardo", "Edad": 19, "Carrera":"Programador", "Telefono": 986421356}
Cod002={"Nombre": "Luis", "Edad": 19, "Carrera":"Programador", "Telefono": 986421356}

Central={"candidato1":Cod001, "candidato2":Cod002}
Empresa=(Central)
print(Empresa(0))