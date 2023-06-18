import numpy as np
import matplotlib.pyplot as plt
from spectral_width import spectral_width
from dispersion import dispersion
from compute_fwhm import compute_fwhm
from signal import signal


delta_t = 10e-6 # длительность импульса
lambda_0 = 1.5e-6 # несущая длина волны

t = np.arange(-30*delta_t, 30*delta_t, 0.1*delta_t) # генерация массива временных значений для импульса

spectrum = np.sinc(t / delta_t) * np.exp(-1j * 2 * np.pi * lambda_0 * t) # расчет спектра

pulse = np.fft.ifftshift(np.fft.ifft(spectrum)) # преобразование сигнала обратно во временную область

# Вычисление спектральной ширины пакета для импульса
sw = spectral_width(pulse, delta_t, lambda_0)
print("Спектральная ширина пакета:", sw*1e+6, "мкм")

b_values = [1, 10, 100]
c = 3e8

for b in b_values:
    distorted_pulse = dispersion(spectrum, delta_t, t, pulse, b, c)
    fwhm = compute_fwhm(distorted_pulse, abs(spectrum[1]-spectrum[2]))
    print(f"b = {b}, FWHM = {fwhm:.3e} s")
    plt.plot(t, np.abs(spectrum) ** 2, label='Original')
    plt.plot(t, np.abs(distorted_pulse) ** 2, label=f'Distorted. b = {b}')
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.show()

    signal(distorted_pulse, fwhm)
