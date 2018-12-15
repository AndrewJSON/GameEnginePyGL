
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
        GL.glClearColor(1,0,0,1)


    def render(self, _model):

        GL.glBindVertexArray( _model.getVaoID() )
        GL.glEnableVertexAttribArray( 1 );
        GL.glDrawElements( GL.GL_TRIANGLES,
                           model.getVertexCount(),
                           GL.GL_UNSIGNED_INT,
                           0 )
        #GL.glDrawArrays( GL.GL_TRIANGLES, 0, model.getVertexCount() )
        GL.glDisableVertexAttribArray( 1 );
        GL.glBindVertexArray( 0 )

''' END '''

