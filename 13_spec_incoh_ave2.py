# %reset -f

# simulate a normal distribution in spectral domain
# sin with large jitter (variability) + noise

import numpy as np
import matplotlib.pyplot as plt


npts=5000

t = np.linspace(0, 2*np.pi, npts, endpoint=True)   # time vector
f0 = 11.5 # Frequency in Hz
A = 100.0 # Amplitude in Unit

rea=500
A=A/rea
y=np.zeros(npts)


# realize a gaussian-like distribution in frequency domain but a sum suitable of sin. functions

for rr in range(0,rea):
    # rr=0
    yn= A * np.sin(2*np.pi*(f0+np.random.randn(1)*1)*t) + np.random.randn(npts)*A # signal + noise
    y= y + np.roll(yn, int(npts*np.random.rand(1)) )



plt.figure()
plt.plot(t,y)


def make_fft(t,y):
    dt = t[1]-t[0] # dt -> temporal resolution ~ sample rate
    f = np.fft.fftfreq(t.size, dt) # frequency axis
    Y = np.fft.fft(y)   # FFT
    f=np.fft.fftshift(f)
    Y= np.fft.fftshift(Y)
    return f,Y

f,spectr=make_fft(t,y)





plt.figure()
plt.plot(f,abs(spectr))
plt.xlabel('f / Hz')
plt.ylabel('amplitude')






def make_icoh(t, y, icoh):

    nptsn=int(np.floor(len(y)/icoh))
    Yi=np.empty(nptsn)
    tn=np.empty(nptsn)
    speci=np.zeros([nptsn,icoh])+1j*np.zeros([nptsn,icoh])

    for i in range(0,icoh):
        # i=0
        yn=y[i*nptsn:i*nptsn+nptsn]
        tn=t[i*nptsn:(i+1)*nptsn]
        
        #plt.plot(tn,yn)
        
        fi,Yi=make_fft(tn,yn)
        
        speci[:,i]=Yi
        
    # spectri=np.mean(abs(speci), axis=1)
    spectri=np.mean(abs(speci), axis=1)*np.sqrt(icoh)
    # spectri=np.mean(abs(speci), axis=1)*icoh
    # spectri=np.mean(speci, axis=1)
        
    if len(fi)>len(spectri):
        fi=fi[:-1]
        
    return fi,spectri




icoh=8;



fi,spectri=make_icoh(t,y,icoh)

plt.figure()
plt.plot(f,abs(spectr))
plt.plot(fi,abs(spectri),'*-')


# apply the 2nd way of performing spectral integrations - Low Pass Filter realization


icoh=4


def make_icoh2(t, y, icoh):
    # LPF version

    nptsn=int(np.floor(len(y)/icoh))
    Yi=np.empty(nptsn)
    tn=np.empty(nptsn)
    speci=np.zeros([nptsn,icoh])+1j*np.zeros([nptsn,icoh])

    for i in range(0,icoh):
        # i=0
        yn=y[i:npts:icoh]
        tn=t[i:npts:icoh]
        
        #plt.plot(tn,yn)
        
        fi,Yi=make_fft(tn,yn)
        
        speci[:,i]=Yi
        
        
    spectri=np.mean(abs(speci), axis=1)*np.sqrt(icoh)
    #spectri=np.mean(abs(speci), axis=1)*icoh
    # spectri=np.mean(abs(speci), axis=1)
    #spectri=np.mean(speci, axis=1)
        
    if len(fi)>len(spectri):
        fi=fi[:-1]
        
    return fi,spectri


fi2,spectri2=make_icoh2(t,y,icoh)

plt.figure()
plt.plot(f,abs(spectr))
plt.plot(fi2,abs(spectri2),'*-')
