# 4 categories of signals:
#   - Aperiodic-Continuous  >> Fourier Transform
#   - Periodic-Continuous   >> Fourier Series
#   - Aperiodic-Discrete    >> Discrete Time Fourier Transform (DTFT)
#   - Periodic-Discrete     >> Discrete Fourier Transform (DFT)

import numpy as np
from matplotlib import pyplot as plt
import mysignals as sigs
from scipy import signal
from signal_processing import Fourier_Transform


if __name__ == '__main__':

    my_signal = sigs.InputSignal_1kHz_15kHz
    fourier = Fourier_Transform()
    fourier.set_input_signal(my_signal)
    fourier.calc_dft()
    fourier.plot_dft()