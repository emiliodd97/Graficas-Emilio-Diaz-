"""
Universidad del Valle

@author: Emilio
"""



import struct

import math

from obj import *

#Importamos la coleccion

from collections import namedtuple



#Variables globales

ViewPort_X = None

ViewPort_Y = None

ViewPort_H = None

ViewPort_W = None



v2 = namedtuple('Punto2', ['x', 'y'])

v3 = namedtuple('Punto3', ['x', 'y', 'z'])





def char(c):

	return struct.pack("=c",c.encode('ascii'))



def word(c):

	return struct.pack("=h",c)



def dword(c):

	return struct.pack("=l",c)



def color(r,g,b):

	return bytes([b,g,r])







#Suma de vectores

def suma(v0,v1):

	#Puntos en cada coordenadas

	px = v0.x + v1.x

	py = v0.y + v1.y

	pz = v0.z + v1.z



	#retorna un vector nuevo con la suma

	return v3(px,py,pz)



#Resta de coordeadas

def resta(v0,v1):

	#Puntos en cada coordenadas

	px = v0.x - v1.x

	py = v0.y - v1.y

	pz = v0.z - v1.z



	#retorna un vector nuevo con la resta

	return v3(px,py,pz)



def mul(v0,k):

	#Puntos en cada coordenadas

	px = v0.x * k

	py = v0.y * k

	pz = v0.z * k



	#retorna un vector nuevo con la multiplicacion a un escalar

	return v3(px,py,pz)



def dot(v0, v1):

  return v0.x * v1.x + v0.y * v1.y + v0.z * v1.z



#Funcion que encontrar un vector nuevo, utlizando algebra producto cruz

def pCruz(v0,v1):

	#Puntos en cada coordenadas

	p1 = v0.y * v1.z - v0.z * v1.y

	p2 = v0.z * v1.x - v0.x * v1.z

	p3 = v0.x * v1.y - v0.y * v1.x



	#Retorna un nuevo vector

	return v3(p1,p2,p3)



#Funcion para la longitud del vector

def longitud(v0):

	px = v0.x ** 2

	py = v0.y ** 2

	pz = v0.z ** 2

	#Suma de puntos

	len = (px+py+pz)**0.5

	return len



#Funcion para encontrar el vector normalr

def normal(v0):

	v0Lon = longitud(v0)



	if not v0Lon:

		return v3(0,0,0)



	px = v0.x/v0Lon

	py = v0.y/v0Lon

	pz = v0.z/v0Lon



	return v3(px,py,pz)



#Bounding Box

def bbox(*vertices):

	xs = [vertex.x for vertex in vertices]

	ys = [vertex.y for vertex in vertices]

	xs.sort()

	ys.sort()



	p1 = xs[0], ys[0]

	p2 = xs[-1], ys[-1]

	return v2(xs[0], ys[0]), v2(xs[-1], ys[-1])



#Rellenando cualquier poligono funciones utilizadas para el laboratorio No. 1

def find_MaxMin(*vertices):

	#Calculando los Y maximos y minimos

	ymax = sorted(vertices, key=lambda tup: tup[1], reverse=True)[0][1]

	ymin = sorted(vertices, key=lambda tup: tup[1])[0][1]

	#Calculamos los X maximo y minimos

	xmin = sorted(vertices, key=lambda tup: tup[0])[0][0]

	xmax = sorted(vertices, key=lambda tup: tup[0], reverse=True)[0][0]



	p1 = xmin, xmax

	p2 = ymin, ymax



	return v2(xmin,xmax), v2(ymin,ymax)



#Funcion para encontrar las coordenadas barycentricas

def baricentricas(A,B,C,P):

	bcoor = pCruz(v3(C.x - A.x, B.x - A.x, A.x - P.x), v3(C.y - A.y, B.y - A.y, A.y - P.y))



	if abs(bcoor.z) < 1:

		return(-1,-1,-1)



	return (1 - (bcoor.x + bcoor.y) / bcoor.z, bcoor.y / bcoor.z, bcoor.x / bcoor.z)



#Funcion definara el area de la imagen

def glViewPort(x,y,width,height):

	global ViewPort_X, ViewPort_Y, ViewPort_H, ViewPort_W

	#variable View Port en el eje x

	ViewPort_X = x

	#variable View Port en el eje y

	ViewPort_Y = y

	#variable View Port del ancho de la imagen

	ViewPort_H = height

	#variable View Port de la altura

	ViewPort_W = width



#Funcion que limpiara

def glClear():

	global windows

	#Llamo la funcion clear que se encuentra en la clase bitmap

	windows.clear()



#Funcion que limpiara el color

def glClearColor(r,g,b):

	global windows

	#windows.clear(int(255*r),int(255*g),int(255*b))



	#Se realiza la multiplicacion para llevar a otro color, FUNCION FLOOR, para aproximar al numero mas pequeño

	R = int(math.floor(r * 255))

	G = int(math.floor(g * 255))

	B = int(math.floor(b * 255))

	#Devuelve los numeros para crear otro color, es decir limpiar el color.

	#print("Limpieza de color: %d, %d, %d" % (R,G,B))

	windows.clearColor = color(R,G,B)



