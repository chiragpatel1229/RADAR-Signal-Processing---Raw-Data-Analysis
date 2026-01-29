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


data.shape # (ranges, samples, receivers)


# datenums ~ days since year 0
# here only the time is important for us -> hours, minutes, seconds
# => fraction / remainder of the integer

t=(datenums-np.floor(np.min(datenums)))*24



# number of range gates , data points, receivers
noRG=np.size(data,0)
noDP=np.size(data,1)
noRx=np.size(data,2)





# time series 

# plotting range gate (altitude) RG for receiver RXsel

RXsel=1;
RG=-1

y=data[RG,:,RXsel]

# I/Q diagram
plt.figure()
plt.plot(np.real(y),np.imag(y),'.')
plt.xlabel('real')
plt.ylabel('imag')


# power of the complex valued voltages (measured by the receiver)
PWR=20*np.log10(np.abs(data[:,:,RXsel]))

type(PWR)
PWR.shape     # dimensions: ( ranges , samples (t) )


# power profile for the first sample - over range (altitude)
plt.figure()
plt.plot(PWR[:,0],ranges)

# power plot for all samples and all ranges (altitude)
plt.figure()
plt.pcolor(t,ranges,PWR,cmap='jet',shading='auto')
plt.xlabel('time / HH')
plt.ylabel('range /km')
plt.title('power /dB')
plt.clim(20,70)
plt.colorbar()




# combine the data of all three receivers - complex sum !
# sum the receivers - dimension 3!
datacomb=np.sum(data,2)

# power for the combined receivers in log-scale
PWRcomb=20*np.log10(np.abs(datacomb))


plt.figure()
plt.pcolor(t,ranges,PWRcomb,cmap='jet',shading='auto')
plt.xlabel('time / HH')
plt.ylabel('range /km')
plt.title('combined power /dB')
plt.clim(20,70)
plt.colorbar()



# Spectra


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
    # plt.colorbar()







# Cross-Spectra for all ranges and all receivers

XSpectr=np.zeros([noRG,noDP,noRx])+1j*np.zeros([noRG,noDP,noRx])

XSpectr[:,:,0]=Spectr[:,:,0]*np.conj(Spectr[:,:,1])
XSpectr[:,:,1]=Spectr[:,:,0]*np.conj(Spectr[:,:,2])
XSpectr[:,:,2]=Spectr[:,:,1]*np.conj(Spectr[:,:,2])

# plt.figure()
# plt.pcolor(f,ranges,10*np.log10(abs(XSpectr[:,:,1]))/2)
# # plt.pcolor(f,ranges,np.angle(XSpectr[:,:,1]))
# plt.colorbar()
# plt.clim([-15, 15])


plt.figure()
for rx in range(noRx):
    plt.subplot(1,3,rx+1)
    plt.pcolor(f,ranges,10*np.log10(abs(XSpectr[:,:,rx])/2),cmap='jet')
    plt.clim([-15, 15])
    plt.title('XSp ampl')


phases=[]
plt.figure()    
for rx in range(noRx):    # rx=0
    plt.subplot(1,3,rx+1)
    phases=np.angle(XSpectr[:,:,rx])/np.pi*180
    plt.pcolor(f,ranges,phases,cmap='jet',shading='auto')
    plt.clim([-180, 180])
    # plt.colorbar()
    plt.title('XSp phase')
    
    


plt.figure()
for rx in range(noRx):
    plt.subplot(1,3,rx+1)
    ampl=10*np.log10(abs(XSpectr[:,:,rx])/2)
     # SNR cleaning
    SNRsel=ampl<-11
    ampl[SNRsel]="nan"
    plt.pcolor(f,ranges,ampl,cmap='jet',shading='auto')
    plt.clim([-10, 20])
    plt.title('XSp ampl')


plt.figure()    
for rx in range(noRx):    # rx=0
    plt.subplot(1,3,rx+1)
    phases=np.angle(XSpectr[:,:,rx])/np.pi*180
    # SNR cleaning
    SNRsel=10*np.log10(abs(XSpectr[:,:,rx])/2)<-11    
    # phases[SNRsel]=float("nan")
    phases[SNRsel]="nan"
    plt.pcolor(f,ranges,phases,cmap='jet',shading='auto')
    plt.clim([-180, 180])
    # plt.colorbar()
    plt.title('XSp phase')
    plt.xlim([-.75,.75])


