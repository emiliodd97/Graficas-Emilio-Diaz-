"""
Universidad del Valle

@author: Emilio
"""



from bmp import *



def imagen_1():

	# Cargamos el archivo donde se guardara la imagen

    filename("imagen_1.bmp")

    #glInit()

    glCreateWindow(600,600)

    

    #-----  (x1, y1), (x2, y2)  -----#

    #-----  (x1, x2, y1, y2)  -------#

    glLine(10,510,10,10)

    glLine(10,462,10,191)

    glLine(10,354,10,354)

    glLine(10,10,10,510)

    glFinish()



def imagen_2():

	# Cargamos el archivo donde se guardara la imagen

	filename("imagen_2.bmp")

	glCreateWindow(800,800)

	glClearColor(0, 0, 0)

	glClear()

	glColor(1, 1, 1)

	#-----  (x1, y1), (x2, y2)  -----#

	glLine(790,790,590,90)

	glLine(790,609,590,138)

	glLine(790,446,590,246)

	glLine(790,338,590,409)

	glLine(790,290,590,590)

	glFinish()



def imagen_3():

	# Cargamos el archivo donde se guardara la imagen

	filename("imagen_3.bmp")

	glCreateWindow(600,600)

	glClearColor(0,0,0)

	glClear()

	glColor(1,1,1)

	#-----  (x1, y1), (x2, y2)  -----#

	glLine(10,510,590,590)

	glLine(10,462,590,409)

	glLine(10,354,590,246)

	glLine(10,191,590,138)

	glLine(10,10,590,90)

	glFinish()



def cubo():

	# Cargamos el archivo donde se guardara la imagen

	filename("cubo.bmp")

	glCreateWindow(360,360)

	glClearColor(0,0,0)

	glClear()

	glColor(1,1,1)

	#-----  (x1, y1), (x2, y2)  -----#

	#PROBLEMA CON DIVISION EN CERO EN DX

	glLine(100, 200, 100, 100)

	glLine(100, 100, 100, 200)

	glLine(200, 200, 100, 200)

	glLine(100, 200, 200, 200)

	glLine(150, 250, 150, 150)

	glLine(150, 150, 150, 250)

	glLine(250, 250, 150, 250)

	glLine(150, 250, 250, 250)

	glLine(100, 150, 100, 150)

	glLine(100, 150, 200, 250)

	glLine(200, 250, 100, 150)

	glLine(200, 250, 200, 250)

	glFinish()



def cubo_isometrico():

	# Cargamos el archivo donde se guardara la imagen

	filename("cubo_isometrico.bmp")

	glCreateWindow(500,500)

	glClearColor(0,0,0)

	glClear()

	glColor(1,1,1)

	#-----  (x1, y1), (x2, y2)  -----#

	#-----  (x1, x2, y1, y2)    -----#

	glLine(200,287,200,250)

	glLine(200,113,200,250)

	glLine(200,200,200,300)

	glLine(287,287,250,350)

	glLine(113,113,250,350)

	glLine(200,287,300,350)

	glLine(200,113,300,350)

	glLine(287,200,350,400)

	glLine(113,200,350,400)

	glFinish()



def personaje_nes():

	# Cargamos el archivo donde se guardar

	filename('personaje_nes.bmp')

	glCreateWindow(300,300)

	glViewPort(10,10,32,32)

	glClearColor(0,0,0)

	glClear()

	glColor(1,1,1)

	#------ Creacion de Lineas -----#



	#------ Creacion de Cuerpo -----#

	glLine(50,250,30,30)

	glLine(40,50,33,33)

	glFinish()



print(personaje_nes())