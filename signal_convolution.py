import numpy as np
from matplotlib import pyplot as plt
import mysignals as sigs
from scipy import signal
import signal_processing as sp

def main():

    #### CONVOLUTION
    output_signal1 = signal.convolve(sigs.InputSignal_1kHz_15kHz, sigs.Impulse_response)
    # output_signal1 = conv.convolve(sigs.InputSignal_1kHz_15kHz, sigs.Impulse_response)

    # Plot 1
    fig1, ax1 = plt.subplots(3, sharex=True)

    fig1.suptitle("Convolution input signals")
    ax1[0].plot(sigs.InputSignal_1kHz_15kHz, color='r')
    ax1[0].set_title("1 kHz + 15kHz signal")

    ax1[1].plot(sigs.Impulse_response, color='g')
    ax1[1].set_title("Inspulse signal")


    ax1[2].plot(output_signal1, color='b')
    ax1[2].set_title("Convolved signal")

    #Plot 2
    t = np.linspace(0, 1.0, 100001)    #Generate 1001 points between 0 and 1

    sig_1khz = np.sin(2*np.pi*1000*t)
    sig_15khz = np.sin(2*np.pi*15000*t)
    input_signal = sig_1khz + sig_15khz
    
    output_signal2 = sp.convolve(input_signal, sigs.Impulse_response)

    fig2, ax2 = plt.subplots(5, sharex=True)

    fig2.suptitle("Convolution input signals")
    ax2[0].plot(sig_1khz, color='k')
    ax2[0].set_title("1 kHz signal")

    ax2[1].plot(sig_15khz, color='m')
    ax2[1].set_title("15kHz signal")

    ax2[2].plot(input_signal, color='r')
    ax2[2].set_title("1kHz + 15kHz signal")

    ax2[3].plot(sigs.Impulse_response, color='g')
    ax2[3].set_title("Inspulse signal")

    ax2[4].plot(output_signal2, color='b')
    ax2[4].set_title("Convolved signal")

    ax2[0].set_xlim(0,500)
    fig2.tight_layout()


    #### DECONVOLUTION
    deconv_signal, remainder = signal.deconvolve(output_signal1, sigs.Impulse_response)

    fig3, ax3 = plt.subplots(3, sharex=True)

    fig3.suptitle("Deconvolution input signals")
    ax3[0].plot(output_signal1, color='k')
    ax3[0].set_title("1 kHz signal")

    ax3[1].plot(sigs.Impulse_response, color='g')
    ax3[1].set_title("Inspulse signal")

    ax3[2].plot(sigs.InputSignal_1kHz_15kHz, color='b', label='Initial signal')
    ax3[2].plot(deconv_signal, color='r', label='Processed signal')
    ax3[2].set_title("Deconvolved signal x Input signal")

    ax3[2].legend()

    plt.show()

if __name__ == '__main__':
    main()