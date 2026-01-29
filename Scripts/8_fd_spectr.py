# %reset -f


import numpy as np
import matplotlib.pyplot as plt


# -> HW    

# car passible sound shift ~ its radial velocity component

# start position and velocity of a car

v=20 # km/h
vm=v* 1000/(60*60) # m/s
x1=-100 

y1=1
y2=50

t=np.linspace(0,10,101)
x=x1+v*t
y1v=np.tile(y1,len(x))  # constant y
y2v=np.tile(y2,len(x))

alpha1=np.arctan(x/y1v)
alpha2=np.arctan(x/y2v)

vr1=alpha1/(np.pi/2)*vm
vr2=alpha2/(np.pi/2)*vm

plt.figure()
plt.subplot(1,2,1)
plt.plot(t,x,'.')   # position x / t
plt.xlabel('t / s')
plt.ylabel('position x')
plt.subplot(1,2,2)
plt.plot(t,np.sqrt(x**2+y1**2),'.') # radial position / t for scen.1
plt.plot(t,np.sqrt(x**2+y2**2),'.') # radial position / t for scen.2
plt.xlabel('t / s')
plt.ylabel('radial distance')

plt.figure()
plt.plot(t,vr1)
plt.plot(t,vr2)
plt.xlabel('t / s')
plt.ylabel('radial velocity / m/s')





# %reset -f


import numpy as np
import matplotlib.pyplot as plt

# airplane

frad=50e6   # radar frequency
c=3e8
wl=c/frad


theta=np.linspace(50,140,91)   #  angle   50...140°

vs=800 # km/h
vs=vs* 1000/(60*60) #  m/s (source vel.)

# Doppler-frequ. - = radial velocity * (radio, radar,..) frequency
fd=np.zeros(len(theta));

for kk in range(0,len(theta)):  
    fd[kk]=frad * (np.sqrt(1- ((vs*2)**2 / c**2 ))) / ( 1- (vs*2)/c*np.cos(theta[kk]/180*np.pi));
    

# relative Doppler-frequ
frel=fd-frad;

# min. height/range
h=12 # km

r=h/np.cos((90-theta)/180*np.pi)
    
plt.figure()
plt.plot(frel,r)
plt.scatter(frel,r,[30],theta)
plt.xlabel('df /Hz')
plt.ylabel('range /km')
plt.colorbar()
plt.title('airplane Doppler shift - color: zenith angle')








# equivalent for the atmosphere
# "air parcels" drifting with winds @ 80km can be about +/-100m/s !


# frad=50e6   # radar frequency
frad=3.2e6   # radar frequency
c=3e8
wl=c/frad


theta=np.linspace(50,140,91)

#vs=360 # km/h
#vs=vs* 1000/(60*60) #  m/s (source vel.)

vs=100 #  m/s (source vel.)

# Doppler-frequ.
fd=np.zeros(len(theta));

for kk in range(0,len(theta)):  
    fd[kk]=frad * (np.sqrt(1- ((vs*2)**2 / c**2 ))) / ( 1- (vs*2)/c*np.cos(theta[kk]/180*np.pi));
    

# relative Doppler-frequ
frel=fd-frad;

# min. height/range
h=85 # km

r=h/np.cos((90-theta)/180*np.pi)
    
plt.figure()
plt.plot(frel,r)
plt.scatter(frel,r,[30],theta)
plt.xlabel('df /Hz')
plt.ylabel('range /km')
plt.colorbar
plt.colorbar()
