# %reset -f

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt



# rect function - code


npts=100

#t = np.linspace(0, 2*np.pi, npts, endpoint=True)   # time vector
t = np.linspace(0, npts-1, npts, endpoint=True)   # time vector

# a random 0-1 sequene - arbitrary sequence

y3=np.round(np.random.rand(npts))



plt.figure()
plt.plot(t,y3)
plt.xlabel('Time ($s$)')
plt.ylabel('Amplitude ($Unit$)')
plt.grid('on')


# auto-correlation of y3

sy3y3=signal.correlate(y3,y3)
t2=-1*t[::-1]
t2=np.append(t2, t[1:])

plt.figure()
plt.plot(t2,sy3y3)

# no changes to the signal (y3) -> peak at the center = no offset!
# perhaps only one peak and quite good separation to the sides (main- vs. sidelobes)
# -> quality depends on the arbitrary rect function ("code")


# normalization by the number of overlapping elements - including weighting

yt=np.ones(npts)
sytyt=signal.correlate(yt,yt)

rel=np.median(sy3y3)/np.median(sytyt)

plt.figure()
plt.plot(t2,sy3y3-rel*sytyt)





# + noise -> correlation y3-y3n 


noise=np.random.randn(npts)
y3n=y3+noise



plt.figure()
plt.plot(t,y3,t,y3n)
plt.xlabel('Time ($s$)')
plt.ylabel('Amplitude ($Unit$)')
plt.grid('on')



sy3y3n=signal.correlate(y3,y3n)

plt.figure()
plt.plot(t2,sy3y3n)


# normalization by the number of overlapping elements - including weighting

yt=np.ones(npts)
sytyt=signal.correlate(yt,yt)

rel=np.median(sy3y3n)/np.median(sytyt)

#plt.figure()
plt.plot(t2,sy3y3n-rel*sytyt)









# rect function shifted



npts=100

#t = np.linspace(0, 2*np.pi, npts, endpoint=True)   # time vector
t = np.linspace(0, npts-1, npts, endpoint=True)   # time vector

y3=np.round(np.random.rand(npts))

noise=np.random.randn(npts)
y3n=y3+noise/3

# shifted version of y3

y4=np.roll(y3,25)

# adding noise

noise=np.random.randn(npts)
y4n=y4+noise/3



plt.figure()
plt.plot(t,y3n,t,y4n)
plt.xlabel('Time ($s$)')
plt.ylabel('Amplitude ($Unit$)')
plt.grid('on')

# cross-correlation

sy3ny4n=signal.correlate(y3n,y4n)
t2=-1*t[::-1]
t2=np.append(t2, t[1:])

plt.figure()
plt.plot(t2,sy3ny4n)


# normalization by the number of overlapping elements - including weighting

yt=np.ones(npts)

# plt.figure()
# plt.plot(t,yt)

sytyt=signal.correlate(yt,yt)

# plt.figure()
# plt.plot(t2,sytyt)

rel=np.median(sy3ny4n)/np.median(sytyt)

#plt.figure()
plt.plot(t2,sy3ny4n-rel*sytyt)






# correlation of two random sequences


# another random 0-1 sequene

y4=np.round(np.random.rand(npts))


plt.figure()
plt.plot(t,y3,t,y4)
plt.xlabel('Time ($s$)')
plt.ylabel('Amplitude ($Unit$)')
plt.grid('on')


# cross-correlation y3-y4

sy3y4=signal.correlate(y3,y4)

t2=-1*t[::-1]
t2=np.append(t2, t[1:])

plt.figure()
plt.plot(t2,sy3y4)


# normalization by the number of overlapping elements - including weighting

yt=np.ones(npts)
sytyt=signal.correlate(yt,yt)

rel=np.median(sy3y4)/np.median(sytyt)

plt.figure()
plt.plot(t2,sy3y4-rel*sytyt)

# -> two random sequences of sufficient length have little/NO similarity





noise=np.random.randn(npts)
y3n=y3+noise

noise=np.random.randn(npts)
y4n=y4+noise


plt.figure()
plt.plot(t,y3n,t,y4n)
plt.xlabel('Time ($s$)')
plt.ylabel('Amplitude ($Unit$)')
plt.grid('on')

sy3ny4n=signal.correlate(y3n,y4n)
t2=-1*t[::-1]
t2=np.append(t2, t[1:])

plt.figure()
plt.plot(t2,sy3ny4n)

# normalization

rel=np.median(sy3ny4n)/np.median(sytyt)

# plt.figure()
plt.plot(t2,sy3ny4n-rel*sytyt)

plt.figure()
plt.plot(t2,abs(sy3ny4n-rel*sytyt))






# two code sequences of different length

# y3 as before - original "transmitted" sequence (arbitrary rect + noise)
# y5 received sequence = noise + noisy transmitted sequence





y5=np.random.randn(3*npts)
noise=np.random.randn(npts)
y5=np.append(y5,y3+noise/2)    # injection of noise y3
noise=np.random.randn(npts)
y5=np.append(y5,noise);


t5=np.linspace(0, npts-1, 5*npts, endpoint=True) 

plt.figure()
plt.plot(t,y3n)
plt.plot(t5,y5)


sy5y3=signal.correlate(y5,y3)

ll=int((len(sy5y3)-1)/2)
ts = np.linspace(-ll, ll, 2*ll+1, endpoint=True)   # time vector


plt.figure()
plt.plot(ts,sy5y3)

# position of the original sequence in the received sequence

sy5y3max=np.amax(sy5y3)
sy5y3maxpos=np.argmax(sy5y3)

ts[sy5y3maxpos]
# offset in respect to the center of the received sequence





