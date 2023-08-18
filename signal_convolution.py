import numpy as np
from matplotlib import pyplot as plt
import mysignals as sigs
from scipy import signal


class Convolution(object):

    def __init__(self) -> None:
        self.signals = {}

    def add_input_signal(self, key, signal):
        if key not in self.signals.keys:
            self[key] = signal
        else:
            print(f"Key '{key}' already used.")
    
    def del_input_signal(self, key):
        if key in self.signals.keys:
            self.signals.pop(key)
        else:
            print(f"Key '{key}' undefined.")
    
    def convolve_all(self):
        pass

    def convolve(self, signal1, signal2):
        output = np.zeros(len(signal1) + len(signal2))
        for n in range(0,len(signal1)):
            for m in range(0,len(signal2)):
                output[n+m] += signal1[n] * signal2[m]
        
        return output



if __name__ == '__main__':

    conv = Convolution()

    # output_signal = signal.convolve(sigs.InputSignal_1kHz_15kHz, sigs.Impulse_response, mode='same')
    output_signal = conv.convolve(sigs.InputSignal_1kHz_15kHz, sigs.Impulse_response)

    fig, ax = plt.subplots(3, sharex=True)

    fig.suptitle("Convolution input signals")
    ax[0].plot(sigs.InputSignal_1kHz_15kHz, color='r')
    ax[0].set_title("1 kHz + 15kHz signal")

    ax[1].plot(sigs.Impulse_response, color='g')
    ax[1].set_title("Inspulse signal")


    ax[2].plot(output_signal, color='b')
    ax[2].set_title("Convolved signal")

    plt.show()