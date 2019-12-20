#ejercisio06
import os
import libreria

#calcula el numero mayor
#declaracion de variable

#input
x=int(os.sys.argv[1])
y=int(os.sys.argv[2])
m=libreria.mayor(x,y)
msg="El mayor entre {} y {} es: {}"
print(msg.format(x,y,m))


