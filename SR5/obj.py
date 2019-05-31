"""
Universidad del Valle

@author: Emilio
"""

import struct

def color(r,g,b):

	return bytes([b,g,r])







class Obj(object):

    def __init__(self, filename):

        with open(filename) as f:

            self.lines = f.read().splitlines()

        self.vertices = []

        self.faces = []

        self.vt = []

        self.read()



    def read(self):

        for lineas in self.lines:

            if lineas:

                prefix, value = lineas.split(' ', 1)

                if prefix == 'v':

                    self.vertices.append(list(map(float, value.split(' '))))

                elif prefix == 'vt':

                    self.vt.append(list(map(float, value.split(' '))))

                elif prefix == 'f':

                    self.faces.append([list(map(int, face.split('/'))) for face in value.split(' ')])



class Texture(object):

	def __init__(self, path):

		self.path = path

		self.read()



	def read(self):

		img = open(self.path, 'rb')

		img.seek(2 + 4 + 4)

		header_size = struct.unpack('=l', img.read(4))[0]

		img.seek(2 + 4 + 4 + 4 + 4)

		self.width = struct.unpack('=l', img.read(4))[0]

		self.height = struct.unpack('=l', img.read(4))[0]

		self.framebuffer = []

		img.seek(header_size)



		for y in range(self.height):

			#Array de pixeles vacios

			self.framebuffer.append([])



			for x in range(self.width):

				#azul

				b = ord(img.read(1))

				#Verde

				g = ord(img.read(1))

				#Rojo

				r = ord(img.read(1))

				self.framebuffer[y].append(color(r,g,b))



		img.close()



	def get_Color(self, tx, ty, intensity=1):

		x = int(tx * self.width)

		y = int(ty * self.height)



		return bytes(map(lambda b: round(b*intensity) if b * intensity > 0 else 0, self.framebuffer[y][x]))



#Clase que abre y guarda dentro de una lista los valores de kd

class Mtl(object):

    def __init__(self, filename):

        with open(filename) as f:

            self.lines = f.read().splitlines()

        self.ka = []

        self.kd = []

        self.ke = []

        self.materiales =[]

        self.read()



    def read(self):

        for lineas in self.lines:

            if lineas:

                prefix, valor = lineas.split(' ', 1)

                if prefix == 'Kd' :

                    self.kd.append(list(map(float, valor.split(' '))))



                if prefix == 'newmtl':

                    self.nombre.append(list(valor.split(' ')))

