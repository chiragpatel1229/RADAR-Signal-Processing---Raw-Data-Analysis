# %reset -f

import numpy as np
import matplotlib.pyplot as plt


npts=1000

#  rectangular function, rounded edges

a=1

#dc=0.1   # duty cycle
y1=a*np.ones(20)
y1[0]=0.2
y1[1]=0.5
y1[2]=0.85
y1[17]=0.85
y1[18]=0.5
y1[19]=0.2
y1=np.append(y1,np.zeros(80))

plt.figure()
plt.plot(y1)

y1=np.tile(y1,int(npts/len(y1)))
           
y1=y1-np.mean(y1)

t = np.linspace(0, 2*np.pi, npts, endpoint=True)   # time vector

plt.figure()
plt.plot(t,y1)
plt.xlabel('Time ($s$)')
plt.ylabel('Amplitude ($Unit$)')
plt.grid('on')




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
plt.ylabel('real(Y1,Y2)')
plt.subplot(1,3,2)
plt.plot(f,np.imag(Y1))
plt.xlabel('f ($Hz$)')
plt.ylabel('imag(Y1,Y2)')
plt.subplot(1,3,3)
plt.plot(f,np.abs(Y1))
plt.xlabel('f ($Hz$)')
plt.ylabel('abs(Y1,Y2)')



noise=np.random.randn(npts)*a/2

y1n=y1+noise

plt.figure()
plt.plot(t,y1n)


# FFT

dt = t[1]-t[0] # dt -> temporal resolution ~ sample rate

f = np.fft.fftfreq(t.size, dt) # frequency axis
Y1n = np.fft.fft(y1n)   # FFT

f=np.fft.fftshift(f)
Y1n= np.fft.fftshift(Y1n)


plt.figure()
plt.subplot(1,3,1)
plt.plot(f,np.real(Y1n))
plt.xlabel('f ($Hz$)')
plt.ylabel('real(Y1n)')
plt.subplot(1,3,2)
plt.plot(f,np.imag(Y1n))
plt.xlabel('f ($Hz$)')
plt.ylabel('imag(Y1n)')
plt.subplot(1,3,3)
plt.plot(f,np.abs(Y1n))
plt.xlabel('f ($Hz$)')
plt.ylabel('abs(Y1n)')


plt.figure()
plt.subplot(1,2,1)
plt.plot(np.real(Y1),np.imag(Y1),'.-')
plt.xlabel('real(Y1)')
plt.ylabel('imag(Y1)')
plt.subplot(1,2,2)
plt.plot(np.real(Y1n),np.imag(Y1n),'.-')
plt.xlabel('real(Y1n)')
plt.ylabel('imag(Y1n)')


