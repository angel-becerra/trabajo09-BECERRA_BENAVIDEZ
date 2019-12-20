#ejercisio04
import os
import libreria
#calcula el nombre completo
#declaracion de variables

#imput
nombre=os.sys.argv[1]
primer_apellido=os.sys.argv[2]
segundo_apellido=os.sys.argv[3]
nombre_completo=libreria.nombre_completo(nombre,primer_apellido,segundo_apellido)

#output
print("el nombre completo es es:",nombre_completo)
