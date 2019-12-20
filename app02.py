#ejercisio02
import os
import libreria
#calcula el volumen de un paralelepipedo
#declaracion de variables

#imput
lado01=int(os.sys.argv[1])
lado02=int(os.sys.argv[2])
lado03=int(os.sys.argv[3])
volumen=libreria.volumen(lado01,lado02,lado03)

#output
print("el volumen final es:",volumen)

