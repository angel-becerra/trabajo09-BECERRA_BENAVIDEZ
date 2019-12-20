#ejercisio19
import os
import libreria

#esto calcula el gasto total de un estudiante
#declaracion de variables

#imput
pasajes=int(os.sys.argv[1])
comida=int(os.sys.argv[2])
vivienda=int(os.sys.argv[3])
gasto_de_estudiante=libreria.gasto_de_estudiante(pasajes,comida,vivienda)
print("el gasto de un estudiante  es:",gasto_de_estudiante)
