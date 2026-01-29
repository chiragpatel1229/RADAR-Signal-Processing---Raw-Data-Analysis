
# %reset -f

# importing math library
import math     # no additional short handle specified ! library functions must be called by full library name  math.sin()


x=3.1415    # approx. PI

print(math.sin(x)) # 9.265e-05
print(math.sin(math.pi))

print(math.degrees(1.4))

print(math.degrees(math.pi/2))


import numpy

print(numpy.sin(numpy.pi))

# importing library and specifying a short handle to call the embedded functions

import numpy as np
print(np.sin(np.pi))

print(np.pi)

# formatting strings

print('{:.100f}'.format(np.pi))
print('{:.50f}'.format(np.pi))
print('{:.5e}'.format(np.pi))
print('{:.5%}'.format(np.pi))




import random

y = [random.random()*100.0 for i in range(10)]

print("Print y")
print(y)


print("random numbers - unsorted List")
for i in range(len(y)):
     print("%.2f" % y[i])


# defining an own "function" avg 
      
def avg(x):
     return sum(x) / len(x)


# calling the function with list of values
avg([4,4,7,10])


print("Avg: " + str(avg(y)))
print("Max: " + str(max(y)))
print("Min: " + str(min(y)))
 
 
z = sum(1 if i<50.0 else 0 for i in y)
print("amount of numbers below 50: " + str(z))

 
 # another way/method using NumPy
import numpy as np
 
 
print(np.mean(y))
print(np.average(y))
print(np.std(y))
print(np.median(y))




x=[1,4,6.7,10,20,15]

y=np.array([1,4,6.7,10,20,15])

np.mean(y)

t= np.linspace(0,1,6)

z=np.empty(6)   # empty still generates list that are NOT empty, but often needed to have variables predefined !
print(z)


