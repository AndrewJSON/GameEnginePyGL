
''' 
 * Transformation.py
 *
 *   Created on:         28.12.2018
 *   Author:             Andrew Jason Bishop
 * 
 * General description:
 *   xxx
'''

import numpy as np


class Transformation:

    def __init__(self, _dimension):
        self.identityMatrix  = self.createIdentityMatrix( _dimension )


    def createIdentityMatrix(self, _dimension):

        identity = np.identity( _dimension, dtype=float )
        return np.matrix( identity, copy=False )


    def createTransforMatrix(self, _translation, _rotation, _scale):

        pass


    def createTranslationMatrix(self, _translation):

        translationMatrix = np.matrix( self.identityMatrix )
        self.addTranslationToGivenMatrix( _translation, translationMatrix )

        return translationMatrix


    def addTranslationToGivenMatrix(self, _translation, _matrix):

        rowElementCount = _translation.shape[0]
        asColumnVector = _translation.reshape(( rowElementCount ,1))
        _matrix[ :rowElementCount, -1] = asColumnVector


    def createTranslationMatrix(self, _translation):

        translationMatrix = np.matrix( self.identityMatrix )
        self.addTranslationToGivenMatrix( _translation, translationMatrix )

        return translationMatrix


    def addTranslationToGivenMatrix(self, _translation, _matrix):

        rowElementCount = _translation.shape[0]
        asColumnVector = _translation.reshape(( rowElementCount ,1))
        _matrix[ :rowElementCount, -1] = asColumnVector


    def rowVectorToColumnVector(self, _rowVector):

        rowElementCount = _rowVector.shape[0]
        asColumnVector = _rowVector.reshape((rowElementCount , 1))
        return asColumnVector


if __name__ == '__main__':

    myT = Transformation(4)
    #print(myT.identityMatrix)

'''
    a = np.matrix('1 2; 3 4')
    b = np.identity(2, dtype=float)

    m1 = np.asmatrix(b)
    m2 = np.matrix( np.identity( 2, dtype=int ), copy=False )

#    print("identity and asmatrix():\n", m1, type(m1))
#    print("matrix(identity):\n", m2, type(m2))

#    m = np.matrix( np.identity( 4, dtype=float ), copy=False )
    m = myT.createIdentityMatrix()
    print("identity matrix:\n", m)
    t = np.array([0.2,0.2,0.2,1.0])
    print(len(t))
    print("translation vector:", t)
    #tt = t.reshape((t.shape[0], 1))
    #m[:, -1] = tt
    myT.addTranslationToGivenMatrix( t, m )
    print("updated to translation matrix:\n", m)
'''

''' END '''

