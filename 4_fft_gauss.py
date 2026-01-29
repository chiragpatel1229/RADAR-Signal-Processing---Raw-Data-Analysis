# %reset -f

import numpy as np
import matplotlib.pyplot as plt


npts=1000

t = np.linspace(-2*np.pi, 2*np.pi, npts, endpoint=True) 

#  gaussian distribution function

# x=np.linspace(-5,5,npts) # -5:5
x=t
mu= 1 # -4:4 
sigma2=.01 #  0.01:5
sigma=np.sqrt(sigma2)

y1=1/(2*np.pi*sigma)*np.exp( -(x-mu)**2 / (2*sigma2) )

plt.figure()
plt.plot(x,y1)
plt.grid('on')

# y1=y1 + np.random.randn(npts)/10

#ts=t[1]-t[0]
ts=(t[-1]-t[0])/(len(t)-1)    #  time sample steps 
Fs=1/ts

dt = t[1]-t[0] # dt -> temporal resolution ~ sample rate

f = np.fft.fftfreq(t.size, dt) # frequency axis
Y1 = np.fft.fft(y1)   # FFT

f=np.fft.fftshift(f)
Y1= np.fft.fftshift(Y1)


plt.figure()
plt.subplot(1,3,1)
plt.plot(f,np.real(Y1))
plt.xlabel('f ($Hz$)')
plt.ylabel('real(Y1)')
plt.subplot(1,3,2)
plt.plot(f,np.imag(Y1))
plt.xlabel('f ($Hz$)')
plt.ylabel('imag(Y1)')
plt.subplot(1,3,3)
plt.plot(f,np.abs(Y1))
plt.xlabel('f ($Hz$)')
plt.ylabel('abs(Y1)')


# vary the width of the gaussian distribution (in time), obs. spectrum

plt.figure()
plt.subplot(1,2,1)
plt.plot(t,y1)
plt.xlabel('t ($s$)')
# plt.ylabel('real(Y1,Y2)')
plt.subplot(1,2,2)
plt.plot(f,np.abs(Y1))
plt.xlabel('f ($Hz$)')
plt.ylabel('abs(Y1)')


