# %reset -f

import numpy as np
import matplotlib.pyplot as plt

npts=2000

t = np.linspace(0, 2*np.pi, npts, endpoint=True)   # time vector
f0 = 22.5 # Frequency in Hz
A = 100.0 # Amplitude in Unit

rea=2000
A=A/rea
y=np.zeros(npts)

# simulate a normal distribution in spectral domain - like before in #13
# sin with large jitter (variability) + noise

for rr in range(0,rea):
    # rr=0
    yn= A * np.sin(2*np.pi*(f0+np.random.randn(1)*2)*t) # + np.random.randn(npts)*A # signal + noise
    y= y + np.roll(yn, int(npts*np.random.rand(1)) )



plt.figure()
plt.plot(t,y)


# phase shift between the receivers / antennas for one given source direction
phi=35/180*np.pi


# generate shifted time series
y1=y*np.exp(1j*-1*phi) + np.random.randn(npts)*A # signal with phase shift + noise
y2=y + np.random.randn(npts)*A # signal without phase shift + noise
y3=y*np.exp(1j*phi) + np.random.randn(npts)*A # signal with phase shift + noise


# remove DC from the time series
# y1=y1-np.mean(y1)
# y2=y2-np.mean(y2)
# y3=y3-np.mean(y3)



def make_fft_DS(x,t):
    #ts=t[1]-t[0]
    ts=(t[-1]-t[0])/(len(t)-1)    #  time sample steps 
    Fs=1/ts

    L = len(x)                    # length of signal 
    
    spectr = np.fft.fft(x)/L; 
    spectr= np.fft.fftshift(spectr)
    dF = Fs/L; 
    
    if  L%2==0:
        f=np.arange(-1*(Fs/2), Fs/2, dF)
        # f=f[0:-1];
    else:
        f=np.arange( -1*(Fs/2 -dF/2), (Fs/2 -dF/2),dF)

    return f, spectr


f,Y1= make_fft_DS(y1,t)
f,Y2= make_fft_DS(y2,t)
f,Y3= make_fft_DS(y3,t)



plt.figure()
plt.plot(f,abs(Y1),f,abs(Y2),f,abs(Y3)) # same magnitude for all signals! 
plt.xlabel('f / Hz')
plt.ylabel('amplitude')



# phases between them ?!?

plt.figure()
plt.subplot(2,2,1)
plt.plot(f,abs(Y2*np.conj(Y1)),f,abs(Y2*np.conj(Y3)),f,abs(Y1*np.conj(Y3)))
plt.title('abs(Y2-Y1), abs(Y2-Y3), abs(Y1-Y3)')
plt.legend(('Y2-Y1','Y2-Y3','Y1-Y3'))
plt.subplot(2,2,2)
plt.plot(f,np.angle(Y2*np.conj(Y1))/np.pi*180,'.')
plt.title('phase(Y2-Y1)')
plt.subplot(2,2,3)
plt.plot(f,np.angle(Y2*np.conj(Y3))/np.pi*180,'.')
plt.title('phase(Y2-Y3)')
plt.subplot(2,2,4)
plt.plot(f,np.angle(Y1*np.conj(Y3))/np.pi*180,'.')
plt.title('phase(Y1-Y3)')




