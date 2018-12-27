
''' 
 * ExampleGame.py
 *
 *   Created on:         15.12.2018
 *   Author:             Andrew Jason Bishop
 * 
 * General description:
 *   Demonstrate and understand the basic concepts of OpenGL in Python.
 *   Makes use of PyOpenGL and Pygame (built on top of SDL).
 *
 *   run with:
 *   MESA_GL_VERSION_OVERRIDE=4.3 python3 ExampleGame.py
 *   
'''

import pygame            as pg
import OpenGL.GL         as GL
import numpy             as np
import OpenGL.GL.shaders as sh

#from   enum              import Enum

import GameHandler       as gh
import ModelFactory      as mf
import Renderer          as rn
import ShaderFactory     as sf


#class Enum(tuple): __getattr__ = tuple.index

#VAO_IDs     = Enum(['ZERO', 'Triangles', 'NumOfVAOs'])
#Buffer_IDs  = Enum(['ZERO', 'ArrayBuffer', 'NumOfBuffers'])
#Attrib_IDs  = Enum(['vPosition'])


vertices = np.array([
            -0.6,  0.6,  0.0,    # v0
            -0.6, -0.6,  0.0,    # v1
             0.6, -0.6,  0.0,    # v2
             0.6,  0.6,  0.0     # v3
            ], dtype=np.float32)

indices = np.array([
            0,1,3,              # triangle 1
            3,1,2               # triangle 2
            ], dtype=np.int32)

texCoords = np.array([
            0.0, 0.0,
            0.0, 1.0,
            1.0, 1.0,
            1.0, 0.0
            ], dtype=np.float32)

if __name__ == '__main__':

    myGameHandler   = gh.GameHandler( (512, 512) )

    myShaderFactory = sf.ShaderFactory()
    shaderProgram   = myShaderFactory.compile_shaderProgram()
    myRenderer      = rn.Renderer( shaderProgram )

    myModelFactory  = mf.ModelFactory( shaderProgram )
    #myModel         = myModelFactory.make_model_from_verts_and_indices( 
                                     #vertices,
                                     #indices )

    myTModel        = myModelFactory.make_textured_model( 
                                     vertices,
                                     indices,
                                     texCoords, 
                                    "01-SciFi-tiles.png" )

    myRenderer.prepare()
    while not myGameHandler.isQuitRequested():     

        myRenderer.render_textured_model( myTModel )
        #myRenderer.render( myModel )
        myGameHandler.update_display_dly_ms( 20 )

        myGameHandler.eval_events()

    #myModelFactory.cleanUp()
    pg.quit()


''' END '''

