
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


def calc_dft(input_signal):
    # print("Calculating Discrete Fourier Transform ...")
    rex_signal = []
    imx_signal = []

    for j in range(int(len(input_signal)/2)):
        rex_signal.append(0)
        imx_signal.append(0)

    for k in range(len(rex_signal)):
        for i in range(len(input_signal)):
            rex_signal[k] = rex_signal[k] + input_signal[i]*math.cos(2*math.pi*k*i/len(input_signal))
            imx_signal[k] = imx_signal[k] - input_signal[i]*math.sin(2*math.pi*k*i/len(input_signal))

    return (rex_signal, imx_signal)

def calc_inverse_dft(rex_source, imx_source):
    # print("Calculating Inverse Discrete Fourier Transform ...")
    idft_signal = []
    for i in range(len(rex_source)*2):
        idft_signal.append(0)

    for x in range(len(rex_source)):
        rex_source[x] = rex_source[x]/len(rex_source)
        imx_source[x] = imx_source[x]/len(rex_source)

    for k in range(len(rex_source)):
        for j in range(len(idft_signal)):
            idft_signal[j] = idft_signal[j] + rex_source[k] * math.cos(2*math.pi*k*j/len(idft_signal))
            idft_signal[j] = idft_signal[j] + imx_source[k] * math.sin(2*math.pi*k*j/len(idft_signal))

    return idft_signal


def calc_dft_mag(rex_source, imx_source):
    signal_magnitude = []
    #Calculate DFT magnitudes
    for x in range(len(rex_source)):
        signal_magnitude.append(math.sqrt(math.pow(rex_source[x],2) + math.pow(imx_source[x],2)))
    
    return signal_magnitude


def plot_dft(time_domain_signal, freq_real_part, freq_imaginary_part):

    sig_mag = calc_dft_mag(freq_real_part, freq_imaginary_part)

    fig, ax = plt.subplots(4, sharex=True)
    fig.suptitle("Discrete Fourier Transform (DFT)")

    ax[0].plot(time_domain_signal, color='red')
    ax[0].set_title("Time Domain Signal")

    ax[1].plot(freq_real_part, color='green')
    ax[1].set_title("Frequency Domain (real part)")

    ax[2].plot(freq_imaginary_part, color='red')
    ax[2].set_title("Frequency Domain (imaginary part)")
    
    ax[3].plot(sig_mag, color='black')
    ax[3].set_title("Magnitude")

    plt.show()