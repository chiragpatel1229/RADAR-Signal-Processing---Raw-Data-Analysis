# %reset -f

import scipy.io as spio
import os
import matplotlib.pyplot as plt
import numpy as np
# import datetime



DataPath='D:/Python/Uni_HWI/scripts20/RAWn/'

Files=os.listdir(DataPath)

ff=2
currentfile=str(DataPath)+str(Files[ff])



print('reading file:')
print(currentfile)

# importing MATLAB mat file   (containing radar raw data)
mat = spio.loadmat(currentfile, squeeze_me=True)

datenums=mat['datenums']
ranges=mat['ranges']
data=np.complex64(mat['data'])
antpos=np.complex64(mat['antpos'])
wl=mat['wl']
    


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

ci=8;

noDPn=int(np.floor(noDP/ci))
# predefine matrix for integrated raw data
datan=np.zeros([noRG,noDPn,noRx])+1j*np.zeros([noRG,noDPn,noRx])

for rx in range(noRx):
    for rg in range(noRG):
        tn,datan[rg,:,rx]=make_ci(t,data[rg,:,rx],ci)

data=datan[:]
t=tn[:]
noDP=np.size(data,1)



plt.figure()
plt.plot(20*np.log10(np.mean(abs(data),1)),ranges)
plt.xlabel('power /dB')
plt.ylabel('altitude /km')
plt.grid(1)

RXsel=1

plt.figure()
plt.pcolor(20*np.log10(abs(data[:,:,RXsel])))
plt.xlabel('samples')
plt.ylabel('altitude /km')
plt.title('power /dB')
plt.colorbar()
plt.clim(15,60)



# Phase-correction - Receiver / antenna phases

# calibration phases:
RXPhases=[0, -15.7, -24.4, 0, 6.65, -6.73, 26.67, 11.92, 10.58]
RXPhases=np.mat(RXPhases)*-1/180*np.pi
# RXPhases[0,3]


# rotation of a complex number - multiplication of an exp.-function

#a=np.complex(2,+3)
## a=2+3j
#b=a*np.exp(1j*180/180*np.pi)
#
#plt.figure()
#plt.plot(a.real,a.imag,'*')
#plt.xlim([-5, 5])
#plt.ylim([-5, 5])
#plt.grid(1)
#plt.plot(b.real,b.imag,'*')




plt.figure()
for rx in range(3):
    plt.subplot(1,3,rx+1)
    plt.plot(np.real(data[21,100:150,rx]),np.imag(data[21,100:150,rx]),'.')
    plt.axis([-100,100,-100,100])
    plt.grid(1)
    plt.title(('I/Q RX ', str(rx)))

    
# receiver phase adjustment 
for rx in range (noRx):
    data[:,:,rx]=data[:,:,rx]*np.exp(1j*RXPhases[0,rx+6])   # used receiver are 7,8,9


for rx in range(3):
    plt.subplot(1,3,rx+1)
    plt.plot(np.real(data[21,100:150,rx]),np.imag(data[21,100:150,rx]),'.')
    plt.axis([-100,100,-100,100])
    plt.grid(1)

            
# DC-offset ? here very little, negligible


dataDC=np.mean(np.mean(data[0:10,:,:],0),0)

plt.figure()
for rx in range(3):
    plt.plot(np.real(dataDC[rx]),np.imag(dataDC[rx]),'x')

plt.grid(1)
plt.title('I/Q diagram DC-offset')
plt.legend(('RX1','RX2','RX3'))
plt.axis([-10,10,-10,10])

# very little DC-offsets in good digital receivers



RXsel=1;


PWRcomb=20*np.log10(np.abs(np.mean(data,2)))
    
plt.figure()
plt.pcolor(t,ranges,PWRcomb,cmap='jet',shading='auto')
plt.xlabel('time / HH')
plt.ylabel('range /km')
plt.title('combined power /dB')
plt.clim(15,90)
plt.colorbar()



datamean=np.mean(data,1)

#test=np.mean(np.mean(data,2),1)

# PWRrg=20*np.log10(np.mean(np.abs(np.mean(data,2)),1))

# plt.figure()
# plt.plot(PWRrg,ranges)


pairs=[[0,1],[0,2],[1,2]]
#pairs
nopairs=np.size(pairs,0)

dx=np.zeros([nopairs])
dy=np.zeros([nopairs])
#phases=np.zeros([noRG,noDP,nopairs])
phases=np.zeros([noRG,nopairs])
# phases=np.angle(data[30,:,0]*np.conjugate(data[30,:,1]))


for pp in range(nopairs):
    dx[pp]=(antpos[pairs[rx][0]]-antpos[pairs[pp][1]]).real
    dy[pp]=(antpos[pairs[rx][0]]-antpos[pairs[pp][1]]).imag
    phases[:,pp]=np.angle(datamean[:,pairs[pp][0]]*np.conjugate(datamean[:,pairs[pp][1]]))

R=2*np.pi/wl * np.array([dx, dy])
#R=np.transpose(R)
R=R.T


# least squares matrix solving 
# numpy linalg 
# https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html

#B=np.matmul(np.transpose(np.mat(R)),np.mat(R))
B=np.matmul(np.mat(R).T,np.mat(R))


pos_data=np.zeros([noRG,2])
phi=np.zeros([noRG,1])
theta=np.zeros([noRG,1])

rg=0
for rg in range(noRG):
#b=np.matmul(np.transpose(np.mat(R)),np.transpose(np.mat(phases[0,:])))
    b=np.matmul(np.mat(R).T,np.mat(phases[rg,:]).T)

    r=np.linalg.solve(B.T.dot(B), B.T.dot(b))
    #r=np.linalg.lstsq(B,b,rcond=None)[0]
    pos_data[rg,:]=r.T
    phi[rg]=np.arctan2(r[1],r[0])/np.pi*180
    theta[rg]=np.arcsin(np.sqrt(r[0]**2+r[1]**2))/np.pi*180

plt.figure()
plt.plot(pos_data[15:,0],pos_data[15:,1],'.')
plt.xlim([-1,1])
plt.ylim([-1,1])
plt.grid(1)
plt.xlabel('dcosx sin(theta)cos(phi)')
plt.ylabel('dcosy sin(theta)sin(phi)')


plt.figure()
plt.subplot(1,2,1)
plt.plot(np.mean(PWRcomb,1),ranges)
plt.grid(1)
plt.ylabel('range /km')
plt.xlabel('power /dB')
plt.subplot(1,2,2)
plt.plot(phi,ranges)
plt.plot(theta,ranges)
plt.legend(('phi','theta'))
plt.title('AOA')
