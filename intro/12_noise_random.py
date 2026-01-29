

# %reset -f

# plotting

import numpy as np
import matplotlib.pyplot as plt




t1=np.random.rand(1000,1)     # random numbers 0...1, equally distributed

plt.figure()
plt.plot(t1,'.')
plt.grid('on')
plt.xlabel('samples')
plt.ylabel('random value')




t2=np.random.randn(1000,1)   # random number, normal distributed

#plt.figure()
plt.plot(t2,'+')
plt.xlabel('samples')
plt.ylabel('random value')


# how one may easily see the distribution properties of the variable?

# histogram
plt.figure()
plt.subplot(1,2,1)  
plt.hist(t1, bins='auto')  # arguments are passed to np.histogram
plt.title("Histogram with 'auto' bins")


plt.subplot(1,2,2)
plt.hist(t2, bins='auto')  # arguments are passed to np.histogram
plt.title("Histogram with 'auto' bins")

# plt.close('all')




plt.figure()
plt.subplot(1,2,1)
plt.hist(t2, bins='auto')   # automatic bins
plt.subplot(1,2,2)
plt.hist(t2, bins=100)      # manual bins

plt.hist(t2+1, bins=100)    # manual bins, values shifted




