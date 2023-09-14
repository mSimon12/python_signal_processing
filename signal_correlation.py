import numpy as np
from matplotlib import pyplot as plt
import mysignals as sigs
from scipy import signal

signal1 = sigs.InputSignal_1kHz_15kHz
signal2 = sigs.Impulse_response

correlation_output = signal.correlate(signal1, signal2, mode='same')
convolution_output = signal.convolve(signal1, signal2, mode='same')

# Plot 1
fig1, ax1 = plt.subplots(3, sharex=True)

fig1.suptitle("Convolution x Correlation")    

ax1[0].plot(signal1, color='r')
ax1[0].plot(signal2, color='b')
ax1[0].set_title("Inputs")

ax1[1].plot(correlation_output, color='m')
ax1[1].set_title("Convolution")

ax1[2].plot(convolution_output, color='g')
ax1[2].set_title("Correlation")

plt.show()