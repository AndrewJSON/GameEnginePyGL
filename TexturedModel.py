
''' 
 * RawModel.py
 *
 *   Created on:         21.12.2018
 *   Author:             Andrew Jason Bishop
 * 
 * General description:
 *   xxx
'''

#import RawModel as rm

class TexturedModel():

    def __init__(self, _rawModel, _modelTexture):

        self.rawModel     = _rawModel
        self.modelTexture = _modelTexture


    def getRawModel(self):
        return self.rawModel

    def getModelTexture(self):
        return self.modelTexture

''' END '''

'''
class LiveCell(Cell):

    def __init__(self, _universe, _coord):

        Cell.__init__(self, _universe, _coord, CellType.LIVE)
        self.create_surrounding_DeadCells()
'''
