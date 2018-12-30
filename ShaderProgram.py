
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

        uniformNames = ["transforMatrix"]

        for uName in uniformNames:
            self.uLocations[ uName] = self.get_uniformLocation( uName )


    def start(self):
        GL.glUseProgram( self.programID )


    def stop(self):
        GL.glUseProgram( 0 )


    def loadTransformationMatrix(self, _tMatrix):
        self.loadMatrix( "transforMatrix", _tMatrix )


    def get_uniformLocation(self, _uName):
        return GL.glGetUniformLocation(self.programID, _uName)


    def loadFloat(self, _location, _value):
        GL.glUniform1f( _location, _value )


    def loadVector(self, _location, _vector):
        GL.glUniform3f( _location, _vector )


    def loadMatrix(self, _location, _matrix):

        locationIndex = self.uLocations[ "transforMatrix" ]
        GL.glUniformMatrix4( locationIndex, false, _matrix )


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

