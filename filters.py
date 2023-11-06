from matplotlib import pyplot as plt
import numpy as np
import mysignals as sigs
from scipy import signal, fft
from scipy.signal import iirfilter, freqs


def median_filter_example():
    median_filter_output = signal.medfilt(sigs.InputSignal_1kHz_15kHz, 11)

    fig, ax = plt.subplots(2, sharex=True)
    fig.suptitle("Median filter")

    ax[0].plot(sigs.InputSignal_1kHz_15kHz, color="red")
    ax[0].set_title("Original signal")

    ax[1].plot(median_filter_output, color="blue")
    ax[1].set_title("Filterd signal")
    
    plt.show()

def lowpass_filter(input_signal, params, samp_freq):
    
    time_axis = np.linspace(0, 1.0, samp_freq + 1)
    
    # Get impulse for lowpass filter
    lowpass_impulse = signal.firwin(params['numtaps'], params['lpf_cutoff'], pass_zero='lowpass', fs=samp_freq)
    lowpass_output = signal.convolve(input_signal, lowpass_impulse)
    
    return (lowpass_impulse, lowpass_output)
    

def highpass_filter(input_signal, params, samp_freq):
    
    time_axis = np.linspace(0, 1.0, samp_freq + 1)
    
    # Get impulse for highpass filter
    highpass_impulse = signal.firwin(params['numtaps'], params['hpf_cutoff'], pass_zero='highpass', fs=samp_freq)
    highpass_output = signal.convolve(input_signal, highpass_impulse)
    
    return (highpass_impulse, highpass_output)


def bandpass_filter(input_signal, params, samp_freq):
    
    time_axis = np.linspace(0, 1.0, samp_freq + 1)
    
    # Get impulse for bandpass filter
    bandpass_impulse = signal.firwin(params['numtaps'], [params['bp_cutoff1'], params['bp_cutoff2']], pass_zero='bandpass', fs=samp_freq)
    bandpass_output = signal.convolve(input_signal, bandpass_impulse)
    
    return (bandpass_impulse, bandpass_output)


def fir_filter_example():
    ''' Example of Finite Impulse Response (FIR) filter application
    '''
    samp_freq = 2000
    t = np.linspace(0, 1.0, samp_freq + 1)
    sig_5Hz = np.sin(2*np.pi*5*t)
    sig_50Hz = np.sin(2*np.pi*50*t)
    sig_250Hz = np.sin(2*np.pi*250*t)
    
    sig_5Hz_50Hz_250Hz = sig_5Hz + sig_50Hz + sig_250Hz
    
    # Plot input signals
    fig, ax = plt.subplots(2, sharex=True)
    fig.suptitle("Input signals")

    ax[0].plot(sig_5Hz, color="red", label='5 Hz')
    ax[0].plot(sig_50Hz, color="blue", label='50 Hz')
    ax[0].plot(sig_250Hz, color="green", label= '250 Hz')
    ax[0].set_title("Isolated signals")
    ax[0].legend()

    ax[1].plot(sig_5Hz_50Hz_250Hz, color="blue")
    ax[1].set_title("Combined signal")
    
    # FIR parameters
    param = {}
    param['numtaps'] = 101
    param['lpf_cutoff'] = 7
    param['hpf_cutoff'] = 100
    param['bp_cutoff1'] = 40
    param['bp_cutoff2'] = 100
    
    lpf_out = lowpass_filter(sig_5Hz_50Hz_250Hz, param, samp_freq)
    hpf_out = highpass_filter(sig_5Hz_50Hz_250Hz, param, samp_freq)
    bpf_out = bandpass_filter(sig_5Hz_50Hz_250Hz, param, samp_freq)
    
    plt.figure()
    plt.plot(lpf_out[0], color="r", label='Impulse Low Pass filter')
    plt.plot(hpf_out[0], color="m", label='Impulse High Pass filter')
    plt.plot(bpf_out[0], color="b", label='Impulse Band Pass filter')
    plt.legend()
    plt.title("Impulse response")
    
    fig, ax = plt.subplots(4,2)
    fig.suptitle("Lowpass filter")

    ax[0,0].plot(sig_5Hz_50Hz_250Hz, color="green")
    ax[0,0].set_title("Input signal")

    ax[1,0].plot(lpf_out[1], color="blue")
    ax[1,0].set_title("Lowpass output signal")
    
    ax[2,0].plot(hpf_out[1], color="blue")
    ax[2,0].set_title("Highpass output signal")
    
    ax[3,0].plot(bpf_out[1], color="blue")
    ax[3,0].set_title("Bandpass output signal") 
    
    # FFT analysis from Signals
    input_fft = abs(fft.fft(sig_5Hz_50Hz_250Hz))
    lpf_fft = abs(fft.fft(lpf_out[1]))
    hpf_fft = abs(fft.fft(hpf_out[1]))
    bpf_fft = abs(fft.fft(bpf_out[1]))
    
    ax[0,1].plot(input_fft[:int(len(input_fft)/2)], color="green")
    ax[0,1].set_title("Input signal FFT")

    ax[1,1].plot(lpf_fft[:int(len(lpf_fft)/2)], color="blue")
    ax[1,1].set_title("Lowpass output signal FFT")
    
    ax[2,1].plot(hpf_fft[:int(len(hpf_fft)/2)], color="blue")
    ax[2,1].set_title("Highpass output signal FFT")
    
    ax[3,1].plot(bpf_fft[:int(len(bpf_fft)/2)], color="blue")
    ax[3,1].set_title("Bandpass output signal FFT") 
    
    plt.tight_layout()
    
    plt.show()


