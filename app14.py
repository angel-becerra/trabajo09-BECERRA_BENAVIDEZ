#ejercisio14
import os
import libreria
#calcula la longitud de arco de un sector circular
#declaracion de variables

#imput
angulo_en_sexagesimales=int(os.sys.argv[1])
radio=int(os.sys.argv[2])

longitud_de_arco=libreria.longitud_de_arco(angulo_en_sexagesimales,radio)

#output
print("la longitud de arco  es:",longitud_de_arco)

