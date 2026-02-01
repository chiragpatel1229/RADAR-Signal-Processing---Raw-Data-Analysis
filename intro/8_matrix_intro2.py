

# %reset -f

import numpy as np
import matplotlib.pyplot as plt

#  y = 2x -3
# 2y = -1/2x +5

# -> y-2x = -3
#   2y +1/2x = 5

A = np.array([[-2,1],[0.5,2]])
b = np.array([[-3],[5]])

# -> xy= inv(A) * b

# does exist an inverse of the matrix ? -> determinant ~= 0  , else  Gauss-Elimination
# A(1,1) * A(2,2) - A(1,2) * A(2,1)

det=A[0,0] * A[1,1] - A[0,1] * A[1,0]
np.linalg.det(A)

xy=np.dot(np.linalg.inv(A),b)

# or

A = np.matrix([[-2,1],[0.5,2]])
b = np.matrix([[-3],[5]])

xy=A.I*b



A2=np.repeat(A,2,axis=0)
A2=np.repeat(A,[1,2],axis=0)

A2=np.tile(A,2)

A2=np.tile(A,(5,1))

A2[2:,:]




# 6x -z +2y  = 48
# 5y -3x +3z = 49
# 3z -2x +y  = 24

A=np.matrix([[6,2,-1],[-3,5,3],[-2,1,3]])
b=np.matrix([[48],[49],[24]])

xyz=A.I*b



A2=np.tile(A,(5,1))     # adding (redundant) information - more equations than necessary
b2=np.tile(b,(5,1))     # of course those are not independent, but just demo...
A2.I*b2


# now generating "independent" equations, noisy estimates...

#np.size(A,0)
matsize=[np.size(A,0),np.size(A,1)]

# matsize=np.shape(A)

rep=10

noise=np.reshape(1/20*np.random.randn(np.size(A)*rep),(matsize[0]*rep,matsize[1]))

# genrate a noise A2 out of A
A2=np.tile(A,(rep,1)) + noise

# exact replication of b
b2=np.tile(b,(rep,1))

xyz=A2.I*b2

# add the "true, noiseless" equation
A3=np.concatenate((A,A2))
b3=np.concatenate((b,b2))

# solution for xyz should become closer to the real
xyz2=A3.I*b3



