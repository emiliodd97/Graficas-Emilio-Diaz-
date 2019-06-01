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




pygame.init()
surface = pygame.display.set_mode((1200, 800), pygame.OPENGLBLIT | pygame.DOUBLEBUF)
background = pygame.image.load("gotham.jpg")
clock = pygame.time.Clock()
pygame.key.set_repeat(1, 10)

glClearColor(0.18, 0.18, 0.18, 1.0)
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

# matrixes
model = glm.mat4(1)
view = glm.mat4(1)
projection = glm.perspective(glm.radians(45), 800/600, 0.1, 1000.0)

glViewport(0, 0, 800, 600)


scene = pyassimp.load('./modelos/batman.obj')


def glize(node):
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

        vertex_buffer_object = glGenVertexArrays(1)
        glBindBuffer(GL_ARRAY_BUFFER, vertex_buffer_object)
        glBufferData(GL_ARRAY_BUFFER, vertex_data.nbytes, vertex_data, GL_STATIC_DRAW)

        glVertexAttribPointer(0, 3, GL_FLOAT, False, 9 * 4, None)
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(1, 3, GL_FLOAT, False, 9 * 4, ctypes.c_void_p(3 * 4))
        glEnableVertexAttribArray(1)
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
            camera.x, camera.y, 100, 1
        )

        glDrawElements(GL_TRIANGLES, len(faces), GL_UNSIGNED_INT, None)


    for child in node.children:
        glize(child)


camera = glm.vec3(0, 0, 160)
vel = 3
rotation = 0
radio = camera.z
zoom = 5
camera_z = 0
status = 0

def radius(x, z):
    return numpy.sqrt((x**2 + z**2))


def process_input():
    global rotation, radio, zoom, camera_z, mitime, status, shader, shader1, shader2, clearBuffer
    radio = radius(camera.x, camera.z)
    mitime += 1
    if(status == 2 or status == 0):
        glClearColor(0.18, 0.18, 0.18, 1.0)
    else:
        glClearColor(random.random(), 0, random.random(), 1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
            return True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rotation += vel
                camera.x = math.sin(rotation) * radio
                camera.z = math.cos(rotation) * radio
            if event.key == pygame.K_RIGHT:
                rotation -= vel
                camera.x = math.sin(rotation) * radio
                camera.z = math.cos(rotation) * radio
            if event.key == pygame.K_UP:
                if camera.z > 20:
                    camera.z -= zoom
                elif camera.z < -20:
                    camera.z += zoom
            if event.key == pygame.K_DOWN:
                if 0 < camera.z <300:
                    camera.z += zoom
                elif 0 > camera.z > -300:
                    camera.z -= zoom
            if event.key == pygame.K_w:
                if camera.y >= -300:
                    camera.y -= zoom
            if event.key == pygame.K_s:
                if camera.y < 300:
                    camera.y += zoom
            if event.key == pygame.K_p:
                if(status == 2):
                    pygame.mixer.music.unpause()
                    shader = shader2
                    #clearBuffer = GL_DEPTH_BUFFER_BIT
                    glUseProgram(shader)
                    status = 1
                elif(status == 1):
                    pygame.mixer.music.pause()
                    shader = shader1
                    clearBuffer = GL_DEPTH_BUFFER_BIT | GL_COLOR_BUFFER_BIT
                    glClear(clearBuffer)
                    glUseProgram(shader)
                    status = 2
                elif(status == 0):
                    pygame.mixer.music.play(0, 16.5)
                    shader = shader2
                    glUseProgram(shader)
                    status = 1
    return False


done = False
while not done:
    glClear(clearBuffer)

    view = glm.lookAt(camera, glm.vec3(0, 0, 0), glm.vec3(0, 1, 0))

    glize(scene.rootnode)

    done = process_input()
    clock.tick(15)
    pygame.display.flip()