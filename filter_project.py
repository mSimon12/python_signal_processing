'''
    Implementation of all steps for developing a Butterworth filter
'''
from matplotlib import pyplot as plt
import numpy as np
from scipy.signal import butter, lfilter, freqz
import mysignals as sigs


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

    fig, ax = plt.subplots(2,1)

    for order in [3,5,6,9]:
        b, a = butter_bandpass(low, high, fs, order)
        w, h = freqz(b, a, worN=2000)
        ax[0].plot((fs*0.5/np.pi)*w, abs(h), label = f"order{order}")

    ax[0].set_xscale('log')
    ax[0].set_xlabel("Frequency (Hz)")
    ax[0].set_ylabel("Gain")
    ax[0].grid()
    ax[0].legend(loc="best")    
    
    # Test Filter 
    sample_time = 0.05
    t = np.linspace(0, sample_time, int(sample_time*fs))
    
    a = 0.5
    f0 = 500 
    main_sig = a*np.sin(2*np.pi*t*f0)
    noise1 = np.cos(2*np.pi*t*100)
    noise2 = 100*t
    sys_input = main_sig + noise1 + noise2

    
    ax[1].plot(t, sys_input, label = f"Filter input")

    for order in [3,5,6,9]:        
        sys_output = butter_bandpass_filter(sys_input, low, high, fs, order)
        ax[1].plot(t, sys_output, label = f"Filter Output (order{order})")
    
    ax[1].hlines([-a, a], 0, sample_time, "k", linestyle="--")
    
    ax[1].set_xlabel("Time (s)")
    ax[1].set_ylabel("Value")
    ax[1].grid()
    ax[1].legend(loc="best")    
    
    
    plt.show()


if __name__ == "__main__":
    run()
