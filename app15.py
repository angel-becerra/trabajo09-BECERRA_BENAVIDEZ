#ejercisio15
import os
import libreria
#calcula los ingresos totales de los postulantes
#declaracion de variables

#imput
costo_por_examen=int(os.sys.argv[1])
total_de_postulantes=int(os.sys.argv[2])

total_ingresos=libreria.total_ingresos(costo_por_examen,total_de_postulantes)

#output
print("el total de ingresos es es:",total_ingresos)
