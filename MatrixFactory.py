
''' 
 * MatrixFactory.py
 *
 *   Created on:         30.12.2018
 *   Author:             Andrew Jason Bishop
 * 
 * General description:
 *   xxx
'''

import numpy as np
import pprint as pp


class MatrixFactory:

    def __init__(self, _dimension):
        self.identity = np.identity( _dimension, dtype=float )


    def createNewIdentityMatrix(self):
        return np.matrix( self.identity )


    def createTranslationMatrix(self, _translation):

        rowElementCount = _translation.shape[0]
        translatAsColumnVector = _translation.reshape(( rowElementCount ,1))

        newMatrix = self.createNewIdentityMatrix()
        # paste translat factors to rightmost matrix column from top row down:
        newMatrix[ :rowElementCount, -1] = translatAsColumnVector

        return newMatrix


    def createScaleMatrix(self, _scale):

        rowElementCount = _scale.shape[0]
        newMatrix = self.createNewIdentityMatrix()

        for i in range(0, rowElementCount):
            newMatrix[i,i] = _scale[i]

        return newMatrix


    def createExtrinsicRotationMatrix(self, _rotAngles):

        rotMatX = self.createRotMatrix_X( _rotAngles[0] )
        rotMatY = self.createRotMatrix_Y( _rotAngles[1] )
        rotMatZ = self.createRotMatrix_Z( _rotAngles[2] )
        rotMatrix = rotMatZ * rotMatY * rotMatX

        return rotMatrix


    def createRotMatrix_X(self, _rotAngle):

        newMatrix = self.createNewIdentityMatrix()
        s, c = self.getSinCos( _rotAngle )

        newMatrix[1,1], newMatrix[1,2] = c, -s
        newMatrix[2,1], newMatrix[2,2] = s, c

        return newMatrix


    def createRotMatrix_Y(self, _rotAngle):

        newMatrix = self.createNewIdentityMatrix()
        s, c = self.getSinCos( _rotAngle )

        newMatrix[0,0], newMatrix[0,2] = c, s
        newMatrix[2,0], newMatrix[2,2] = -s, c

        return newMatrix


    def createRotMatrix_Z(self, _rotAngle):

        newMatrix = self.createNewIdentityMatrix()
        s, c = self.getSinCos( _rotAngle )

        newMatrix[0,0], newMatrix[0,1] = c, -s
        newMatrix[1,0], newMatrix[1,1] = s, c

        return newMatrix


    def getSinCos(self, _rotAngle):

        theta = np.radians(_rotAngle)
        return np.sin(theta), np.cos(theta)


    def rowVectorToColumnVector(self, _rowVector):

        rowElementCount = _rowVector.shape[0]
        asColumnVector = _rowVector.reshape((rowElementCount , 1))
        return asColumnVector



if __name__ == '__main__':

    def verbose(_title, _array):
        print(_title)
        pp.pprint(_array)
        print("")

    print("")

    float_formatter = lambda x: "%+.3f" % x
    np.set_printoptions(formatter={'float_kind':float_formatter})
    #rM = myMF.createExtrinsicRotationMatrix( (0,90,0) )

    myMF = MatrixFactory(4)
    r2 = np.sqrt(2)
    v = np.array([0.,0.,r2,1.])
    a = np.array([45.,45.,45.])
    v = myMF.rowVectorToColumnVector( v )

    rMx = myMF.createRotMatrix_X(45.)
    rMy = myMF.createRotMatrix_Y(45.)
    rMz = myMF.createRotMatrix_Z(45.)

    verbose("column vertex:", v)
    rMx_v = rMx*v
    verbose("x rotated vertex:", rMx_v)
    rMxy_v = rMy*rMx_v
    verbose("xy rotated vertex:", rMxy_v)
    rMxyz_v = rMz*rMxy_v
    verbose("xyz rotated vertex:", rMxyz_v)

    rall = rMz*rMy*rMx*v
    verbose("combi matrix rotated vertex:", rall)

    #rMex = myMF.createExtrinsicRotationMatrix( (0.,0.,45.) )
    rMex = myMF.createExtrinsicRotationMatrix( a )
    verbose("extrinsic rotation matrix:", rMex)
    rMex_v = rMex*v
    verbose("extrinsic rotated vertex:", rMex_v)


''' END '''

