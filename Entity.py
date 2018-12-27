
''' 
 * Entity.py
 *
 *   Created on:         27.12.2018
 *   Author:             Andrew Jason Bishop
 * 
 * General description:
 *   xxx
'''

class Entity:

	def __init__(self, _texModel, _pos, _rot, _scale):

		self.texturedModel  = _texModel
        self.position       = _pos      # 3D vector / numpy array
		self.rotation       = _rot      # 3D vector / numpy array
        self.scale          = _scale    # scalar


    def getTexModel(self):
        return self.texturedModel


    def increasePosition(self, _deltaPos):
        self.position += _deltaPos


    def increaseRotation(self, _deltaRot):
        self.rotation += _deltaRot


''' END '''

