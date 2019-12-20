#ejercisio20
import os
import libreria

#calcula energia cinetica
#declaracion de variables

#input
masa=int(os.sys.argv[1])
gravedad=int(os.sys.argv[2])
haltura=int(os.sys.argv[3])
energia_cinetica=libreria.energia_cinetica(masa,gravedad,haltura)

print("la energia cinetica es:", energia_cinetica)
