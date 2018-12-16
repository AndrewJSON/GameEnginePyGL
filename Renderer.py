
''' 
 * Renderer.py
 *
 *   Created on:         15.12.2018
 *   Author:             Andrew Jason Bishop
 * 
 * General description:
 *   xxx
'''

import OpenGL.GL  as GL

class Renderer:

    def prepare(self):

        GL.glClearColor(0.231, 0.231, 0.243, 1.0)
        GL.glEnable(GL.GL_DEPTH_TEST)
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)


    def render(self, _model):

        GL.glBindVertexArray( _model.getVaoID() )
        GL.glEnableVertexAttribArray( 0 );
        #GL.glDrawElements( GL.GL_TRIANGLES,
        #                   model.getVertexCount(),
        #                   GL.GL_UNSIGNED_INT,
        #                   0 )
        GL.glDrawArrays( GL.GL_TRIANGLES, 0, _model.getVertexCount() )
        GL.glDisableVertexAttribArray( 0 );
        GL.glBindVertexArray( 0 )

''' END '''

