
# reset -f

# from numpy import *


import numpy as np

# assume measurement data
y=np.array([1,4,6.7,10,20,15])

# time vector of the measurements
t= np.linspace(0,1,6)

# plotting of data using matplotlib - equivalent to MATLAB plotting routines

import matplotlib.pyplot as plt

plt.plot(t,y,'ro')
#plt.show() # e.g. in plain Python or other GUIs needed

# NOTE: in Spyder you may set in Preferences whether figures are to be shown in separate windows or in the console...




x=np.linspace(0,6,100)

y=np.sin(x)
z=np.cos(x)


plt.figure()
# plt.plot(y)
plt.plot(x,y,'r--',linewidth=3)  # red dashed
plt.plot(x,z,'k:',linewidth=2)   # black dotted
plt.legend(['y','z'])
plt.xlabel('x')
plt.ylabel('y')

plt.xlim([0, 6])
plt.ylim([-1.5, 1.5])
#plt.show()


plt.savefig('fig01.png')
# plt.savefig('fig01.eps')


#import time
#
#time.clock()
#
#time.perf_counter()
#time.process_time()






x, y = np.mgrid[-10:10:0.1, -10:10:0.1]

plt.figure()
plt.imshow(np.sin(x*y))
plt.colorbar()





data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}

data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

plt.figure()
plt.scatter('a', 'b', c='c', s='d', data=data)

plt.xlabel('entry a')
plt.ylabel('entry b')

#plt.show()

