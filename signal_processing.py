
import numpy as np
import math
from matplotlib import pyplot as plt


def convolve(signal1, signal2):
    output = np.zeros(len(signal1) + len(signal2))
    for n in range(0,len(signal1)):
        for m in range(0,len(signal2)):
            output[n+m] += signal1[n] * signal2[m]
    
    return output


def deconvolve(signal, divisor):
    pass


class Fourier_Transform(object):

    def __init__(self) -> None:
        self.input_signal = None
        self.rex_signal = []
        self.imx_signal = []


    def set_sample_rate(self, rate):
        self.sample_rate = rate


    def set_input_signal(self, signal):
        self.input_signal = signal


    def calc_dft(self):
        if not self.input_signal:
            print("This call requires a signal input signal defined with 'set_input_signal(signal)")
            return

        print("Calculating Discrete Fourier Transform ...")

        for j in range(int(len(self.input_signal)/2)):
            self.rex_signal.append(0)
            self.imx_signal.append(0)

        for k in range(len(self.rex_signal)):
            for i in range(len(self.input_signal)):
                self.rex_signal[k] = self.rex_signal[k] + self.input_signal[i]*math.cos(2*math.pi*k*i/len(self.input_signal))
                self.imx_signal[k] = self.imx_signal[k] - self.input_signal[i]*math.sin(2*math.pi*k*i/len(self.input_signal))


    def calc_dft_mag(self):
        signal_magnitude = []
        #Calculate DFT magnitudes
        for x in range(len(self.rex_signal)):
            signal_magnitude.append(math.sqrt(math.pow(self.rex_signal[x],2) + math.pow(self.imx_signal[x],2)))
        
        return signal_magnitude


    def plot_dft(self):
        if not self.rex_signal or not self.imx_signal:
            print("This call requires Fourier Transform to be executed first, so execute 'calc_dft()")
            return

        sig_mag = self.calc_dft_mag()

        fig, ax = plt.subplots(4, sharex=True)
        fig.suptitle("Discrete Fourier Transform (DFT)")

        ax[0].plot(self.input_signal, color='red')
        ax[0].set_title("Input Signal")

        ax[1].plot(self.rex_signal, color='green')
        ax[1].set_title("Frequency Domain (real part)")

        ax[2].plot(self.imx_signal, color='red')
        ax[2].set_title("Frequency Domain (imaginary part)")
        
        ax[3].plot(sig_mag, color='black')
        ax[3].set_title("Magnitude")

        plt.show()