
''' 
 * ModelFactory.py
 *
 *   Created on:         15.12.2018
 *   Author:             Andrew Jason Bishop
 * 
 * General description:
 *   Greates OpenGL 3D Models using VAOs and VBOs
'''

import OpenGL.GL            as GL
import pygame               as pg
import ctypes               as ct

import VertexObjectFactory  as vof
import RawModel             as rm
import ModelTexture         as mt
import TexturedModel        as tm


class ModelFactory:

    def __init__(self, _shader):

        self.vertObjFact = vof.VertexObjectFactory()
        self.VERT_COMPONENT_COUNT = 3
        self.ctype     = ct.c_void_p(0)
        self.shader = _shader
        self.textures = []


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


    def make_model_from_verts_and_indices(self, _verts, _indices, _texCoords):

        vaoID = self.vertObjFact.create_and_bind_VAO()
        self.bind_and_fill_buffer( GL.GL_ELEMENT_ARRAY_BUFFER, _indices )
        attribList = 0
        self.store_data_in_attributeList( GL.GL_ARRAY_BUFFER, 0, 3, _verts )
        self.store_data_in_attributeList( GL.GL_ARRAY_BUFFER, 1, 2, _texCoords )
        self.vertObjFact.unbind_VAO()

        vertCount = self.vertObjFact.eval_vert_count_from_indices( _indices )
        rawModel = rm.RawModel( vaoID, vertCount )
        return rawModel


    def store_data_in_attributeList(self, _glBufferType, _attribNum, _vecSize, _data):

        vboID        = self.vertObjFact.create_and_bind_VBO( _glBufferType )
        byteCount    = self.vertObjFact.determine_vertexArray_byteCount( _data )

        #vPosition = GL.glGetAttribLocation(self.shader, 'vPosition')
        #GL.glEnableVertexAttribArray(vPosition)
        GL.glEnableVertexAttribArray(_attribNum)

        GL.glBufferData( _glBufferType, byteCount, _data, GL.GL_STATIC_DRAW )
        GL.glVertexAttribPointer( _attribNum,     # vPosition
                                  _vecSize,
                                  GL.GL_FLOAT,
                                  False,           # is data normalized?
                                  0,               # stride of vertex sets
                                  self.offset(0) ) # start offset

        GL.glDisableVertexAttribArray(_attribNum)
        self.vertObjFact.unbind_VBO( _glBufferType )


    def bind_and_fill_buffer(self, _glBufferType, _data):
        vboID        = self.vertObjFact.create_and_bind_VBO( _glBufferType )
        byteCount    = self.vertObjFact.determine_vertexArray_byteCount( _data )

        GL.glBufferData( _glBufferType, byteCount, _data, GL.GL_STATIC_DRAW )


    def make_textured_model(self, _verts, _indices, _texCoords, _texFileName):

        rawMod = self.make_model_from_verts_and_indices( _verts,
                                                         _indices,
                                                         _texCoords )

        texID = self.load_texture( _texFileName )
        modTex = mt.ModelTexture( texID )
        texMod = tm.TexturedModel( rawMod, modTex )
        #GL.glDeleteTextures( texID )

        return texMod


    def load_texture(self, _fileName):

        textureSurface = pg.image.load( _fileName )
        textureData = pg.image.tostring(textureSurface, "RGBA", 1)
        width = textureSurface.get_width()
        height = textureSurface.get_height()
    
        GL.glEnable(GL.GL_TEXTURE_2D)
        texID = GL.glGenTextures(1)
        self.textures.append(texID)

        GL.glBindTexture(GL.GL_TEXTURE_2D, texID)
        GL.glTexImage2D(GL.GL_TEXTURE_2D, 0, GL.GL_RGB, width, height,
                     0, GL.GL_RGBA, GL.GL_UNSIGNED_BYTE, textureData)

        GL.glTexParameterf(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_S, GL.GL_REPEAT)
        GL.glTexParameterf(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_T, GL.GL_REPEAT)
        GL.glTexParameterf(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MAG_FILTER, GL.GL_NEAREST)
        GL.glTexParameterf(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MIN_FILTER, GL.GL_NEAREST)

        return texID


    def offset(self, _off):
        return ct.c_void_p( _off )


''' END '''

