"""
Universidad del Valle

@author: Emilio
"""
import struct

import math

from obj import *

#Importamos la coleccion

from collections import namedtuple



#Creamos los vectores

v2 = namedtuple('Point2', ['x','y'])

v3 = namedtuple('Point3', ['x','y','z'])



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



#Funcion para terminar

def glFinish():

	global windows

	windows.write(filename)



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



def load(filename, translate=(0,0), scale=(1,1)):	

	objeto = Obj(filename)



	for cara in objeto.faces:

		#Lista para guardar cada uno de los vertices

		verticesCaras = []

		for vertice in cara:

			coordenadaVertice = nor(objeto.vertices[vertice-1])

			#Vertices en x

			vx = int((coordenadaVertice[0] + translate[0]) * scale[0])

			#Vertices en y

			vy = int((coordenadaVertice[1] + translate[1]) * scale[1])

			coordenadaVertice = (vx,vy)

			#Agragamos los vertices a la lista

			verticesCaras.append(coordenadaVertice)



		#numero de vertices dentro de la lista

		nvertices = len(verticesCaras)

		#La primera linea utlizando los vertices correctoss

		glLine(verticesCaras[0], verticesCaras[-1])



		#Ciclo para encontrar las uniones de cada uno de las caras

		for i in range(nvertices-1):

			if i  != nvertices:

				glLine(verticesCaras[i], verticesCaras[i+1])



def filling_any_polygon(vertices):

	pass



def verificar_puntos(x,y,vertices):

	pass



#Transformar datos a normal

def nor(n):

	global ViewPort_X, ViewPort_Y, ViewPort_H, ViewPort_W, windows

	return int(ViewPort_H * (n[0]+1) * (1/2) + ViewPort_X), int(ViewPort_H * (n[1]+1) * (1/2) + ViewPort_X)	



class Vertex(object):

	def __init__(self, vert):

		self.x = vert[0]

		self.y = vert[1]



	def __str__(self):

		return "x: " + str(self.x) + " y: " + str(self.y)



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



	#def point(self, x, y):

		#self.framebuffer[y][x]= self.vertexColor



	def point(self, x, y, color = None):

		try:

			self.framebuffer[y][x] = color or self.vertexColor

		except:

			pass