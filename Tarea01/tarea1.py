"""
Universidad del Valle

@author: Emilio
"""


from bmpgn import *

import random

import math



#funcion de una imagen negra con un punto blanco

def imagen_1():

	# Cargamos el archivo donde se guardara la imagen

    filename("imagen_1.bmp")

    print("RENDERIZAR UNA IMAGEN NEGRA CON UN PUNTO BLANCO EN UNA UBICACIÓN RANDOM")

    #glInit()

    glCreateWindow(300,300)

    glViewPort(10,10,290,290)

    glClearColor(0, 0, 0)

    glClear()

    glColor(1, 1, 1)

    X = random.uniform(-1, 1)

    Y = random.uniform(-1, 1)

    glVertex(X, Y)

    glFinish()



def imagen_2():

	# Cargamos el archivo donde se guardara la imagen

    filename("imagen_2.bmp")

    print("RENDERIZAR UNA IMAGEN NEGRA CON UN PUNTO BLANCO EN CADA ESQUINA")

    #glInit()

    glCreateWindow(300,300)

    glViewPort(20,20, 260, 260)

    glClearColor(0, 0, 0)

    glClear()

    glColor(1, 1, 1)

    glVertex(-1, -1)

    glVertex(-1, 1)

    glVertex(1, -1)

    glVertex(1, 1)

    glFinish()



def imagen_4():

    #Cargamos el archib¿vo donde se guardara la imagen

    filename("imagen_4.bmp")

    print('RENDERIZAR LINEAS BLANCAS EN TODA LA ORILLA DE SU IMAGEN')

    glCreateWindow(300,300)

    glViewPort(20,20,260,260)

    glClearColor(0,0,0)

    glClear()

    glColor(1,1,1)

    dato = 1/299

    #Ciclo que recorra cada punto con un intervalo de [-(1/299), (1/299)], el intervalo funciona para que no se salga del tamaño de la ventana

    for x in range(-299,299):

        glVertex((x*dato),-1)

        glVertex((x*dato),1)

        glVertex(-1,(x*dato))

        glVertex(1, (x*dato))

    #glClear()

    glFinish()



def imagen_5():

    # Cargamos el archivo donde se guardara la imagen

    filename('imagen_5.bmp')

    print('RENDERIZAR UNA LINEA BLANCA EN DIAGONAL POR EL CENTRO DE SU IMAGEN')

    glCreateWindow(300,300)

    glViewPort(10,10,290,290)

    glClearColor(0,0,0)

    glClear()

    glColor(1,1,1)

    dato = 1/299

    #Ciclo que recorra cada punto con un intervalo de [-(1/299), (1/299)], el intervalo funciona para que no se salga del tamaño de la ventana 

    for x in range(-299,299):

        #(0,0) para que parte desde el origen 

        glVertex(0,0)

        glVertex((x*dato),(x*dato))

    glFinish()



def imagen_7():

    # Cargamos el archivo donde se guardara la imagen

    filename('imagen_7.bmp')

    print('POR LLENAR SU IMAGEN ENTERA DE PUNTOS DE COLORES RANDOM')

    glCreateWindow(300,300)

    glViewPort(10,10,290,290)

    glClearColor(0,0,0)

    glClear()

    #glColor(1,1,1)

    dato = 1/299

    #Ciclo que recorra cada punto con un intervalo de [-(1/299), (1/299)], el intervalo funciona para que no se salga del tamaño de la ventana 

    for x in range(-299,299):

        for y in range (-299,299):

            glColor(random.random(), random.random(), random.random())

            glVertex((dato*x),(dato*y))

    glFinish()



#Lluvia de estrellas

def imagen_8():

    filename('imagen_8.bmp')

    print('POR LLENAR SU IMAGEN ENTERA DE PUNTOS DE COLORES RANDOM')

    glCreateWindow(300,300)

    glViewPort(10,10,290,290)

    glClearColor(0,0,0)

    glClear()

    glColor(1,1,1)

    dato = 1/299



    for x in range(random.randint(1,1000)):

        X = random.uniform(-1,1)

        Y = random.uniform(-1,1)

        glVertex(X,Y)

    glFinish()





#Escena de Atari

def escena_Atari():

    filename('escena_Atari.bmp')

    print('ESCENA DE JUEGO DE ATARI')

    glCreateWindow(200,200)

    glViewPort(20,5,162,192)

    glClearColor(0,0,0)

    glClear()

    glColor(1,1,1)



    dato_y = 1/192

    dato_x = 1/160



    

    for x in range(-192,192):

        glVertex((x*dato_y),-1)

        glVertex((x*dato_y),1)

        glVertex(-1,(x*dato_y))

        glVertex(1, (x*dato_y))

        glVertex(0, (x*dato_y))



    

    for x in range(-155,160):

        glVertex((x*dato_x),0)

        glVertex(0,(x*dato_x))

        glVertex(dato_x-(x*dato_x),-(x*dato_x))



    glFinish()