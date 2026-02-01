# %reset -f

# session 2020/04/24 - content 1) - 3)
# homework for next week in the end of this script

import numpy as np
import matplotlib.pyplot as plt




#  create a sinusoidal signal in time domain, f= 5Hz, amplitude= 150
#  create an equivalent cosine signal
#
#  perform FFT and plot time as well as frequency domain




npts=1000
t = np.linspace(0, 2*np.pi, npts, endpoint=True)   # time vector
f0 = 5.0 # Frequency in Hz
A = 150.0 # Amplitude in Unit
y1 = A * np.sin(2*np.pi*f0*t) # sinusoidal signal
y2 = A * np.cos(2*np.pi*f0*t) # sinusoidal signal


#ts=t[1]-t[0]
#ts=(t[-1]-t[0])/(len(t)-1)    #  time sample steps 
#Fs=1/ts

plt.figure()
plt.plot(t,y1)
plt.plot(t,y2)

plt.xlabel('Time ($s$)')
plt.ylabel('Amplitude ($Unit$)')
plt.grid('on')


dt = t[1]-t[0] # dt -> temporal resolution ~ sample rate

f = np.fft.fftfreq(t.size, dt) # frequency axis
Y1 = np.fft.fft(y1)   # FFT
Y2 = np.fft.fft(y2)   # FFT

f=np.fft.fftshift(f)
Y1= np.fft.fftshift(Y1)
Y2=  np.fft.fftshift(Y2) 



plt.figure()
plt.plot(f,abs(Y1))
plt.plot(f,abs(Y2))
plt.xlabel('f ($Hz$)')
plt.ylabel('abs(Y1,Y2)')






plt.figure()
plt.plot(f,10*np.log10(abs(Y1)))
plt.plot(f,10*np.log10(abs(Y2)))
plt.xlabel('f ($Hz$)')
plt.ylabel('10*log10(abs(Y1,Y2))')





plt.figure()
plt.subplot(2,2,1)
plt.plot(f,np.real(Y1))
plt.xlabel('f ($Hz$)')
plt.ylabel('real(Y1)')
plt.grid('on')
plt.subplot(2,2,2)
plt.plot(f,np.imag(Y1))
plt.xlabel('f ($Hz$)')
plt.ylabel('imag(Y1)')
plt.grid('on')
plt.subplot(2,2,3)
plt.plot(f,np.real(Y2))
plt.xlabel('f ($Hz$)')
plt.ylabel('real(Y2)')
plt.grid('on')
plt.subplot(2,2,4)
plt.plot(f,np.imag(Y2))
plt.xlabel('f ($Hz$)')
plt.ylabel('imag(Y2)')
plt.grid('on')





# create another sinusoidal function of different frequency (18?Hz)
# superimpose both sinussoidals and perform FFT & plotting

f0 = 18.5 # Frequency in Hz
A = 70.0 # Amplitude in Unit
y3 = A * np.sin(2*np.pi*f0*t)

plt.figure()
plt.plot(y3)

y13=y1+y3

plt.figure()
plt.subplot(2,1,1)
plt.plot(t,y13)

Y13 = np.fft.fft(y13)   # FFT
Y13= np.fft.fftshift(Y13)

plt.subplot(2,1,2)
plt.plot(f,abs(Y13))
#plt.plot(f,10*np.log10(abs(Y13)))






# add noise to the time signal - sin
# perform FFT & plot
# vary (increase) the noise and watch the changes!


noise=np.random.randn(npts)
noise_ratio=1
#plt.plot(noise)

# noise power 
pnoise=np.median(abs(noise))*np.sqrt(2)

# signal power 
psig=np.median(abs(y13))*np.sqrt(2)


noise_mult=psig/noise_ratio


y13n=y13+noise*noise_mult

plt.figure()
plt.subplot(2,1,1)
plt.plot(y13n)
plt.xlabel('time ($s$)')
plt.ylabel('amplitude y13n')

Y13n = np.fft.fft(y13n)   # FFT
Y13n= np.fft.fftshift(Y13n)

plt.subplot(2,1,2)
plt.plot(f,abs(Y13n))
plt.xlabel('f ($Hz$)')
plt.ylabel('abs(Y13n)')







