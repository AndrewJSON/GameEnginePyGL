
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

import VertexObjectFactory as vof
import RawModel as rm


class ModelFactory:

    def __init__(self, _shader):

        self.vertObjFact = vof.VertexObjectFactory()
        self.VERT_COMPONENT_COUNT = 3
        self.ctype     = ct.c_void_p(0)
        self.shader = _shader


    def make_model_from_verts(self, _verts):

        vaoID = self.vertObjFact.create_and_bind_VAO("triangles")
        attribList = 0
        self.store_data_in_attributeList( GL.GL_ARRAY_BUFFER, 
                                          attribList,
                                          _verts )
        self.vertObjFact.unbind_VAO()

        vertCount = self.vertObjFact.eval_vert_count_from_verts( _verts )
        print("vertCount:", vertCount)
        rawModel = rm.RawModel( vaoID, vertCount )
        return rawModel


    def make_model_from_verts_and_indices(self, _verts, _indices):

        vaoID = self.vertObjFact.create_and_bind_VAO("triangles")
        self.bind_and_fill_buffer( GL.GL_ELEMENT_ARRAY_BUFFER, _indices )
        attribList = 0
        self.store_data_in_attributeList( GL.GL_ARRAY_BUFFER, 
                                          attribList,
                                          _verts )
        self.vertObjFact.unbind_VAO()

        vertCount = self.vertObjFact.eval_vert_count_from_indices( _indices )
        rawModel = rm.RawModel( vaoID, vertCount )
        return rawModel


    def store_data_in_attributeList(self, _glBufferType, _attribNum, _data):

        vboID        = self.vertObjFact.create_and_bind_VBO( _glBufferType )
        byteCount    = self.vertObjFact.determine_vertexArray_byteCount( _data )

        vPosition = GL.glGetAttribLocation(self.shader, 'vPosition')
        print("vPosition:", vPosition, "attribNum:", _attribNum)
        GL.glEnableVertexAttribArray(vPosition)

        GL.glBufferData( _glBufferType, byteCount, _data, GL.GL_STATIC_DRAW )
        GL.glVertexAttribPointer( vPosition,     # attrib list id with verts
                                  self.VERT_COMPONENT_COUNT,
                                  GL.GL_FLOAT,
                                  False,           # is data normalized?
                                  0,               # stride of vertex sets
                                  self.offset(0) ) # start offset

        GL.glDisableVertexAttribArray(vPosition)
        self.vertObjFact.unbind_VBO( _glBufferType )


    def bind_and_fill_buffer(self, _glBufferType, _data):
        vboID        = self.vertObjFact.create_and_bind_VBO( _glBufferType )
        byteCount    = self.vertObjFact.determine_vertexArray_byteCount( _data )

        GL.glBufferData( _glBufferType, byteCount, _data, GL.GL_STATIC_DRAW )


    def offset(self, _off):
        return ct.c_void_p( _off )


''' END '''

