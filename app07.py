#ejercisio06
import os
import libreria

#calcula el numero mayor
#declaracion de variables

#input
a=int(os.sys.argv[1])
b=int(os.sys.argv[2])
m=libreria.mayor(a,b)
msg="El mayor entre {} y {} es: {}"
print(msg.format(a,b,m))
