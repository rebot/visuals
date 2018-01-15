import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation, rc
from pyaudio import PyAudio, paInt16

RATE = 48000  # time resolution of the recording device (Hz)
CHUNK = int(RATE / 20)  # RATE / number of updates per second)


class Microphone():

    def __init__(self):
        plt.xlabel('Time (s)')
        plt.ylabel('Intensity')
        plt.title('Realtime Audio Visualisation')
        plt.ylim([0, 2**16])
        plt.grid(True)

    def __call__(self, stream):
        data = np.fromstring(stream.read(
            CHUNK, exception_on_overflow=False), dtype=np.int16)
        data = data * np.hanning(len(data))
        fft = abs(np.fft.fft(data).real)
        fft = fft[:int(len(fft) / 2)]
        return fft


def animate(fft):
    ax.clear()
    return ax.plot(fft, '-')

def frames(stream):
    while True:
        yield microphone(stream)

if __name__ == "__main__":
    pa = PyAudio()
    stream = pa.open(format=paInt16,
                     channels=1,
                     rate=RATE,
                     input=True,
                     frames_per_buffer=CHUNK)

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    microphone = Microphone()
    anim = animation.FuncAnimation(
        fig, animate, frames=frames(stream), interval=10)
    plt.show()

    # for i in range(int(20*RATE/CHUNK)):
    #    soundplot(stream)

    # stream.stop_stream()
    # stream.close()
    # pa.terminate()
