#ejercisio10
import os
import libreria
#calcula el estado del curso del alumno
#declaracion de variables

#imput
nota_de_trabajos=int(os.sys.argv[1])
nota_de_examenes=int(os.sys.argv[2])
nota_de_exposiciones=int(os.sys.argv[3])
nota_final=libreria.nota_final(nota_de_trabajos,nota_de_examenes,nota_de_exposiciones)

#output
print("el estado final del alumno en el curso es final es:",nota_final)
