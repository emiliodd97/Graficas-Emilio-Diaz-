"""
Universidad del Valle

@author: Emilio
"""


import pygame

import glm
import pyassimp
import numpy
import math
import random

from OpenGL.GL import *
import OpenGL.GL.shaders

pygame.init()

surface = pygame.display.set_mode((1200, 800), pygame.OPENGLBLIT | pygame.DOUBLEBUF)
background = pygame.image.load("gotham.jpg")
count = pygame.time.Clock()
pygame.key.set_repeat(1, 10)

#Musiquita pa que todo sea mas cool 
pygame.mixer.music.load("newBatman.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)


bmpText = pygame.image.load("./modelos/batman.bmp")
texture_data = pygame.image.tostring(bmpText,"RGB",1)
width = bmpText.get_width()
height = bmpText.get_height()
mitime = 0
clearBuffer = GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT

disp = False


glClearColor(0.25, 0.25, 0.25, 1.0)
glEnable(GL_DEPTH_TEST)
glEnable(GL_TEXTURE_2D)

# OpenGL.GL.shaders
vertex_shader = ""
fragment_shader = ""
pin_shader = ""



shader1 = OpenGL.GL.shaders.compileProgram(
    OpenGL.GL.shaders.compileShader(vertex_shader, GL_VERTEX_SHADER),
    OpenGL.GL.shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER),

)

shader2 = OpenGL.GL.shaders.compileProgram(
    OpenGL.GL.shaders.compileShader(vertex_shader, GL_VERTEX_SHADER),
    OpenGL.GL.shaders.compileShader(pin_shader, GL_FRAGMENT_SHADER), validate = False
)

shader = shader1

glUseProgram(shader)


model = glm.mat4(1)
view = glm.mat4(1)
projection = glm.perspective(glm.radians(45), 800/600, 0.1, 1000.0)

glViewport(0, 0, 800, 600)


batmanobj = pyassimp.load('./modelos/batman.obj')
"""
class cam(object):

    def __init__(self, screen, resolution):

        self.screen = screen

        # get_size_arma ---> funcion que obtiene el tamaño de la camara

        self.width, self.height = self.screen.get_size()

        self.resolution = float(resolution)


    def render(self, player, gmap):

        self.limpiando_movimiento(player.direction, gmap.cielo, gmap.light)

        self.columnasRender(player, gmap)

        self.armaRender(player.weapon, player.positionWeapon)

  

    def  Render(self, player, gmap):

        for column in range(int(self.resolution)):

            angle = (math.pi*0.4) * (column/self.resolution-0.5)

            # damos los puntos a cada eje

            point = player.x, player.y

            ray = gmap.raycast(point, player.direction+angle, 8)

            self.renderC(column, ray, angle, gmap)

            """


