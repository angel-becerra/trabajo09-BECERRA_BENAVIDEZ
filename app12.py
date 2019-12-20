#ejercisio12
import os
import libreria
#calcula el voltaje electrico
#declaracion de variables

#imput
intensidad_electrica=int(os.sys.argv[1])
resistencia_electronica=int(os.sys.argv[2])
voltaje=libreria.voltaje(intensidad_electrica,resistencia_electronica)

#output
print("el voltaje final de circuito es:",voltaje)
