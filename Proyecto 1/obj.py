"""
Universidad del Valle

@author: Emilio
"""



import struct

import mmap

import numpy



def color(r,g,b):

    return bytes([r, b , g])





def try_int(s, base=10, valor=None):

    try:

        return int(s, base) -1

    except ValueError:

        return valor



"Clase que sirve para abrir un archivo obj"

class Obj(object):

    def __init__(self, filename, mtl=None):

        self.verificador = False

        #Condicion para abrir archivo obj

        with open(filename) as f:

            self.lines = f.read().splitlines()

        if mtl:

            self.verificador = True

            with open(mtl) as x:

                self.linea = x.read().splitlines()

        #Todos los datos se guardaran en un arraay

        self.vertices = []

        self.vt = []    #tvertices

        self.faces = []

        self.nvertices = []

        self.tipoMat = []

        self.kD = []

        self.kdMap = []

        self.ordenarMateriales = []

        self.contadorCaras = []

        self.material = {}

        #inicializamos la funcion para leer

        self.read()



    #Funcion para leer archivo

    def read(self):

        self.mater = ''



        for line in self.lines:

            if line:

                prefix, value = line.split(' ', 1)

                if prefix == 'v':

                    #Guardamos los datos en la lista

                    self.vertices.append(list((map(float, value.split(' ')))))

                elif prefix == 'vt':

                    #Guardamos los datos en la lista

                    self.vt.append(list((map(float, value.split(' ')))))

                elif prefix == 'f':

                        if self.verificador == False:

                            self.faces.append([list(map(int, face.split('/'))) for face in value.split(' ')])

                        else:

                            lista = [list(map(int, face.split('/'))) for face in value.split(' ')]

                            lista.append(self.mater)

                            self.faces.append(lista)



                elif prefix == 'usemtl':

                    self.mater = value

        if self.verificador:

            for line2 in self.linea:

                if line2:

                    prefix2, valor = line2.split(' ', 1)

                    if prefix2 == 'newmtl':

                        self.tipoMat.append(valor)

                    if prefix2 == 'Kd':

                        self.kD.append(list(map(float, valor.split(' '))))

            for indice in range(len(self.tipoMat) - 1):

                self.material[self.tipoMat[indice]] = self.kD[indice]



'Clase para leer un archivo bmp'

class Texture(object):

    def __init__(self, path):

        self.path = path

        self.read()




    def read(self):

        img = open(self.path, "rb")

        m = mmap.mmap(img.fileno(), 0, access=mmap.ACCESS_READ)

        ba = bytearray(m)

        header_size = struct.unpack("=l", ba[10:14])[0]

        self.width = struct.unpack("=l", ba[18:22])[0]

        self.height = struct.unpack("=l", ba[18:22])[0]

        all_bytes = ba[header_size::]

        self.pixels = numpy.frombuffer(all_bytes, dtype='uint8')

        img.close()



  

    def get_color(self, tx, ty, intensity):

        x = int(tx * self.width)

        y = int(ty * self.height)

        index = (y * self.width + x) * 3

        processed = self.pixels[index:index+3] * intensity

        return bytes(processed.astype(numpy.uint8))