def iir_filter_example():
    ''' Example of Infinite Impulse Response (IIR) filter application also called Recursive Filters
    '''
    
    ###################################################
    # Computing the frequency response
    b = signal.firwin(80, 0.5, window=('kaiser', 8))
    
    #Compute the frequency response of a digital filter.
    w,h = signal.freqz(b)
    
    plt.semilogy(w, np.abs(h), 'g')
    plt.ylabel('Amplitude (dB)')
    plt.xlabel('Frequency (rad/sample)')
    
    ###################################################
    #Computing frequency response from Chebyshev Filter
    plt.figure()
    
    f_order = 4         #The order of the filter
    window = [1, 10]    #Critical frequencies
    rp = 1              #Maximum ripple
    rs = 60             #Minimum attenuation
    b,a = iirfilter(f_order, window, rp, rs, analog=True, ftype='cheby1')
    
    #Compute frequency response of analog filter
    w,h = freqs(b,a, worN=np.logspace(-1, 2, 1000))
    
    plt.semilogx(w, np.abs(h), 'g')
    plt.ylabel('Amplitude (dB)')
    plt.xlabel('Frequency (rad/seconds)')
    plt.grid()
    
    ###################################################
    #Creating a Butterworth low pass filter
    plt.figure()
    b,a = signal.butter(4, 100, 'low', analog=True)
    w,h = freqs(b,a)    
    
    plt.plot(w, 20*np.log10(abs(h)))
    plt.xscale('log')
    
    plt.title('Butterworth filter (Lowpass)  frequency response')
    plt.ylabel('Amplitude (dB)')
    plt.xlabel('Frequency (rad/seconds)')
    plt.grid()
    
    ###################################################
    fig, ax = plt.subplots(2,1, sharex=True)

    #Creating a type 1 Chebyshev Lowpass Filter
    b,a = signal.cheby1(4, 5, 100, 'low', analog=True)
    w,h = freqs(b,a)    
    
    ax[0].plot(w, 20*np.log10(abs(h)))
    ax[0].set_xscale('log')
    
    ax[0].set_title('Chebyshev type 1 filter (Lowpass) frequency response')
    ax[0].set_ylabel('Amplitude (dB)')
    ax[0].grid()
    ax[0].axhline(-5, color='green') # rs
    ax[0].axvline(100, color='green') # rp

    #Creating a type 2 Chebyshev Lowpass Filter
    b,a = signal.cheby2(4, 40, 100, 'low', analog=True)
    w,h = freqs(b,a)    
    
    ax[1].plot(w, 20*np.log10(abs(h)))
    ax[1].set_xscale('log')
    
    ax[1].set_title('Chebyshev type 2 filter (Lowpass) frequency response')
    ax[1].set_ylabel('Amplitude (dB)')
    ax[1].set_xlabel('Frequency (rad/seconds)')
    ax[1].grid()
    ax[1].axhline(-40, color='green') # rs
    ax[1].axvline(100, color='green') # rp


    ###################################################
    #Creating a Elliptic lowpass filter
    plt.figure()
    b,a = signal.ellip(4, 5, 40, 100, 'low', analog=True)
    w,h = freqs(b,a)    
    
    plt.plot(w, 20*np.log10(abs(h)))
    plt.xscale('log')
    
    plt.title('Elliptic filter (Lowpass) frequency response')
    plt.ylabel('Amplitude (dB)')
    plt.xlabel('Frequency (rad/seconds)')
    plt.grid()
    plt.axhline(-40, color='g') # rs
    plt.axhline(-5, color='m') # rp
    plt.axvline(100, color='r') # cutoff
    
    ###################################################
    #Creating a Bessel lowpass filter
    plt.figure()
    b,a = signal.butter(4, 100, 'low', analog=True)
    w,h = freqs(b,a)    
    plt.plot(w, 20*np.log10(abs(h)), color='m', label= 'Butterworth')

    b,a = signal.bessel(4, 100, 'low', analog=True)
    w,h = freqs(b,a)    
    plt.plot(w, 20*np.log10(abs(h)), color='g', label= 'Bessel')

    plt.xscale('log')
    plt.title('Butterworth x Bessel filters (Lowpass) frequency response')
    plt.ylabel('Amplitude (dB)')
    plt.xlabel('Frequency (rad/seconds)')
    plt.grid()
    plt.axvline(100, color='r') # cutoff
    plt.legend()

    plt.show()

if __name__ == '__main__':
    # median_filter_example()
    # fir_filter_example()
    iir_filter_example()