import numpy as np


def dispersion(spectrum, delta_t, t, pulse, b, c):
    # pulse - импульс, который необходимо пропустить через среду
    # b - дисперсия
    # c - скорость света в вакууме

    # расчет частоты в спектре и фазовой скорости
    lambda_ = np.fft.fftfreq(len(pulse), d=delta_t)
    v_phase = np.sqrt(c ** 2 + (b ** 2 * (lambda_) ** 2))

    # умножение на функцию фазовой скорости
    distorted_spectrum = spectrum * np.exp(-1j * 2 * np.pi * v_phase * t)

    # обратное преобразование Фурье
    distorted_pulse = np.fft.ifftshift(np.fft.ifft(distorted_spectrum))

    return distorted_pulse