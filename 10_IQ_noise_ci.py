# %reset -f


import numpy as np
import matplotlib.pyplot as plt


# generate a time series of random QAM  values... I/Q diagramm 
# npts-times the same I/Q-value -> oversampling


npts=50

iq=np.zeros(1)
for jj in range(npts):
    iq=np.append(iq,np.tile(np.round(np.random.randn(1))+1j*np.round(np.random.randn(1)),npts))
    
iq=iq[1:]

x=np.arange(1,len(iq)+1)

plt.figure()
plt.subplot(211)
plt.plot(x,np.real(iq))
plt.ylabel('Re')
plt.subplot(212)
plt.plot(x,np.imag(iq))
plt.ylabel('Im')
    

plt.figure()
plt.plot(np.real(iq),np.imag(iq),'.')
plt.grid('on')
plt.title('IQ time series without noise')
plt.ylabel('Im')
plt.xlabel('Re')

# adding noise to the I/Q data

noiseampl=1/2

iqn=iq + np.random.randn(len(iq))*noiseampl+1j*np.random.randn(len(iq))*noiseampl

# I/Q diagram

plt.figure()
plt.plot(np.real(iqn),np.imag(iqn),'.')
plt.grid('on')
plt.title('IQ time series with noise')
plt.ylabel('Im')
plt.xlabel('Re')


# How to reconstruct the orignal I/Q values???

# What knowledge about the original signal do we have?
# ->  oversampling 

# What knowledge about noise do we have ?
# -> propability density function

noise=np.random.randn(int(1e6))

plt.figure()
plt.hist(noise,100)
plt.title('PDF noise')

# where is the central (first) moment? == mean !
noise_mean=np.mean(noise)


# smoothing function - box car
def smooth(y, pts):
    nptsn=int(len(y)/pts)
    yn=np.zeros(len(y))+1j*np.zeros(len(y))
    for i in range(0,nptsn):    # i=0    i=i+1
        yn[i*pts:(i+1)*pts]=np.tile(np.mean(y[i*pts:(i+1)*pts]),pts)
       
    return yn

smpts=int(npts/ 2 )

yn=smooth(iqn,smpts)


plt.figure()
plt.plot(np.real(iqn),np.imag(iqn),'.')
plt.plot(np.real(yn),np.imag(yn),'.')
plt.grid('on')
plt.title('IQ time series with noise')
plt.ylabel('Im')
plt.xlabel('Re')
plt.legend(('signal+noise','after smooth'))






def make_ci(t,y, ci):
    nptsn=int(np.floor(len(y)/ci))
    yn=np.empty(nptsn)+1j*np.empty(nptsn)
    tn=np.empty(nptsn)
    for i in range(0,nptsn):
        yn[i]=np.mean(y[i*ci:i*ci+ci-1])
        tn[i]=np.mean(t[i*ci:(i+1)*ci])
    return tn,yn


ci=50
xn,iqs=make_ci(x,iqn,ci)


plt.figure()
plt.plot(np.real(iqn),np.imag(iqn),'.')
plt.plot(np.real(iqs),np.imag(iqs),'.')
plt.grid('on')
plt.title('IQ time series with noise')
plt.ylabel('Im')
plt.xlabel('Re')
plt.legend(('signal+noise','after coh. int.'))



