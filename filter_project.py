'''
    Implementation of all steps for developing a Butterworth filter
'''
from matplotlib import pyplot as plt
import numpy as np
from scipy.signal import butter, lfilter, freqz


def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = fs/2
    low = lowcut/nyq
    high = highcut/nyq
    b,a = butter(order, [low, high], btype='band')

    return b,a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y


def run():
    fs = 5000
    low = 500
    high = 1250

    plt.figure()

    for order in [3,5,6,9]:
        b, a = butter_bandpass(low, high, fs, order)
        w, h = freqz(b, a, worN=2000)
        plt.plot((fs*0.5/np.pi)*w, abs(h), label = f"order{order}")

    plt.xscale('log')
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Gain")
    plt.grid()
    plt.legend(loc="best")    
    
    # Test Filter 


if __name__ == "__main__":
    run()
