import numpy as np

def signal(distorted_pulse, t_distorted):
    message = "exam"

    # Кодирование сообщения
    coded_message = np.zeros(1024)
    for i, char in enumerate(message):
        coded_message[100*i+50] = ord(char)

    # Моделирование передачи сообщения до времен порядка характерного времени расплывания пакета
    t = np.linspace(0, t_distorted, 1024)
    transmitted_message = np.convolve(coded_message, distorted_pulse)[:1024]

    import matplotlib.pyplot as plt

    plt.figure(figsize=(10,5))
    plt.plot(t, transmitted_message)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Transmitted Message')
    plt.show()
