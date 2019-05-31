"""
Universidad del Valle

@author: Emilio
"""

import struct

import math

from obj import *



def char(c):

	return struct.pack("=c",c.encode('ascii'))



def word(c):

	return struct.pack("=h",c)



def dword(c):

	return struct.pack("=l",c)



def color(r,g,b):

	return bytes([b,g,r])



#Variables globales

windows = None

filename = "out.bmp"

ViewPort_X = None

ViewPort_Y = None

ViewPort_H = None

ViewPort_W = None





def filename(name):

	global filename

	filename = name



#Funcion que inicializara el escritorio de imagen

def glCreateWindow(width,height):

	global windows

	#Declar la clase con relacion a una variable global

	windows = Bitmap(width, height)



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



#Funcion para crear lineas

def glLine(vertex1, vertex2):

	global windows



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

			windows.point(x1, y)

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

			windows.point(y,x)

		else:

			windows.point(x,y)

		llenar += dy * 2

		if llenar >= limite:

			y += 1 if y1 < y2 else -1

			limite += 2*dx



#Funcion para terminar

def glFinish():

	global windows

	windows.write(filename)



def load(filename, translate=(0,0), scale=(1,1)):

	objeto = Obj(filename)

	caras = objeto.faces

	vertices = objeto.vertices



	for cara in caras:

		verticesCaras = []

		for vertice in cara:

			coordenadaVertice = nor(vertices[vertice-1])

			coordenadaVertice = (int((coordenadaVertice[0] + translate[0]) * scale[0]), int((coordenadaVertice[1] + translate[1]) * scale[1]))

			verticesCaras.append(coordenadaVertice)

		#Lista de coordenadas

		nvertices = len(verticesCaras)

		glLine(verticesCaras[0], verticesCaras[-1])

		#Ciclo para encontrar el numero de vertices de un poligono

		for i in range(nvertices-1):

			if i  != nvertices:

				glLine(verticesCaras[i], verticesCaras[i+1])







def nor(n):

	global ViewPort_X, ViewPort_Y, ViewPort_H, ViewPort_W, windows

	return int(ViewPort_H * (n[0]+1) * (1/2) + ViewPort_X), int(ViewPort_H * (n[1]+1) * (1/2) + ViewPort_X)



def filling_any_polygon(vertices):

	global ViewPort_X, ViewPort_Y, ViewPort_H, ViewPort_W, windows

	#numero de vertices

	nvertices = len(vertices)



	#Calculando los Y maximos y minimos

	ymax = sorted(vertices, key=lambda tup: tup[1], reverse=True)[0][1]

	ymin = sorted(vertices, key=lambda tup: tup[1])[0][1]

	#Calculamos los X maximo y minimos

	xmin = sorted(vertices, key=lambda tup: tup[0])[0][0]

	xmax = sorted(vertices, key=lambda tup: tup[0], reverse=True)[0][0]

	

	#Lista de coordenadas

	glLine(vertices[0], vertices[-1])



	#Ciclo para encontrar el numero de vertices de un poligono

	for i in range(nvertices-1):

		if i  != nvertices:

			glLine(vertices[i], vertices[i+1])



	for x in range(xmin, xmax):

		for y in range(ymin, ymax):

			dentro = verificar_puntos(x,y,vertices)

			if dentro:

				windows.point(x,y)



	#Ordenando a partir de ymin

	#scan = sorted(vertices, key=lambda tup: tup[1], reverse=False)



	#Comprobando cual es el numero mayor

	#mat = [vertices[0],vertices[1],vertices[2],vertices[3]]

	#print(max(mat[0]))	



def verificar_puntos(x,y,vertices):

	counter = 0

	p1 = vertices[0]

	n = len(vertices)

	for i in range(n+1):

		p2 = vertices[i % n]

		if(y > min(p1[1], p2[1])):

			if(y <= max(p1[1], p2[1])):

				if(p1[1] != p2[1]):

					xinters = (y-p1[1])*(p2[0]-p1[0])/(p2[1]-p1[1])+p1[0]

					if(p1[0] == p2[0] or x <= xinters):

						counter += 1

		p1 = p2

	if(counter % 2 == 0):

		return False

	else:

		return True

	

class Vertex(object):



	def __init__(self, vert):

		self.x = vert[0]

		self.y = vert[1]



	def __str__(self):

		return "x: " + str(self.x) + " y: " + str(self.y)

			

#CLASE QUE GENERA ESCRITORIO DE IMAGEN

class Bitmap(object):

	#constructor de la clase

	def __init__(self, width,height):

		self.width = width

		self.height = height

		self.framebuffer = []

		self.clearColor = color(91,204,57)

		self.vertexColor = color(1,1,1)

		self.clear()



	def clear(self):

		self.framebuffer = [

		[

			self.clearColor

				for x  in range(self.width)

			]

   			for y in range(self.height)



		]

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



	#def point(self, x, y):

		#self.framebuffer[y][x]= self.vertexColor



	def point(self, x, y, color = None):

		try:

			self.framebuffer[y][x] = color or self.vertexColor

		except:

			pass