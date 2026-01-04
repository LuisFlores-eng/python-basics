#al usar from y no impor al inicio significa que solo voy a traer una porcion de la paqueteria
# Traer el archivo txt
#busca la ruta, con ROOT, donde esta el codigo y luego se añade la ruta del archivo de ingreso
from pathlib import Path                         #importar el comando path

ROOT=Path(__file__).resolve().parents[0]      #sirve para subir desde donde esta la raiz del proyecto, donde esta el arcvifo de codigo .py (donde estan todos tus codigos .py: ahi esta la carpeta archivos)
TXT=ROOT / "archivos" / "Voltajes_Sucios.txt"   #Es cero por que ahi es donde esta la carpeta archivos
                                                #conforme elevas el numero retocede de carpeta

values=[]
with open(TXT,'r',encoding='"UTF-8"') as f:
    for line in f:              #lee linea por linea del archivo ingresado
        s=line.strip()          #valores tipo str
        if not s or s.startswith("#"):
            continue

        s=s.replace(",",".")        #Cambia de decimal a punto
        try:
            values.append(float(s))
        except ValueError:
            #si no es linea ni numero, debe saltarlo
            pass            #saltar

Vmenor=[]
Vmayor=[]
for i in values:            #range(len(Vint)) y luego usar otro for para imprimir cada valor de la lista.

    if i>=5:
        Vmayor.append(i)
    else:
        Vmenor.append(i)

print(Vmayor)
print(Vmenor)
print(len(Vmayor))
print(len(Vmenor))
   
