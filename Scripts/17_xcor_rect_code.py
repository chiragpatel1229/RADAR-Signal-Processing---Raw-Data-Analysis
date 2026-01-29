# %reset -f

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt



# rect function - Barker code

code=[1,1,1,-1,1]
# code=[1,1,1,-1,-1,1,-1]
# code=[1,1,1,1,1,-1,-1,1,1,-1,1,-1,1]

npts=len(code)
t = np.linspace(0, npts-1, npts, endpoint=True)



plt.figure()
plt.plot(t,code)
plt.xlabel('Time ($s$)')
plt.ylabel('Amplitude ($Unit$)')
plt.grid('on')


# oversampling for plotting


def plot_ovs(t,data,ovs):
    datan=np.zeros(ovs*len(data))
    
    for i in range(len(data)):
        datan[ovs*i:ovs*(i+1)]=data[i]

    tn=np.linspace(t[0],t[-1],len(datan))
    return tn,datan


ovs=10
    
tn,code_ovs=plot_ovs(t,code,ovs)


plt.figure()
plt.plot(tn,code_ovs)
plt.xlabel('Time ($s$)')
plt.ylabel('Amplitude ($Unit$)')
plt.grid('on')    



# auto-correlation of code

rb=signal.correlate(code,code)

t2=-1*t[::-1]
t2=np.append(t2, t[1:])

plt.figure()
plt.plot(t2,rb)



# complementary code - pair of codes

npts=16

#t = np.linspace(0, 2*np.pi, npts, endpoint=True)   # time vector
t = np.linspace(0, npts-1, npts, endpoint=True)   # time vector


c16a=[1, 1, 1, -1, 1, 1, -1, 1, 1, 1, 1, -1, -1, -1, 1, -1]
c16b=[1, 1, 1, -1, 1, 1, -1, 1, -1, -1, -1, 1, 1, 1, -1, 1]


tn,c16a_ovs=plot_ovs(t,c16a,ovs)
tn,c16b_ovs=plot_ovs(t,c16b,ovs)

plt.figure()
plt.subplot(2,1,1)
plt.plot(tn,c16a_ovs)
plt.xlabel('Time ($s$)')
plt.ylabel('Amplitude ($Unit$)')
plt.grid('on')
plt.subplot(2,1,2)
plt.plot(tn,c16b_ovs)
plt.xlabel('Time ($s$)')
plt.ylabel('Amplitude ($Unit$)')
plt.grid('on')


# auto-correlation of y3

r16a=signal.correlate(c16a,c16a)
r16b=signal.correlate(c16b,c16b)
t2=-1*t[::-1]
t2=np.append(t2, t[1:])

plt.figure()
plt.subplot(3,1,1)
plt.plot(t2,r16a)
plt.subplot(3,1,2)
plt.plot(t2,r16b)
plt.subplot(3,1,3)
plt.plot(t2,r16a+r16b)




# + noise -> 

A=1/5;
noise=np.random.randn(npts)
r16an=signal.correlate(c16a+A*noise,c16a+A*noise)
noise=np.random.randn(npts)
r16bn=signal.correlate(c16b+A*noise,c16b+A*noise)

plt.figure()
plt.subplot(3,1,1)
plt.plot(t2,r16an)
plt.subplot(3,1,2)
plt.plot(t2,r16bn)
plt.subplot(3,1,3)
plt.plot(t2,r16an+r16bn)

# sumlog=20*np.log(r16an+r16bn)

# plt.figure()
# plt.plot(t2,sumlog)


