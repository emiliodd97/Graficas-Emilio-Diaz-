"""
Universidad del Valle

@author: Emilio
"""

from bmp import *



class Obj(object):

	def __init__(self,filename):

		#with open(filename) as f:

			#self.lines = f.read().splitlines()



		self.filename = filename

		self.vertices = []

		self.faces = []

		self.read()



	def read(self):

		#Abrimos el archivo

		archivo = open(self.filename, 'r')



		for lineas in archivo.readlines():

			#lineV,lineF = lineas.split(' ',1)



			#Lineas con valores de V

			#Para realizar este algoritmo se utilizo el ejemplo de abajo

			if(lineas[0] == 'v' and lineas[0] != 'n'):

				lineV = lineas.split(' ')

				#contador para los valores

				n = 1

				#vertice = [x,y]

				self.vertices.append(((float(lineV[n])),((float(lineV[n+1])))))

			#Lineas con valores de F

			if(lineas[0] == 'f'):

				lineF = lineas.split(' ')

				face = lineF.pop(0)

				face = []

				#Ciclo para quitar lo parametro extras

				for i in lineF:

					i = i.split("/")

					#El valor sera guardado en una lista

					face.append(int(i[0]))

				self.faces.append(face)

				#self.faces.append([list(map(int, face.split('/'))) for face in lineas[0].split(' ')])

		#Cerramos el archivo

		archivo.close()





#-------- INTENTO CON SOLO UNA LINEA ----------#

#vertice = []

#lineas = 'v 0.376516 1.770015 -2.274176'

#valor = lineas.strip().split(" ")

#valor_x = valor.pop(1)

#valor_Y = valor.pop(2)

#vertice.append((float(valor_x),float(valor_Y)))

#print(vertice)





#-------- INTENTO CON UN CICLO --------#

#faces = []

#contador = 1

#lineas = 'f 5//1 4//1 10//1 11//1'

#while(contador<2):

	#line = lineas.strip().split(' ')

	#if(line[0] == 'f'):

		#line.pop(0)

		#face = []

		#for i in line:

			#i = i.split("/")

			#face.append(int(i[0]))

		#faces.append(face)

	#print(faces)

	#contador +=1



#-------- EJEMPLO DE CLASE ---------#

#for line in self.lines:

			#if line:

				#prefix,value = line.split(' ', 1)



				#if prefix == 'v':

					#self.vertice.append(list(map(float, value.split(' '))))



				#elif prefix == 'f':

					#self.faces.append([list(map(int, face.split('/'))) for face in value.split(' ')])