"""
Universidad del Valle

@author: Emilio
"""


import struct

import math 





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

	print("Limpieza de color: %d, %d, %d" % (R,G,B))

	windows.clearColor = color(R,G,B)





#Funcion que cambie el color de un punto.

def glVertex(x,y):

	global ViewPort_X, ViewPort_Y, ViewPort_H, ViewPort_W, windows

	

	PortX = int((x+1) * ViewPort_W * (1/2) + ViewPort_X)

	PortY = int((y+1) * ViewPort_H * (1/2) + ViewPort_Y)

	print('glVertex X: %d y %d' % (PortX,PortY))

	windows.point(PortX,PortY)



#Funcion para cambiar el color de la funcion glVertex

def glColor(r,g,b):

	global windows

	#Se realiza la multiplicacion para llevar a otro color, FUNCION FLOOR, para aproximar al numero mas pequeño

	R = int(math.floor(r * 255))

	G = int(math.floor(g * 255))

	B = int(math.floor(b * 255))

	#Devuelve los numeros para crear otro color, es decir limpiar el color. 

	print("Vertex Color: %d, %d, %d" % (R,G,B))

	windows.vertexColor = color(R,G,B)



#Funcion para terminar

def glFinish():

	global windows

	windows.write(filename)





#CLASE QUE GENERA ESCRITORIO DE IMAGEN

class Bitmap(object):

	#constructor de la clase

	def __init__(self, width,height):

		self.width = width

		self.height = height

		self.framebuffer = []

		self.clearColor = color(91,204,57)

		self.vertexColor = color(0,0,0)

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



	def point(self, x, y):

		self.framebuffer[y][x]= self.vertexColor