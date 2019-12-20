#ejercisio09
import os
import libreria

#calcula la cantidad de postulantes
#declaracion dee variables

#input
ingenierias=int(os.sys.argv[1])
biomedicas=int(os.sys.argv[2])
letras=int(os.sys.argv[3])
total_de_postulantes=libreria.total_de_postulantes(ingenierias,biomedicas,letras)
print("el total de postulantes son:", total_de_postulantes)
