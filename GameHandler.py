
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

        self.screen = None
        self.isQuitRequest = False

        pg.init()
        self.set_up_display( _screenSize )


    def set_up_display(self, _screenSize):

        self.screen = pg.display.set_mode( _screenSize, pg.OPENGL|pg.DOUBLEBUF )
        pg.display.set_caption('OpenGL Example')
        self.set_up_OpenGL()


    def set_up_OpenGL(self):

        GL.glClearColor(0.231, 0.231, 0.243, 1.0)
        GL.glEnable(GL.GL_DEPTH_TEST)


    def update_display_dly_ms(self, _dly):

        pg.display.flip()
        print("flip")
        pg.time.wait(_dly)


    def eval_events(self):

        for event in pg.event.get():
            self.eval_event( event )

        return self.isQuitRequest


    def eval_event(self, _event):

        if pg.QUIT == _event.type:
            self.request_quit_game()

        if pg.KEYUP == _event.type and pg.K_ESCAPE == _event.key:
            self.request_quit_game()


    def request_quit_game(self):
        self.isQuitRequest = True


    def isQuitRequested(self):
        return self.isQuitRequest


''' END '''

