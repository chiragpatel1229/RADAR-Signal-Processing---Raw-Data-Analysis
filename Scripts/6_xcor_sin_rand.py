# %reset -f

# correlation: similarity of two signals 
#
# R(tau) = integral [ x1(t) x2(t-tau) dt ]
#
# -> see similarity to convolution
#
# correlation output: 
# a) similarity b) temporal shift c) phase relation of both signals 
# d) characteristics of the signal (auto-correlation)




import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


# correlate sinusoidals + noise (AWGN)
# generate a "code" -> series of rand numbers and correlate them including added noise


npts=1000

t = np.linspace(0, 2*np.pi, npts, endpoint=True)   # time vector
f0 = 5.0 # Frequency in Hz
A = 150.0 # Amplitude in Unit
y1 = A * np.sin(2*np.pi*f0*t) # sinusoidal signal
# y2 = 1/2 * np.roll(y1,-76,0) # sinusoidal signal
y2 = 1/2 *A* np.sin(2*np.pi*f0*(t+0.05)) # sinusoidal signal


plt.figure()
plt.plot(t,y1,t,y2)
plt.xlabel('Time ($s$)')
plt.ylabel('Amplitude ($Unit$)')
plt.grid('on')

# cross-correlation

sy1y2=signal.correlate(y1,y2)

t2=-1*t[::-1]
t2=np.append(t2, t[1:])

plt.figure()
plt.plot(t2,sy1y2)

# time lag between both sinusoidals...

sy2y1=signal.correlate(y2,y1)


plt.figure()
plt.plot(t2,abs(sy1y2))
plt.plot(t2,abs(sy2y1))

# correlation y2-y1 is "mirrored/flipped" y1-y2 



noise1=np.random.randn(npts)*50
noise2=np.random.randn(npts)*50

y1n=y1+noise1
y2n=y2+noise2

plt.figure()
plt.plot(t,y1n,t,y2n)
plt.xlabel('Time ($s$)')
plt.ylabel('Amplitude ($Unit$)')
plt.grid('on')


sy1y2=signal.correlate(y1n,y2n)


plt.figure()
plt.plot(t2,abs(sy1y2))

# with increased noise intensity -> correlation peak (shift) is "lost/gone" 
# other parts (offsets) of the two time series show more similarity


# normalization by the number of overlapping elements 
# auto-correlation

yt=np.ones(npts)
sytyt=signal.correlate(yt,yt)

plt.figure()
plt.plot(t2,abs(sytyt))

plt.figure()
plt.plot(t2,abs(sy1y2/sytyt))

# no or high correlation always to see ?!? 
# -> sinusoidal function is always similar to another sinusoidal of same frequency
# only little phase shifts without much of noise can be seen by correlations






#  %reset -f


import numpy as np
from scipy import signal
import matplotlib.pyplot as plt



# sin appended noise, shifted


npts=100

t = np.linspace(0, 2*np.pi, npts, endpoint=True)   # time vector
f0 = 5.0 # Frequency in Hz
A = 50.0 # Amplitude in Unit
y1 = A * np.sin(2*np.pi*f0*t) # sinusoidal signal

noise=np.random.rand(npts)*A/1.5

y1=np.append(noise,y1)
y1=np.append(y1,np.random.rand(8*npts)*A/1.5)

y2 = np.random.rand(1)*np.roll(y1,-76,0) # sinusoidal signal

t = np.linspace(0, 2*np.pi, 10*npts, endpoint=True)   # time vector

plt.figure()
plt.plot(t,y1,t,y2)
plt.xlabel('Time ($s$)')
plt.ylabel('Amplitude ($Unit$)')
plt.grid('on')


t = np.linspace(0, 10*npts, 10*npts, endpoint=True)   # time vector

sy1y2=signal.correlate(y1,y2)
t2=-1*t[::-1]
t2=np.append(t2, t[1:])

plt.figure()
plt.plot(t2,sy1y2)


# normalization - autocorrelation of two ones vectors

yt=np.ones(len(y1))
sytyt=signal.correlate(yt,yt)

plt.figure()
plt.plot(t2,sytyt)

plt.figure()
plt.plot(t2,sy1y2/sytyt)

sy1y2max=np.amax(sy1y2)
sy1y2maxpos=np.argmax(sy1y2)

sy1y2maxpos2=np.where(sy1y2==np.amax(sy1y2))

t2[sy1y2maxpos]







