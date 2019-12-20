#ejercisio19
import os
import libreria

#esto calcula el gato total de una vivienda
#declaracion de variables

#imput
numero_de_habitantes=int(os.sys.argv[1])
gasto_por_habitante=int(os.sys.argv[2])
alquiler_de_vivienda=int(os.sys.argv[3])
gasto_total=libreria.gasto_total(gasto_por_habitante,numero_de_habitantes,alquiler_de_vivienda)
print("el gasto total  es:",gasto_total)
