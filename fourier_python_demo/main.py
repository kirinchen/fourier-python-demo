import numpy as np
import matplotlib.pyplot as plt
import scipy.constants
from scipy.fftpack import fft
from scipy.fftpack import ifft

from fourier_python_demo import data_supplier_service

if __name__ == "__main__":

    sample_num = 2000  # Sampling points
    total_time = 2  # Sampling number
    sampling_rate = sample_num / total_time  # 取樣頻率

    # fs = [(20, 12), (100, 5), (250, 2)] # sin 波的頻率與振幅組合。 (Hz, Amp)
    fs = []  # sin 波的頻率與振幅組合。 (Hz, Amp)
    noise_mag = 2

    time = np.linspace(0, total_time, sample_num, endpoint=False)
    # vib_data = [amp * np.sin(2 * scipy.constants.pi * hz * time) for hz, amp in fs]
    vib_data = []
    for hz, amp in fs:
        vobj = amp * np.sin(2 * scipy.constants.pi * hz * time)
        vib_data.append(vobj)
    vib_data.append(data_supplier_service.gen_x_pow())
    # vib_data = [amp * np.sin(2 * scipy.constants.pi * hz * time) for hz, amp in fs]

    # max_time = int(sample_num / 4)
    max_time = int(sample_num / 1)

    plt.figure(figsize=(12, 8))
    # Show seperated signal
    for idx, vib in enumerate(vib_data):
        plt.subplot(2, 2, idx + 1)
        plt.plot(time[0:max_time], vib[0:max_time])
        plt.xlabel('time')
        plt.ylabel('vib_' + str(idx))
        plt.ylim((-24, 24))

    vib = sum(vib_data) + np.random.normal(0, noise_mag, sample_num)  # Add noise

    plt.subplot(2, 2, 4)
    plt.plot(time[0:max_time], vib[0:max_time])
    plt.xlabel('time')
    plt.ylabel('vib(with noise)')
    plt.ylim((-24, 24))
    plt.show()

    fd = np.linspace(0.0, sampling_rate, int(sample_num), endpoint=False)

    vib_fft = fft(vib)
    mag = 2/sample_num * np.abs(vib_fft) # Magnitude

    plt.plot(fd[0:int(sample_num/2)], mag[0:int(sample_num/2)])
    plt.xlabel('Hz')
    plt.ylabel('Mag')
    plt.show()

    vib_re = np.real(ifft(vib_fft))  # Real part of complex number

    plt.plot(time[0:max_time], vib_re[0:max_time])
    plt.ylim((-24, 24))
    plt.show()