#Funcion que cambie el color de un punto.

def glVertex(x,y):

	global ViewPort_X, ViewPort_Y, ViewPort_H, ViewPort_W, windows



	PortX = int((x+1) * ViewPort_W * (1/2) + ViewPort_X)

	PortY = int((y+1) * ViewPort_H * (1/2) + ViewPort_Y)

	#print('glVertex X: %d y %d' % (PortX,PortY))

	windows.point(PortX,PortY)



#Funcion para cambiar el color de la funcion glVertex

def glColor(r,g,b):

	global windows

	#Se realiza la multiplicacion para llevar a otro color, FUNCION FLOOR, para aproximar al numero mas pequeño

	R = int(math.floor(r * 255))

	G = int(math.floor(g * 255))

	B = int(math.floor(b * 255))

	#Devuelve los numeros para crear otro color, es decir limpiar el color.

	#print("Vertex Color: %d, %d, %d" % (R,G,B))

	windows.vertexColor = color(R,G,B)



#Transformar datos a normal

def nor(n):

	global ViewPort_X, ViewPort_Y, ViewPort_H, ViewPort_W, windows

	nx = int(ViewPort_H * (n[0]+1) * (1/2) + ViewPort_X)

	ny = int(ViewPort_H * (n[1]+1) * (1/2) + ViewPort_Y)

	return nx, ny



#Funcion de llenado

def poligono(*vertices, color=None):

	#numero de vertices

	nvertices = len(vertices)

	#Calculando los Y maximos y minimos

	ymax = sorted(vertices, key=lambda tup: tup[1], reverse=True)[0][1]

	ymin = sorted(vertices, key=lambda tup: tup[1])[0][1]

	#Calculamos los X maximo y minimos

	xmin = sorted(vertices, key=lambda tup: tup[0])[0][0]

	xmax = sorted(vertices, key=lambda tup: tup[0], reverse=True)[0][0]



	#Lista de coordenadas

	self.glLine(vertices[0], vertices[-1])

	#Ciclo para encontrar el numero de vertices de un poligono

	for i in range(nvertices-1):

		if i  != nvertices:

			self.glLine(vertices[i], vertices[i+1])



	for x in range(xmin, xmax):

		for y in range(ymin, ymax):

			w,v,u = baricentricas(A,B,C, v2(x,y))

			if  w < 0 or v < 0 or u < 0:

				continue



			#Encontramos el valor z

			z = A.z * w + B.z * v + C.z * u



			#Coloreando el objeto

			if z > self.zbuffer[x][y]:

				self.point(x,y,color)

				self.zbuffer[x][y] = z



Negro = color(0,0,0)

Blanco = color(255,255,255)

#CLASE QUE GENERA ESCRITORIO DE IMAGEN

