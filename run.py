import time
import numpy as np
import matplotlib.pyplot as plt
from pyaudio import PyAudio, paInt16

RATE = 48000 # time resolution of the recording device (Hz)
CHUNK = int(RATE/20) # RATE / number of updates per second)

def soundplot(stream):
    t = time.time()
    data = np.fromstring(stream.read(CHUNK, exception_on_overflow = False), dtype=np.int16)
    data = data * np.hanning(len(data)) # smooth the FFT by windowing data
    fft = abs(np.fft.fft(data).real)
    fft = fft[:int(len(fft)/2)] # keep only first half

    plt.plot(fft)
    plt.xlabel('Time (s)')
    plt.ylabel('Intensity')
    plt.title('Realtime Audio Visualisation')

    #plt.ylim([-2**16,2**16])
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('wave.png')

    plt.close('all')

if __name__ == "__main__":
    p = PyAudio() # start the PyAudio class
    stream = p.open(format=paInt16, channels=1, rate=RATE, input=True, frames_per_buffer=CHUNK) # uses default input device

    # create a numpy array holding a single read of audio data
    for i in range(int(20*RATE/CHUNK)):
        soundplot(stream)

    stream.stop_stream()
    stream.close()
    p.terminate()
