
''' 
 * Entity.py
 *
 *   Created on:         27.12.2018
 *   Author:             Andrew Jason Bishop
 * 
 * General description:
 *   xxx
'''

import numpy             as np


class Entity:

    def __init__(self, _texModel, _matFac):

        self.texturedModel        = _texModel
        self.matrixFactory        = _matFac
        self.transformationMatrix = _matFac.createNewIdentityMatrix()

        self.position = np.array([0.0,0.0,0.0])
        self.scale    = np.array([1.0,1.0,1.0])
        self.rotation = np.array([0.0,0.0,0.0])

        #self.updateRotation()


    def getTransformationMatrix(self):
        return self.transformationMatrix


    def updateTransformation(self):
        pass


    def updateRotation(self):

        tm = self.matrixFactory.createExtrinsicRotationMatrix( self.rotation )
        self.transformationMatrix = tm


    def increasePosition(self, _deltaPos):
        self.position += _deltaPos


    def increaseRotation(self, _deltaRot):
        self.rotation += _deltaRot
        self.updateRotation()


''' END '''

