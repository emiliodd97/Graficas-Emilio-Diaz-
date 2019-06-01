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

countime = 0
clear = GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT
disp = False


glClearColor(0.25, 0.25, 0.25, 1.0)
glEnable(GL_DEPTH_TEST)
glEnable(GL_TEXTURE_2D)

#GL SHADERS FROM https://realpythonGL.com/pythonguide/
vert = """ vertex()
"""
def vertex():

    layout (location = 0) in vec4 position;

    layout (location = 1) in vec4 normal;

    layout (location = 2) in vec2 texcoords;



    uniform mat4 model;

    uniform mat4 view;

    uniform mat4 projection;



    uniform vec4 color;

    uniform vec4 light;



    out vec4 vertexColor;

    out vec2 vertexTexcoords;



    void main()

    {

        float intensity = dot(normal, normalize(light - position))+0.5;



        gl_Position = projection * view * model * position;

        vertexColor = color * intensity;

        vertexTexcoords = texcoords;

    }


frag = """ fragment()

"""
def fragment():
    layout (location = 0) out vec4 diffuseColor;



    in vec4 vertexColor;

    in vec2 vertexTexcoords;



    uniform sampler2D tex;



    void main()

    {

        diffuseColor = vertexColor * texture(tex, vertexTexcoords);

    }

pin = """ def pin_shaderpro()
"""
def pin_shaderpro():

    in vec4 vertexColor;
    in vec2 vertexTexcoords;
    uniform float time;
    uniform vec2 resolution;
    uniform sampler2D tex;

    void main():

    {

        vec2 p = (2. * gl_FragCoord.xy - 1000) / 300;
        for(int i=0; i<5; i++){
            p = abs(p) - 0.375;

        }
        float n = 50.;
        vec2 st = floor(p * n) / n; 

        float r = length(st*abs(cos(time+st.x)*5.));
        float g = length(st*abs(sin(time+st.y)*5.));
        float b = length(st*abs(cos(time*2.)*5.));
        gl_FragColor = vec4(vec3(r,g, b), 1.0 );


upper = OpenGL.GL.shaders.compileProgram(
    OpenGL.GL.shaders.compileShader(vert, GL_VERTEX_SHADER),
    OpenGL.GL.shaders.compileShader(frag, GL_FRAGMENT_SHADER),

)

downer = OpenGL.GL.shaders.compileProgram(
    OpenGL.GL.shaders.compileShader(vert, GL_VERTEX_SHADER),
    OpenGL.GL.shaders.compileShader(pin, GL_FRAGMENT_SHADER), validate = False
)

shader = upper

glUseProgram(shader)


model = glm.mat4(1)
view = glm.mat4(1)
projection = glm.perspective(glm.radians(45), 1200/800, 0.1, 1000.0)

glViewport(0, 0, 800, 600)


batmanobj = pyassimp.load('./modelos/batman.obj')


"""
class cam(object):

    def __init__(self, screen, resolution):

        self.screen = screen


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

            ray = gmap(point, player.direction+angle, 8)

            self.renderC(column, ray, angle, gmap)

            """


cam = glm.vec3(0, 0, 160)
vel = 3
rotationvar = 0
diamn = zfac
frameud = 5

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
            countime
        )

        glUniform4f(
            glGetUniformLocation(shader, "light"),
            xfac, yfac, 100, 1
        )

        glDrawElements(GL_TRIANGLES, len(faces), GL_UNSIGNED_INT, None)


    for child in node.children:
        mainfunc(child)


onz = 0
status = 0

def diam(x, z):
    return numpy.sqrt((x**2 + z**2))

#Movimientos de la camara
#Se incluye las condiciones para que no vaya a traspasar al modelo o se aleje demasiado
def dispfunc():
    global rotationvar, diamn, frameud, onz, countime, status, shader, upper, downer, clear
    diamn = diam(xfac, zfac)
    countime += 1
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
                xfac = math.sin(rotationvar) * diamn
                zfac = math.cos(rotationvar) * diamn


            if event.key == pygame.K_RIGHT:
                rotationvar -= vel
                xfac = math.sin(rotationvar) * diamn
                zfac = math.cos(rotationvar) * diamn


            if event.key == pygame.K_UP:
                if zfac > 10:
                    zfac -= frameud
                elif zfac < -10:
                    zfac += frameud


            if event.key == pygame.K_DOWN:
                if 0 < zfac <500:
                    zfac += frameud
                elif 0 > zfac > -500:
                    zfac -= frameud


            if event.key == pygame.K_w:
                if yfac >= -500:
                    yfac -= frameud


            if event.key == pygame.K_s:
                if yfac < 500:
                    yfac += frameud
            
    return False



while not disp:
    glClear(clear)

    view = glm.lookAt(cam, glm.vec3(0, 0, 0), glm.vec3(0, 1, 0))

    mainfunc(batmanobj.rootnode)

    disp = dispfunc()
    count.tick(30)
    pygame.display.flip()