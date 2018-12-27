
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
        GL.glEnableVertexAttribArray( 0 );
        GL.glDrawElements( GL.GL_TRIANGLES,
                           _model.getVertexCount(),
                           GL.GL_UNSIGNED_INT,
                           ct.c_void_p(0) ) #ct.c_void_p(0)
        #GL.glDrawArrays( GL.GL_TRIANGLES, 0, _model.getVertexCount() )
        GL.glDisableVertexAttribArray( 0 );
        GL.glBindVertexArray( 0 )
        self.stop()


    def render_textured_model(self, _texModel):

        model = _texModel.getRawModel()

        GL.glClear( GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT )
        self.start()
        GL.glBindVertexArray( model.getVaoID() )
        GL.glEnableVertexAttribArray( 0 );
        GL.glEnableVertexAttribArray( 1 );
        GL.glDrawElements( GL.GL_TRIANGLES,
                           model.getVertexCount(),
                           GL.GL_UNSIGNED_INT,
                           ct.c_void_p(0) ) #ct.c_void_p(0)
        #GL.glDrawArrays( GL.GL_TRIANGLES, 0, _model.getVertexCount() )
        GL.glDisableVertexAttribArray( 0 );
        GL.glDisableVertexAttribArray( 1 );
        GL.glBindVertexArray( 0 )
        self.stop()


    def start(self):
        GL.glUseProgram( self.shaderProgram )


    def stop(self):
        GL.glUseProgram( 0 )





''' END '''

