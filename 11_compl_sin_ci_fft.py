# %reset -f


import numpy as np
import matplotlib.pyplot as plt

# complex !


#  create a sinusoidal signal in time domain, f= 5Hz, amplitude= 150
#  create an equivalent cosine signal
#  perform FFT and plot time as well as frequency domain




npts=1000
t = np.linspace(0, 2*np.pi, npts, endpoint=True)   # time vector
f1 = 8.7 # Frequency in Hz
A = 15.0 # Amplitude in Unit
y1 = A * np.sin(2*np.pi*f1*t) # sinusoidal signal

# complex time signal  "I/Q"

y1c=y1-1j*A*np.cos(2*np.pi*f1*t)

y1cn=y1c+ A/2*np.random.randn(npts) + 1j*A/2*np.random.randn(npts)


plt.figure()
plt.subplot(211)
plt.plot(np.real(y1c),np.imag(y1c),'.')
plt.ylim(-50, 50)
plt.xlim(-50, 50)
plt.title('IQ diagram of complex sinusoidal function w/o noise')
plt.xlabel('Re')
plt.ylabel('Im')
plt.subplot(212)
plt.plot(np.real(y1cn),np.imag(y1cn),'.')
plt.ylim(-50, 50)
plt.xlim(-50, 50)
plt.title('IQ diagram of complex sinusoidal function with noise')
plt.xlabel('Re')
plt.ylabel('Im')




def make_fft(t,y):
    dt = t[1]-t[0] # dt -> temporal resolution ~ sample rate
    f = np.fft.fftfreq(t.size, dt) # frequency axis
    Y = np.fft.fft(y)   # FFT
    f=np.fft.fftshift(f)
    Y= np.fft.fftshift(Y)
    return f,Y


f,Y1c=make_fft(t,y1c)
f,Y1cn=make_fft(t,y1cn)


plt.figure()
plt.plot(f,np.abs(Y1c))
plt.plot(f,np.abs(Y1cn))
plt.xlabel('frequency /Hz')
plt.ylabel('amplitude')




# perform coherent integrations
def make_ci(t,y, ci):
    nptsn=int(np.floor(len(y)/ci))
    yn=np.empty(nptsn)+1j*np.empty(nptsn)
    tn=np.empty(nptsn)
    for i in range(0,nptsn):
        yn[i]=np.mean(y[i*ci:i*ci+ci-1])
        tn[i]=np.mean(t[i*ci:(i+1)*ci])
    return tn,yn


ci=2
tn,yn=make_ci(t,y1cn,ci)

plt.figure()
plt.plot(t,y1cn,tn,yn)
plt.legend(('noisy time series','after CI'))



plt.figure()
plt.subplot(211)
plt.plot(np.real(y1cn),np.imag(y1cn),'.')
plt.title('IQ diagram of noise time series')
plt.xlabel('Re')
plt.ylabel('Im')
plt.subplot(212)
plt.plot(np.real(yn),np.imag(yn),'.')
plt.title('IQ diagram after CI')
plt.xlabel('Re')
plt.ylabel('Im')



fn,Yn=make_fft(tn,yn)
 
plt.figure()
plt.subplot(221)
plt.plot(t,y1cn)
plt.title('noisy time series')
plt.xlabel('time')
plt.ylabel('amplitude')
plt.subplot(222)
plt.plot(f,abs(Y1cn))
plt.title('spectrum noisy time series')
plt.xlabel('frequency')
plt.ylabel('amplitude')
plt.subplot(223)
plt.plot(tn,yn)
plt.title('noisy time series after CI')
plt.xlabel('time')
plt.ylabel('amplitude')
plt.subplot(224)
plt.plot(fn,abs(Yn))
plt.title('spectrum after CI')
plt.xlabel('frequency')
plt.ylabel('amplitude')



