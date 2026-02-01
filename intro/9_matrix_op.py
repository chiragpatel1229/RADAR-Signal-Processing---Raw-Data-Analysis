

# reset -f

# matrix as a list of list , otherwise e.g. numpy needed

A = [[1, 4, 5, 12], 
    [-5, 8, 9, 0],
    [-6, 7, 11, 19]]

A

len(A)
len(A[0])

A[0][3]

# matrix operations without numpy/scipy... - iterative Aij + Bij  i=0:: , j=0::


B = [[12,7,3,2],
    [4 ,5,-6,1],
    [7 ,8,9,-9]]

result = [[0,0,0,0], [0,0,0,0], [0,0,0,0]]


# iterate through rows
for i in range(len(A)):
   # iterate through columns
   for j in range(len(A[0])):
       result[i][j] = A[i][j] + B[i][j]

for r in result:
   print(r)
   
# in short notation

result = [[0,0,0,0], [0,0,0,0], [0,0,0,0]]

result = [[A[i][j] + B[i][j]  for j in range(len(A[0]))] for i in range(len(A))]



# reset -f

# using numpy

import numpy as np
C = np.array([1, 2, 3, 4])              # array int
print(type(C))         

C = np.array([[6, 3, 5], [2, 14, 7]], dtype = complex)   # matrix complex numbers

C = np.array([[1.1,2.5,3.3,4.9],[-7,-8,9,9],[3,7,9,-3]])


# array of zeros

zeros_array = np.zeros((2,4))

# array of ones

ones_array = np.ones((2,4))                    # float
ones_array2 = np.ones((2,4), dtype=np.int32)   # int

# "sorted" vector 

D=np.arange(3,17,2)    # 3:2:15

# same example as in the beginning of the script
A = np.array([[1, 4, 5, 12], [-5, 8, 9, 0], [-6, 7, 11, 19]])
B = np.array([[12,7,3,2],[4 ,5,-6,1],[7 ,8,9,-9]])

A[1,1]

A[1]
A[1,:]
A[:,1]


C=A+B       # elementwise add.

C=A-B       # elementwise subtr.

C=A+B*-1



C=A*B       # elementwise mult.

C=B/A       # elementwise div.

# transpose matrix

print(A)

print(A.transpose())
print(A.T)

C= np.dot([2j, 3j], [2j, 3j])   # dot-product A*B


a = [[1, 0], [0, 1]]
b = [[4, 1], [2, 2]]
np.dot(a, b) 
 
 
 
C=np.dot(A, B.transpose())     # matrix multiplication
 
# complex valued data

D=np.array([[1+3j, 2+2j,-3+1j, 1+1j],[2-3j,3-1j,-2+3j,1+0j],[-2+3j,1+1j,4-0j,2+1j]])

print(D)

print(np.conj(D))   # conjugate the comlpex values (matrix)

print(D.conjugate())


# matrix inversion 

from numpy.linalg import inv

C=np.array([[2,3,5],[-1,3,2],[2,1,1]])

print(C)

print(inv(C))

D=np.dot(C,inv(C))

D=np.round(np.dot(C,inv(C)))

print(D)            # C * inv(C) => diag=1

# matrix diagonal

print(C.diagonal())

print(np.diagonal(C))

np.trace(D)



