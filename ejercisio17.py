#ejercisio17
import os
import libreria

#calcula el valor mayor de los numeros
#declaracion de variables

#input
angel=int(os.sys.argv[1])
santiago=int(os.sys.argv[2])
m=libreria.mayor(angel,santiago)
msg="El menor entre {} y {} es: {}"
print(msg.format(angel,santiago,m))
