
# spectrogram - Scipy Doc

from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(1234)

fs = 10e3    # 10kHz
N = 1e5     # no data points / samples
amp = 2*np.sqrt(2)
freq = 1234.0
noise_power = 0.001 * fs / 2
time = np.arange(N) / fs
x = amp*np.sin(2*np.pi*freq*time)   # sinusoid
x += np.random.normal(scale=np.sqrt(noise_power), size=time.shape)    # adding noise


# power spectral density - density -> normalization : amplitude / bin unit frequ. 

f, Pxx_den = signal.periodogram(x, fs)

plt.figure()
plt.semilogy(f, Pxx_den)
plt.ylim([1e-7, 1e2])
plt.xlabel('frequency [Hz]')
plt.ylabel('PSD [V**2/Hz]')

# power spectrum

f, Pxx_spec = signal.periodogram(x, fs, 'flattop', scaling='spectrum')
plt.figure()
plt.semilogy(f, np.sqrt(Pxx_spec))
plt.ylim([1e-4, 1e1])
plt.xlabel('frequency [Hz]')
plt.ylabel('Linear spectrum [V RMS]')
plt.show()


# Welch periodogram - PSD
# PSD estimate bay dividing the data into overlapping segments

f, Pxx_wel = signal.welch(x, fs, nperseg=1024)
plt.semilogy(f, Pxx_wel)
plt.ylim([0.5e-3, 1])
plt.xlabel('frequency [Hz]')
plt.ylabel('PSD [V**2/Hz]')
plt.show()





# PSD  Lomb-Scargle
# estimate for unevenly temporal samples - time series data

A = 2.
w = 1.
phi = 0.5 * np.pi
nin = 1000
nout = 100000
frac_points = 0.9 # Fraction of points to select

# Randomly select a fraction of an array with timesteps:

r = np.random.rand(nin)
x = np.linspace(0.01, 10*np.pi, nin)
x = x[r >= frac_points]

y = A * np.sin(w*x+phi)

# Define the array of frequencies for which to compute the periodogram:

f = np.linspace(0.01, 10, nout)

# Calculate Lomb-Scargle periodogram - not normalized 

pgram = signal.lombscargle(x, y, f, normalize=False)


plt.figure()
plt.subplot(2, 1, 1)
plt.plot(x, y, 'b+')
plt.subplot(2, 1, 2)
plt.plot(f, pgram)





