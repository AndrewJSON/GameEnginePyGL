
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
        self.VERT_COMPONENT_COUNT = 4
        self.ctype     = ct.c_void_p(0)
        self.vaos      = []
        self.vbos      = []
        self.shader = _shader


    def make_model_from_verts(self, _verts):

        vaoID = self.vertObjFact.create_and_bind_VAO()
        print("vaoID:", vaoID)
        attribList = 0
        self.store_data_in_attributeList( attribList, _verts )
        self.vertObjFact.unbind_VAO()

        vertCount = self.vertObjFact.eval_vert_count_from_verts( _verts )
        print("vertCount:", vertCount)
        rawModel = rm.RawModel( vaoID, vertCount )
        return rawModel


    def store_data_in_attributeList(self, _attribNum, _data):

        glBufferType = GL.GL_ARRAY_BUFFER
        vboID        = self.vertObjFact.create_and_bind_VBO( glBufferType )
        byteCount    = self.vertObjFact.determine_vertexArray_byteCount( _data )

        vPosition = GL.glGetAttribLocation(self.shader, 'vPosition')
        print("vPosition:", vPosition, "attribNum:", _attribNum)
        GL.glEnableVertexAttribArray(vPosition)

        GL.glBufferData( glBufferType, byteCount, _data, GL.GL_STATIC_DRAW )
        GL.glVertexAttribPointer( vPosition,     # attrib list id with verts
                                  self.VERT_COMPONENT_COUNT,
                                  GL.GL_FLOAT,
                                  False,        # is data normalized?
                                  0,            # distance between vertex data
                                  self.ctype)   # start offset

        GL.glDisableVertexAttribArray(vPosition)
        self.vertObjFact.unbind_VBO( glBufferType )


''' END '''

