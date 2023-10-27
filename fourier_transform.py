# 4 categories of signals:
#   - Aperiodic-Continuous  >> Fourier Transform
#   - Periodic-Continuous   >> Fourier Series
#   - Aperiodic-Discrete    >> Discrete Time Fourier Transform (DTFT)
#   - Periodic-Discrete     >> Discrete Fourier Transform (DFT)

import mysignals as sigs
from scipy import fft
from matplotlib import pyplot as plt
from timeit import default_timer as timer
import signal_processing as sp

def dft_example():
    my_signal = sigs.InputSignal_1kHz_15kHz
    dft_rex, dft_imx = sp.calc_dft(my_signal)
    sp.plot_dft(my_signal, dft_rex, dft_imx)
    inverse_dft = sp.calc_inverse_dft(dft_rex, dft_imx)
    sp.plot_dft(inverse_dft, dft_rex, dft_imx)

    my_ecg_signal = sigs.ecg_signal
    dft_rex, dft_imx = sp.calc_dft(my_ecg_signal)
    sp.plot_dft(my_ecg_signal, dft_rex, dft_imx)
    inverse_dft = sp.calc_inverse_dft(dft_rex, dft_imx)
    sp.plot_dft(inverse_dft, dft_rex, dft_imx)


def fft_example():
    # Fast Fourier Transfortm (FFT)
    freq_domain_signal = fft.fft(my_ecg_signal)
    time_domain_signal = fft.ifft(freq_domain_signal)
    magnitude = abs(freq_domain_signal)

    fig, ax = plt.subplots(4, sharex=True)
    fig.suptitle("Fast Fourier Transform Scipy")

    ax[0].plot(my_ecg_signal, color='red')
    ax[0].set_title("Time Domain (Input Signal)")

    ax[1].plot(freq_domain_signal, color='blue')
    ax[1].set_title("Frequency Domain (FFT)")
    
    ax[2].plot(magnitude, color='green')
    ax[2].set_title("Magnitude")
    
    ax[3].plot(time_domain_signal, color='red')
    ax[3].set_title("Time Domain (FFT)")

    plt.show()


def fft_dft_time_comparison():
    # Performance comparison FFT x DFT
    signal_for_comparison = sigs.ecg_signal

    start = timer()
    sp.calc_dft(signal_for_comparison)
    end = timer()
    dft_time = end - start

    start = timer()
    fft.fft(signal_for_comparison)
    end = timer()
    fft_time = end - start

    print(f"Time for calculating DFT: {dft_time:.6f} seconds")
    print(f"Time for calculating FFT: {fft_time:.6f} seconds")


if __name__ == '__main__':

    # dft_example()
    # fft_example()
    fft_dft_time_comparison()