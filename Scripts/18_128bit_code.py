# %reset -f

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt



# rect function - code

# number of data points - bit length of the code
npts=128 # 1024

#t = np.linspace(0, 2*np.pi, npts, endpoint=True)   # time vector
t = np.linspace(0, npts-1, npts, endpoint=True)   # time vector


# generate a random 0-1 sequene -> simulate a 128bit code sequence
x1=np.round(np.random.rand(npts))*2-1



def plot_ovs(t,data,ovs):
    datan=np.zeros(ovs*len(data))
    
    for i in range(len(data)):
        datan[ovs*i:ovs*(i+1)]=data[i]

    tn=np.linspace(t[0],t[-1],len(datan))
    return tn,datan


ovs=10
    
tn,x1_ovs=plot_ovs(t,x1,ovs)



plt.figure()
plt.plot(tn,x1_ovs,'*-')
plt.xlabel('Time ($s$)')
plt.ylabel('Amplitude ($Unit$)')
plt.grid('on')


# auto-correlation of x1

rx1=signal.correlate(x1,x1)

t2=-1*t[::-1]
t2=np.append(t2, t[1:])

plt.figure()
plt.plot(t2,rx1)
plt.title('auto-correlation')

# main lobe intensity
ml=rx1[npts-1]
# side lobe intensity
sl=sum(abs(rx1[0:npts-2])) + sum(abs(rx1[npts:]))
# main - side lobe ratio
mlsl=ml/sl


# how may we find a better code - a code with better properties?
#
# a) use know good codes or b) try to find a better one in simulations


x_mlsl=mlsl
x_ref=x1




it=10000

# for ii in range(it):
#     x1=np.round(np.random.rand(npts))*2-1
#     rx1=signal.correlate(x1,x1)
#     ml=rx1[npts-1]
#     # sum of all side lobes
#     sl=sum(abs(rx1[0:npts-2])) + sum(abs(rx1[npts:]))
#     mlsl=ml/sl
#     if mlsl > x_mlsl:
#         x_ref=x1
#         x_mlsl=mlsl
#         print('found a better one')
#         plt.plot(t2,rx1)
        

plt.figure()
plt.title('auto-correlation')

for ii in range(it):
    x1=np.round(np.random.rand(npts))*2-1
    rx1=signal.correlate(x1,x1)
    ml=rx1[npts-1]
    # average of all side lobes
    sl=np.zeros(2*npts-1)
    sl[0:npts-2]=abs(rx1[0:npts-2])
    sl[npts:]=abs(rx1[npts:])
    mlsl=ml/np.mean(sl)
    if mlsl > x_mlsl:
        x_ref=x1
        x_mlsl=mlsl
        print('found a better one')
        plt.plot(t2,abs(rx1))



plt.figure()
plt.plot(t2,abs(rx1))
plt.title('auto-correlation')
