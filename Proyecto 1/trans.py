"""
Universidad del Valle

@author: Emilio
"""

import struct

from math import *

from math import sin, cos

import numpy

from collections import namedtuple




V2 = namedtuple('Punto2', ['x', 'y'])

V3 = namedtuple('Punto3', ['x', 'y', 'z'])





def char(c):

	return struct.pack("=c",c.encode('ascii'))



def word(c):

	return struct.pack("=h",c)



def dword(c):

	return struct.pack("=l",c)



def color(r,g,b):

	return bytes([b,g,r])



#Suma de vectores

def sum(v0,v1):

	#Puntos en cada coordenadas

	px = v0.x + v1.x

	py = v0.y + v1.y

	pz = v0.z + v1.z



	

	return V3(px,py,pz)



#Resta de coordeadas

def sub(v0,v1):

	#Puntos en cada coordenadas

	px = v0.x - v1.x

	py = v0.y - v1.y

	pz = v0.z - v1.z



	#retorna un vector nuevo con la resta

	return V3(px,py,pz)



def mul(v0,k):

	#Puntos en cada coordenadas

	px = v0.x * k

	py = v0.y * k

	pz = v0.z * k



	#retorna un vector nuevo con la multiplicacion a un escalar

	return V3(px,py,pz)



def dot(v0, v1):

  return v0.x * v1.x + v0.y * v1.y + v0.z * v1.z



#Funcion que encontrar un vector nuevo, utlizando algebra producto cruz

def cross(v0,v1):

	#Puntos en cada coordenadas

	p1 = v0.y * v1.z - v0.z * v1.y

	p2 = v0.z * v1.x - v0.x * v1.z

	p3 = v0.x * v1.y - v0.y * v1.x



	#Retorna un nuevo vector

	return V3(p1,p2,p3)



#Funcion para la longitud del vector

def length(v0):

	px = v0.x ** 2

	py = v0.y ** 2

	pz = v0.z ** 2

	#Suma de puntos

	len = (px+py+pz)**0.5

	return len



#Funcion para encontrar el vector normalr

def norm(v0):

	v0Lon = length(v0)



	if not v0Lon:

		return V3(0,0,0)



	px = v0.x/v0Lon

	py = v0.y/v0Lon

	pz = v0.z/v0Lon



	return V3(px,py,pz)



#Bounding Box

def bbox(*vertices):

	xs = [vertex.x for vertex in vertices]

	ys = [vertex.y for vertex in vertices]

	xs.sort()

	ys.sort()



	return V2(xs[0], ys[0]), V2(xs[-1], ys[-1])





def baricentricas(A,B,C,P):

	bcoor = cross(

		V3(C.x - A.x, B.x - A.x, A.x - P.x),

		V3(C.y - A.y, B.y - A.y, A.y - P.y)

	)



	if abs(bcoor.z) < 1:

		return(-1,-1,-1)



	return (1 - (bcoor.x + bcoor.y) / bcoor.z, bcoor.y / bcoor.z, bcoor.x / bcoor.z)



#Comprobando teorema para crear una multiplicacion

def teorema(filas, columna):

	matriz = []

	for i in range(filas):

		#Añadimos una lista vacia

		matriz.append([])

		for j in range(columna):

			matriz[-1].append(0.0)

	#Retornamos la matriz creada

	return matriz



#Funcion para multiplicar las matrices

def multiplicarMatrices(m1,m2):

	matrizResultante = teorema(len(m1), len(m2[0]))

	for i in range(len(m1)):

		#Creamos la matriz

		for j in range(len(m2[0])):

			for k in range(len(m2)):

				matrizResultante[i][j] += m1[i][k] * m2[k][j]

	
	return matrizResultante