class Bitmap(object):

	#constructor de la clase

	def __init__(self, width,height):

		self.width = width

		self.height = height

		self.framebuffer = []

		self.clearColor = Blanco

		self.vertexColor = Blanco

		self.clear()



	def clear(self):

		self.framebuffer = [[Negro for x  in range(self.width)] for y in range(self.height)]

		self.zbuffer = [[-float('inf') for x in range(self.width)] for y in range(self.height)]



	def write(self,filename="out.bmp"):

		f = open(filename,'bw')

		#file header (14)

		f.write(char('B'))

		f.write(char('M'))

		f.write(dword(14 + 40 + self.width * self.height * 3))

		f.write(dword(0))

		f.write(dword(14 + 40))



		#image header (40)

		f.write(dword(40))

		f.write(dword(self.width))

		f.write(dword(self.height))

		f.write(word(1))

		f.write(word(24))

		f.write(dword(0))

		f.write(dword(0))

		f.write(dword(self.width * self.height * 3))

		f.write(dword(0))

		f.write(dword(0))

		f.write(dword(0))

		f.write(dword(0))



		for x in range(self.height):

			for y in range(self.width):

				f.write(self.framebuffer[x][y])

		f.close()



	def archivo(self, filename='out.bmp'):

		self.write(filename)



	def point(self, x, y,color=None):

		self.framebuffer[y][x]= color or self.vertexColor



	def glLine(self, vertex1, vertex2):

		x1 = vertex1[0]

		y1 = vertex1[1]

		x2 = vertex2[0]

		y2 = vertex2[1]

		#--------# y = mx + b #--------#

		#Valores en X

		dx = abs(x2-x1)

		#Valores en Y

		dy = abs(y2-y1)

		st = dy > dx

		#Condicion cuando la pendiente es ---> (dy/0)

		if dx == 0:

			for y in range(y1, y2+1):

				self.point(x1, y)

			return 0

		#Condicion para completar la linea

		if(st):

			x1,y1 = y1,x1

			x2,y2 = y2,x2

		if(x1>x2):

			x1,x2 = x2,x1

			y1,y2 = y2,y1

		#Valores en X

		dx = abs(x2-x1)

		#Valores en Y

		dy = abs(y2-y1)

		llenar = 0

		limite = dx

		y = y1

		#pendiente

		#m = dy/dx

		for x in range(x1,(x2+1)):

			if (st):

				self.point(y,x)

			else:

				self.point(x,y)

			llenar += dy * 2

			if llenar >= limite:

				y += 1 if y1 < y2 else -1

				limite += 2*dx



	def load(self, filename, scale=(1, 1), translate=(0, 0)):

		objeto = Obj(filename)

		caras = objeto.faces

		vertexes = objeto.vertices

		for face in caras:

			vcount = len(face)

			for j in range(vcount):

				#Por cada cara se saca modulo para emparejamiento.

				i = (j+1)%vcount



				f1 = face[j][0]

				f2 = face[i][0]

				v1 = vertexes[f1 - 1]

				v2 = vertexes[f2 - 1]

				#Le damos un valor a las coordeadas redondeadas

				x1 = round((v1[0] + translate[0]) * scale[0]);

				y1 = round((v1[1] + translate[1]) * scale[1]);

				x2 = round((v2[0] + translate[0]) * scale[0]);

				y2 = round((v2[1] + translate[1]) * scale[1]);

				#Guardando las coordenadas en un lista

				vertex = []

				vertex.append(x1)

				vertex.append(y1)

				vertex.append(x2)

				vertex.append(y2)

				self.glLine((vertex[0],vertex[1]),(vertex[2],vertex[3]))



	def triangulos(self,A,B,C, color=None):

		b_min, b_max = bbox(A,B,C)

		for x in range(b_min.x, b_max.x+1):

			for y in range(b_min.y, b_max.y):

				w, v, u = baricentricas(A,B,C, v2(x,y))

				#Si los valores son negativos que continue sin nada

				if  w < 0 or v < 0 or u < 0:

					continue



				#Encontramos el valor z

				z = A.z * w + B.z * v + C.z * u



				#Coloreando el objeto

				if z > self.zbuffer[x][y]:

					self.point(x,y,color)

					self.zbuffer[x][y] = z



	#Vector 3 transformado

	def transform(self, vertex, translate=(0, 0, 0), scale=(1, 1, 1)):

		#Transformando los datos

		t1 = round((vertex[0] + translate[0]) * scale[0])

		t2 = round((vertex[1] + translate[1]) * scale[1])

		t3 = round((vertex[2] + translate[2]) * scale[2])



		return v3(t1,t2,t3)



	def renderer(self, filename, scale=(1, 1), translate=(0, 0)):

		#Abrimos el archivo

		objetos = Obj(filename)

		luz = v3(0,0,1)



		caras = objetos.faces

		vertexes = objetos.vertices

		for face in caras:

			vcount = len(face)

			if vcount == 3:

				f1 = face[0][0] - 1

				f2 = face[1][0] - 1

				f3 = face[2][0] - 1



				vector_1 = self.transform(vertexes[f1], translate, scale)

				vector_2 = self.transform(vertexes[f2], translate, scale)

				vector_3 = self.transform(vertexes[f3], translate, scale)



				vector_normal = normal(pCruz(resta(vector_1, vector_2), resta(vector_3, vector_1)))

				intensidad = dot(vector_normal, luz)

				tonalidad = round(255 * intensidad)



				#Si la tonalidad es menor a 0, es decir, negativo, que no pinte nada

				if tonalidad < 0:

					continue



				self.triangulos(vector_1, vector_2, vector_3, color(tonalidad, tonalidad, tonalidad))

			else:



				f1 = face[0][0] - 1

				f2 = face[1][0] - 1

				f3 = face[2][0] - 1

				f4 = face[3][0] - 1



				lista_vertices = []

				V1 = self.transform(vertexes[f1], translate, scale)

				V2 = self.transform(vertexes[f2], translate, scale)

				V3 = self.transform(vertexes[f3], translate, scale)

				V4 = self.transform(vertexes[f4], translate, scale)



				lista_vertices.append(V1)

				lista_vertices.append(V2)

				lista_vertices.append(V3)

				lista_vertices.append(V4)



				vector_normal = normal(pCruz(resta(lista_vertices[0], lista_vertices[1]), resta(lista_vertices[1], lista_vertices[2])))  # no necesitamos dos normales!!

				intensidad = dot(vector_normal, luz)

				tonalidad = round(255 * intensidad)



				#Si la tonalidad es menor a 0, es decir, negativo, que no pinte nada

				if tonalidad < 0:

					continue



				self.triangulos(lista_vertices[0], lista_vertices[1], lista_vertices[2], color(tonalidad, tonalidad, tonalidad))

				self.triangulos(lista_vertices[0], lista_vertices[2], lista_vertices[3], color(tonalidad, tonalidad, tonalidad))



				#self.filling_any_polygon(lista_vertices[0], lista_vertices[1], lista_vertices[2], color(tonalidad, tonalidad, tonalidad))

				#self.filling_any_polygon(lista_vertices[0], lista_vertices[2], lista_vertices[3], color(tonalidad, tonalidad, tonalidad))