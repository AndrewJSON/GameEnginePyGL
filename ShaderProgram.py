
''' 
 * ShaderProgram.py
 *
 *   Created on:         27.12.2018
 *   Author:             Andrew Jason Bishop
 * 
 * General description:
 *   xxx
'''


class ShaderProgram:

    def __init__(self, _progID, _shaderIDs):

        self.programID = _progID
        self.shaderIDs = _shaderIDs


    def start(self):
        GL.glUseProgram( self.programID )


    def stop(self):
        GL.glUseProgram( 0 )


    def get_uniformLocation(self, _uniformName):
        return GL.glGetUniformLocation(self.progID, _uniformName)


    def loadFloat(self, _location, _value):
        GL.glUniform1f( _location, _value )


    def loadVector(self, _location, _vector):
        GL.glUniform3f( _location, _vector )


    def loadMatrix(self, _location, _matrix):
        GL.glUniformMatrix4( _location, false, _matrix )


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

