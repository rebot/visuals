import time
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import animation, rc
from pyaudio import PyAudio, paInt16

RATE = 48000  # time resolution of the recording device (Hz)
CHUNK = int(RATE / 20)  # RATE / number of updates per second)

plt.style.use('dark_background')
mpl.rcParams['toolbar'] = 'None'

class Microphone():

    def __init__(self):
        pass

    def __call__(self, stream):
        data = np.fromstring(stream.read(
            CHUNK, exception_on_overflow=False), dtype=np.int16)
        data = data * np.hanning(len(data))
        fft = abs(np.fft.fft(data).real)
        fft = fft[:int(len(fft) / 2)]
        return fft, np.amax(fft)

def init():
    ax.axis('off')

def animate(args):
    _, ymax = ax.get_ylim()
    ax.clear()
    ax.axis('off')
    if args[1] > ymax:
        ax.set_ylim([0, args[1]])
    else:
        ax.set_ylim([0, 0.9 * ymax])
    return ax.plot(args[0])

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
    ax = plt.Axes(fig, [0.15, 0.15, 0.7, 0.7])
    fig.add_axes(ax)
    microphone = Microphone()
    anim = animation.FuncAnimation(
        fig, animate, frames=frames(stream), interval=10, init_func=init)
    plt.show()

    # for i in range(int(20*RATE/CHUNK)):
    #    soundplot(stream)

    # stream.stop_stream()
    # stream.close()
    # pa.terminate()
