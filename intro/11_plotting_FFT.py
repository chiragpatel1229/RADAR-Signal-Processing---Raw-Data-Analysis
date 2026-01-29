
# %reset -f

# plotting

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi, 1000, endpoint=True)   # time vector
f0 = 3.0 # Frequency in Hz
A = 10.0 # Amplitude in Unit
s = A * np.sin(2*np.pi*f0*t) # sinusoidal signal

#ts=t[1]-t[0]
ts=(t[-1]-t[0])/(len(t)-1)    #  time sample steps 
Fs=1/ts

plt.figure()
plt.plot(t,s)
plt.xlabel('Time ($s$)')
plt.ylabel('Amplitude ($Unit$)')

plt.grid('on')      # or 'true'

# plt.grid('off')     # or 'false'


# plt.show()

plt.close(fig=1)

# plt.close('all')








dt = t[1]-t[0] # dt -> temporal resolution ~ sample rate

# fourier transform of s (sinusoidal signal)

f = np.fft.fftfreq(t.size, dt) # frequency axis

Y = np.fft.fft(s)   # FFT
# Y = np.fft.fft(s)*dt   # FFT


plt.figure()
plt.plot(f)
plt.ylabel('f / Hz')

plt.figure()
plt.plot(np.fft.fftshift(f))
plt.ylabel('f / Hz')

plt.figure()
plt.plot(f,Y)  #  Y is complex > Warning
                # eigther plotting magnitude or real/imag

plt.figure()
plt.plot(f,abs(Y))    # line at y=0 !?!? forgot fftshift!


# fft shift
plt.figure()
plt.plot(np.fft.fftshift(f), np.fft.fftshift(np.abs(Y)))
plt.xlabel('f / Hz')
plt.ylabel('|Y|')

plt.figure()
plt.stem(np.fft.fftshift(f), 10*np.log10(np.fft.fftshift(np.abs(Y))), linefmt='grey', use_line_collection=True)
plt.xlabel('f / Hz')
plt.ylabel('10*log10(|Y|)')


plt.figure()
plt.stem(np.fft.fftshift(f),np.fft.fftshift(np.abs(Y)), linefmt='grey', use_line_collection=True)
plt.yscale('log')
plt.xlabel('f / Hz')
plt.ylabel('|Y|')

           

plt.close('all')







