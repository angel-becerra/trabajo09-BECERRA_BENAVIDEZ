#ejercisio11
import os
import libreria
#calcula el empuje de una particula
#declaracion de variables

#imput
densidad_del_liquido=int(os.sys.argv[1])
volumen_sumergido=int(os.sys.argv[2])
gravedad=int(os.sys.argv[1])

empuje=libreria.empuje(densidad_del_liquido,volumen_sumergido,gravedad)

#output
print("el  empuje total  es:",empuje)
