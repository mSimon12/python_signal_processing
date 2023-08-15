from matplotlib import pyplot as plt
from scipy import signal
import numpy as np

t = np.linspace(0, 1.0, 2001)    #Generate 2001 points between 0 and 1

sig_5hz = np.sin(2*np.pi*5*t)
sig_250hz = np.sin(2*np.pi*250*t)
sig_5hz_250hz = sig_5hz + sig_250hz

signal_mean = np.mean(sig_5hz_250hz)
signal_var = np.var(sig_5hz_250hz)
signal_std = np.std(sig_5hz_250hz)

print("The mean value from the signal combination is ", signal_mean)
print("The variance from the signal combination is ", signal_var)
print("The standard deviation from the signal combination is ", signal_std)

fig, ax = plt.subplots(3, sharex=True)

fig.suptitle("Multiple plots")
ax[0].plot(sig_5hz, color='r')
ax[0].set_title("5 Hz signal")

ax[1].plot(sig_250hz, color='g')
ax[1].set_title("250 Hz signal")

ax[2].plot(sig_5hz_250hz, color='b')
ax[2].set_title("Combined signal")
plt.show()