
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
'''

import numpy        as np
import pygame       as pg

import GameHandler  as gh
import OpenGL.GL as GL
import ModelFactory as mf
import Renderer     as rn


vertices = [
            -0.6,  0.6,  0.0, 1.0,  # triangle 1
            -0.6, -0.6,  0.0, 1.0,
             0.6,  0.6,  0.0, 1.0,

             0.6,  0.6,  0.0, 1.0,    # triangle 2
            -0.6, -0.6,  0.0, 1.0,
             0.6, -0.6,  0.0, 1.0
           ]

vertices = np.array(vertices, dtype=np.float32)


if __name__ == '__main__':

    myGameHandler   = gh.GameHandler( (512, 512) )
    myModelFactory  = mf.ModelFactory()
    myRenderer      = rn.Renderer()
    myModel         = myModelFactory.make_model_from_verts( vertices )

    while not myGameHandler.isQuitRequested():     

        myRenderer.prepare()
        myRenderer.render( myModel )
        myGameHandler.update_display_dly_ms( 20 )

        myGameHandler.eval_events()

    #myModelFactory.cleanUp()
    pg.quit()


''' END '''
