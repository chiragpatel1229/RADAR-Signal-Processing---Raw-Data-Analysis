# %reset -f

import scipy.io as spio
import os
import matplotlib.pyplot as plt
import numpy as np
# import datetime



DataPath='D:/Python/Uni_HWI/scripts20/RAW_ex2021/'

Files=os.listdir(DataPath)

currentfile=str(DataPath)+str(Files[0])

# importing MATLAB mat file   (containing radar raw data)
mat = spio.loadmat(currentfile, squeeze_me=True)

datenums=mat['datenums']
ranges=mat['ranges']
# data=mat['data']
data=mat['RD']

np.shape(data)
# 81 range gates, 7950 time samples, 4 receiver channel, 2 beam directions
# receiver index 0: entire array, 1-3 individual antennas

# perhaps delete mat as soon as you don't need it anymore - freeing memory

plt.figure()
plt.plot(datenums)

# -> multiple experiment runs in the raw data

# for further examination - find the jumps in the time and seperate the individual experiments

# no. range gates, no. data samples, no. receivers, no. polarisations

data1=data[:,0:1589,:,:]


# datenums ~ days since year 0
# here only the time is important for us -> hours, minutes, seconds
# => fraction / remainder of the integer

t=(datenums-np.floor(np.min(datenums)))*24



# number of range gates , data points, receivers
noRG=np.size(data,0)
noDP=np.size(data,1)
noRx=np.size(data,2)
noPol=np.size(data,3)

pol=1
RXsel=1





def make_fft(t,y):
    dt = t[1]-t[0] # dt -> temporal resolution ~ sample rate
    f = np.fft.fftfreq(t.size, dt) # frequency axis
    Y = np.fft.fft(y)   # FFT
    f=np.fft.fftshift(f)
    Y= np.fft.fftshift(Y)/(len(y))
    return f,Y



tsec=t*60*60

t1=tsec[0:1589]

f,spec=make_fft(t1,data1[22,:,RXsel,pol])


plt.figure()
plt.plot(f,10*np.log10(abs(spec)))
plt.grid ('on')
plt.xlabel('f / Hz')
plt.ylabel('amplitude /dB')





# Spectra for all ranges 


Spectr=np.zeros([noRG,1589])+1j*np.zeros([noRG,1589])

rx=0;

for rg in range(noRG):
    f,Spectr[rg,:]=make_fft(t1,data1[rg,:,rx,pol])


plt.figure()
plt.pcolor(f,ranges,10*np.log10(abs(Spectr[:,:])),cmap='jet',shading='auto')
plt.clim([-15, 15])
plt.xlabel('f /Hz')
plt.ylabel('range /km')
plt.xlim([-1,1])
plt.colorbar()

