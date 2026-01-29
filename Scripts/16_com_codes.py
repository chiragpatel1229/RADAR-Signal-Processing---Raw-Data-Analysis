
# %reset -f 


import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# communication codes - example from wikipedia

seq=[1,1,0,1,1,0,0,0,1,0,0]



# RZ codes

code_rz=np.zeros(2*len(seq))
code_nrz=np.zeros(2*len(seq))

for i in range(len(seq)):
    if seq[i]==1:
        code_rz[2*i]=1
        code_rz[2*i+1]=0
        code_nrz[2*i]=1
        code_nrz[2*i+1]=1
    else:
        code_rz[2*i]=-1
        code_rz[2*i+1]=0    
        code_nrz[2*i]=-1
        code_nrz[2*i+1]=-1    

plt.figure()
plt.plot(seq)

plt.figure()
plt.subplot(2,1,1)
plt.plot(code_rz)
plt.subplot(2,1,2)
plt.plot(code_nrz)


# oversampling for plotting

# ovs=10

# code_rz_ovs=np.zeros(ovs*len(code_rz))
# code_nrz_ovs=np.zeros(ovs*len(code_nrz))

# for i in range(len(code_rz)):
#     code_rz_ovs[ovs*i:ovs*(i+1)]=code_rz[i]
#     code_nrz_ovs[ovs*i:ovs*(i+1)]=code_nrz[i]
    




def plot_ovs(data,ovs):
    datan=np.zeros(ovs*len(data))
    
    for i in range(len(data)):
        datan[ovs*i:ovs*(i+1)]=data[i]

    return datan


ovs=10
    
code_rz_ovs=plot_ovs(code_rz,ovs)
code_nrz_ovs=plot_ovs(code_nrz,ovs)

plt.figure()
plt.subplot(2,1,1)
plt.plot(code_rz_ovs)
plt.subplot(2,1,2)
plt.plot(code_nrz_ovs)


np.mean(code_rz)
np.mean(code_nrz)


# ASCII codes CP852
cA=[0,1,0,0,0,0,0,1]    # "A"

cR=[0,1,0,1,0,0,1,0]    # "R"

cK=[0,1,0,0,1,0,1,1]    # "K"

# property of codes... correlations ! auto & cross correlation
R_rk=signal.correlate(cR,cK)
R_ar=signal.correlate(cA,cR)
R_ak=signal.correlate(cA,cK)

R_aa=signal.correlate(cA,cA)
R_kk=signal.correlate(cK,cK)
R_rr=signal.correlate(cR,cR)


plt.figure()
plt.subplot(2,1,1)
plt.plot(R_aa)
plt.plot(R_kk)
plt.plot(R_rr)
plt.title('auto-correlations')
plt.subplot(2,1,2)
plt.plot(R_ar)
plt.plot(R_rk)
plt.plot(R_ar)
plt.title('cross-correlations')




# generate the full code including start-, stop- and paritybit

# startbit  symbol(code) parity stopbit

ch=cA

# convert list to str
chstr = ''.join(str(e) for e in ch)
# convert bin to dec
chdec=int(chstr, 2)

# even parity bit 
if chdec%2 == 0:
    par=0
else:
    par=1

# # odd parity bit 
# if chdec%2 == 0:
#     par=1
# else:
#     par=0

    
startbit=0
stopbit=1
        
seq2=np.zeros(11)
seq2[0]=startbit
seq2[1:9]=ch
seq2[9]=par
seq2[10]=stopbit





