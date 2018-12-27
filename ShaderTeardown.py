
''' 
 * ShaderTeardown.py
 *
 *   Created on:         27.12.2018
 *   Author:             Andrew Jason Bishop
 * 
 * General description:
 *   xxx
'''

import OpenGL.GL         as GL

class ShaderTeardown:

    def teardown_shaderProgram(self, _shaderProgram):

        _shaderProgram.stop()

        programID = _shaderProgram.getProgramID
        shaderIDs = _shaderProgram.getShaderIDs

        for shaderID in shaderIDs:
            self.detachShader( programID, shaderID )
            self.deleteShader( shaderID )


    def detachShader(self, _progID, _shaderID):
        GL.glDetachShader( self.programID, _shaderID )


    def deleteShader(self, _shaderID):
        GL.glDeleteShader( _shaderID )


''' END '''

