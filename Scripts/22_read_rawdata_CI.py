# %reset -f

import scipy.io as spio
import os
import matplotlib.pyplot as plt
import numpy as np
# import datetime



DataPath='D:/Python/Uni_HWI/scripts20/RAW/'
# DataPath='C:/Toralf/Python/Uni_HWI/scripts20/RAW/'

Files=os.listdir(DataPath)

currentfile=str(DataPath)+str(Files[1])

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





# perform coherent integrations
def make_ci(t, y, ci):
    nptsn=int(np.floor(len(y)/ci))
    yn=np.empty(nptsn)+1j*np.empty(nptsn)
    tn=np.empty(nptsn)
    for i in range(0,nptsn):
        yn[i]=np.mean(y[i*ci:i*ci+ci-1])
        tn[i]=np.mean(t[i*ci:(i+1)*ci])
    return tn,yn



# make FFT spectrum, frequency axis
def make_fft(t,y):
    dt = t[1]-t[0] # dt -> temporal resolution ~ sample rate
    f = np.fft.fftfreq(t.size, dt) # frequency axis
    Y = np.fft.fft(y)   # FFT
    f=np.fft.fftshift(f)
    Y= np.fft.fftshift(Y)/(len(y))
    return f,Y


# number of coherent integrations of I/Q raw data (time series)
ci=12


y=data[-25,:,0]

tn,yn=make_ci(t,y,ci)

plt.figure()
plt.subplot(1,2,1)
plt.plot(np.real(y),np.imag(y),'*')
plt.xlim([-100,100])
plt.ylim([-100,100])
plt.subplot(1,2,2)
plt.plot(np.real(yn),np.imag(yn),'*')
plt.xlim([-100,100])
plt.ylim([-100,100])



# length of the "new" integrated time series
noDPn=int(np.floor(noDP/ci))


# predefine matrix for integrated raw data
datan=np.zeros([noRG,noDPn,noRx])+1j*np.zeros([noRG,noDPn,noRx])

for rx in range(noRx):
    for rg in range(noRG):
        tn,datan[rg,:,rx]=make_ci(t,data[rg,:,rx],ci)



# time vector in s
tsec=t*60*60
tnsec=tn*60*60




# Spectra for all ranges and all receivers

Spectr=np.zeros([noRG,noDP,noRx])+1j*np.zeros([noRG,noDP,noRx])

for rx in range(noRx):
    for rg in range(noRG):
        f,Spectr[rg,:,rx]=make_fft(tsec,data[rg,:,rx])


# Spectra for all ranges and all receivers integrated time series

Spectrn=np.zeros([noRG,noDPn,noRx])+1j*np.zeros([noRG,noDPn,noRx])

for rx in range(noRx):
    for rg in range(noRG):
        fn,Spectrn[rg,:,rx]=make_fft(tnsec,datan[rg,:,rx])




plt.figure()
for rx in range(noRx):
    plt.subplot(2,3,rx+1)
    ampl=10*np.log10(abs(Spectr[:,:,rx]))
    SNRsel=ampl<-5   
    ampl[SNRsel]="nan"
    plt.pcolor(f,ranges,ampl,cmap='jet',shading='auto')
    plt.clim([-5, 25])
    # plt.xlim([min(fn), max(fn)])
    # plt.xlabel('f /Hz')
    # plt.ylabel('range /km')
    # plt.colorbar()
    
for rx in range(noRx):
    plt.subplot(2,3,rx+4)
    ampln=10*np.log10(abs(Spectrn[:,:,rx]))
    SNRsel=ampln<-5   
    ampln[SNRsel]="nan"
    plt.pcolor(fn,ranges,ampln,cmap='jet',shading='auto')
    plt.clim([-5, 25])
    plt.xlabel('f /Hz')
    # plt.ylabel('range /km')
    # plt.colorbar()
plt.subplot(2,3,1)
plt.ylabel('range /km')
plt.subplot(2,3,4)
plt.ylabel('range /km')




# # Cross-Spectra for all ranges and all receivers

# XSpectr=np.zeros([noRG,noDP,noRx])+1j*np.zeros([noRG,noDP,noRx])

# XSpectr[:,:,0]=Spectr[:,:,0]*np.conj(Spectr[:,:,1])
# XSpectr[:,:,1]=Spectr[:,:,0]*np.conj(Spectr[:,:,2])
# XSpectr[:,:,2]=Spectr[:,:,1]*np.conj(Spectr[:,:,2])

# # plt.figure()
# # plt.pcolor(f,ranges,10*np.log10(abs(XSpectr[:,:,1]))/2)
# # # plt.pcolor(f,ranges,np.angle(XSpectr[:,:,1]))
# # plt.colorbar()
# # plt.clim([-15, 15])


# plt.figure()
# for rx in range(noRx):
#     plt.subplot(1,3,rx+1)
#     plt.pcolor(f,ranges,10*np.log10(abs(XSpectr[:,:,rx]))/2,cmap='jet')
#     plt.clim([-15, 15])
#     plt.title('XSp ampl')

# plt.figure()    
# for rx in range(noRx):
#     plt.subplot(1,3,rx+1)
#     plt.pcolor(f,ranges,np.angle(XSpectr[:,:,rx])/np.pi*180,cmap='jet')
#     plt.clim([-180, 180])
#     # plt.colorbar()
#     plt.title('XSp phase')



