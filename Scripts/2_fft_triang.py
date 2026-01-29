# %reset -f

import numpy as np
import matplotlib.pyplot as plt


npts=1000

#  triangular function

n=0
a=0.5
x=np.linspace(0,2*np.pi,int(npts/50),endpoint=True)

y1=a*x+n

plt.figure()
plt.plot(y1)


y1=np.append(y1,y1[::-1])
# y1=np.append(y1,np.flip(y1,0))

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
plt.ylabel('real(Y1)')
plt.subplot(1,3,2)
plt.plot(f,np.imag(Y1))
plt.xlabel('f ($Hz$)')
plt.ylabel('imag(Y1)')
plt.subplot(1,3,3)
plt.plot(f,np.abs(Y1))
plt.xlabel('f ($Hz$)')
plt.ylabel('abs(Y1)')







y2=np.roll(np.tile(y1[::2],2),3)/3

plt.figure()
plt.plot(t,y1,t,y2)


# FFT

dt = t[1]-t[0] # dt -> temporal resolution ~ sample rate

f = np.fft.fftfreq(t.size, dt) # frequency axis
Y2 = np.fft.fft(y2)   # FFT

f=np.fft.fftshift(f)
Y2= np.fft.fftshift(Y2)


plt.figure()
plt.subplot(1,3,1)
plt.plot(f,np.real(Y2))
plt.xlabel('f ($Hz$)')
plt.ylabel('real(Y2)')
plt.subplot(1,3,2)
plt.plot(f,np.imag(Y2))
plt.xlabel('f ($Hz$)')
plt.ylabel('imag(Y2)')
plt.subplot(1,3,3)
plt.plot(f,np.abs(Y2))
plt.xlabel('f ($Hz$)')
plt.ylabel('abs(Y2)')





noise=np.random.randn(npts)/1

y12=y1+y2# +noise

plt.figure()
plt.plot(t,y12)





# FFT

dt = t[1]-t[0] # dt -> temporal resolution ~ sample rate

f = np.fft.fftfreq(t.size, dt) # frequency axis
Y12 = np.fft.fft(y12)   # FFT

f=np.fft.fftshift(f)
Y12= np.fft.fftshift(Y12)


plt.figure()
plt.subplot(1,3,1)
plt.plot(f,np.real(Y12))
plt.xlabel('f ($Hz$)')
plt.ylabel('real(Y12)')
plt.subplot(1,3,2)
plt.plot(f,np.imag(Y12))
plt.xlabel('f ($Hz$)')
plt.ylabel('imag(Y12)')
plt.subplot(1,3,3)
plt.plot(f,np.abs(Y12))
plt.xlabel('f ($Hz$)')
plt.ylabel('abs(Y12)')


plt.figure()
plt.plot(np.real(Y12),np.imag(Y12),'.-')
plt.xlabel('real(Y12)')
plt.ylabel('imag(Y12)')


