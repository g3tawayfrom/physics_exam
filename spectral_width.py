import numpy as np

def spectral_width(pulse, delta_t, lambda_0):
    # pulse - одномерный массив значений сигнала во временной области
    # delta_t - длительность импульса
    # lambda_0 - несущая длина волны

    # расчет и получение амплитудного спектра
    spectrum = np.fft.fft(pulse)
    amplitude_spectrum = np.abs(spectrum)

    # нахождений максимального и половины от максимального значения амплитуды
    max_amplitude = np.max(amplitude_spectrum)
    half_max_amplitude = max_amplitude / 2

    idx = np.argwhere(amplitude_spectrum >= half_max_amplitude)

    # вычисления FWHM в единицах частоты и длины волны
    fwhm = (idx[-1] - idx[0]) * (1 / delta_t) / len(pulse)
    spectral_width = fwhm / (2 * np.sqrt(2 * np.log(2))) * lambda_0**2

    return spectral_width