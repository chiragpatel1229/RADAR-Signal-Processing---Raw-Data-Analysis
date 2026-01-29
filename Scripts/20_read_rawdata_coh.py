# %reset -f

import scipy.io as spio
from scipy import signal
import os
import matplotlib.pyplot as plt
import numpy as np
# import datetime



DataPath='D:/Python/Uni_HWI/scripts20/RAW/'
# DataPath='C:/Toralf/Python/Uni_HWI/scripts20/RAW/'

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

ts=(t[1]-t[0])*60*60   # delta-t : sampling distance in time [s]

# number of range gates , data points, receivers
noRG=np.size(data,0)
noDP=np.size(data,1)
noRx=np.size(data,2)

RXsel=1


# averaged power per receiver for all datapoints

PWR=np.zeros([noRG,noRx])

for rx in range(noRx):
    PWR[:,rx]=20*np.log10(np.abs(np.mean(data[:,:,rx],1)))


plt.figure()
plt.plot(PWR,ranges)
plt.legend(['RX1','RX2','RX3'])
plt.xlabel('power /dB')
plt.ylabel('ranges /km')


# coherence for one range and two receivers -> testing reasons

RG=17
x1=data[RG,:,0]
x2=data[RG,:,1]

plt.figure()
plt.plot(t,abs(x1),t,abs(x2))

Fs=1/ts

f,coh=signal.coherence(x1,x2,Fs)

f=np.fft.fftshift(f)
coh=np.fft.fftshift(coh)

plt.figure()
plt.plot(f,coh)
plt.xlabel('f / Hz')
plt.ylabel('coh')




# coherence for all ranges and all receivers

npts=256
cohtemp=np.zeros(256)
Coh=np.zeros([noRG,npts,noRx])

for rg in range(noRG):
    f,cohtemp=signal.coherence(data[rg,:,0],data[rg,:,1],Fs)
    Coh[rg,:,0]=np.fft.fftshift(cohtemp)
    f,cohtemp=signal.coherence(data[rg,:,0],data[rg,:,2],Fs)
    Coh[rg,:,1]=np.fft.fftshift(cohtemp)
    f,cohtemp=signal.coherence(data[rg,:,1],data[rg,:,2],Fs)
    Coh[rg,:,2]=np.fft.fftshift(cohtemp)

f=np.fft.fftshift(f)

plt.figure()
for rx in range(noRx):
    plt.subplot(1,3,rx+1)
    plt.pcolor(f,ranges,(np.abs(Coh[:,:,rx])),cmap='jet',shading='auto' )
    plt.xlabel('f / Hz')
    plt.ylabel('range /km')
    plt.clim([0.2,1])
    plt.xlim([-1,1])
    plt.colorbar()

plt.subplot(1,3,1)
plt.title('coherence RX1-2')
plt.subplot(1,3,2)
plt.title('coherence RX1-3')
plt.subplot(1,3,3)
plt.title('coherence RX2-3')




         
         
