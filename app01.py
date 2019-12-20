#ejercisio01
import os
import libreria

#calcula el calor final
#declaracion de variables

#imput
masa=int(os.sys.argv[1])
temperatura=int(os.sys.argv[2])
calor_especifico=int(os.sys.argv[3])
calor_final=libreria.calor(masa,temperatura,calor_especifico)

#output
print("el calor final es:",calor_final)

