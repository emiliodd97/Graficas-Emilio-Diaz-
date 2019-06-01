"""
Universidad del Valle

@author: Emilio
"""



from bmp import *

objetos = Bitmap(1000,1000)
objetos.glCreateWindow(1000,1000)
objetos.glViewPort(0,0,999,999)

objetos.glLine(10,10,10,110)
objetos.glLine(990,10,10,10)
objetos.glLine(990,110,10,110)
objetos.glLine(990,10,990,110)

i = 10
x1 = 20
x2 = 20

while(i<950):

    objetos.glLine((x1+i),20,(x2+i),50)
    i += 1

objetos.glLine(90, 70, 90, 100)
objetos.glLine(150, 70, 150, 100)
objetos.glLine(210, 70, 210, 100)
objetos.glLine(270, 70, 270, 100)
objetos.glLine(330, 70, 330, 100)
objetos.glLine(390, 70, 390, 100)
objetos.glLine(450, 70, 450, 100)
objetos.glLine(510, 70, 510, 100)
objetos.glLine(570, 70, 570, 100)
objetos.glLine(630, 70, 630, 100)
objetos.glLine(690, 70, 690, 100)
objetos.glLine(750, 70, 750, 100)
objetos.glLine(810, 70, 810, 100)
objetos.glLine(870, 70, 870, 100)
objetos.glLine(930, 70, 930, 100)
objetos.glLine(990, 70, 990, 100)

#Lobo izquierda
objetos.lookAt(V3(-1,0,5), V3(0.8,0.7,0), V3(0,1,0))
objetos.load('./modelos/WOLF.OBJ', mtl='./modelos/WOLF.MTL', translate=(0, 0, 0), scale=(0.2,0.2,0.2), rotate=(0, -1, 0))

#Cocodrilo derecha
objetos.lookAt(V3(1,0,5), V3(-0.8,0.7,0), V3(0,1,0))
objetos.load('./modelos/CROCODIL.OBJ', mtl='./modelos/CROCODIL.MTL', translate=(0, 0, 0), scale=(0.2,0.2,0.2), rotate=(0, -4, 0))

#Murcielago derecha
objetos.lookAt(V3(1,1,5), V3(-0.4,0,0), V3(0,1,0))
objetos.load('./modelos/VAMP_BAT.OBJ', mtl='./modelos/VAMP_BAT.MTL', translate=(0, 0, 0), scale=(0.1,0.1,0.1), rotate=(0, -1, 0))

#Aguila izquierda
objetos.lookAt(V3(1,1,5), V3(-0.8,0,0), V3(0,1,0))
objetos.load('./modelos/EAGLE_2.OBJ', mtl='./modelos/EAGLE_2.MTL', translate=(0, 0, 0), scale=(0.1,0.1,0.1), rotate=(0, -0.1, 0))

#Oso centro
objetos.lookAt(V3(1,1,5), V3(-0.3,-0.3,0), V3(0,1,0))
objetos.load('./modelos/BEAR_KDK.OBJ', mtl='./modelos/BEAR_KDK.MTL', translate=(0, 0, 0), scale=(0.3,0.3,0.3), rotate=(0, -0.3, 0))

objetos.archivo('EscenaFinal.bmp')