"""
Universidad del Valle

@author: Emilio
"""



from bitmap import *




def newModelo():

	renderizando = Bitmap(1000,1000)

	glViewPort(0,0,800,800)

	renderizando.renderer('./Modelos/effel-tower.obj',(200,200,200),(3,3,3))

	renderizando.archivo('effel-tower.bmp')



print(newModelo())