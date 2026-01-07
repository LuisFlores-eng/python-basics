#limpiar _csv_simpple.py
#Objetivo: leer CSV "sucio", limpiar y guardar "limpio" con:
#-timestamp en formato ISO YYYY-MM-DDTHH:MM:SS
#-value como float con punto y 3 decimaless
#-Separador de salidad : coma
#Filas invalidas: se saltan

import csv
from datetime import datetime
from pathlib import Path




#Path-Ruta de aceeso

ROOT= Path(__file__).resolve().parents[0] #igual = \Users\LUIS FLORES\OneDrive\Escritorio\ProgramacionPython\Settimana2
TXT= ROOT/"Archivos"        #Direccion del archivo Csv 

IN_FILE=TXT/"voltajes_250_sucio1.csv"           #Archivo de ingreso
OUT_FILE=TXT/"voltajes_250_limpios.csv"         #Archivo de salidas

#APERTURA DE ARCHIVOS

with open(IN_FILE, 'r', encoding="  utf-8", newline="") as fin,\
    open(OUT_FILE, 'w', encoding="  utf-8", newline="") as fout:
    reader=csv.DictReader(fin, delimiter=';')       # usa ',' si tu archivo lo requiere
    writer=csv.DictWriter(fout, fieldnames=["timestamp","value"])
    writer.writeheader()

#leer linea por linea y seleciona en crudo raw/row

    total=kept=0
    for row in reader:
        total+=1
        ts_raw=(row.get("timestamp") or "").strip() 
        val_raw=(row.get("value") or "").strip()
        #print(ts_raw,val_raw) imprime valores en crudo (comas, puntos,etc)

#Limpieza de los datos obtenidos en crudo  linea 31
        val_raw=val_raw.replace(",", ".")
        val_low=val_raw.lower()         #cambio de miniscula a mayuscula(cambio de sistemas)
        if val_low in {"", "na", "n/a", "nan", "null", "none", "error"}:
            continue        #Saltar linea si ve vacio, coma, etc reemplaza o salta (linea 41-44)
        
        try:
            val=float(val_raw)
        
        except ValueError:
            continue        #saltar fila si no es numero


        #print(val) imprime todo limpio voltajes

#Limpieza de datos de tiempo
        ts_clean= None
        for fmt in ("%Y-%m-%dT%H:%M:%S", "%d/%m/%Y %H:%M:%S"):
            try:
                dt=datetime.strptime(ts_raw, fmt)
                ts_clean=dt.strftime("%Y-%m-%dT%H:%M:%S")
                break
            except ValueError:
                pass
        #print(ts_clean)

#Grabar datos en write
        writer.writerow({"timestamp": ts_clean, "value": f"{val:.3f}"})
        kept+=1         #suma 1 a kept: cambia de fila

        

