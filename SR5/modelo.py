"""
Universidad del Valle

@author: Emilio
"""
from bitmap import *

from obj import *



def texture():

	renderizando = Bitmap(1000,1000)

	glViewPort(0,0,800,800)

	t = Texture('./Modelos/model.bmp')

	renderizando.renderer('./Modelos/effel-tower.obj', scale=(0,0,0), translate=(0,0,0))

	renderizando.archivo('model.bmp')


print(texture())