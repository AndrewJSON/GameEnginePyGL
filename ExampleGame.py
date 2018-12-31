
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
import pprint            as pp

#from   enum              import Enum

import GameHandler       as gh
import ModelFactory      as mf
import Renderer          as rn
import ShaderFactory     as sf
import Entity            as ent
import MatrixFactory     as tmf


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

translation = np.array([0.3,-0.4,0.2])
tx = translation[0]; ty = translation[1]; tz = translation[2];
scale       = np.array([0.8,0.4,1.0])
rotation    = np.array([30.0,0.0,0.0])
dRot        = np.array([0.0,0.0,0.3])

myM1        = np.matrix([[1.0, 0.0, 0.0, 0.4],
                         [0.0, 1.0, 0.0, 0.4],
                         [0.0, 0.0, 1.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0]])

myM2        = np.matrix([[1.0, 0.0, 0.0, 0.0],
                         [0.0, 1.0, 0.0, 0.0],
                         [0.0, 0.0, 1.0, 0.0],
                         [ tx,  ty,  tz, 1.0]])

myM = myM2

if __name__ == '__main__':

    #float_formatter = lambda x: "%+.3f" % x
    #np.set_printoptions(formatter={'float_kind':float_formatter})

    myGameHandler   = gh.GameHandler( (512, 512) )

    myShaderFactory = sf.ShaderFactory()
    myShaderProgram = myShaderFactory.compile_shaderProgram()
    myRenderer      = rn.Renderer( myShaderProgram )
    myMatrixFactory = tmf.MatrixFactory(4)


    myModelFactory  = mf.ModelFactory( myShaderProgram )
    #myModel         = myModelFactory.make_model_from_verts_and_indices( 
                                     #vertices,
                                     #indices )

    myTModel        = myModelFactory.make_textured_model( 
                                     vertices,
                                     indices,
                                     texCoords, 
                                    "01-SciFi-tiles.png" )
    myTlM           = myMatrixFactory.createTranslationMatrix( translation )
    pp.pprint( myTlM )
    myScM           = myMatrixFactory.createScaleMatrix( scale )
    pp.pprint( myScM )
    myRtM           = myMatrixFactory.createExtrinsicRotationMatrix( rotation )
    pp.pprint( myRtM )

    myEntity        = ent.Entity( myTModel, myMatrixFactory )
    pp.pprint( myM )
    myEntity.transformationMatrix = myTlM

    myRenderer.prepare()
    while not myGameHandler.isQuitRequested():     

        myShaderProgram.start()
        #myRenderer.render_textured_model( myTModel )
        #myEntity.increaseRotation( dRot )
        myRenderer.render_entity( myEntity, myShaderProgram )
        myShaderProgram.stop()
        myGameHandler.update_display_dly_ms( 20 )

        myGameHandler.eval_events()

    myShaderProgram.cleanUp()
    #myModelFactory.cleanUp()
    pg.quit()


''' END '''

