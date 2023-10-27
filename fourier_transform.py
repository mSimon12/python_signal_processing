# 4 categories of signals:
#   - Aperiodic-Continuous  >> Fourier Transform
#   - Periodic-Continuous   >> Fourier Series
#   - Aperiodic-Discrete    >> Discrete Time Fourier Transform (DTFT)
#   - Periodic-Discrete     >> Discrete Fourier Transform (DFT)

import mysignals as sigs
import signal_processing as sp

if __name__ == '__main__':

    my_signal = sigs.InputSignal_1kHz_15kHz
    dft_rex, dft_imx = sp.calc_dft(my_signal)
    sp.plot_dft(my_signal, dft_rex, dft_imx)

    inverse_dft = sp.calc_inverse_dft(dft_rex, dft_imx)
    sp.plot_dft(inverse_dft, dft_rex, dft_imx)
