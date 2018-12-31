
''' 
 * ShaderProgram.py
 *
 *   Created on:         27.12.2018
 *   Author:             Andrew Jason Bishop
 * 
 * General description:
 *   xxx
'''

import OpenGL.GL            as GL


class ShaderProgram:

    def __init__(self, _progID, _shaderIDs):

        self.programID = _progID
        self.shaderIDs = _shaderIDs
        self.uLocations = {}

        self.updateUniformLocations()


    def updateUniformLocations(self):

        uniformVariableNames = ["transforMatrix", "uniScale"]

        for uVarName in uniformVariableNames:
            self.uLocations[ uVarName] = self.get_uniformLocation( uVarName )


    def get_uniformLocation(self, _uName):
        return GL.glGetUniformLocation(self.programID, _uName)


    def start(self):
        GL.glUseProgram( self.programID )


    def stop(self):
        GL.glUseProgram( 0 )


    def loadTransformationMatrix(self, _tMatrix):
        self.loadMatrix( "transforMatrix", _tMatrix )


    def loadMatrix(self, _uVarName, _matrix):

        locationIndex = self.uLocations[ _uVarName ]
        GL.glUniformMatrix4fv( locationIndex, 1, GL.GL_FALSE, _matrix )


    def loadFloat(self, _uVarName, _value):

        locationIndex = self.uLocations[ _uVarName ]
        GL.glUniform1f( locationIndex, _value )


    def loadVector(self, _uVarName, _vector):

        locationIndex = self.uLocations[ _uVarName ]
        GL.glUniform3f( locationIndex, _value )


    def cleanUp(self):

        self.stop()

        for shaderID in self.shaderIDs:
            self.detachShader( shaderID )
            self.deleteShader( shaderID )

        self.delete()


    def detachShader(self, _shaderID):
        GL.glDetachShader( self.programID, _shaderID )


    def deleteShader(self, _shaderID):
        GL.glDeleteShader( _shaderID )


    def delete(self):
        GL.glDeleteProgram( self.programID )


''' END '''

