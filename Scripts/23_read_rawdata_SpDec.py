
# %reset -f

import scipy.io as spio
import os
import matplotlib.pyplot as plt
import numpy as np
# import datetime



DataPath='D:/Python/Uni_HWI/scripts20/RAW/'

Files=os.listdir(DataPath)

currentfile=str(DataPath)+str(Files[0])

# importing MATLAB mat file   (containing radar raw data)
mat = spio.loadmat(currentfile, squeeze_me=True)

datenums=mat['datenums']
ranges=mat['ranges']
data=mat['data']


# datenums ~ days since year 0
# here only the time is important for us -> hours, minutes, seconds
# => fraction / remainder of the integer

t=(datenums-np.floor(np.min(datenums)))*24



# number of range gates , data points, receivers
noRG=np.size(data,0)
noDP=np.size(data,1)
noRx=np.size(data,2)



RXsel=1





def make_fft(t,y):
    dt = t[1]-t[0] # dt -> temporal resolution ~ sample rate
    f = np.fft.fftfreq(t.size, dt) # frequency axis
    Y = np.fft.fft(y)   # FFT
    f=np.fft.fftshift(f)
    Y= np.fft.fftshift(Y)/(len(y))
    return f,Y



tsec=t*60*60

f,spec=make_fft(tsec,data[-25,:,RXsel])


plt.figure()
plt.plot(f,10*np.log10(abs(spec)))
plt.grid ('on')
plt.xlabel('f / Hz')
plt.ylabel('amplitude /dB')





# Spectra for all ranges and all receivers


Spectr=np.zeros([noRG,noDP,noRx])+1j*np.zeros([noRG,noDP,noRx])

for rx in range(noRx):
    for rg in range(noRG):
        f,Spectr[rg,:,rx]=make_fft(tsec,data[rg,:,rx])


plt.figure()
for rx in range(noRx):
    plt.subplot(1,3,rx+1)
    plt.pcolor(f,ranges,10*np.log10(abs(Spectr[:,:,rx])),cmap='jet',shading='auto')
    plt.clim([-15, 15])
    plt.xlabel('f /Hz')
    plt.ylabel('range /km')
    plt.xlim([-1,1])
    # plt.colorbar()



# perform spectral decimation
def make_SpDec(f,Sp,dec):
    nptsn=int(np.floor(np.size(Sp,1)/dec))
    noRG=np.size(Sp,0)
    Spn=np.empty([noRG,nptsn])+1j*np.empty([noRG,nptsn])
    fn=np.empty(nptsn)
    for i in range(0,nptsn):  # i=0
        Spn[:,i]=np.mean(Sp[:,i*dec:i*dec+dec-1],1)
        fn[i]=np.mean(f[i*dec:(i+1)*dec])
    return fn,Spn



dec=4


fn,SpectrDec=make_SpDec(f,Spectr[:,:,1],dec)

plt.figure()
plt.subplot(1,2,1)
plt.pcolor(f,ranges,10*np.log10(abs(Spectr[:,:,1])),cmap='jet',shading='auto')
plt.clim([-15, 15])
plt.xlabel('f /Hz')
plt.ylabel('range /km')
plt.xlim([-1,1])
plt.subplot(1,2,2)
plt.pcolor(fn,ranges,10*np.log10(abs(SpectrDec[:,:])),cmap='jet',shading='auto')
plt.clim([-15, 15])
plt.xlabel('f /Hz')
plt.ylabel('range /km')
plt.xlim([-1,1])


