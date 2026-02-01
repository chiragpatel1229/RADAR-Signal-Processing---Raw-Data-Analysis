

# %reset -f

import matplotlib.pyplot as plt
plt.style.use('classic')

# %matplotlib inline
import numpy as np

x = np.linspace(0, 10, 1000)

I = np.sin(x) * np.cos(x[:, np.newaxis])  # pseudo index, temporary addition of an axis
                                        # vector -> matrix

plt.figure()

plt.imshow(I)

plt.colorbar();



plt.figure()
plt.pcolor(x,x,I**2)
plt.colorbar();
plt.clim(-.25,1.25)      # color (bar/map) axis limits


Z = np.random.rand(6, 10)

plt.figure()
plt.pcolor(Z)
plt.colorbar()






def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')







x=np.linspace(1,10,10)
y=np.linspace(11,20,10)
z1= np.random.rand(10, 10)
z2= np.random.rand(10, 10)
z3= np.random.rand(10, 10)
z4= np.random.rand(10, 10)


fig , ( (ax1,ax2) , (ax3,ax4)) = plt.subplots(2, 2,sharex = True,sharey=True)
z1_plot = ax1.pcolor(x,y,z1)
plt.colorbar(z1_plot,ax=ax1)
z2_plot = ax2.pcolor(x,y,z2)
plt.colorbar(z1_plot,ax=ax2)
z3_plot = ax3.pcolor(x,y,z3)
plt.colorbar(z1_plot,ax=ax3)
z4_plot = ax4.pcolor(x,y,z4)
plt.colorbar(z1_plot,ax=ax4)




