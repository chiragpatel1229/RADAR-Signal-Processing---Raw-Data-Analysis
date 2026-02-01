

# %reset -f

import numpy as np

# plotting of data
import matplotlib.pyplot as plt

x = np.array([3,2])
y = np.array([5,1])

type(x)

x[0]

z = x + y
z2= x - y

plt.figure()
plt.plot(x[0],x[1],'x')
plt.plot(y[0],y[1],'x')
plt.plot(z[0],z[1],'x')
plt.plot(z2[0],z2[1],'x')
plt.xlim(-5, 10)
plt.ylim(-5, 10)
plt.grid(1)



x = np.asarray([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

x[2]

x[0,1]

x[:,1]

np.size(x)

np.ndim(x)


empty= np.empty((3,3))  # remember, empty is NOT empty :)

zeros = np.zeros((3,3))

ones = np.ones((3,3))


k=np.linspace(0, 1, 11)

np.linspace(0, 1, 10, endpoint = False)


identity = np.identity(5)

eye1 = np.eye(3)   # Identity

eye2 = np.eye(3, k= -1) + 2*np.eye(3) + np.eye(3, k= +1)


diag=np.diag([1,2,3,4])




x = np.asarray([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
y = np.zeros_like(x)



x = np.asarray([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
y = x
x[0, 0] = 9
id(x)
id(y)           # same id, connected!


x = np.asarray([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
y = x.view()
x[0, 0] = 9
id(x)
id(y)           # different id, but still connected


x = np.asarray([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
y=x[:]
x[0, 0] = 9
id(x)
id(y)           # different id, but still connected


x = np.asarray([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
y= x.copy()
x[0, 0] = 9
id(x)
id(y)           # different id, independent



x= np.arange(16)        # generate simple vector (iterations...)
x

x1=x.reshape(4, 4)      # reshape to 2-dim 4x4 


# %reset -f

import numpy as np
import matplotlib.pyplot as plt 

x = np.arange(36).reshape(6, 6)

A = x[0:3, 0:3]     # "copy" the content of x first 3x3
B = x[0:3, 3:]      # "copy" the content of x first 3 x last 3
C = x[3:, 0:3]
D = x[:3, 3:]       # = B


x.sum(axis=0)       # sum "vertical"
x.sum(axis=1)       # sum "horizontal"

np.sum(x,1)         # = x.sum(axis=1)


# NumPy array - n-dim ! -> componentwise multiplication
x = np.array( ((2,3), (3, 5)) )
y = np.array( ((1,2), (5, -1)) )
x * y

# NumPy matrix 2-dim ! -> matrix multiplication
x = np.matrix( ((2,3), (3, 5)) )
y = np.matrix( ((1,2), (5, -1)) )
x * y

# np.matmul(x,y)
# np.dot(x,y)

x = np.array( ((3,2,1), (1,0,1)))
y = np.array( ((1,2), (0,1), (4,0)))

np.matmul(x,y)
np.dot(x,y)
x @ y



x = np.array( ((3,2,1), (1,0,1)))
y = np.array( ((1,2), (0,1), (4,0)))

# rotieren, transponieren
y1=np.rot90(y)

y2=np.transpose(y)
y2=y.T


x*np.rot90(y)
x*y.T

