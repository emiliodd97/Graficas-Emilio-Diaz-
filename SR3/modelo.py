"""
Universidad del Valle

@author: Emilio
"""



def modelo():

	filename('effel-tower.bmp')

	glCreateWindow(800,800)

	glViewPort(0,0,800,800)

	load('./Modelos/effel-tower.obj', (200,500),(0.5,0.5))

	glFinish()



print(modelo())