def mainfunc(node):
    global texture_data, width, height
    model = node.transformation.astype(numpy.float32)

    for mesh in node.meshes:
        texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, texture_data)
        glGenerateMipmap(GL_TEXTURE_2D)

        vertex_data = numpy.hstack((
            numpy.array(mesh.vertices, dtype=numpy.float32),
            numpy.array(mesh.normals, dtype=numpy.float32),
            numpy.array(mesh.texturecoords[0], dtype=numpy.float32)
        ))

        faces = numpy.hstack(
            numpy.array(mesh.faces, dtype=numpy.int32)
        )

        glVertexAttribPointer(0, 3, GL_FLOAT, False, 9 * 4, None)
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(1, 3, GL_FLOAT, False, 9 * 4, ctypes.c_void_p(3 * 4))
        glEnableVertexAttribArray(1)

        vertex_buffer_object = glGenVertexArrays(1)
        glBindBuffer(GL_ARRAY_BUFFER, vertex_buffer_object)
        glBufferData(GL_ARRAY_BUFFER, vertex_data.nbytes, vertex_data, GL_STATIC_DRAW)

        
        glVertexAttribPointer(2, 3, GL_FLOAT, False, 9 * 4, ctypes.c_void_p(6 * 4))
        glEnableVertexAttribArray(2)


        element_buffer_object = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, element_buffer_object)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, faces.nbytes, faces, GL_STATIC_DRAW)

        glUniformMatrix4fv(
            glGetUniformLocation(shader, "model"), 1 , GL_FALSE, 
            model
        )
        glUniformMatrix4fv(
            glGetUniformLocation(shader, "view"), 1 , GL_FALSE, 
            glm.value_ptr(view)
        )
        glUniformMatrix4fv(
            glGetUniformLocation(shader, "projection"), 1 , GL_FALSE, 
            glm.value_ptr(projection)
        )

        diffuse = mesh.material.properties["diffuse"]

        glUniform4f(
            glGetUniformLocation(shader, "color"),
            *diffuse,
            1
        )

        glUniform1f(
            glGetUniformLocation(shader, "time"),
            mitime
        )

        glUniform4f(
            glGetUniformLocation(shader, "light"),
            cam.x, cam.y, 100, 1
        )

        glDrawElements(GL_TRIANGLES, len(faces), GL_UNSIGNED_INT, None)


    for child in node.children:
        mainfunc(child)

"""
def renderC(self, column, ray, angle, gmap):

        left = int(math.floor(column*(self.width/self.resolution)))

        for i in range(len(ray)-1, -1, -1):

            step = ray[i]

            if (step.height > 0):

                texture = gmap.textura

                width = int(math.ceil((self.width/self.resolution)))

                textureX = int(texture.width*step.offset)

                wall = self.project(step.height, angle, step.distance)

                imagenDir = pygame.Rect(textureX, 0, 1, texture.height)

                cambiarImagen = texture.image.subsurface(imagenDir)

                scaleR = pygame.Rect(left, wall.size_arma, width, wall.height)

                escamed = pygame.transform.scale(cambiarImagen, scaleR.size)

                self.screen.blit(escamed, scaleR)

"""

cam = glm.vec3(0, 0, 160)
vel = 3
rotationvar = 0
diamn = cam.z
zoom = 5
onz = 0
status = 0

def diam(x, z):
    return numpy.sqrt((x**2 + z**2))

#Movimientos de la camara
#Se incluye las condiciones para que no vaya a traspasar al modelo o se aleje demasiado
def dispfunc():
    global rotationvar, diamn, zoom, onz, mitime, status, shader, shader1, shader2, clearBuffer
    diamn = diam(cam.x, cam.z)
    mitime += 1
    if(status == 2 or status == 0):
        glClearColor(0.25, 0.25, 0.25, 1.0)
    else:
        glClearColor(random.random(), 0, random.random(), 1)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            return True


        if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
            return True


        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                rotationvar += vel
                cam.x = math.sin(rotationvar) * diamn
                cam.z = math.cos(rotationvar) * diamn


            if event.key == pygame.K_RIGHT:
                rotationvar -= vel
                cam.x = math.sin(rotationvar) * diamn
                cam.z = math.cos(rotationvar) * diamn


            if event.key == pygame.K_UP:
                if cam.z > 10:
                    cam.z -= zoom
                elif cam.z < -10:
                    cam.z += zoom


            if event.key == pygame.K_DOWN:
                if 0 < cam.z <500:
                    cam.z += zoom
                elif 0 > cam.z > -500:
                    cam.z -= zoom


            if event.key == pygame.K_w:
                if cam.y >= -500:
                    cam.y -= zoom


            if event.key == pygame.K_s:
                if cam.y < 500:
                    cam.y += zoom
            
    return False



while not disp:
    glClear(clearBuffer)

    view = glm.lookAt(cam, glm.vec3(0, 0, 0), glm.vec3(0, 1, 0))

    mainfunc(batmanobj.rootnode)

    disp = dispfunc()
    count.tick(15)
    pygame.display.flip()