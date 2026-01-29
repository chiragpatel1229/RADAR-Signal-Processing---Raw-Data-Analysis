# %reset -f

import numpy as np
import matplotlib.pyplot as plt

# perform non-coherent integrations on a spectra of a sinussoidal function 

npts=1000

t = np.linspace(0, 2*np.pi, npts, endpoint=True)   # time vector
f = 15.0 # Frequency in Hz
A = 100.0 # Amplitude in Unit
y = A * np.sin(2*np.pi*f*t) # Signal

y=y+np.random.randn(npts)*2*A


plt.figure()
plt.plot(t,y)
plt.xlabel('time / samples')
plt.ylabel('signal')


# perform FFT 
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

f,spectr= make_fft_DS(y,t)

# plt.figure()
# plt.plot(f,abs(spectr))



# performs non-coherent integration of a time series
def make_icoh(t, y, icoh):

    nptsn=int(np.floor(len(y)/icoh))
    Yi=np.empty(nptsn)
    tn=np.empty(nptsn)
    speci=np.zeros([nptsn,icoh])+1j*np.zeros([nptsn,icoh])

    # time series splitting
    for i in range(0,icoh):
        # i=0
        yn=y[i*nptsn:i*nptsn+nptsn]
        tn=t[i*nptsn:(i+1)*nptsn]
        
        #plt.plot(tn,yn)
        
        fi,Yi=make_fft_DS(yn,tn)
        
        # individual spectra
        speci[:,i]=Yi
        
        # integrated spectrum
        spectri=np.mean(abs(speci), axis=1)/np.sqrt(icoh)
        
        if len(fi)>len(spectri):
            fi=fi[:-1]
        
    return fi,spectri


icoh=5;

fi,spectri=make_icoh(t,y,icoh)

plt.figure()
plt.plot(f,abs(spectr))
plt.plot(fi,abs(spectri),'*-')
plt.xlabel('frequency')
plt.ylabel('amplitude')

