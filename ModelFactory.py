
''' 
 * ModelFactory.py
 *
 *   Created on:         15.12.2018
 *   Author:             Andrew Jason Bishop
 * 
 * General description:
 *   xxx
'''

import OpenGL.GL  as GL

import RawModel as rm


class ModelFactory:

    def __init__(self):
        self.DIMENSIONS = 3
        self.ct = ctypes.c_void_p(0)
        self.vaos = []
        self.vbos = []


    def make_model_from_verts(self, _verts):

        vaoID = self.create_and_bind_VAO()

        self.bindIndicesBuffer( _indices )
        self.store_data_in_attributeList( 0, _positions )
        self.unbindVAO() # TODO order of unbinding?

        posCount = len(_indices)
        rawModel = rm.RawModel( vaoID, posCount )
        return rawModel


    def cleanUp(self):

        self.cleanUp_VAOs()
        self.cleanUp_VBOs()


    def cleanUp_VAOs(self):

        for vao in self.vaos:
            GL.glDeleteVertexArrays(vao)


    def cleanUp_VBOs(self):

        for vbo in self.vbos:
            GL.glDeleteBuffers(vbo)


    def create_and_bind_VAO(self):

        vaoID = GL.glGenVertexArrays( 1 )
        self.vaos.append(vaoID)

        GL.glBindVertexArray( vaoID )
        return vaoID


    def store_data_in_attributeList(self, _attribNumber, _data):

        glBufferType = GL.GL_ARRAY_BUFFER
        vboID = self.create_and_bind_VBO( glBufferType )

        va_size = ArrayDatatype.arrayByteCount( _data )
        GL.glBufferData( glBufferType, va_size, _data, GL.GL_STATIC_DRAW )
        GL.glVertexAttribPointer(position, 4, GL.GL_FLOAT, False, 0, self.ct)

        # TODO first unbind VAO like mentioned in gitSample-00.py?
        # not done at this pint in youtube: OpenGL 3D Game Tutorial 2
        # see line 30
        self.unbind_VAO() # TODO see comments above
        self.unbind_VBO( glBufferType )


    def bindIndicesBuffer(self, _indices):

        glBufferType = GL.GL_ELEMENT_ARRAY_BUFFER
        vboID = self.create_and_bind_VBO( glBufferType )

        va_size = ArrayDatatype.arrayByteCount( _data )
        GL.glBufferData( glBufferType, va_size, _data, GL.GL_STATIC_DRAW )


    def create_and_bind_VBO(self):

        vboID = GL.glGenBuffers( 1 )
        self.vbos.append(vboID)

        GL.glBindBuffer( GL.GL_ARRAY_BUFFER, vboID )
        return vboID


    def create_and_bind_VBO(self, _glBufferType):

        vboID = GL.glGenBuffers( 1 )
        self.vbos.append(vboID)

        GL.glBindBuffer( _glBufferType, vboID )
        return vboID


   def unbind_VBO(self, _glBufferType):
        GL.glBindBuffer( _glBufferType, 0 )


    def unbind_VAO(self):
        GL.glBindVertexArray( 0 )


''' END '''

