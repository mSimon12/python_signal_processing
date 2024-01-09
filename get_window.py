from matplotlib import pyplot as plt
import numpy as np
from scipy import signal
from scipy.fftpack import fft, fftshift

def run():
    filter_windows = {}
    filter_windows['triangular'] = signal.get_window('triang', 30)
    filter_windows['kaiser1'] = signal.get_window(('kaiser', 4.0), 30)
    filter_windows['kaiser2'] = signal.get_window(4.0, 30)
    filter_windows['hamm'] = signal.get_window('hamming', 30)
    filter_windows['black'] = signal.get_window('blackman', 30)
    
    fig, ax = plt.subplots(5,1, sharex=True)
    fig.suptitle("Filter Windows")

    plt_idx = 0
    for win in filter_windows:
        ax[plt_idx].plot(filter_windows[win])
        ax[plt_idx].set_title(f"{win} window")
        
        plt_idx +=1
    
    fig.tight_layout()
    
    ################################################
    ''' Windows
        Barlett-Hann / Bartlett / Blackman / Blackman-Harris
        Bohman / Boxcar / Chebyshev / Cosine / Flattop
        Gaussian / Hamming / Hanning / Kaiser / Nuttal
        Parzen / Slepian / Triangular
    '''
    # window = signal.barthann(50)
    # window = signal.bartlett(50)
    # window = signal.blackman(50)
    # window = signal.blackmanharris(50)
    # window = signal.bohman(50)
    window = signal.chebwin(50, at=100)
    
    A = fft(window, 2048) / (len(window)/2.0)
    freq = np.linspace(-0.5, 0.5, len(A))
    response = 20 * np.log10(np.abs(fftshift(A/abs(A).max())))
    
    fig, ax = plt.subplots(1,2)
    ax[0].plot(window)
    ax[0].set_title("Barlett-Hann Window")
    ax[0].set_xlabel("Sample")
    ax[0].set_ylabel("Amplitude")
    
    ax[1].plot(freq, response)
    ax[1].set_title("Frequency response of the Barlett-Hann Window")
    ax[1].set_xlabel("Normalized frequency (cycles/rad)")
    ax[1].set_ylabel("Normalized Magnitude (dB)")
    
    
    
    plt.show()
    
if __name__ == "__main__":
    run()