
''' 
 * ShaderFactory.py
 *
 *   Created on:         15.12.2018
 *   Author:             Andrew Jason Bishop
 * 
 * General description:
 *   xxx
'''

import OpenGL.GL         as GL
import OpenGL.GL.shaders as sh

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



class ShaderProgram:

    def __init__(self, _progID):
        self.progID = _progID
        

    def get_uniformLocation(self, _uniformName):
        return GL.glGetUniformLocation(self.progID, _uniformName)


    def loadFloat(self, _location, _value):
        GL.glUniform1f( _location, _value )


    def loadVector(self, _location, _vector):
        GL.glUniform3f( _location, _vector )


    def loadMatrix(self, _location, _matrix):
        GL.glUniformMatrix4( _location, false, _matrix )


''' END '''

