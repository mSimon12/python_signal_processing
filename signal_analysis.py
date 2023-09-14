from matplotlib import pyplot as plt
import numpy as np

# First difference is for discret signals as Derivate is for continuous signals
def compute_first_difference(signal):
    output_signal = []
    for i in range(1,len(signal)):
        output_signal.append(signal[i] - signal[i-1])
    return output_signal


## Running sum is for discret signals as Integral is for continuous signals
# It is capable of filtering higher frequency noises in the signal (we can then check frequency wih crossing zero algorithms)
def compute_running_sum(signal):
    output_signal = [signal[0]]
    for i in range(1,len(signal)):
        output_signal.append(signal[i] + output_signal[i-1])
    return output_signal


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


## Verify the data First difference and Running sum
fig2, ax2 = plt.subplots(3, sharex=True)

fig.suptitle("First difference & Running sum")
ax2[0].plot(sig_5hz_250hz, color='r')
ax2[0].set_title("Signal")

ax2[1].plot(compute_first_difference(sig_5hz_250hz), color='b', label='Own algorithm')
ax2[1].plot(np.diff(sig_5hz_250hz), color='g', label='Numpy algorithm')
ax2[1].set_title("First difference")
ax2[1].legend()

ax2[2].plot(compute_running_sum(sig_5hz_250hz), color='b', label='Own algorithm')
ax2[2].plot(np.cumsum(sig_5hz_250hz), color='g', label='Numpy algorithm')
ax2[2].set_title("Running sum")
ax2[2].legend()

plt.show()