
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

    def __init__(self):

        self.programID = None
        self.shaderIDs = None

    def compile_shaderProgram(self):

        self.createProgramID()
        self.compileShaders()

        self.attachShaders()
        self.bindAttributes()
        self.linkAndValidateProgram()

        #return self.programID
        return self.createShaderProgram()


    def createProgramID(self):
        self.programID = GL.glCreateProgram()


    def compileShaders(self):

        vs = self.compileShader( 'vertexShader.glslv', GL.GL_VERTEX_SHADER )
        fs = self.compileShader( 'fragmentShader.glslf', GL.GL_FRAGMENT_SHADER )

        self.shaderIDs = [vs, fs]


    def compileShader(self, _fileName, _glShaderType):

        shaderSrc = self.read_shaderSource( _fileName )
        shaderID  = sh.compileShader( shaderSrc, _glShaderType)

        return shaderID


    def read_shaderSource(self, _fileName):

        with open(_fileName, 'r') as inFile:
            shaderSrc = inFile.read()

        return shaderSrc


    def attachShaders(self):

        for shaderID in self.shaderIDs:
            GL.glAttachShader( self.programID, shaderID )


    def linkAndValidateProgram(self):

        GL.glLinkProgram( self.programID )
        GL.glValidateProgram( self.programID )


    def bindAttributes(self):

        self.bindAttribute( 0, "vPosition" )


    def bindAttribute(self, _attribute, _variableName):
        GL.glBindAttribLocation( self.programID, _attribute, _variableName )


    def createShaderProgram(self):
        return sp.ShaderProgram( self.programID, self.shaderIDs )


''' END '''

