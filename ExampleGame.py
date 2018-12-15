
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

#import GameHandler  as gh
import OpenGL.GL as GL
#import ModelFactory as mf
#import Renderer     as rn


vertices = [
            -0.6,  0.6,  0.0, 1.0,  # triangle 1
            -0.6, -0.6,  0.0, 1.0,
             0.6,  0.6,  0.0, 1.0,

             0.6,  0.6,  0.0, 1.0,    # triangle 2
            -0.6, -0.6,  0.0, 1.0,
             0.6, -0.6,  0.0, 1.0
           ]

vertices = np.array(vertices, dtype=np.float32)


def main():

    pg.init()
    screen = pg.display.set_mode((512, 512), pg.OPENGL|pg.DOUBLEBUF)
    GL.glClearColor(0.231, 0.231, 0.243, 1.0)
    GL.glEnable(GL.GL_DEPTH_TEST)
    
    while True:     
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYUP and event.key == pg.K_ESCAPE:
                return
        
        pg.display.flip()
        print("flip")
        pg.time.wait(20)



if __name__ == '__main__':


    #myModelFactory  = mf.ModelFactory()
    #myRenderer      = rn.Renderer()
    #myModel         = myModelFactory.make_model_from_verts( vertices )

    main()

    #myGameHandler.quit_game() # just in case of an unexpected break out


''' END '''

