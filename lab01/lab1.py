"""
Universidad del Valle

@author: Emilio
"""

from bmp import *



def poligono_1():

	filename('Polygon_1.bmp')

	glCreateWindow(500,500)

	glViewPort(0,0,800,800)

	glClearColor(0,0,0)

	glClear() 

	glColor(1,1,1)

	#utilizamos la funcion lineas

	puntos = [(165, 380), (185, 360), (180, 330), (207, 345), (233, 330) ,(230, 360), (250, 380), (220, 385), (205, 410), (193, 383)]

	filling_any_polygon(puntos)

	glFinish()



def poligono_2():

	filename('Polygon_2.bmp')

	glCreateWindow(800,800)

	glViewPort(0,0,800,800)

	glClearColor(0,0,0)

	glClear() 

	glColor(1,1,1)

	#Utilizamos la funcion de lineas

	#------ (x1,y1,x2,y2)

	puntos =[(321, 335) ,(288, 286) ,(339, 251) ,(374, 302)]

	filling_any_polygon(puntos)

	glFinish()



def poligono_3():

	filename('Polygon_3.bmp')

	glCreateWindow(500,500)

	glViewPort(0,0,800,800)

	glClearColor(0,0,0)

	glClear() 

	glColor(1,1,1)

	#--------------------#

	puntos_3 = [(377, 249), (411, 197), (436, 249)]

	filling_any_polygon(puntos_3)

	glFinish()



def poligono_4():

	filename('All_Polygon.bmp')

	glCreateWindow(800,800)

	glViewPort(0,0,800,800)

	glClearColor(0,0,0)

	glClear() 

	glColor(1,1,1)

	#------------------------#

	puntos_1 = [(165, 380), (185, 360), (180, 330), (207, 345), (233, 330) ,(230, 360), (250, 380), (220, 385), (205, 410), (193, 383)]

	puntos_2 = [(321, 335) ,(288, 286) ,(339, 251) ,(374, 302)]

	puntos_3 = [(377, 249), (411, 197), (436, 249)]

	puntos_4 = [(413, 177) ,(448, 159) ,(502, 88), (553, 53) ,(535, 36), (676, 37), (660, 52), (750, 145) ,(761, 179), (672, 192), (659, 214), (615, 214) ,(632, 230) ,(580, 230) ,(597, 215) ,(552, 214) ,(517, 144), (466, 180)]

	puntos_5 = [(682, 175) ,(708, 120) ,(735, 148), (739, 170)]



	filling_any_polygon(puntos_1)

	filling_any_polygon(puntos_2)

	filling_any_polygon(puntos_3)

	filling_any_polygon(puntos_4)

	glColor(0,0,0)

	filling_any_polygon(puntos_5)

	glFinish()









poligono_2()

poligono_4()