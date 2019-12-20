#ejercisio04
import os
import libreria
#calcula la cantidad de cosas compradas
#declaracion de variables

#imput
nro_producto1=int(os.sys.argv[1])
nro_producto2=int(os.sys.argv[2])
nro_producto3=int(os.sys.argv[3])
cantidad_total=libreria.cantidad_total(nro_producto1,nro_producto2,nro_producto3)

#output
print("el cantidad final es:",cantidad_total)
