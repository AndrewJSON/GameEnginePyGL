
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
import ShaderProgram     as sp

class ShaderFactory:

    def compile_shaderProgram(self):

        programID = GL.glCreateProgram()
        shaderIDs = self.compileShaders()

        self.attachShaders( programID, shaderIDs )
        self.linkAndValidateProgram( programID )

        return programID


    def compileShaders(self):

        vs = self.compileShader( 'vertexShader.glslv', GL.GL_VERTEX_SHADER )
        fs = self.compileShader( 'fragmentShader.glslf', GL.GL_FRAGMENT_SHADER )

        return [vs, fs]


    def compileShader(self, _fileName, _glShaderType):

        shaderSrc = self.read_shaderSource( _fileName )
        shaderID  = sh.compileShader( shaderSrc, _glShaderType)

        return shaderID


    def read_shaderSource(self, _fileName):

        with open(_fileName, 'r') as inFile:
            shaderSrc = inFile.read()

        return shaderSrc


    def attachShaders(self, _progID, _shaderIDs):

        for shaderID in _shaderIDs:
            GL.glAttachShader( _progID, shaderID )


    def linkAndValidateProgram(self, _progID):

        GL.glLinkProgram( _progID )
        GL.glValidateProgram( _progID )


    def make_shaderProgramInstance(self, _progID):
        return sp.ShaderProgram( _progID )


''' END '''

