
''' 
 * ModelFactory.py
 *
 *   Created on:         15.12.2018
 *   Author:             Andrew Jason Bishop
 * 
 * General description:
 *   Greates OpenGL 3D Models using VAOs and VBOs
'''

import OpenGL.GL  as GL
import ctypes as ct

import RawModel as rm



class ModelFactory:

    def __init__(self):
        self.VERT_COMPONENT_COUNT = 4
        self.ctype     = ct.c_void_p(0)
        self.vaos      = []
        self.vbos      = []


    def make_model_from_verts(self, _verts):

        vaoID = self.create_and_bind_VAO()
        print("vaoID:", vaoID)
        attribList = 0
        self.store_data_in_attributeList( attribList, _verts )
        self.unbind_VAO()

        vertCount = self.eval_vert_count_from_verts( _verts )
        print("vertCount:", vertCount)
        rawModel = rm.RawModel( vaoID, vertCount )
        return rawModel


    def store_data_in_attributeList(self, _attribNum, _data):

        glBufferType = GL.GL_ARRAY_BUFFER
        vboID        = self.create_and_bind_VBO( glBufferType )
        byteCount    = self.determine_vertexArray_byteCount( _data )

        GL.glBufferData( glBufferType, byteCount, _data, GL.GL_STATIC_DRAW )
        GL.glVertexAttribPointer( _attribNum, 
                                  self.VERT_COMPONENT_COUNT,
                                  GL.GL_FLOAT,
                                  False,        # is data normalized?
                                  0,            # distance between vertex data
                                  self.ctype)   # start offset

        self.unbind_VBO( glBufferType )


    def eval_vert_count_from_verts(self, _verts):
        return int( _verts.size / self.VERT_COMPONENT_COUNT )


    def eval_vert_count_from_indices(self, _indices):
        return len(_indices)


    def create_and_bind_VAO(self):

        vaoID = GL.glGenVertexArrays( 1 )
        self.vaos.append(vaoID)

        GL.glBindVertexArray( vaoID )
        return vaoID


    def unbind_VAO(self):
        GL.glBindVertexArray( 0 )


    def create_and_bind_VBO(self, _glBufferType):

        vboID = GL.glGenBuffers( 1 )
        self.vbos.append(vboID)

        GL.glBindBuffer( _glBufferType, vboID )
        return vboID


    def determine_vertexArray_byteCount(self, _verts):
        return GL.ArrayDatatype.arrayByteCount( _verts )


    def unbind_VBO(self, _glBufferType):
        GL.glBindBuffer( _glBufferType, 0 )


    def cleanUp(self):

        self.cleanUp_VAOs()
        self.cleanUp_VBOs()


    def cleanUp_VAOs(self):

        for vao in self.vaos:
            GL.glDeleteVertexArrays(1, vao)


    def cleanUp_VBOs(self):

        for vbo in self.vbos:
            GL.glDeleteBuffers(1, vbo)


''' END '''

