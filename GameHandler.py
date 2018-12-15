
''' 
 * Gamehandler.py
 *
 *   Created on:         15.12.2018
 *   Author:             Andrew Jason Bishop
 * 
 * General description:
 *   initiates and manages a program based on Pygame 
'''

import pygame    as pg
import OpenGL.GL as GL

class GameHandler:

    def __init__(self, _screenSize):
        pass
        #pg.init()



    def startUp(self, _screenSize):

        self.screen = pg.display.set_mode( _screenSize, pg.OPENGL|pg.DOUBLEBUF)
        #self.clock  = pg.time.Clock()

        GL.glClearColor(0.231, 0.231, 0.243, 1.0)
        GL.glEnable(GL.GL_DEPTH_TEST)


    def eval_events(self):

        for event in pg.event.get():
            self.eval_event( event )


    def eval_event(self, _event):

        if pg.QUIT == _event.type:
            self.quit_game()

        if pg.KEYUP == _event.type and pg.K_ESCAPE == _event.key:
            self.quit_game()


    def quit_game(self):
        pg.quit()


    def update_display_dly_ms(self, _dly):
        pg.display.flip()
        pg.time.wait(_dly)


''' END '''

