
''' 
 * Renderer.py
 *
 *   Created on:         15.12.2018
 *   Author:             Andrew Jason Bishop
 * 
 * General description:
 *   xxx
'''

import OpenGL.GL         as GL
import ctypes            as ct


class Renderer:

    def __init__(self, _shaderProg):
        self.shaderProgram = _shaderProg


    def prepare(self):

        GL.glClearColor( 0.231, 0.231, 0.243, 1.0 )
        GL.glEnable( GL.GL_DEPTH_TEST )

    def render(self, _model):

        GL.glClear( GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT )
        self.start()
        GL.glBindVertexArray( _model.getVaoID() )
        GL.glEnableVertexAttribArray( 0 )
        GL.glDrawElements( GL.GL_TRIANGLES,
                           _model.getVertexCount(),
                           GL.GL_UNSIGNED_INT,
                           ct.c_void_p(0) ) #ct.c_void_p(0)
        #GL.glDrawArrays( GL.GL_TRIANGLES, 0, _model.getVertexCount() )
        GL.glDisableVertexAttribArray( 0 )
        GL.glBindVertexArray( 0 )
        self.stop()


    def render_textured_model(self, _texModel):

        rawModel = _texModel.rawModel
        texture = _texModel.modelTexture
        texID = texture.texID

        GL.glClear( GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT )
        
        GL.glBindVertexArray( rawModel.getVaoID() )
        GL.glEnableVertexAttribArray( 0 )
        GL.glEnableVertexAttribArray( 1 )
        #GL.glBindTexture(GL.GL_TEXTURE_2D, texID)
        GL.glDrawElements( GL.GL_TRIANGLES,
                           rawModel.getVertexCount(),
                           GL.GL_UNSIGNED_INT,
                           ct.c_void_p(0) ) #ct.c_void_p(0)
        GL.glDisableVertexAttribArray( 0 )
        GL.glDisableVertexAttribArray( 1 )
        GL.glBindVertexArray( 0 )


    def render_entity(self, _entity, _shader):

        texModel = _entity.texturedModel
        modelTex = texModel.modelTexture
        texID    = modelTex.texID
        rawModel = texModel.getRawModel()
        tMat     = _entity.transformationMatrix

        GL.glClear( GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT )

        GL.glBindVertexArray( rawModel.getVaoID() )
        GL.glEnableVertexAttribArray( 0 )
        GL.glEnableVertexAttribArray( 1 )
        self.shaderProgram.loadTransformationMatrix( tMat )
        #GL.glBindTexture(GL.GL_TEXTURE_2D, texID)
        GL.glDrawElements( GL.GL_TRIANGLES,
                           rawModel.getVertexCount(),
                           GL.GL_UNSIGNED_INT,
                           ct.c_void_p(0) )
        GL.glDisableVertexAttribArray( 0 )
        GL.glDisableVertexAttribArray( 1 )
        GL.glBindVertexArray( 0 )


    def start(self):
        GL.glUseProgram( self.shaderProgram )


    def stop(self):
        GL.glUseProgram( 0 )





''' END '''

