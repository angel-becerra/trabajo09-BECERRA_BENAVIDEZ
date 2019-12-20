#ejercisio08
import os
import libreria

#calcula el numero mayor
#declaracion de variables

#input
JUAN=os.sys.argv[1]
ANGEL=os.sys.argv[2]
msg=libreria.menor(JUAN,ANGEL)
m="El menor" " entre {} y {} es: {}"
print(m.format(JUAN,ANGEL,msg))
