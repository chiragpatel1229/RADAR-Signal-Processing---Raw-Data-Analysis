# %reset -f


import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# generate a time series of random QAM  values... I/Q diagramm 
# npts-times the same I/Q-value -> oversampling


# > phase offset between two time series...
#  a) correlation


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
plt.xlabel('samples / time')
plt.subplot(212)
plt.plot(x,np.imag(iq))
plt.ylabel('Im')
plt.xlabel('samples / time')
    


# example for testing IQ phase rotation

phi=33
a=1+0j;

# rotating a by phi

b=a*np.exp(1j*phi/180*np.pi)

plt.figure()
plt.plot(np.real(a),np.imag(a),'r*',markersize=15)
plt.plot(np.real(b),np.imag(b),'b*',markersize=15)
plt.xlim(-1.5,1.5)
plt.ylim(-1.5,1.5)
plt.grid('ON')
plt.title('example rotating a complex number')
plt.xlabel('Re(a)')
plt.xlabel('Im(a)')



# rotating iq time series by phi 

phi=90;

iq2=iq*np.exp(1j*phi/180*np.pi)

plt.figure()
plt.plot(np.real(iq[1]),np.imag(iq[1]),'.',markersize=15)
plt.plot(np.real(iq2[1]),np.imag(iq2[1]),'.',markersize=15)
plt.grid('on')
plt.xlim(-5,5)
plt.ylim(-5,5)
plt.xlabel('Re(iq)')
plt.xlabel('Im(iq)')

# adding noise to the I/Q data

noiseampl=1/2

iqn=iq + np.random.randn(len(iq))*noiseampl+1j*np.random.randn(len(iq))*noiseampl

iq2n=iq2 + np.random.randn(len(iq2))*noiseampl+1j*np.random.randn(len(iq2))*noiseampl


# I/Q diagram

plt.figure()
plt.plot(np.real(iqn),np.imag(iqn),'.')
plt.plot(np.real(iq2n),np.imag(iq2n),'.')
plt.grid('on')
plt.title('IQ diagram of noisy time series')
plt.xlabel('Re(iq)')
plt.xlabel('Im(iq)')


# correlate signals

R12=signal.correlate(iqn,iq2n)

plt.figure()
plt.subplot(2,2,1)
plt.plot(np.real(R12))
plt.title('Re')
plt.subplot(2,2,2)
plt.plot(np.imag(R12))
plt.title('Im')
plt.subplot(2,2,3)
plt.plot(np.abs(R12))
plt.title('Magn')
plt.subplot(2,2,4)
plt.plot(np.angle(R12)/np.pi*180)
plt.title('Phase')



# phase offset between iqn and iq2n from R12

phoffset=np.angle(R12[2500])/np.pi*180










# b) complex time series multiplication

iqdiff=iq2n*np.conj(iqn)


plt.figure()
plt.plot(np.real(iqdiff),np.imag(iqdiff),'.')
plt.plot(np.real(np.mean(iqdiff)),np.imag(np.mean(iqdiff)),'*')



plt.figure()
plt.subplot(2,2,1)
plt.plot(np.real(iqdiff))
plt.title('Re')
plt.subplot(2,2,2)
plt.plot(np.imag(iqdiff))
plt.title('Im')
plt.subplot(2,2,3)
plt.plot(np.abs(iqdiff))
plt.title('Magn')
plt.subplot(2,2,4)
plt.plot(np.angle(iqdiff)/np.pi*180)
plt.title('Phase')


iqdiffmean=np.mean(iqdiff)

# phase offset between iqn and iq2n from iqdiff
phoffset2= np.angle(iqdiffmean)/np.pi*180



