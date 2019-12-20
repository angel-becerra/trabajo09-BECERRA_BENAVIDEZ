#ejercisio16
import os
import libreria
#pide los datos personales
#declaracion de variables

#imput
nombre=os.sys.argv[1]
edad=int(os.sys.argv[2])
dni=int(os.sys.argv[3])
datos_personales=libreria.datos_personales(nombre,edad,dni)

#output
print("los datos son :",datos_personales)
