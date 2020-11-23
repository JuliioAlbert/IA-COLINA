from operator import itemgetter
import random
import json

with open('camino.json', 'r') as f:
    archivo = json.load(f)

pos = []
nodo = []
ruta = []

def subir(inicio, fin):
		llegamos = 0
		anterior = ""
		it= 1
		while (llegamos == 0):
				nodo = [n for n in archivo['rutas'] if (n[0] == inicio and n[1] != anterior)]
				valorMenor = (min(nodo, key=itemgetter(2))[2])
				
				pos = [cp for cp in nodo if (cp[2] == valorMenor and cp[1] != anterior) ]
				#print(pos)
				if (len(pos) > 1):
						sigue = 0
						indice = random.randint(0, len(pos) - 1 )
						count = 1
						while(sigue == 0):
								menor = pos[indice]
								if (len([item for item in ruta if item[1] == menor[1]]) == 0 and len([item for item in ruta if item[0] == menor[1]]) == 0 ):
										sigue = 1
								count += 1
								#print(count)
								if (count > len(pos)):
										sigue = 1
										llegamos = 1
										print ('¡¡No se encontro')


				else:
						menor = pos[0]
				ruta.append(menor)
				siguiente = menor[1]
				anterior = inicio
				if (siguiente == fin):
						llegamos = 1
				else:
						inicio = siguiente
				it += 1
subir("A","K")
if subir:
	print (' Toma la Ruta => ')
	print (ruta)
else:
	print ('No Existe Ruta :(')
