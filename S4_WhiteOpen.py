

#toda esta parte es para traer el archivo y ver en la terminal
#r significa : leer, w significa W: escribir
with open('Voltajes_Sucios.txt','r',encoding='"utf-8"') as f:
        contenido=f.read()
        print(contenido)