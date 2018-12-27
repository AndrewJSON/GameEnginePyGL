
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

