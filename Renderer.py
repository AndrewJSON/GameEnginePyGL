
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
import OpenGL.GL.shaders as sh
import ctypes            as ct


class Renderer:

    def __init__(self, _shaderProg):
        self.shaderProgram = _shaderProg


    def prepare(self):

        GL.glClearColor( 0.231, 0.231, 0.243, 1.0 )
        GL.glEnable( GL.GL_DEPTH_TEST )
        GL.glClear( GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT )
        GL.glUseProgram( self.shaderProgram )


    def render(self, _model):

        GL.glBindVertexArray( _model.getVaoID() )
        GL.glEnableVertexAttribArray( 0 );
        GL.glDrawElements( GL.GL_TRIANGLES,
                           _model.getVertexCount(),
                           GL.GL_UNSIGNED_INT,
                           ct.c_void_p(0) ) #ct.c_void_p(0)
        #GL.glDrawArrays( GL.GL_TRIANGLES, 0, _model.getVertexCount() )
        GL.glDisableVertexAttribArray( 0 );
        GL.glBindVertexArray( 0 )


class ShaderFactory:

    def __init__(self):

        self.vertexShaderSrc   = ""
        self.fragmentShaderSrc = ""


    def read_shaderPrograms(self):

        with open('vertexShader.glslv', 'r') as inFile:
            self.vertexShaderSrc = inFile.read()

        with open('fragmentShader.glslf', 'r') as inFile:
            self.fragmentShaderSrc = inFile.read()


    def compile_shaderProgram(self):

        self.read_shaderPrograms()
        shaderProg = sh.compileProgram(
            sh.compileShader(self.vertexShaderSrc, GL.GL_VERTEX_SHADER),
            sh.compileShader(self.fragmentShaderSrc, GL.GL_FRAGMENT_SHADER)
            )

        return shaderProg


''' END '''

