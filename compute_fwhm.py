import numpy as np

def compute_fwhm(distorted_spectrum, delta_freq):
    # t - массив временных значений
    # pulse - импульс, для которого необходимо вычислить FWHM

    # Вычисляем корректированный спектр
    corrected_spectrum = np.fft.fftshift(distorted_spectrum)
    corrected_spectrum = np.abs(corrected_spectrum)

    # Находим максимальное значение
    max_value = np.max(corrected_spectrum)

    # Находим индексы точек ниже половины максимального значения
    lower_half_indices = corrected_spectrum < max_value / 2.0
    first_index = np.min(np.where(lower_half_indices)[0])
    last_index = np.max(np.where(lower_half_indices)[0])

    # Находим соответствующие значения времени
    first_time = first_index * delta_freq
    last_time = last_index * delta_freq

    # Находим разницу между временными значениями
    fwhm = last_time - first_time

    return fwhm