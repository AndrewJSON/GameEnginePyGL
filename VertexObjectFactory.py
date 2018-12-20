
''' 
 * VertexObjectFactory.py
 *
 *   Created on:         16.12.2018
 *   Author:             Andrew Jason Bishop
 * 
 * General description:
 *   creates VertexArrayObjects (VAOs) and VertexArrayBuffers (VBOs)
'''

import OpenGL.GL as GL
import ctypes as ct


class VertexObjectFactory:

    def __init__(self):

        self.VERT_COMPONENT_COUNT = 4
        self.ctype     = ct.c_void_p(0)
        self.vaos      = {}
        self.vbos      = []


    def eval_vert_count_from_verts(self, _verts):
        return int( _verts.size / self.VERT_COMPONENT_COUNT )


    def eval_vert_count_from_indices(self, _indices):
        return _indices.size


    def create_and_bind_VAO(self, _name = "default"):

        vaoID = GL.glGenVertexArrays( 1 )
        self.vaos.update({_name : vaoID})

        GL.glBindVertexArray( vaoID )
        return vaoID


    def unbind_VAO(self):
        GL.glBindVertexArray( 0 )


    def create_and_bind_VBO(self, _glBufferType, _name = "default"):

        vboID = GL.glGenBuffers( 1 )
        self.vbos.append( vboID )
        #self.vbos.update({_name : vboID})

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
            GL.glDeleteVertexArrays(vao)


    def cleanUp_VBOs(self):

        for vbo in self.vbos:
            GL.glDeleteBuffers(vbo)


''' END '''

